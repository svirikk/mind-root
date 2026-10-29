# -*- coding: utf-8 -*-
"""
Web server for the Mind Root site.

  GET  /              -> public/index.html
  GET  /legal         -> public/legal.html   (privacy / terms / returns — owner must complete)
  GET  /assets/...    -> static files
  POST /api/order     -> validates the cart, prices it ON THE SERVER, saves the order,
                         pushes a card to the Website admin bot, answers honestly
                         whether Telegram really accepted it ("notified")
  GET  /healthz       -> health check

Env (all optional — without the Telegram token the site still works and orders are saved;
the customer is simply told the owner has not been notified yet):
  ADMIN_WEB_BOT_TOKEN, ADMIN_WEB_CHAT_ID (default: ADMIN_TG_CHAT_ID), PAYMENT_REQUISITES,
  BUYER_BOT_USERNAME (Bogdan, no @), OWNER_TELEGRAM (your @username, no @, used as a fallback link),
  PORT (set by Railway), DATA_DIR
"""
import html
import logging
import os
import secrets
import time
from collections import defaultdict, deque
from pathlib import Path

from aiohttp import web
from aiogram import Bot

import storage
from keyboards import admin_order_keyboard
from order_validation import OrderError, validate_order

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("web_server")

ADMIN_WEB_BOT_TOKEN = os.environ.get("ADMIN_WEB_BOT_TOKEN", "")
_chat = os.environ.get("ADMIN_WEB_CHAT_ID") or os.environ.get("ADMIN_TG_CHAT_ID") or ""
ADMIN_WEB_CHAT_ID = int(_chat) if _chat.lstrip("-").isdigit() else None
PAYMENT_REQUISITES = os.environ.get("PAYMENT_REQUISITES", "")
BUYER_BOT_USERNAME = os.environ.get("BUYER_BOT_USERNAME", "").lstrip("@")
OWNER_TELEGRAM = os.environ.get("OWNER_TELEGRAM", "").lstrip("@")
PORT = int(os.environ.get("PORT", "8080"))

PUBLIC_DIR = Path(__file__).parent / "public"

ITEM_NAMES = {
    "mane": "Lion's Mane",
    "cord": "Cordyceps",
    "dual": "Dual Complex (Lion's Mane + Cordyceps)",
}

# very small in-memory rate limit: max 5 orders / 10 minutes per IP
_hits: dict[str, deque] = defaultdict(deque)


def rate_limited(ip: str, limit: int = 5, window: int = 600) -> bool:
    now = time.time()
    q = _hits[ip]
    while q and now - q[0] > window:
        q.popleft()
    if len(q) >= limit:
        return True
    q.append(now)
    return False


def client_ip(request: web.Request) -> str:
    fwd = request.headers.get("X-Forwarded-For")
    return fwd.split(",")[0].strip() if fwd else (request.remote or "unknown")


@web.middleware
async def security_headers(request: web.Request, handler):
    resp = await handler(request)
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    resp.headers.setdefault("X-Frame-Options", "DENY")
    if request.path.startswith("/assets/"):
        resp.headers.setdefault("Cache-Control", "public, max-age=604800")
    elif request.path.startswith("/api/"):
        resp.headers["Cache-Control"] = "no-store"
    return resp


async def handle_index(request):
    return web.FileResponse(PUBLIC_DIR / "index.html")


async def handle_legal(request):
    return web.FileResponse(PUBLIC_DIR / "legal.html")


async def handle_health(request):
    return web.Response(text="ok")


def esc(value) -> str:
    """Escape for Telegram HTML parse mode: only & < > need it (quotes must stay as-is)."""
    return html.escape(str(value), quote=False)


