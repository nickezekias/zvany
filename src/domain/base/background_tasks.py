from abc import ABC, abstractmethod
# from typing import Generic, TypeVar

class BackgroundTasks(ABC):
    @abstractmethod
    def add_task(self, *arg, **kwargs) -> None:
        pass