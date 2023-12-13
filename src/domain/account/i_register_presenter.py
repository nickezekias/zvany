from abc import abstractmethod
from typing import TypeVar

from src.domain.base.i_presenter import IPresenter

TUserEntity = TypeVar('TUserEntity')
TRegisterResponse = TypeVar('TRegisterResponse')

class IRegisterPresenter(IPresenter):

    @abstractmethod
    def output(self, user: TUserEntity) -> TRegisterResponse:
        pass

    @abstractmethod
    def output_error_email_exists(self) -> None:
        pass

    @abstractmethod
    def output_error_phone_exists(self) -> None:
        pass

    @abstractmethod
    def output_error_user_data_duplicate(self) -> None:
        pass

    @abstractmethod
    def output_error_invalid_data(self) -> None:
        pass