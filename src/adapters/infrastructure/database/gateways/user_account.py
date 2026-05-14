from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.user_account import UserAccount
from src.application.interfaces import IUserAccountSaver, IUserAccountGetter

from src.adapters.infrastructure.database.models import UserAccount as UserAccountDB


class UserAccountGatewayImpl(IUserAccountGetter, IUserAccountSaver):
    def __init__(self, session: AsyncSession):
        self._session = session

    def save(self, user_account: UserAccount) -> None:
        user = UserAccountDB(
            user_id=user_account.user_id,
            platform=user_account.platform,
            platform_user_id=user_account.platform_user_id,
        )
        self._session.add(user)

    async def get_by_platform_user_id(
        self, user_account_id: str, platform: str
    ) -> UserAccount | None:
        stmnt = select(UserAccountDB).where(
            UserAccountDB.platform_user_id == user_account_id,
            UserAccountDB.platform == platform,
        )
        user_account_db = (await self._session.execute(stmnt)).scalar_one_or_none()
        if user_account_db:
            return UserAccount(
                user_id=user_account_db.user_id,
                platform=user_account_db.platform,
                platform_user_id=user_account_db.platform_user_id,
            )

    async def get_all_by_platform(self, platform: str) -> List[UserAccount]:
        stmnt = select(UserAccountDB).where(UserAccountDB.platform == platform)
        user_accounts_db = (await self._session.execute(stmnt)).all()
        return [
            UserAccount(
                user_id=user_account_db[0].user_id,
                platform=user_account_db[0].platform,
                platform_user_id=user_account_db[0].platform_user_id,
            )
            for user_account_db in user_accounts_db
        ]
