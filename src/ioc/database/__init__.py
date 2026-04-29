from .session import DatabaseSessionProvider
from .gateways import DatabaseGatewaysProvider


class DatabaseProvider(DatabaseSessionProvider, DatabaseGatewaysProvider):
    pass
