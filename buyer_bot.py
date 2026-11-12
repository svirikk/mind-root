# -*- coding: utf-8 -*-
"""
Bogdan — Mind Root buyer bot.
1. Sends the order card to Admin immediately when the buyer submits delivery details.
2. Lets the buyer switch between Bank Transfer and Crypto silently.
3. Clears FSM state once the buyer taps "✅ I have paid" or sends a screenshot so they can
   freely chat with Admin anytime.
4. Links every admin message (order card, payment alert, screenshot, question) to the buyer's
   chat_id so Admin can Reply to ANY message in the admin bot to talk to the customer.
5. Runs a background retention scheduler that messages buyers 60 days after payment with a
   repeat-order discount.
"""
import html
import asyncio
import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, BufferedInputFile, FSInputFile

import storage
from texts import T, PRODUCTS
from keyboards import (
    lang_keyboard,
    product_keyboard,
    back_keyboard,
    payment_method_keyboard,
    payment_confirm_keyboard,
    admin_order_keyboard,
)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("buyer_bot")

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_TG_BOT_TOKEN = os.environ["ADMIN_TG_BOT_TOKEN"]
ADMIN_TG_CHAT_ID = int(os.environ["ADMIN_TG_CHAT_ID"])
PAYMENT_REQUISITES = os.environ.get("PAYMENT_REQUISITES", "GE00XXXXXXXXXXXXXXXXXXXX (TBC Bank)")
CRYPTO_TRC20 = os.environ.get("CRYPTO_TRC20", "Ask admin for TRC20 address")
CRYPTO_BEP20 = os.environ.get("CRYPTO_BEP20", "Ask admin for BEP20 address")
USDT_RATE = float(os.environ.get("USDT_RATE", "2.70"))

# Налаштування 60-денного нагадування та додаткової знижки (%)
RETENTION_DAYS = float(os.environ.get("RETENTION_DAYS", "60"))
RETENTION_DISCOUNT = int(os.environ.get("RETENTION_DISCOUNT", "15"))

bot = Bot(token=BOT_TOKEN)
admin_bot = Bot(token=ADMIN_TG_BOT_TOKEN)

ADMIN_WEB_BOT_TOKEN = os.environ["ADMIN_WEB_BOT_TOKEN"]
ADMIN_WEB_CHAT_ID = int(os.environ.get("ADMIN_WEB_CHAT_ID") or ADMIN_TG_CHAT_ID)
admin_web_bot = Bot(token=ADMIN_WEB_BOT_TOKEN)

IMG_DIR = Path(__file__).parent / "public" / "assets" / "img"
PRODUCT_IMAGES = {
    "mane": IMG_DIR / "bot-mane.jpg",
    "cord": IMG_DIR / "bot-cord.jpg",
    "bundle": IMG_DIR / "bot-bundle.jpg",
}


def admin_target(source: str):
    if source == "website":
        return admin_web_bot, ADMIN_WEB_CHAT_ID
    return admin_bot, ADMIN_TG_CHAT_ID


def calc_usdt(gel_amount: int) -> str:
    if USDT_RATE <= 0:
        return str(gel_amount)
    val = round(gel_amount / USDT_RATE, 2)
    return f"{val:.2f}".rstrip("0").rstrip(".")


def format_method_label(order: dict) -> str:
    price = storage.order_total(order)
    pm = order.get("payment_method")
    if pm == "crypto":
        return f"💎 Crypto (~{calc_usdt(price)} USDT / {price} ₾)"
    if pm == "bank":
        return f"💳 Bank Transfer ({price} ₾)"
    return f"{price} ₾"


async def send_initial_admin_card(order: dict, user) -> int | None:
    """Sends the initial order card to the admin bot and saves relay link for two-way chat."""
    source = order.get("source", "telegram")
    if order.get("admin_order_msg_id"):
        if order.get("chat_id"):
            storage.save_relay(source, order["admin_order_msg_id"], order["chat_id"])
        return order["admin_order_msg_id"]

    lang = order.get("lang") if order.get("lang") in T else "uk"
    t = T[lang]
    product = order.get("product", "mane")
    price = storage.order_total(order)
    p_name = t["name"].get(product, product)

    esc_product = html.escape(str(p_name))
    esc_name = html.escape(str(user.full_name or ""))
    esc_username = html.escape(str(user.username or "-"))
    esc_details = html.escape(str(order.get("details_raw") or ""))

    admin_text = (
        f"🆕 <b>Order #{html.escape(str(order['id']))}</b> (telegram)\n"
        f"Product: {esc_product}  ({price} ₾)\n"
        f"Buyer: {esc_name} (@{esc_username})\n"
        f"Lang: {lang}\n\n"
        f"<b>Details:</b>\n{esc_details}\n\n"
        f"Status: <i>awaiting payment</i>\n"
        f"💬 <i>Reply to this card anytime to message the buyer</i>"
    )
    a_bot, a_chat = admin_target(source)
    admin_msg = await a_bot.send_message(
        a_chat,
        admin_text,
        parse_mode="HTML",
        reply_markup=admin_order_keyboard(order["id"]),
    )
    storage.update_order(order["id"], admin_order_msg_id=admin_msg.message_id)
    order["admin_order_msg_id"] = admin_msg.message_id
    if order.get("chat_id"):
        storage.save_relay(source, admin_msg.message_id, order["chat_id"])
    return admin_msg.message_id


