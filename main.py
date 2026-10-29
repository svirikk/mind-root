# -*- coding: utf-8 -*-
"""
One process, one Railway service, one volume:
  - web server (site + POST /api/order)
  - Bogdan (buyer bot)
  - Admin bot — Telegram channel
  - Admin bot — Website channel
  - Admin bot — Instagram channel (only if ADMIN_IG_BOT_TOKEN is set)

If one bot fails (e.g. a wrong token), it's logged and retried; the others keep running.
Run: python main.py
"""
import asyncio
import logging
import os

from aiohttp import web

import admin_bot_telegram
import admin_bot_website
import buyer_bot
import web_server

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("main")


async def supervised(name: str, dp, bot):
    """Keep one bot polling; never let its failure take the others down."""
    while True:
        try:
            log.info("starting %s", name)
            await dp.start_polling(bot, handle_signals=False)
            return
        except asyncio.CancelledError:
            raise
        except Exception:
            log.exception("%s crashed, restarting in 15s", name)
            await asyncio.sleep(15)


async def main():
    runner = web.AppRunner(web_server.make_app())
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", web_server.PORT).start()
    log.info("web server listening on :%s", web_server.PORT)

    bots = [
        ("buyer_bot (Bogdan)", buyer_bot.dp, buyer_bot.bot),
        ("admin_telegram", admin_bot_telegram.dp, admin_bot_telegram.admin_bot),
        ("admin_website", admin_bot_website.dp, admin_bot_website.admin_bot),
    ]
    if os.environ.get("ADMIN_IG_BOT_TOKEN"):
        import admin_bot_instagram
        bots.append(("admin_instagram", admin_bot_instagram.dp, admin_bot_instagram.bot))

    try:
        await asyncio.gather(*(supervised(n, dp, b) for n, dp, b in bots))
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
