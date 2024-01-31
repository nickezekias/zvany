from abc import ABC, abstractmethod
from typing import Generic, TypeVar

I = TypeVar('I')
O = TypeVar('O')

class IPresenter(ABC):
    @abstractmethod
    def output(self, data: I) -> O:
        pass

    @abstractmethod
    def output_error_server_db_commit(self, details: str | None  = None) -> None:
        pass

    @abstractmethod
    def output_error_domain_validation(self, details: dict) -> None:
        pass