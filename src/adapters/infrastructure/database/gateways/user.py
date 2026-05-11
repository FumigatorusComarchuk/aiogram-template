from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.application.interfaces import UserSaver, UserGetter
from src.domain.user import User, UserRole

from src.adapters.infrastructure.database.models import User as UserDB


class UserGateway(UserSaver, UserGetter):
    def __init__(self, session: AsyncSession):
        self._session = session

    def save(self, user: User) -> None:
        user = UserDB(uuid=user.uuid, role=user.role)
        self._session.add(user)

    async def get_by_uuid(self, uuid: str) -> None | User:
        user_db = (
            await self._session.execute(select(UserDB).where(UserDB.uuid == uuid))
        ).scalar_one_or_none()
        if user_db is not None:
            return User(uuid=user_db.uuid, role=UserRole(user_db.role))
