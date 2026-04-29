from abc import abstractmethod
from typing import Protocol

from src.domain.user_account import UserAccount


class UserAccountSaver(Protocol):
    @abstractmethod
    def save(self, user_account: UserAccount) -> None: ...


class UserAccountGetter(Protocol):
    @abstractmethod
    async def get_by_platform_user_id(
        self, user_account_id: str
    ) -> UserAccount | None: ...


class UserAccountGateway(UserAccountSaver, UserAccountGetter, Protocol):
    ...