async def forward_buyer_text_to_admin(message: Message):
    """Forwards any free text from buyer to the appropriate admin bot and links reply relay."""
    lang = storage.get_user_lang(message.from_user.id) or "uk"
    if lang not in T:
        lang = "uk"
    order = (
        storage.find_latest_open_order_for_user(message.from_user.id)
        or storage.find_latest_order_for_user(message.from_user.id)
    )
    order_tag = f" (Order #{order['id']})" if order else ""
    username_tag = f" (@{message.from_user.username})" if message.from_user.username else ""

    relay_text = (
        f"💬 Message from {message.from_user.full_name}{username_tag}{order_tag}:\n\n"
        f"{message.text}"
    )
    source = order.get("source", "telegram") if order else "telegram"
    a_bot, a_chat = admin_target(source)
    reply_to = order.get("admin_order_msg_id") if order else None
    try:
        sent = await a_bot.send_message(a_chat, relay_text, reply_to_message_id=reply_to)
    except Exception:
        sent = await a_bot.send_message(a_chat, relay_text)
    storage.save_relay(source, sent.message_id, message.chat.id)
    await message.answer(T[lang]["question_forwarded"])


async def retention_loop():
    """Background task: checks every 6 hours for paid orders that reached 60 days."""
    await asyncio.sleep(15)
    while True:
        try:
            due_orders = storage.find_orders_due_for_followup(RETENTION_DAYS)
            for o in due_orders:
                lang = o.get("lang") if o.get("lang") in T else "uk"
                text = T[lang]["course_ending"].format(
                    order_id=o["id"],
                    discount=RETENTION_DISCOUNT,
                )
                try:
                    await bot.send_message(
                        o["chat_id"],
                        text,
                        parse_mode="Markdown",
                        reply_markup=back_keyboard(lang),
                    )
                    storage.update_order(o["id"], followup_sent=True)
                    a_bot, a_chat = admin_target(o.get("source", "telegram"))
                    await a_bot.send_message(
                        a_chat,
                        f"🔔 60-day retention reminder (+{RETENTION_DISCOUNT}% discount code ROOT{RETENTION_DISCOUNT}) "
                        f"was automatically sent to buyer of <b>Order #{html.escape(str(o['id']))}</b>.",
                        parse_mode="HTML",
                        reply_to_message_id=o.get("admin_order_msg_id"),
                    )
                except Exception:
                    log.exception("Failed to send 60-day retention message for order %s", o.get("id"))
                    storage.update_order(o["id"], followup_sent=True)
        except asyncio.CancelledError:
            raise
        except Exception:
            log.exception("Error in retention_loop")
        await asyncio.sleep(6 * 3600)


dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)


@dp.startup()
async def on_startup():
    asyncio.create_task(retention_loop())


class OrderStates(StatesGroup):
    waiting_details = State()
    waiting_screenshot = State()


# ---------------------------- buyer flow ----------------------------

@router.message(CommandStart(deep_link=True))
async def cmd_start_deeplink(message: Message, command: CommandObject, state: FSMContext):
    """t.me/<bogdan>?start=order_<id>_<token> — comes from the website confirmation screen."""
    parts = (command.args or "").split("_")
    if len(parts) == 3 and parts[0] == "order":
        order_id = parts[1]
        order = storage.get_order(order_id)
        if order and order.get("source") == "website" and order.get("link_token") == parts[2]:
            lang = order["lang"] if order.get("lang") in T else "en"
            storage.set_user_lang(message.from_user.id, lang)
            storage.link_buyer(order["id"], message.from_user.id, message.chat.id, lang)
            await state.clear()
            await state.set_state(OrderStates.waiting_screenshot)
            await state.update_data(order_id=order["id"])

            price = storage.order_total(order)
            await message.answer(
                T[lang]["choose_payment"].format(order_id=order["id"], price=price),
                parse_mode="Markdown",
                reply_markup=payment_method_keyboard(lang, order["id"]),
            )
            return
    await cmd_start(message, state)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    lang = storage.get_user_lang(message.from_user.id)
    if lang and lang in T:
        await send_catalog(message.chat.id, lang)
    else:
        await message.answer(T["uk"]["choose_lang"], reply_markup=lang_keyboard())


