from dishka import Provider, Scope, provide, AnyOf

from src.application.interfaces import (
    UserSaver,
    UserGetter,
    UserAccountGetter,
    UserAccountSaver,
    UserAccountGateway as IUserAccountGateway,
)
from src.adapters.infrastructure.database.gateways import (
    UserGateway,
    UserAccountGateway,
)


class DatabaseGatewaysProvider(Provider):
    user_gateway = provide(
        UserGateway, scope=Scope.REQUEST, provides=AnyOf[UserSaver, UserGetter]
    )
    user_account = provide(
        UserAccountGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[UserAccountGetter,
                       UserAccountSaver, IUserAccountGateway],
    )
