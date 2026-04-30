from src.domain.user import User
from src.domain.user_account import UserAccount

from src.application.interfaces import (
    UserSaver,
    UserAccountGateway,
    MessageGateway,
    UUIDGenerator,
    DBSession,
)
from src.application.dto import StartResponseDTO, StartRequestDTO


class StartInteractor:
    def __init__(
        self,
        uuid_generator: UUIDGenerator,
        db_session: DBSession,
        message_gateway: MessageGateway,
        user_gateway: UserSaver,
        user_account_gateway: UserAccountGateway,
    ):
        self._uuid_generator = uuid_generator
        self._db_session = db_session
        self._message_gateway = message_gateway
        self._user_gateway = user_gateway
        self._user_account_gateway = user_account_gateway

    async def __call__(self, dto: StartRequestDTO) -> StartResponseDTO:
        if dto.platform is not None:
            if dto.platform_user_id is not None:
                user_account = await self._user_account_gateway.get_by_platform_user_id(
                    dto.platform_user_id
                )
                if user_account is None:
                    uuid = str(self._uuid_generator())
                    user = User(uuid=uuid)
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
