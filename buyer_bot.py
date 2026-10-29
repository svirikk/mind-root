# -*- coding: utf-8 -*-
"""
Bogdan — Mind Root buyer bot.
Talks to customers. Pushes order/question notifications to the separate Admin bot
(different token) by sending messages with ITS token into the admin's chat.
Does not poll or handle anything on the admin side — that lives in admin_actions.py.

Run: python buyer_bot.py
Required env vars: BOT_TOKEN, ADMIN_TG_BOT_TOKEN, ADMIN_TG_CHAT_ID, ADMIN_WEB_BOT_TOKEN,
ADMIN_WEB_CHAT_ID (optional, defaults to ADMIN_TG_CHAT_ID), PAYMENT_REQUISITES, DATA_DIR (optional)
"""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, BufferedInputFile

import storage
from texts import T, PRODUCTS
from keyboards import lang_keyboard, product_keyboard, back_keyboard, admin_order_keyboard

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("buyer_bot")

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_TG_BOT_TOKEN = os.environ["ADMIN_TG_BOT_TOKEN"]
ADMIN_TG_CHAT_ID = int(os.environ["ADMIN_TG_CHAT_ID"])
PAYMENT_REQUISITES = os.environ.get("PAYMENT_REQUISITES", "GE00XXXXXXXXXXXXXXXXXXXX (TBC Bank)")

bot = Bot(token=BOT_TOKEN)                 # this bot — talks to buyers
admin_bot = Bot(token=ADMIN_TG_BOT_TOKEN)  # the Telegram-channel admin bot — we only push through it

# Website-channel admin bot: website buyers who tap "Send receipt in Telegram" end up here too
ADMIN_WEB_BOT_TOKEN = os.environ["ADMIN_WEB_BOT_TOKEN"]
ADMIN_WEB_CHAT_ID = int(os.environ.get("ADMIN_WEB_CHAT_ID") or ADMIN_TG_CHAT_ID)
admin_web_bot = Bot(token=ADMIN_WEB_BOT_TOKEN)


def admin_target(source: str):
    """Which admin bot + chat an order's notifications belong to."""
    if source == "website":
        return admin_web_bot, ADMIN_WEB_CHAT_ID
    return admin_bot, ADMIN_TG_CHAT_ID

dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)


class OrderStates(StatesGroup):
    waiting_details = State()
    waiting_screenshot = State()


# ---------------------------- buyer flow ----------------------------

@router.message(CommandStart(deep_link=True))
async def cmd_start_deeplink(message: Message, command: CommandObject, state: FSMContext):
    """t.me/<bogdan>?start=order_<id>_<token> — comes from the website confirmation screen."""
    parts = (command.args or "").split("_")
    if len(parts) == 3 and parts[0] == "order" and parts[1].isdigit():
        order = storage.get_order(int(parts[1]))
        if order and order.get("source") == "website" and order.get("link_token") == parts[2]:
            lang = order["lang"]
            storage.set_user_lang(message.from_user.id, lang)
            storage.link_buyer(order["id"], message.from_user.id, message.chat.id, lang)
            await state.clear()
            await state.set_state(OrderStates.waiting_screenshot)
            await state.update_data(order_id=order["id"])
            await message.answer(
                T[lang]["order_created"].format(
                    order_id=order["id"], price=storage.order_total(order), requisites=PAYMENT_REQUISITES),
                parse_mode="Markdown",
            )
            a_bot, a_chat = admin_target("website")
            await a_bot.send_message(
                a_chat,
                f"🔗 Order #{order['id']}: buyer connected on Telegram (@{message.from_user.username or '-'}) — "
                f"buttons now message them automatically.",
                reply_to_message_id=order.get("admin_order_msg_id"),
            )
            return
    await cmd_start(message, state)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    lang = storage.get_user_lang(message.from_user.id)
    if lang:
        await send_catalog(message.chat.id, lang)
    else:
        await message.answer(T["uk"]["choose_lang"], reply_markup=lang_keyboard())


@router.callback_query(F.data.startswith("lang:"))
async def on_lang_chosen(callback: CallbackQuery, state: FSMContext):
    lang = callback.data.split(":", 1)[1]
    storage.set_user_lang(callback.from_user.id, lang)
    await callback.answer()
    await send_catalog(callback.message.chat.id, lang)


async def send_catalog(chat_id: int, lang: str):
    t = T[lang]
    await bot.send_message(chat_id, t["welcome"])
    for key in ["mane", "cord", "bundle"]:
        name = t["name"][key]
        tagline = t["tagline"][key]
        price = PRODUCTS[key]["price"]
        emoji = PRODUCTS[key]["emoji"]
        text = f"{emoji} *{name}*\n{tagline}\n\n*{price} ₾*"
        await bot.send_message(chat_id, text, parse_mode="Markdown",
                                reply_markup=product_keyboard(lang, key))


