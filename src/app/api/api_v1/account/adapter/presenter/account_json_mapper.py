from datetime import datetime

from src.domain.base.mapper import Mapper

from src.domain.account.user import User
from src.app.api.api_v1.account.adapter.request.register_request import UserPostRequest
from src.app.api.api_v1.account.adapter.response.user_response import UserPostResponse

from src.domain.util.date_time_util import DateTimeUtil

class AccountJsonMapper(Mapper[UserPostRequest, User | UserPostResponse]):
    def map_to_domain(self, param: UserPostRequest) -> User:
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
    
    def map_to_domain_list(self, params: list[UserPostRequest]) -> list[User]:
        entities: list[User] = []

        for param in params:
            entities.append(self.map_to_domain(param))

        return entities

    def map_from_domain(self, param: User) -> UserPostResponse:
        email_verified_at = param.email_verified_at
        phone_verified_at = param.phone_verified_at
        ID_document_verified_at = param.ID_document_verified_at
        if (email_verified_at):
            email_verified_at = DateTimeUtil.date_to_string(email_verified_at)
        if (phone_verified_at):
            phone_verified_at = DateTimeUtil.date_to_string(phone_verified_at)
        if (ID_document_verified_at):
            ID_document_verified_at = DateTimeUtil.date_to_string(ID_document_verified_at)
        return UserPostResponse(
            id = param.id,
            avatar = param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            email_verified_at = email_verified_at,
            phone_verified_at = phone_verified_at,
            ID_document = param.ID_document,
            ID_document_verified_at = ID_document_verified_at,
            is_active = param.is_active,
            created_at = DateTimeUtil.date_to_string(param.created_at),
            updated_at = DateTimeUtil.date_to_string(param.updated_at)
        )
    
    def map_from_domain_list(self, params: list[User]) -> list[UserPostResponse]:
        res_list: list[UserPostResponse] = []

        for param in params:
            res_list.append(self.map_from_domain(param))

        return res_list