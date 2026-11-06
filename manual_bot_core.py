# -*- coding: utf-8 -*-
"""
Shared logic for admin bots that track orders from a channel with NO live Telegram
chat to the buyer (Instagram DMs, or the website before it's wired up to a bot).
"""
import html
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup

import storage
from texts import PRODUCTS

SOURCE_ICON = {"instagram": "📸", "website": "🌐"}


class NewOrderStates(StatesGroup):
    choosing_product = State()
    entering_details = State()


def product_choice_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🧠 Lion's Mane — 80₾", callback_data="newprod:mane")],
        [InlineKeyboardButton(text="⚡ Cordyceps — 80₾", callback_data="newprod:cord")],
        [InlineKeyboardButton(text="🍄 Bundle — 128₾", callback_data="newprod:bundle")],
    ])


def manual_order_keyboard(order_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ Оплачено", callback_data=f"m_paid:{order_id}"),
        InlineKeyboardButton(text="📋 Текст нагадування", callback_data=f"m_remind:{order_id}"),
    ]])


def build_router(source: str) -> Router:
    router = Router()
    icon = SOURCE_ICON.get(source, "•")

    @router.message(CommandStart())
    async def cmd_start(message: Message, state: FSMContext):
        await state.clear()
        await message.answer(
            f"{icon} Order tracker for {source}.\n\n"
            f"/new — log a new order\n/stats — orders across all channels"
        )

    @router.message(Command("stats"))
    async def cmd_stats(message: Message):
        stats = storage.stats_by_source()
        if not stats:
            await message.answer("No orders yet.")
            return
        lines = ["📊 <b>Orders by channel:</b>\n"]
        icons = {"telegram": "📱", "instagram": "📸", "website": "🌐"}
        for src, data in sorted(stats.items(), key=lambda kv: -kv[1]["total"]):
            lines.append(f"{icons.get(src, '•')} {html.escape(src)}: {data['total']} total, {data['paid']} paid")
        await message.answer("\n".join(lines), parse_mode="HTML")

    @router.message(Command("new"))
    async def cmd_new(message: Message, state: FSMContext):
        await state.set_state(NewOrderStates.choosing_product)
        await message.answer("Which product?", reply_markup=product_choice_keyboard())

    @router.callback_query(NewOrderStates.choosing_product, F.data.startswith("newprod:"))
    async def on_product_chosen(callback: CallbackQuery, state: FSMContext):
        product = callback.data.split(":", 1)[1]
        await state.update_data(product=product)
        await state.set_state(NewOrderStates.entering_details)
        await callback.answer()
        await callback.message.edit_text(
            "Got it. Now send me the buyer's details in one message "
            "(name, phone, email, Instagram handle, address):"
        )

    @router.message(NewOrderStates.entering_details)
    async def on_details_entered(message: Message, state: FSMContext):
        data = await state.get_data()
        product = data["product"]
        price = PRODUCTS[product]["price"]

        order = storage.create_order(
            user_id=0,
            chat_id=0,
            lang="uk",
            product=product,
            details_raw=message.text,
            source=source,
        )
        await state.clear()

        esc_details = html.escape(str(message.text or ""))
        card = (
            f"{icon} <b>Order #{html.escape(str(order['id']))}</b> ({html.escape(source)})\n"
            f"Product: {html.escape(product)}  ({price} ₾)\n\n"
            f"<b>Buyer details:</b>\n{esc_details}\n\n"
            f"Status: <i>awaiting payment</i>"
        )
        await message.answer(card, parse_mode="HTML", reply_markup=manual_order_keyboard(order["id"]))

    @router.callback_query(F.data.startswith("m_paid:"))
    async def on_manual_paid(callback: CallbackQuery):
        order_id = callback.data.split(":", 1)[1]
        order = storage.get_order(order_id)
        if not order:
            await callback.answer("Order not found", show_alert=True)
            return
        storage.update_order(order_id, status="paid")
        await callback.answer("Marked as paid ✅")
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.reply(f"✅ Order #{order_id} marked as PAID.")

    @router.callback_query(F.data.startswith("m_remind:"))
    async def on_manual_remind(callback: CallbackQuery):
        order_id = callback.data.split(":", 1)[1]
        order = storage.get_order(order_id)
        if not order:
            await callback.answer("Order not found", show_alert=True)
            return
        price = PRODUCTS[order["product"]]["price"]
        text = (
            f"Hi! Just a reminder about your order (#{order_id}), {price} ₾ — "
            f"let me know once you've sent the payment and I'll ship it right away 🙂"
        )
        await callback.answer()
        await callback.message.reply(f"📋 Copy this into {source}:\n\n{text}")

    return router