@router.callback_query(F.data.startswith("learn:"))
async def on_learn_more(callback: CallbackQuery):
    product = callback.data.split(":", 1)[1]
    lang = storage.get_user_lang(callback.from_user.id) or "uk"
    t = T[lang]
    await callback.answer()
    await bot.send_message(
        callback.message.chat.id,
        t["details"][product],
        parse_mode="Markdown",
        reply_markup=back_keyboard(lang),
    )


@router.callback_query(F.data == "back_to_catalog")
async def on_back(callback: CallbackQuery):
    lang = storage.get_user_lang(callback.from_user.id) or "uk"
    await callback.answer()
    await send_catalog(callback.message.chat.id, lang)


@router.callback_query(F.data.startswith("order:"))
async def on_order_start(callback: CallbackQuery, state: FSMContext):
    product = callback.data.split(":", 1)[1]
    lang = storage.get_user_lang(callback.from_user.id) or "uk"
    t = T[lang]
    await state.update_data(product=product)
    await state.set_state(OrderStates.waiting_details)
    await callback.answer()
    await bot.send_message(callback.message.chat.id, t["ask_details"], parse_mode="Markdown")


@router.message(OrderStates.waiting_details)
async def on_order_details(message: Message, state: FSMContext):
    data = await state.get_data()
    product = data["product"]
    lang = storage.get_user_lang(message.from_user.id) or "uk"
    t = T[lang]
    price = PRODUCTS[product]["price"]

    order = storage.create_order(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        lang=lang,
        product=product,
        details_raw=message.text,
        source="telegram",
    )

    await message.answer(
        t["order_created"].format(order_id=order["id"], price=price, requisites=PAYMENT_REQUISITES),
        parse_mode="Markdown",
    )
    await state.set_state(OrderStates.waiting_screenshot)
    await state.update_data(order_id=order["id"])

    admin_text = (
        f"🆕 *Order #{order['id']}*\n"
        f"Product: {t['name'][product]}  ({price} ₾)\n"
        f"Buyer: {message.from_user.full_name} (@{message.from_user.username or '-'})\n"
        f"Lang: {lang}\n\n"
        f"*Details:*\n{message.text}\n\n"
        f"Status: _awaiting payment_"
    )
    # pushed via the ADMIN bot's token, so the buttons below are handled by admin_bot.py
    admin_msg = await admin_bot.send_message(
        ADMIN_TG_CHAT_ID, admin_text, parse_mode="Markdown", reply_markup=admin_order_keyboard(order["id"])
    )
    storage.update_order(order["id"], admin_order_msg_id=admin_msg.message_id)


@router.message(OrderStates.waiting_screenshot, F.photo)
async def on_screenshot(message: Message, state: FSMContext):
    data = await state.get_data()
    order_id = data.get("order_id")
    order = storage.get_order(order_id) if order_id else storage.find_latest_open_order_for_user(message.from_user.id)
    if not order:
        return
    lang = order["lang"]
    t = T[lang]

    file_id = message.photo[-1].file_id
    storage.update_order(order["id"], screenshot_file_id=file_id, status="awaiting_review")
    await message.answer(t["screenshot_received"])

    # file_id values are NOT portable between different bots, so we download the photo
    # with our own token and re-upload it through the admin bot's token.
    file = await bot.get_file(file_id)
    file_bytes = await bot.download_file(file.file_path)
    photo_input = BufferedInputFile(file_bytes.read(), filename="receipt.jpg")

    caption = f"📸 Payment screenshot for *Order #{order['id']}*"
    a_bot, a_chat = admin_target(order.get("source", "telegram"))
    await a_bot.send_photo(
        a_chat,
        photo_input,
        caption=caption,
        parse_mode="Markdown",
        reply_to_message_id=order.get("admin_order_msg_id"),
        reply_markup=admin_order_keyboard(order["id"]),
    )


@router.message(OrderStates.waiting_screenshot)
async def on_waiting_screenshot_text(message: Message, state: FSMContext):
    data = await state.get_data()
    order = storage.get_order(data.get("order_id"))
    lang = order["lang"] if order else (storage.get_user_lang(message.from_user.id) or "uk")
    await message.answer(T[lang]["ask_screenshot_again"])


# ---------------------------- free-text relay (buyer -> admin) ----------------------------

@router.message(F.text)
async def on_free_text(message: Message):
    """Any text outside the order flow is treated as a question and relayed to the admin bot."""
    lang = storage.get_user_lang(message.from_user.id) or "uk"
    order = storage.find_latest_open_order_for_user(message.from_user.id)
    order_tag = f" (order #{order['id']})" if order else ""

    relay_text = f"💬 Question from {message.from_user.full_name}{order_tag}:\n{message.text}"
    source = order.get("source", "telegram") if order else "telegram"
    a_bot, a_chat = admin_target(source)
    sent = await a_bot.send_message(a_chat, relay_text)
    # persisted (not in-memory) so the admin bot — a separate process — can resolve the reply later
    storage.save_relay(source, sent.message_id, message.chat.id)

    await message.answer(T[lang]["question_forwarded"])


# ---------------------------- entrypoint ----------------------------

async def main():
    log.info("Buyer bot (Bogdan) starting, data dir: %s", storage.DATA_DIR)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
