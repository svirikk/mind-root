# -*- coding: utf-8 -*-
"""
Admin bot — TELEGRAM channel: orders that came through Bogdan.
Run: python admin_bot_telegram.py
Env: BOT_TOKEN, ADMIN_TG_BOT_TOKEN, ADMIN_TG_CHAT_ID, PAYMENT_REQUISITES, DATA_DIR
"""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from admin_actions import build_router

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]                    # Bogdan — used only to message buyers
ADMIN_TG_BOT_TOKEN = os.environ["ADMIN_TG_BOT_TOKEN"]  # this bot
ADMIN_TG_CHAT_ID = int(os.environ["ADMIN_TG_CHAT_ID"])
PAYMENT_REQUISITES = os.environ.get("PAYMENT_REQUISITES", "GE00XXXXXXXXXXXXXXXXXXXX (TBC Bank)")

admin_bot = Bot(token=ADMIN_TG_BOT_TOKEN)
buyer_bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(build_router("telegram", ADMIN_TG_CHAT_ID, buyer_bot, PAYMENT_REQUISITES))


async def main():
    await dp.start_polling(admin_bot)


if __name__ == "__main__":
    asyncio.run(main())
