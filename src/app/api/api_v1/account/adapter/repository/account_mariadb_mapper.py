from src.domain.util.date_time_util import DateTimeUtil

from src.domain.base.mapper import Mapper
from src.domain.account.user import User
from src.app.db.models.user_orm import UserORM
class AccountMariaDbMapper(Mapper[UserORM, User]):
    def map_to_domain(self, param: UserORM) -> User:
        created_at = param.created_at
        if (isinstance(created_at, str)):
            created_at = DateTimeUtil.string_to_date(param.created_at),
        updated_at = param.updated_at
        if (isinstance(updated_at, str)):
            updated_at = DateTimeUtil.string_to_date(param.updated_at),
        user =  User(
            id = param.id,
            avatar = param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            password = param.password,
            token = param.token,
            email_verified_at = param.email_verified_at,
            phone_verified_at = param.phone_verified_at,
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            is_active = param.is_active,
            created_at = created_at,
            updated_at = updated_at
        )
        return user
        

    def map_to_domain_list(self, params: list[UserORM]) -> list[UserORM]:
        users: list[User]
        for param in params:
            users.append(self.map_to_domain(param))
        return users

    def map_from_domain(self, param: User) -> UserORM:
        return UserORM(
            id=param.id,
            avatar=param.avatar,
            first_name = param.first_name,
            last_name = param.last_name,
            email = param.email,
            phone = param.phone,
            password = param.password,
            token = param.token,
            email_verified_at = param.email_verified_at,
            phone_verified_at = param.phone_verified_at,
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            is_active = param.is_active,
            created_at = DateTimeUtil.date_to_string(param.created_at),
            updated_at = DateTimeUtil.date_to_string(param.updated_at)
        )

    def map_from_domain_list(self, params: list[User]) -> list[UserORM]:
        orms: list[UserORM]
        for param in params:
            orms.append(self.map_from_domain(param))
        return orms
