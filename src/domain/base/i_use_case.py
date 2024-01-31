from abc import ABC, abstractmethod
from typing import Generic, TypeVar

S = TypeVar('S')
T = TypeVar('T')

class IUseCase( ABC, Generic[S, T] ):
    @abstractmethod
    async def execute(self, **payload: S) -> T:
        pass