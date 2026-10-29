# -*- coding: utf-8 -*-
"""
Admin bot — WEBSITE channel. Order cards arrive here automatically from web_server.py
the moment someone submits the order form on the site.
Run: python admin_bot_website.py
Env: BOT_TOKEN, ADMIN_WEB_BOT_TOKEN, ADMIN_WEB_CHAT_ID, PAYMENT_REQUISITES, DATA_DIR
"""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from admin_actions import build_router

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_WEB_BOT_TOKEN = os.environ["ADMIN_WEB_BOT_TOKEN"]
ADMIN_WEB_CHAT_ID = int(os.environ.get("ADMIN_WEB_CHAT_ID") or os.environ["ADMIN_TG_CHAT_ID"])
PAYMENT_REQUISITES = os.environ.get("PAYMENT_REQUISITES", "GE00XXXXXXXXXXXXXXXXXXXX (TBC Bank)")

admin_bot = Bot(token=ADMIN_WEB_BOT_TOKEN)
buyer_bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(build_router("website", ADMIN_WEB_CHAT_ID, buyer_bot, PAYMENT_REQUISITES))


async def main():
    await dp.start_polling(admin_bot)


if __name__ == "__main__":
    asyncio.run(main())