def build_card(order_id: int, o: dict) -> str:
    t = o["totals"]
    lines = "\n".join(f"• {esc(ITEM_NAMES[i['id']])} × {i['qty']}" for i in o["items"])
    contact = ""
    if o["contact_method"] or o["contact_handle"]:
        contact = f"\n💬 {esc(o['contact_method'] or '-')}: {esc(o['contact_handle'] or '-')}"
    discount = f"\nDiscount (20%): −{t['discount']} ₾" if t["discount"] else ""
    return (
        f"🌐 <b>Order #{order_id}</b> (website)\n\n{lines}\n\n"
        f"Subtotal: {t['subtotal']} ₾{discount}\n<b>Total: {t['total']} ₾</b>\n\n"
        f"👤 {esc(o['name'])}\n📞 {esc(o['phone'])}\n"
        f"🏙 {esc(o['city'])}\n🏠 {esc(o['address'])}{contact}\n"
        f"Lang: {o['lang']}\n\nStatus: <i>awaiting payment</i>"
    )


async def handle_order(request: web.Request) -> web.Response:
    try:
        payload = await request.json()
    except Exception:
        return web.json_response({"ok": False, "error": "bad json"}, status=400)

    # honeypot: real users never fill this hidden field; bots do. Pretend success, store nothing.
    if isinstance(payload, dict) and payload.get("website"):
        return web.json_response({"ok": True, "order_id": 0, "notified": False, "totals": {},
                                  "requisites": "", "bot_link": "", "owner_telegram": ""})

    if rate_limited(client_ip(request)):
        return web.json_response({"ok": False, "error": "too many requests"}, status=429)

    try:
        o = validate_order(payload)
    except OrderError as e:
        return web.json_response({"ok": False, "error": str(e)}, status=400)

    link_token = secrets.token_urlsafe(6).replace("-", "a").replace("_", "b")  # [A-Za-z0-9] only
    details = f"{o['name']}\n{o['phone']}\n{o['city']}, {o['address']}"
    order = storage.create_order(
        user_id=0,
        chat_id=0,  # becomes the buyer's chat id if they tap "Send receipt in Telegram"
        lang=o["lang"],
        product="cart",
        details_raw=details,
        source="website",
        extra={
            "items": o["items"],
            "subtotal": o["totals"]["subtotal"],
            "discount": o["totals"]["discount"],
            "total": o["totals"]["total"],
            "link_token": link_token,
            "customer": {k: o[k] for k in ("name", "phone", "city", "address", "contact_method", "contact_handle")},
        },
    )

    # Telegram push. `notified` is True ONLY if Telegram actually accepted the message.
    notified = False
    admin_bot = request.app.get("admin_bot")
    if admin_bot and ADMIN_WEB_CHAT_ID:
        try:
            msg = await admin_bot.send_message(
                ADMIN_WEB_CHAT_ID, build_card(order["id"], o), parse_mode="HTML",
                reply_markup=admin_order_keyboard(order["id"]),
            )
            storage.update_order(order["id"], admin_order_msg_id=msg.message_id)
            notified = True
        except Exception:
            log.exception("Failed to push order #%s to Telegram", order["id"])
    else:
        log.warning("Telegram not configured — order #%s saved but owner NOT notified", order["id"])
    storage.update_order(order["id"], notified=notified)

    bot_link = (
        f"https://t.me/{BUYER_BOT_USERNAME}?start=order_{order['id']}_{link_token}" if BUYER_BOT_USERNAME else ""
    )
    return web.json_response({
        "ok": True,
        "order_id": order["id"],
        "notified": notified,
        "totals": o["totals"],
        "requisites": PAYMENT_REQUISITES,
        "bot_link": bot_link,
        "owner_telegram": OWNER_TELEGRAM,
    })


async def on_cleanup(app: web.Application):
    if app.get("admin_bot"):
        await app["admin_bot"].session.close()


def make_app() -> web.Application:
    app = web.Application(client_max_size=64 * 1024, middlewares=[security_headers])
    app["admin_bot"] = Bot(token=ADMIN_WEB_BOT_TOKEN) if ADMIN_WEB_BOT_TOKEN else None
    app.router.add_get("/", handle_index)
    app.router.add_get("/legal", handle_legal)
    app.router.add_get("/healthz", handle_health)
    app.router.add_post("/api/order", handle_order)
    app.router.add_static("/assets", PUBLIC_DIR / "assets")
    app.on_cleanup.append(on_cleanup)
    return app


if __name__ == "__main__":
    web.run_app(make_app(), host="0.0.0.0", port=PORT)
