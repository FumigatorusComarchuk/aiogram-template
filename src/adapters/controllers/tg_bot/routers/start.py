from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from src.application.dto import StartRequestDTO
from src.application.interactors import StartInteractor

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message, interactor: FromDishka[StartInteractor]):
    req_dto = StartRequestDTO(
        platform="telegram", platform_user_id=str(message.from_user.id)
    )
    resp_dto = await interactor(req_dto)
    await message.answer(resp_dto.text)
