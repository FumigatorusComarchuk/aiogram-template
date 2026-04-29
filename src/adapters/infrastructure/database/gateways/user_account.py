from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.user_account import UserAccount
from src.application.interfaces import UserAccountSaver, UserAccountGetter

from src.adapters.infrastructure.database.models import UserAccount as UserAccountDB


class UserAccountGateway(UserAccountGetter, UserAccountSaver):
    def __init__(self, session: AsyncSession):
        self._session = session

    def save(self, user_account: UserAccount) -> None:
        user = UserAccountDB(
            user_id=user_account.user_id,
            platform=user_account.platform,
            platform_user_id=user_account.platform_user_id,
        )
        self._session.add(user)

    async def get_by_platform_user_id(self, user_account_id: str) -> UserAccount | None:
        stmnt = select(UserAccountDB).where(
            UserAccountDB.platform_user_id == user_account_id
        )
        user_account_db = (await self._session.execute(stmnt)).scalar_one_or_none()
        if user_account_db:
            return UserAccount(
                user_id=user_account_db.user_id,
                platform=user_account_db.platform,
                platform_user_id=user_account_db.platform_user_id,
            )
