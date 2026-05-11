from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from src.application.dto import GetNumberOfUsersRequestDTO, FromUserDTO
from src.application.interactors import GetNumberOfUsersInteractor

admin_router = Router()


@admin_router.message(Command("get_number_of_users"))
async def get_number_of_users(
    message: Message, interactor: FromDishka[GetNumberOfUsersInteractor]
):
    resp_dto = await interactor(
        GetNumberOfUsersRequestDTO(
            platform="telegram",
            from_user=FromUserDTO(
                platform="telegram", user_id=str(message.from_user.id)
            ),
        )
    )
    await message.answer(resp_dto.text)
