from src.domain.user import User, UserRole
from src.domain.user_account import UserAccount

from src.application.interfaces import (
    IUserSaver,
    IUserAccountGateway,
    IMessageGateway,
    IUUIDGenerator,
    IDBSession,
)
from src.application.dto import StartResponseDTO, StartRequestDTO


class StartInteractor:
    def __init__(
        self,
        uuid_generator: IUUIDGenerator,
        db_session: IDBSession,
        message_gateway: IMessageGateway,
        user_gateway: IUserSaver,
        user_account_gateway: IUserAccountGateway,
    ):
        self._uuid_generator = uuid_generator
        self._db_session = db_session
        self._message_gateway = message_gateway
        self._user_gateway = user_gateway
        self._user_account_gateway = user_account_gateway

    async def __call__(self, dto: StartRequestDTO) -> StartResponseDTO:
        user_account = await self._user_account_gateway.get_by_platform_user_id(
            user_account_id=dto.platform_user_id, platform=dto.platform
        )
        if user_account is None:
            uuid = str(self._uuid_generator())
            user = User(uuid=uuid, role=UserRole.USER)
            self._user_gateway.save(user)
            user_account = UserAccount(
                user_id=user.uuid,
                platform=dto.platform,
                platform_user_id=dto.platform_user_id,
            )
            self._user_account_gateway.save(user_account)
            await self._db_session.commit()
        message = self._message_gateway.start()
        return StartResponseDTO(text=message.text)
