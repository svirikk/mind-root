# -*- coding: utf-8 -*-
"""
Shared admin logic for the Telegram and Website admin bots.

Buttons under every order card:
  ✅ Оплачено  🔔 Нагадати  ❌ Невірний чек

Admin can Reply to ANY order card, screenshot, or relayed message to send a message
directly to the customer through Bogdan.
"""
import html
from datetime import datetime, timezone
from aiogram import Bot, Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

import storage
from texts import T


def build_router(source: str, admin_chat_id: int, buyer_bot: Bot, requisites: str) -> Router:
    router = Router()
    icons = {"telegram": "📱", "instagram": "📸", "website": "🌐"}

    @router.message(CommandStart())
    async def cmd_start(message: Message):
        await message.answer(
            f"{icons.get(source, '•')} Admin bot — {source} orders.\n"
            f"New orders appear here automatically.\n"
            f"💬 Tip: Reply to any order card or customer message to write directly to the buyer.\n\n"
            f"/stats — orders across all channels"
        )

    @router.message(Command("stats"))
    async def cmd_stats(message: Message):
        stats = storage.stats_by_source()
        if not stats:
            await message.answer("No orders yet.")
            return
        lines = ["📊 <b>Orders by channel:</b>\n"]
        for src, data in sorted(stats.items(), key=lambda kv: -kv[1]["total"]):
            lines.append(f"{icons.get(src, '•')} {html.escape(src)}: {data['total']} total, {data['paid']} paid")
        await message.answer("\n".join(lines), parse_mode="HTML")

    @router.callback_query(F.data.startswith("paid:"))
    async def on_paid(callback: CallbackQuery):
        order_id = callback.data.split(":", 1)[1]
        order = storage.get_order(order_id)
        if not order:
            await callback.answer("Order not found", show_alert=True)
            return
        now_iso = datetime.now(timezone.utc).isoformat()
        storage.update_order(order["id"], status="paid", paid_at=now_iso)
        lang = order.get("lang") if order.get("lang") in T else "en"
        if order.get("chat_id"):
            await buyer_bot.send_message(order["chat_id"], T[lang]["paid_confirmed"])
            await callback.message.reply(
                f"✅ Order #{order['id']} marked as PAID — buyer notified (60-day retention timer started)."
            )
        else:
            await callback.message.reply(
                f"✅ Order #{order['id']} marked as PAID.\n"
                f"This buyer isn't linked to Telegram — confirm shipping to them by phone/WhatsApp/email."
            )
        await callback.answer("Marked as paid ✅")

    @router.callback_query(F.data.startswith("remind:"))
    async def on_remind(callback: CallbackQuery):
        order_id = callback.data.split(":", 1)[1]
        order = storage.get_order(order_id)
        if not order:
            await callback.answer("Order not found", show_alert=True)
            return
        lang = order.get("lang") if order.get("lang") in T else "en"
        t = T[lang]
        text = t["reminder"].format(order_id=order["id"], price=storage.order_total(order), requisites=requisites)
        if order.get("chat_id"):
            await buyer_bot.send_message(order["chat_id"], text, parse_mode="Markdown")
            await callback.answer("Reminder sent 🔔")
        else:
            await callback.answer()
            await callback.message.reply(f"📋 Buyer isn't on Telegram — copy this to them (phone/WhatsApp/email):\n\n{text}")

    @router.callback_query(F.data.startswith("invalid:"))
    async def on_invalid(callback: CallbackQuery):
        order_id = callback.data.split(":", 1)[1]
        order = storage.get_order(order_id)
        if not order:
            await callback.answer("Order not found", show_alert=True)
            return
        lang = order.get("lang") if order.get("lang") in T else "en"
        text = T[lang]["invalid_receipt"].format(order_id=order["id"])
        if order.get("chat_id"):
            await buyer_bot.send_message(order["chat_id"], text)
            await callback.answer("Buyer asked to resend the receipt ❌")
        else:
            await callback.answer()
            await callback.message.reply(f"📋 Buyer isn't on Telegram — copy this to them (phone/WhatsApp/email):\n\n{text}")

    @router.message(F.chat.id == admin_chat_id, F.reply_to_message)
    async def on_admin_reply(message: Message):
        """Use Telegram's native Reply on ANY order card, receipt, or question -> goes to that buyer."""
        buyer_chat = storage.get_relay(source, message.reply_to_message.message_id)
        if not buyer_chat:
            await message.reply("⚠️ Buyer is not linked to a Telegram chat yet (or order came from website without opening the bot).")
            return
        await buyer_bot.send_message(buyer_chat, message.text or "")
        await message.reply("↩️ Sent to the customer.")

    return router