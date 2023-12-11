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
    def output_errors_email_exists(self) -> None:
        pass

    @abstractmethod
    def output_errors_phone_exists(self) -> None:
        pass

    @abstractmethod
    def output_errors_user_data_duplicate(self) -> None:
        pass

    @abstractmethod
    def output_errors_invalid_data(self) -> None:
        pass