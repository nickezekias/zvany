from abc import ABC as Abstract
from dataclasses import asdict
from datetime import datetime
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

        # if class has created_at attr, check created_at is valid date
        try:
            if not isinstance(self.created_at, datetime):
                raise ValueError("created_at must be a valid datetime")
        except AttributeError:
            pass
        
        # if class has update_at attr, check updated_at is valid date
        try:
            if self.updated_at:
                if not isinstance(self.updated_at, datetime):
                    raise ValueError("updated_at must be a valid datetime")
        except AttributeError:
            pass

    def as_dict(self) -> dict:
        return asdict(self)
