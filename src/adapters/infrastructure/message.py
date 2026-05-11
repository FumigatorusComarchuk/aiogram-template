from src.domain.message import Message
from src.application.interfaces import MessageGateway as IMessageGateway


class MessageGateway(IMessageGateway):
    def start(self) -> Message:
        return Message(text="Hello")

    def get_number_of_users(self, number_of_users: int) -> Message:
        return Message(text=f"Number of users: {number_of_users}")

    def you_have_no_rights(self) -> Message:
        return Message(text="You have no rights")
