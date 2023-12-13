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
    errors: list[dict] = []

    def __init__(self) -> None:
        if not self.id:
            self.id = uuid.uuid4().hex

        # if class has created_at attr, check created_at is valid date
        self.validate_created_at()
        
        # if class has update_at attr, check updated_at is valid date
        self.validate_updated_at()
        
        # trigger attributes validation
        self.validate()

    def validate(self) -> None:
        if len(self.errors) > 0:
            raise ValueError(self.errors)


    def as_dict(self) -> dict:
        return asdict(self)

    def validate_created_at(self) -> None:
        try:
            if not isinstance(self.created_at, datetime):
                    self.errors.append({ "type": "datetime", "loc": "created_at", "msg": "attribute should be a valid datetime", "input": self.created_at })
        except AttributeError:
            pass

    def validate_updated_at(self) -> None:
        try:
            if self.updated_at:
                if not isinstance(self.updated_at, datetime):
                    self.errors.append({ "type": "datetime", "loc": "updated_at", "msg": "attribute should be a valid datetime", "input": self.updated_at })
        except AttributeError:
            pass

    def lazy_validation(self) -> None:
        self.validate_created_at()
        self.validate_updated_at()
        self.validate()