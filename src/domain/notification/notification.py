from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, TypeVar
from src.domain.base.background_tasks import BackgroundTasks

TEntity = TypeVar("TEntity")

class Notification(ABC, Generic[TEntity]):
    _notifiable: TEntity
    _background_tasks: BackgroundTasks

    """ Possible channels on which to send notifications """
    class Channels(Enum):
        DATABASE = 1
        EMAIL = 2
        SMS = 3

    def __init__(self, background_tasks: BackgroundTasks) -> None:
        self._background_tasks = background_tasks

    """The channel by which the email is sent: mail, database, sms, ..."""
    #[]FIXME: create an enum class for channels
    channel: Channels = Channels.EMAIL

    @property
    def notifiable(self) -> TEntity:
        return self._notifiable

    @notifiable.setter
    def notifiable(self, value: TEntity) -> None:
        self._notifiable = value

    @abstractmethod    
    def via(self, channels: list[Channels] = [Channels.EMAIL]):
        pass

    """ def to_array(entity: TEntity):
        pass """

    @abstractmethod
    def to_mail(self):
        pass

    """ def to_sms(entity: TEntity):
        pass """

    async def send(self):
        if not len(self.via()) > 0:
            raise ValueError("errors.api.notification.noDefinedChannel")
        else:
            if Notification.Channels.EMAIL in self.via():
                self._background_tasks.add_task(self.to_mail)
