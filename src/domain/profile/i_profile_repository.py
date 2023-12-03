from abc import abstractmethod

from src.domain.base.i_repository import IRepository
from src.domain.account.user import User
from src.app.db.models.user_orm import UserORM

class IProfileRepository(IRepository[UserORM, User]):
    pass