from abc import abstractmethod
from typing import TypeVar
from src.domain.base.i_presenter import IPresenter

TUserEntity = TypeVar('TUserEntity')

class IProfilePresenter(IPresenter):
    
    @abstractmethod
    def output_view_current_user(self, user:TUserEntity) -> dict:
        pass