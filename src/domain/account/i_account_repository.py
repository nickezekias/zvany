from abc import abstractmethod

from src.domain.base.i_repository import IRepository
from src.domain.account.user import User
from src.domain.account.pr_token import PRToken
from src.app.db.models.user_orm import UserORM

class IAccountRepository(IRepository[UserORM, User]):
    #[]FIXME: Find a way to handle this in a different class
    @abstractmethod
    def add_pr_token(self, data: PRToken) -> None:
        pass

    #[]FIXME: Find a way to handle this in a different class
    @abstractmethod
    def get_pr_token(self, token: str) -> dict | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def get_by_phone(self, phone: str) -> User | None:
        pass

    @abstractmethod
    def set_email_as_verified(self, user: User) -> None:
        pass
    
    @abstractmethod
    def update_pr_token(self, data: PRToken) -> None:
        pass

    # def isAuthenticated
    
    # def getCurrentUser

    # def forgotPassword

    # def logout
    
    