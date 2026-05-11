from typing import Protocol
from abc import abstractmethod

from src.domain.message import Message


class MessageGateway(Protocol):
    @abstractmethod
    def start(self) -> Message: ...

    def get_number_of_users(self, number_of_users: int) -> Message: ...

    def you_have_no_rights(self) -> Message: ...
