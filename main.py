import asyncio
import logging
import config
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import handlers, career_choise

# Создаем диспетчер
#dp = Dispatcher(storage=MemoryStorage())


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(career_choise.router)
    dp.include_router(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