@router.callback_query(F.data.startswith("lang:"))
async def on_lang_chosen(callback: CallbackQuery, state: FSMContext):
    lang = callback.data.split(":", 1)[1]
    if lang not in T:
        lang = "en"
    storage.set_user_lang(callback.from_user.id, lang)
    await callback.answer()
    await send_catalog(callback.message.chat.id, lang)


async def send_catalog(chat_id: int, lang: str):
    t = T.get(lang, T["en"])
    await bot.send_message(chat_id, t["welcome"], parse_mode="Markdown")
    for key in ["mane", "cord", "bundle"]:
        name = t["name"][key]
        tagline = t["tagline"][key]
        price = PRODUCTS[key]["price"]
        emoji = PRODUCTS[key]["emoji"]
        text = f"{emoji} *{name}*\n{tagline}\n\n*{price} ₾*"
        kb = product_keyboard(lang, key)

        img_path = PRODUCT_IMAGES.get(key)
        if img_path and img_path.exists():
            await bot.send_photo(
                chat_id,
                FSInputFile(img_path),
                caption=text,
                parse_mode="Markdown",
                reply_markup=kb,
            )
        else:
            await bot.send_message(
                chat_id,
                text,
                parse_mode="Markdown",
                reply_markup=kb,
            )


@router.callback_query(F.data.startswith("learn:"))
async def on_learn_more(callback: CallbackQuery):
    product = callback.data.split(":", 1)[1]
    lang = storage.get_user_lang(callback.from_user.id) or "uk"
    t = T.get(lang, T["uk"])
    await callback.answer()
    await bot.send_message(
        callback.message.chat.id,
        t["details"][product],
        parse_mode="Markdown",
        reply_markup=back_keyboard(lang),
    )


@router.callback_query(F.data == "back_to_catalog")
async def on_back(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    lang = storage.get_user_lang(callback.from_user.id) or "uk"
    await callback.answer()
    await send_catalog(callback.message.chat.id, lang)


@router.callback_query(F.data.startswith("order:"))
async def on_order_start(callback: CallbackQuery, state: FSMContext):
    product = callback.data.split(":", 1)[1]
    lang = storage.get_user_lang(callback.from_user.id) or "uk"
    t = T.get(lang, T["uk"])
    await state.update_data(product=product)
    await state.set_state(OrderStates.waiting_details)
    await callback.answer()
    await bot.send_message(callback.message.chat.id, t["ask_details"], parse_mode="Markdown")


@router.message(OrderStates.waiting_details)
async def on_order_details(message: Message, state: FSMContext):
    data = await state.get_data()
    product = data["product"]
    lang = storage.get_user_lang(message.from_user.id) or "uk"
    t = T.get(lang, T["uk"])
    price = PRODUCTS[product]["price"]

    order = storage.create_order(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        lang=lang,
        product=product,
        details_raw=message.text,
        source="telegram",
    )

    await state.set_state(OrderStates.waiting_screenshot)
    await state.update_data(order_id=order["id"])

    await message.answer(
        t["choose_payment"].format(order_id=order["id"], price=price),
        parse_mode="Markdown",
        reply_markup=payment_method_keyboard(lang, order["id"]),
    )

    await send_initial_admin_card(order, message.from_user)


@router.callback_query(F.data.startswith("paym:"))
async def on_payment_method_chosen(callback: CallbackQuery, state: FSMContext):
    parts = callback.data.split(":", 2)
    if len(parts) != 3:
        await callback.answer()
        return
    _, method, order_id = parts
    order = storage.get_order(order_id)
    if not order:
        await callback.answer("Order not found", show_alert=True)
        return

    lang = order.get("lang") or storage.get_user_lang(callback.from_user.id) or "uk"
    t = T.get(lang, T["uk"])
    price = storage.order_total(order)

    storage.update_order(order_id, payment_method=method)
    await state.set_state(OrderStates.waiting_screenshot)
    await state.update_data(order_id=order_id)
    await callback.answer()

    if method == "crypto":
        usdt_amount = calc_usdt(price)
        text = t["crypto_instructions"].format(
            order_id=order_id,
            price=price,
            usdt=usdt_amount,
            trc20=CRYPTO_TRC20,
            bep20=CRYPTO_BEP20,
        )
    else:
        text = t["bank_instructions"].format(
            order_id=order_id,
            price=price,
            requisites=PAYMENT_REQUISITES,
        )

    kb = payment_confirm_keyboard(lang, order_id)
    try:
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=kb)
    except Exception:
        await callback.message.answer(text, parse_mode="Markdown", reply_markup=kb)


