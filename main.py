import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dishka import make_async_container
from dishka.integrations.aiogram import (
    setup_dishka,
    AiogramProvider,
)

from src.config import Config
from src.adapters.controllers.tg_bot import start_router, admin_router
from src.ioc import AppProvider

config = Config()
container = make_async_container(
    AppProvider(), AiogramProvider(), context={Config: config}
)


def get_telegram_bot() -> Bot:
    bot = Bot(
        token=config.telegram.bot_token,
        default=DefaultBotProperties(parse_mode="Markdown"),
    )
    return bot


def get_telegram_bot_dispatcher() -> Dispatcher:
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_routers(start_router, admin_router)
    setup_dishka(container=container, router=dp, auto_inject=True)
    return dp


async def main():
    bot = get_telegram_bot()
    dp = get_telegram_bot_dispatcher()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
