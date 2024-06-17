
import asyncio
import logging

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import router
from utils import bot

from app.middlewares.check_user import CheckInDB
async def start_bot():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    dp.message.middleware(CheckInDB())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

def start_web_server():
    app = create_app()
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_bot())
    print("Telegram Bot is running.")








