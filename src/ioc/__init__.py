from .database import DatabaseProvider
from .message import MessageGatewayProvider
from .interactors import InteractorsProvider
from .uuid import UUIDProvider


class AppProvider(DatabaseProvider, MessageGatewayProvider, UUIDProvider, InteractorsProvider):
    pass
