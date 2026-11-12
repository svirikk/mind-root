# -*- coding: utf-8 -*-
"""
File-based storage on the Railway volume (no database).
Set DATA_DIR env var to the mounted volume path, e.g. /data
Everything lives in a couple of JSON files there.
"""
import json
import os
import secrets
import threading
from datetime import datetime, timezone

DATA_DIR = os.environ.get("DATA_DIR", "./data")
os.makedirs(DATA_DIR, exist_ok=True)

ORDERS_FILE = os.path.join(DATA_DIR, "orders.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
COUNTER_FILE = os.path.join(DATA_DIR, "counter.json")
RELAY_FILE = os.path.join(DATA_DIR, "relay.json")

_lock = threading.Lock()


def _read(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return default


def _write(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


# ---------- users (language preference) ----------

def get_user_lang(user_id: int):
    users = _read(USERS_FILE, {})
    return users.get(str(user_id), {}).get("lang")


def set_user_lang(user_id: int, lang: str):
    with _lock:
        users = _read(USERS_FILE, {})
        users.setdefault(str(user_id), {})["lang"] = lang
        _write(USERS_FILE, users)


# ---------- orders ----------

def _generate_order_id(existing_orders: dict) -> str:
    """Generates a non-sequential alphanumeric order ID like MR-4829."""
    for _ in range(100):
        code = f"MR-{1000 + secrets.randbelow(9000)}"
        if code not in existing_orders:
            return code
    return f"MR-{10000 + secrets.randbelow(90000)}"


def create_order(user_id: int, chat_id: int, lang: str, product: str, details_raw: str,
                 source: str = "telegram", extra: dict | None = None) -> dict:
    """source: 'telegram' | 'instagram' | 'website' — which admin bot this order belongs to."""
    with _lock:
        orders = _read(ORDERS_FILE, {})
        order_id = _generate_order_id(orders)
        order = {
            "id": order_id,
            "source": source,
            "user_id": user_id,
            "chat_id": chat_id,
            "lang": lang,
            "product": product,
            "details_raw": details_raw,
            "status": "awaiting_payment",  # awaiting_payment -> awaiting_review -> paid
            "payment_method": None,        # bank | crypto
            "screenshot_file_id": None,
            "admin_order_msg_id": None,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "paid_at": None,
            "followup_sent": False,
        }
        if extra:
            order.update(extra)
        orders[str(order_id)] = order
        _write(ORDERS_FILE, orders)
    return order


def get_order(order_id) -> dict | None:
    if not order_id:
        return None
    orders = _read(ORDERS_FILE, {})
    return orders.get(str(order_id))


def update_order(order_id, **fields):
    with _lock:
        orders = _read(ORDERS_FILE, {})
        key = str(order_id)
        if key not in orders:
            return None
        orders[key].update(fields)
        _write(ORDERS_FILE, orders)
        return orders[key]


# ---------- relay: links ANY admin-chat message id (order card, receipt, question) to buyer chat ----------

def save_relay(source: str, admin_message_id: int, buyer_chat_id: int):
    if not admin_message_id or not buyer_chat_id:
        return
    with _lock:
        relay = _read(RELAY_FILE, {})
        relay[f"{source}:{admin_message_id}"] = buyer_chat_id
        _write(RELAY_FILE, relay)


def get_relay(source: str, admin_message_id: int) -> int | None:
    relay = _read(RELAY_FILE, {})
    chat_id = relay.get(f"{source}:{admin_message_id}")
    if chat_id:
        return chat_id
    # Fallback: check if the replied-to message is an order card in orders.json
    orders = _read(ORDERS_FILE, {})
    for o in orders.values():
        if o.get("source") == source and o.get("admin_order_msg_id") == admin_message_id:
            if o.get("chat_id"):
                return o["chat_id"]
    return None


def stats_by_source() -> dict:
    orders = _read(ORDERS_FILE, {})
    out = {}
    for o in orders.values():
        s = o.get("source", "telegram")
        out.setdefault(s, {"total": 0, "paid": 0})
        out[s]["total"] += 1
        if o["status"] == "paid":
            out[s]["paid"] += 1
    return out


def find_latest_open_order_for_user(user_id: int) -> dict | None:
    """Latest order of this user that's not yet marked paid."""
    orders = _read(ORDERS_FILE, {})
    candidates = [o for o in orders.values() if o.get("user_id") == user_id and o.get("status") != "paid"]
    if not candidates:
        return None
    return sorted(candidates, key=lambda o: o.get("created_at", ""))[-1]


def find_latest_order_for_user(user_id: int) -> dict | None:
    """Latest order of this user (even if already paid) — used to tag incoming buyer messages."""
    orders = _read(ORDERS_FILE, {})
    candidates = [o for o in orders.values() if o.get("user_id") == user_id]
    if not candidates:
        return None
    return sorted(candidates, key=lambda o: o.get("created_at", ""))[-1]


def find_orders_due_for_followup(days: float = 60.0) -> list[dict]:
    """Finds paid orders with a linked Telegram chat_id where `days` have passed since paid_at."""
    orders = _read(ORDERS_FILE, {})
    now = datetime.now(timezone.utc)
    due = []
    for o in orders.values():
        if o.get("status") != "paid" or o.get("followup_sent") or not o.get("chat_id"):
            continue
        ts_str = o.get("paid_at") or o.get("created_at")
        if not ts_str:
            continue
        try:
            paid_dt = datetime.fromisoformat(ts_str)
            if paid_dt.tzinfo is None:
                paid_dt = paid_dt.replace(tzinfo=timezone.utc)
            elapsed_days = (now - paid_dt).total_seconds() / 86400.0
            if elapsed_days >= days:
                due.append(o)
        except Exception:
            continue
    return due


def order_total(order: dict) -> int:
    """Total in GEL. Website orders store 'total' (price x qty); bot orders are single items."""
    if order.get("total"):
        return order["total"]
    from texts import PRODUCTS
    return PRODUCTS[order["product"]]["price"]


def link_buyer(order_id: str, user_id: int, chat_id: int, lang: str):
    """Bind a website order to the buyer's Telegram chat (via the /start order_<id>_<token> deep link)."""
    order = update_order(order_id, user_id=user_id, chat_id=chat_id, lang=lang)
    if order and order.get("admin_order_msg_id"):
        save_relay(order.get("source", "website"), order["admin_order_msg_id"], chat_id)
    return order