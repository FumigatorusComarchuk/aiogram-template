from src.domain.user import UserRole

from src.application.interfaces import IUserGetter, IUserAccountGetter, IMessageGateway
from src.application.dto import GetNumberOfUsersResponseDTO, GetNumberOfUsersRequestDTO


class GetNumberOfUsersInteractor:
    def __init__(
        self,
        user_gateway: IUserGetter,
        user_account_gateway: IUserAccountGetter,
        message_gateway: IMessageGateway,
    ):
        self._user_gateway = user_gateway
        self._user_account_gateway = user_account_gateway
        self._message_gateway = message_gateway

    async def __call__(
        self, dto: GetNumberOfUsersRequestDTO
    ) -> GetNumberOfUsersResponseDTO:
        request_initiator_account = (
            await self._user_account_gateway.get_by_platform_user_id(
                user_account_id=dto.from_user.user_id, platform=dto.from_user.platform
            )
        )
        request_initiator = await self._user_gateway.get_by_uuid(
            request_initiator_account.user_id
        )
        if request_initiator.role == UserRole.MAIN_ADMIN:
            number_of_users = len(
                await self._user_account_gateway.get_all_by_platform(dto.platform)
            )
            message = self._message_gateway.get_number_of_users(
                number_of_users)
        else:
            message = self._message_gateway.you_have_no_rights()
        return GetNumberOfUsersResponseDTO(text=message.text)
