
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TEntity = TypeVar('TEntity')
ORMEntity = TypeVar('ORMEntity')
TQuery = TypeVar('TQuery')

class IRepository(ABC, Generic[ORMEntity, TEntity]):
    @abstractmethod
    def get(self,id: int | str) -> TEntity:
        pass

    @abstractmethod
    def get_all(self) -> list[TEntity]:
        pass

    @abstractmethod
    def find(self,query: TQuery)-> list[TEntity]:
        pass

    @abstractmethod
    def add(self,entity: TEntity) -> None:
        pass

    @abstractmethod
    def add_range(self, entities: list[TEntity], NO_COMMIT=False) -> list[TEntity]:
        pass

    @abstractmethod
    def update(self, entity: TEntity) -> None:
        pass

    @abstractmethod
    def remove(self, entity: TEntity) -> None:
        pass

    @abstractmethod
    def remove_range(self, entities: list[TEntity]) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def refresh(self) -> None:
        pass