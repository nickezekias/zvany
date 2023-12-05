from abc import ABC, abstractmethod
from typing import TypeVar
TUserEntity = TypeVar('TUserEntity')

class IProfilePresenter(ABC):
    
    @abstractmethod
    def output_view_current_user(self, user:TUserEntity) -> dict:
        pass