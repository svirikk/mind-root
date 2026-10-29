# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from texts import T, LANGS, LANG_BUTTON_LABELS


def lang_keyboard() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text=LANG_BUTTON_LABELS[c], callback_data=f"lang:{c}")] for c in LANGS]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def product_keyboard(lang: str, product: str) -> InlineKeyboardMarkup:
    t = T[lang]
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=t["order_btn"], callback_data=f"order:{product}"),
        InlineKeyboardButton(text=t["learn_more_btn"], callback_data=f"learn:{product}"),
    ]])


def back_keyboard(lang: str) -> InlineKeyboardMarkup:
    t = T[lang]
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=t["back_btn"], callback_data="back_to_catalog")
    ]])


def admin_order_keyboard(order_id: int) -> InlineKeyboardMarkup:
    """For 'telegram' source: these buttons message the buyer directly through Bogdan."""
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ Оплачено", callback_data=f"paid:{order_id}"),
        InlineKeyboardButton(text="🔔 Нагадати", callback_data=f"remind:{order_id}"),
        InlineKeyboardButton(text="❌ Невірний чек", callback_data=f"invalid:{order_id}"),
    ]])


def manual_order_keyboard(order_id: int) -> InlineKeyboardMarkup:
    """For 'instagram' / 'website' sources: there's no live Telegram chat with the buyer,
    so this just tracks status and hands you ready-to-copy text instead of auto-sending it."""
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ Оплачено", callback_data=f"paid:{order_id}"),
        InlineKeyboardButton(text="📋 Текст нагадування", callback_data=f"remind:{order_id}"),
    ]])
