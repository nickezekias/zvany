from abc import ABC, abstractmethod
from typing import TypeVar

I = TypeVar('I')
O = TypeVar('O')

class ILoginPresenter(ABC):
    @abstractmethod
    def output(self, data: I) -> O:
        pass

    @abstractmethod
    def output_error_user_not_found(self) -> None:
        pass