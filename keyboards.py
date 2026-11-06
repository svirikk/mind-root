# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from texts import T, LANGS, LANG_BUTTON_LABELS


def lang_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text=LANG_BUTTON_LABELS[code], callback_data=f"lang:{code}")]
        for code in LANGS
    ]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def product_keyboard(lang: str, product_key: str) -> InlineKeyboardMarkup:
    t = T.get(lang, T["en"])
    # Перша кнопка — Замовити, друга — Дізнатися більше
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=t["order_btn"], callback_data=f"order:{product_key}"),
        InlineKeyboardButton(text=t["learn_more_btn"], callback_data=f"learn:{product_key}"),
    ]])


def back_keyboard(lang: str) -> InlineKeyboardMarkup:
    t = T.get(lang, T["en"])
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=t["back_btn"], callback_data="back_to_catalog")
    ]])


def payment_method_keyboard(lang: str, order_id: str) -> InlineKeyboardMarkup:
    t = T.get(lang, T["en"])
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["pay_btn_bank"], callback_data=f"paym:bank:{order_id}")],
        [InlineKeyboardButton(text=t["pay_btn_crypto"], callback_data=f"paym:crypto:{order_id}")],
    ])


def payment_confirm_keyboard(lang: str, order_id: str) -> InlineKeyboardMarkup:
    t = T.get(lang, T["en"])
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["i_paid_btn"], callback_data=f"ipaid:{order_id}")],
        [InlineKeyboardButton(text=t["back_btn"], callback_data=f"payback:{order_id}")],
    ])


def admin_order_keyboard(order_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ Оплачено", callback_data=f"paid:{order_id}"),
        InlineKeyboardButton(text="🔔 Нагадати", callback_data=f"remind:{order_id}"),
        InlineKeyboardButton(text="❌ Невірний чек", callback_data=f"invalid:{order_id}"),
    ]])