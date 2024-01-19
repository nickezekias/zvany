from abc import ABC, abstractmethod
from typing import Generic, TypeVar

I = TypeVar('I')
O = TypeVar('O')

class Mapper(ABC, Generic[I, O]):
    @abstractmethod
    def map_to_domain(self, param: I) -> O:
        """ Map from external input to domain """
        pass

    @abstractmethod
    def map_to_domain_list(self, params: list[I]) -> list[O]:
        """ Map from external input to domain """
        pass
    
    @abstractmethod
    def map_from_domain(self, param: O) -> I:
        """ Map from domain model to external input format """
        pass

    @abstractmethod
    def map_from_domain_list(self, params: list[O]) -> list[I]:
        """ Map from domain model to external input format """
        pass
