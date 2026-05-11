from abc import abstractmethod
from typing import Protocol

from src.domain.user import User


class IUserSaver(Protocol):
    @abstractmethod
    def save(self, user: User) -> None: ...


class IUserGetter(Protocol):
    @abstractmethod
    async def get_by_uuid(self, uuid: str) -> None | User: ...
