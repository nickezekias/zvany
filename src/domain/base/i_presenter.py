from abc import ABC, abstractmethod


class IPresenter(ABC):
    @abstractmethod
    def output(self, data: object) -> object:
        pass

    @abstractmethod
    def output_error_server_db_commit(self, details: str | None = None) -> None:
        pass

    @abstractmethod
    def output_error_domain_validation(self, details: dict | str) -> None:
        pass

    @abstractmethod
    def output_error_object_not_found(self, details: dict | str) -> None:
        pass
