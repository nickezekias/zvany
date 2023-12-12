from sqlalchemy.orm import Session
from datetime import datetime
from src.app.db.repository import Repository
from src.domain.account.i_account_repository import IAccountRepository
from src.app.api.api_v1.account.adapter.repository.account_mariadb_mapper import AccountMariaDbMapper

from src.domain.account.user import User
from src.domain.account.pr_token import PRToken
from src.app.db.models.user_orm import UserORM
from src.app.db.models.pr_token_orm import PRTokenORM

class AccountMariaDbRepository(Repository[UserORM, User], IAccountRepository):
    db: Session
    mapper: AccountMariaDbMapper

    def __init__(self, db: Session, mapper = AccountMariaDbMapper()) -> None:
        super().__init__(db, mapper)
        self.db = db
        self.mapper = mapper

    #[]FIXME: Find a way to handle this in a different class
    """ Add password reset token to db """
    def add_pr_token(self, data: PRToken) -> None:
        from src.domain.util.date_time_util import DateTimeUtil
        pr_token_orm = PRTokenORM(
            id=data.id,
            email=data.email,
            token=data.token,
            created_at=DateTimeUtil.date_to_string(data.created_at),
            used_at=data.used_at,
            ip_address=data.ip_address,
            user_agent=data.user_agent
        )
        self.db.add(pr_token_orm)

    #[]FIXME: Find a way to handle this in a different class
    """ Get Password Reset Token for a given token """
    def get_pr_token(self, token: str) -> dict | None:
        res = self.db.query(PRTokenORM).filter(PRTokenORM.token == token).one_or_none()
        if res:
            data = res.asdict()
            return PRToken(
                id=data["id"],
                email=data["email"],
                token=data["token"],
                created_at=data["created_at"],
                used_at=data["used_at"],
                ip_address=data["ip_address"],
                user_agent=data["user_agent"]
            )
        return None


    def get(self, id: int | str) -> User:
        orm: UserORM =  self.db.query(UserORM).get(id)
        if orm:
            return self.mapper.mapToDomain(orm)
        return None

    def get_by_email(self, email: str) -> User | None:
        orm = self.db.query(UserORM).filter(UserORM.email == email).one_or_none()
        if orm:
            return self.mapper.mapToDomain(orm)
        return None
    
    def get_by_phone(self, phone: str) -> User | None:
        orm = self.db.query(UserORM).filter(UserORM.phone == phone).one_or_none()
        if orm:
            return self.mapper.mapToDomain(orm)
        return None

    def update(self, user: User) -> User:
        user.updated_at = datetime.now()
        user_query = self.db.query(UserORM).filter_by(id=user.id)
        user_query.update(user.as_dict())
        return self.get(user.id)
    
    def update_pr_token(self, data: PRToken) -> None:
        query = self.db.query(PRTokenORM).filter_by(id=data.id)
        query.update(data.as_dict())
    
    def set_email_as_verified(self, user: User) -> None:
        user.email_verified_at = datetime.now()
        self.update(user)