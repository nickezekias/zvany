from abc import ABC, abstractmethod
from typing import Generic, TypeVar

I = TypeVar('I')
O = TypeVar('O')

class Mapper(ABC, Generic[I, O]):
    @abstractmethod
    def mapToDomain(self, param: I) -> O:
        """ Map from external input to domain """
        pass
    
    @abstractmethod
    def mapFromDomain(self, param: O) -> I:
        """ Map from domain model to external input format """
        pass