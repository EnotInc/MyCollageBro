import asyncio
import os

from routers.callbacks import rout_callbacks
from routers.comands import rout_commands
from routers.messages import rout_messages

from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    try:
        dp.include_router(rout_callbacks)
        dp.include_router(rout_commands)
        dp.include_router(rout_messages)
        await dp.start_polling(bot)
    except:
         print("Bot Got Stopped")

if __name__ == "__main__":
        load_dotenv()
        asyncio.run(main())
