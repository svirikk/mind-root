# -*- coding: utf-8 -*-
"""
File-based storage on the Railway volume (no database).
Set DATA_DIR env var to the mounted volume path, e.g. /data
Everything lives in a couple of JSON files there.
"""
import json
import os
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

def _next_order_id():
    with _lock:
        counter = _read(COUNTER_FILE, {"n": 0})
        counter["n"] += 1
        _write(COUNTER_FILE, counter)
        return counter["n"]


def create_order(user_id: int, chat_id: int, lang: str, product: str, details_raw: str,
                  source: str = "telegram", extra: dict | None = None) -> dict:
    """source: 'telegram' | 'instagram' | 'website' — which admin bot this order belongs to."""
    order_id = _next_order_id()
    order = {
        "id": order_id,
        "source": source,
        "user_id": user_id,
        "chat_id": chat_id,  # buyer's Telegram chat id — only meaningful when source == 'telegram'
        "lang": lang,
        "product": product,
        "details_raw": details_raw,
        "status": "awaiting_payment",  # awaiting_payment -> awaiting_review -> paid
        "screenshot_file_id": None,
        "admin_order_msg_id": None,  # message id of the admin card, for replies/threading
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    if extra:
        order.update(extra)  # e.g. qty, total for website orders
    with _lock:
        orders = _read(ORDERS_FILE, {})
        orders[str(order_id)] = order
        _write(ORDERS_FILE, orders)
    return order


def get_order(order_id) -> dict | None:
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


# ---------- relay: links an admin-chat message id to the buyer chat it came from ----------
# Needed because buyer_bot and admin_bot are separate processes/tokens — this file is
# the only thing they share, so a reply on the admin side can find its way back.

def save_relay(source: str, admin_message_id: int, buyer_chat_id: int):
    with _lock:
        relay = _read(RELAY_FILE, {})
        relay[f"{source}:{admin_message_id}"] = buyer_chat_id
        _write(RELAY_FILE, relay)


def get_relay(source: str, admin_message_id: int):
    relay = _read(RELAY_FILE, {})
    return relay.get(f"{source}:{admin_message_id}")


def stats_by_source() -> dict:
    """{'telegram': {'total': 12, 'paid': 7}, 'instagram': {...}, 'website': {...}}"""
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
    """Latest order of this user that's not yet marked paid - used to attach a screenshot to it."""
    orders = _read(ORDERS_FILE, {})
    candidates = [o for o in orders.values() if o["user_id"] == user_id and o["status"] != "paid"]
    if not candidates:
        return None
    return sorted(candidates, key=lambda o: o["id"])[-1]


def order_total(order: dict) -> int:
    """Total in GEL. Website orders store 'total' (price x qty); bot orders are single items."""
    if order.get("total"):
        return order["total"]
    from texts import PRODUCTS
    return PRODUCTS[order["product"]]["price"]


def link_buyer(order_id: int, user_id: int, chat_id: int, lang: str):
    """Bind a website order to the buyer's Telegram chat (via the /start order_<id> deep link)."""
    return update_order(order_id, user_id=user_id, chat_id=chat_id, lang=lang)
