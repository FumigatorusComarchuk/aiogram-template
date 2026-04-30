from src.domain.message import Message
from src.application.interfaces import MessageGateway as IMessageGateway


class MessageGateway(IMessageGateway):
    def start(self) -> Message:
        return Message(text="hello")