@router.callback_query(F.data.startswith("payback:"))
async def on_payment_back(callback: CallbackQuery, state: FSMContext):
    order_id = callback.data.split(":", 1)[1]
    order = storage.get_order(order_id)
    if not order:
        await callback.answer("Order not found", show_alert=True)
        return

    lang = order.get("lang") or storage.get_user_lang(callback.from_user.id) or "uk"
    t = T.get(lang, T["uk"])
    price = storage.order_total(order)
    await callback.answer()

    text = t["choose_payment"].format(order_id=order_id, price=price)
    kb = payment_method_keyboard(lang, order_id)
    try:
        await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=kb)
    except Exception:
        await callback.message.answer(text, parse_mode="Markdown", reply_markup=kb)


@router.callback_query(F.data.startswith("ipaid:"))
async def on_i_paid_clicked(callback: CallbackQuery, state: FSMContext):
    """Кнопка '✅ Я оплатив(ла)' — очищує стан блокування, шле підтвердження і сповіщає адміна."""
    order_id = callback.data.split(":", 1)[1]
    order = storage.get_order(order_id)
    if not order:
        await callback.answer("Order not found", show_alert=True)
        return

    lang = order.get("lang") or storage.get_user_lang(callback.from_user.id) or "uk"
    t = T.get(lang, T["uk"])

    storage.update_order(order_id, status="awaiting_review")
    order["status"] = "awaiting_review"

    # Очищуємо стан, щоб клієнт міг вільно писати будь-які повідомлення в чат
    await state.clear()
    await callback.answer()
    try:
        await callback.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass
    await callback.message.answer(t["screenshot_received"])

    msg_id = await send_initial_admin_card(order, callback.from_user)
    source = order.get("source", "telegram")
    a_bot, a_chat = admin_target(source)
    esc_user = html.escape(str(callback.from_user.username or "-"))
    esc_method = html.escape(format_method_label(order))
    sent = await a_bot.send_message(
        a_chat,
        f"✅ Buyer (@{esc_user}) tapped <b>«I have paid»</b> for <b>Order #{html.escape(str(order_id))}</b>\n"
        f"Method: <b>{esc_method}</b>",
        parse_mode="HTML",
        reply_to_message_id=msg_id,
        reply_markup=admin_order_keyboard(order_id),
    )
    storage.save_relay(source, sent.message_id, callback.message.chat.id)


@router.message(F.photo)
async def on_any_photo(message: Message, state: FSMContext):
    """Приймає фото чека як у стані waiting_screenshot, так і після натискання 'Я оплатив'."""
    data = await state.get_data()
    order_id = data.get("order_id")
    order = storage.get_order(order_id) if order_id else storage.find_latest_open_order_for_user(message.from_user.id)
    if not order:
        order = storage.find_latest_order_for_user(message.from_user.id)
    if not order:
        return
    lang = order.get("lang") if order.get("lang") in T else "uk"
    t = T[lang]

    file_id = message.photo[-1].file_id
    storage.update_order(order["id"], screenshot_file_id=file_id, status="awaiting_review")
    order["screenshot_file_id"] = file_id
    order["status"] = "awaiting_review"

    # Очищуємо стан, щоб клієнт міг далі вільно писати текст
    await state.clear()
    await message.answer(t["screenshot_received"])

    msg_id = await send_initial_admin_card(order, message.from_user)

    file = await bot.get_file(file_id)
    file_bytes = await bot.download_file(file.file_path)
    photo_input = BufferedInputFile(file_bytes.read(), filename="receipt.jpg")

    esc_method = html.escape(format_method_label(order))
    caption = (
        f"📸 Payment screenshot for <b>Order #{html.escape(str(order['id']))}</b>\n"
        f"Method: <b>{esc_method}</b>"
    )
    source = order.get("source", "telegram")
    a_bot, a_chat = admin_target(source)
    sent_photo = await a_bot.send_photo(
        a_chat,
        photo_input,
        caption=caption,
        parse_mode="HTML",
        reply_to_message_id=msg_id,
        reply_markup=admin_order_keyboard(order["id"]),
    )
    storage.save_relay(source, sent_photo.message_id, message.chat.id)


# ---------------------------- two-way free-text relay (buyer -> admin anytime) ----------------------------

@router.message(F.text)
async def on_free_text(message: Message, state: FSMContext):
    """Будь-яке текстове повідомлення (навіть під час очікування чека чи після оплати) летить адміну."""
    await forward_buyer_text_to_admin(message)


async def main():
    log.info("Buyer bot (Bogdan) starting, data dir: %s", storage.DATA_DIR)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())