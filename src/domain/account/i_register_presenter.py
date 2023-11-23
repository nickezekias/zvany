from abc import ABC, abstractmethod
from typing import TypeVar

TUserEntity = TypeVar('TUserEntity')
TRegisterResponse = TypeVar('TRegisterResponse')

class IRegisterPresenter(ABC):

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