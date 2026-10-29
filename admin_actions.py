# -*- coding: utf-8 -*-
"""
Shared admin logic for the Telegram and Website admin bots.

Buttons under every order card:
  ✅ Оплачено  🔔 Нагадати  ❌ Невірний чек

If the buyer is linked to a Telegram chat (always for Telegram orders; for website
orders once the buyer taps "Send receipt in Telegram" on the confirmation screen),
these messages go to the buyer automatically through Bogdan. Otherwise the bot
shows you a ready-to-copy text instead (you reach that buyer by phone/WhatsApp).
"""
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
            f"New orders appear here automatically.\n\n/stats — orders across all channels"
        )

    @router.message(Command("stats"))
    async def cmd_stats(message: Message):
        stats = storage.stats_by_source()
        if not stats:
            await message.answer("No orders yet.")
            return
        lines = ["📊 *Orders by channel:*\n"]
        for src, data in sorted(stats.items(), key=lambda kv: -kv[1]["total"]):
            lines.append(f"{icons.get(src, '•')} {src}: {data['total']} total, {data['paid']} paid")
        await message.answer("\n".join(lines), parse_mode="Markdown")

    @router.callback_query(F.data.startswith("paid:"))
    async def on_paid(callback: CallbackQuery):
        order = storage.get_order(int(callback.data.split(":", 1)[1]))
        if not order:
            await callback.answer("Order not found", show_alert=True)
            return
        storage.update_order(order["id"], status="paid")
        if order["chat_id"]:
            await buyer_bot.send_message(order["chat_id"], T[order["lang"]]["paid_confirmed"])
            await callback.message.reply(f"✅ Order #{order['id']} marked as PAID — buyer notified.")
        else:
            await callback.message.reply(
                f"✅ Order #{order['id']} marked as PAID.\n"
                f"This buyer isn't linked to Telegram — confirm shipping to them by phone/WhatsApp."
            )
        await callback.answer("Marked as paid ✅")

    @router.callback_query(F.data.startswith("remind:"))
    async def on_remind(callback: CallbackQuery):
        order = storage.get_order(int(callback.data.split(":", 1)[1]))
        if not order:
            await callback.answer("Order not found", show_alert=True)
            return
        t = T[order["lang"]]
        text = t["reminder"].format(order_id=order["id"], price=storage.order_total(order), requisites=requisites)
        if order["chat_id"]:
            await buyer_bot.send_message(order["chat_id"], text, parse_mode="Markdown")
            await callback.answer("Reminder sent 🔔")
        else:
            await callback.answer()
            await callback.message.reply(f"📋 Buyer isn't on Telegram — copy this to them:\n\n{text}")

    @router.callback_query(F.data.startswith("invalid:"))
    async def on_invalid(callback: CallbackQuery):
        order = storage.get_order(int(callback.data.split(":", 1)[1]))
        if not order:
            await callback.answer("Order not found", show_alert=True)
            return
        text = T[order["lang"]]["invalid_receipt"].format(order_id=order["id"])
        if order["chat_id"]:
            await buyer_bot.send_message(order["chat_id"], text)
            await callback.answer("Buyer asked to resend the receipt ❌")
        else:
            await callback.answer()
            await callback.message.reply(f"📋 Buyer isn't on Telegram — copy this to them:\n\n{text}")

    @router.message(F.chat.id == admin_chat_id, F.reply_to_message)
    async def on_admin_reply(message: Message):
        """Use Telegram's native Reply on a relayed question -> goes back to that buyer."""
        buyer_chat = storage.get_relay(source, message.reply_to_message.message_id)
        if not buyer_chat:
            return
        await buyer_bot.send_message(buyer_chat, message.text or "")
        await message.reply("↩️ Sent to the customer.")

    return router
