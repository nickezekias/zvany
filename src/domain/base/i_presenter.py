from abc import ABC, abstractmethod
from typing import Generic, TypeVar

I = TypeVar('I')
O = TypeVar('O')

class IPresenter(ABC):
    @abstractmethod
    def output(self, data: I) -> O:
        pass