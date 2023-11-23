from datetime import datetime

from src.domain.base.mapper import Mapper

from src.domain.account.user import User
from src.app.api.api_v1.account.adapter.request.register_request import UserPostRequest
from src.app.api.api_v1.account.adapter.response.user_response import UserPostResponse

from src.app.core.util.date_time_util import DateTimeUtil

class AccountJsonMapper(Mapper[UserPostRequest, User | UserPostResponse]):
    def mapToDomain(self, param: UserPostRequest) -> User:
        now = datetime.now()
        return User(
            id = "",
            avatar = param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            password = param.password,
            token = "",
            email_verified_at = None,
            phone_verified_at = None,
            ID_document = "",
            ID_document_verified_at = None,
            is_active = True,
            created_at = now,
            updated_at = now,
        )

    def mapFromDomain(self, param: User) -> UserPostResponse:
        return UserPostResponse(
            id = param.id,
            avatar = param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            password = param.password,
            email_verified_at = param.email_verified_at,
            phone_verified_at = param.phone_verified_at,
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            is_active = param.is_active,
            created_at = DateTimeUtil.date_to_string(param.created_at),
            updated_at = DateTimeUtil.date_to_string(param.updated_at)
        )