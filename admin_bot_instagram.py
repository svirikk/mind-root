# -*- coding: utf-8 -*-
"""
Admin bot — INSTAGRAM CHANNEL. You log Instagram orders here manually with /new,
since there's no automated bot on the Instagram side. Tracks status, shares /stats
with the other two channels via the common storage files.

Run: python admin_bot_instagram.py
Required env vars: ADMIN_IG_BOT_TOKEN, DATA_DIR (optional)
"""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from manual_bot_core import build_router

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("admin_bot_instagram")

ADMIN_IG_BOT_TOKEN = os.environ["ADMIN_IG_BOT_TOKEN"]

bot = Bot(token=ADMIN_IG_BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(build_router(source="instagram"))


async def main():
    log.info("Instagram admin bot starting")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
