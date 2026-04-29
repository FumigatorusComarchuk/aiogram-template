from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces import UserSaver
from src.domain.user import User

from src.adapters.infrastructure.database.models import User as UserDB


class UserGateway(
    UserSaver,
):
    def __init__(self, session: AsyncSession):
        self._session = session

    def save(self, user: User) -> None:
        user = UserDB(uuid=user.uuid)
        self._session.add(user)
