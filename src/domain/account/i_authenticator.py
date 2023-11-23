from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Any

from src.domain.account.user import User


class IAuthenticator(ABC):

    @abstractmethod
    def create_access_token(
        self, data: dict
    ) -> str:
        pass

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        pass

    @abstractmethod
    def get_password_hash(self, password: str) -> str:
        pass

    """ Get current user """
    @abstractmethod
    def user() -> User:
        pass
