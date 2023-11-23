from abc import ABC as Abstract
from dataclasses import asdict
import uuid


class Entity(Abstract):
    #FIXME: use a factory to initialize uuid instead of entity abstract class
    #FIX: implement a factory pattern
    #FIX: remove the need for an id in the whole system
    #FIX: or use db generated id and refresh models after transaction commit
    id: str = ""
    def __init__(self) -> None:
        if not self.id:
            self.id = uuid.uuid4().hex

    def as_dict(self) -> dict:
        return asdict(self)
