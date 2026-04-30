from typing import Protocol
from abc import abstractmethod

from src.domain.message import Message


class MessageGateway(Protocol):
    @abstractmethod
    def start(self) -> Message: ...
