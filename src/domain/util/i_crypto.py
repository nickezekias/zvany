from abc import ABC, abstractmethod
from datetime import timedelta

class ICrypto(ABC):

    @abstractmethod
    def generate_token(self, data: dict, expires_after: timedelta) -> str:
        pass

    @abstractmethod
    def verify_token(self, token: str) -> dict:
        pass