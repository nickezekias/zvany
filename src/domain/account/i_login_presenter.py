from abc import abstractmethod
from src.domain.base.i_presenter import IPresenter

class ILoginPresenter(IPresenter):
    @abstractmethod
    def output_error_user_not_found(self) -> None:
        pass