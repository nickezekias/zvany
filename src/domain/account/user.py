from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar

from src.domain.base.entity import Entity
from src.domain.util.date_time_util import DateTimeUtil

@dataclass
class User(Entity):
    avatar: str
    first_name: str
    last_name: str
    email: str
    phone: str
    password: str
    token: str
    email_verified_at: datetime | None
    phone_verified_at: datetime | None
    ID_document: str
    ID_document_verified_at: datetime | None
    is_active: bool
    created_at: datetime
    updated_at: datetime
    id: str # this should be last attribute

    def __init__(
        self,
        id: str,
        avatar: str,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        password: str,
        token: str,
        email_verified_at: datetime | None,
        phone_verified_at: datetime | None,
        ID_document: str,
        ID_document_verified_at: datetime | None,
        is_active: bool,
        created_at: datetime,
        updated_at: datetime
    ) -> None:
        self.id = id
        self.avatar = avatar

        self.first_name = first_name
        self.validate_first_name()

        self.last_name = last_name
        self.validate_last_name()
    
        self.email = email
        self.validate_email()

        self.phone = phone
        self.validate_phone()

        
        self.password = password
        self.validate_password()

        self.token = token

        self.email_verified_at = email_verified_at
        self.validate_email_verified_at()

        self.phone_verified_at = phone_verified_at
        self.validate_phone_verified_at()

        #TODO: Implement verification algorithm
        self.ID_document = ID_document

        self.ID_document_verified_at = ID_document_verified_at
        self.validate_ID_document_verified_at()

        self.is_active = is_active
        self.validate_is_active()

        self.created_at = created_at
        self.updated_at = updated_at
        super().__init__()

    def full_name(self, locale: str = 'en') -> str:
        if locale == 'en':
            return f'{self.first_name} {self.last_name}'
                
    def active(self) -> bool:
        return self.is_active
    
    def is_email_verified(self) -> bool:
        if (self.email_verified_at != None):
            return True
        return False

    def validate_first_name(self) -> None:
        if not isinstance(self.first_name, str) or len(self.first_name) < 3:
            self.errors.append({ "type": "str", "loc": "User, first_name", "msg": "Attribute must be str and have at least 3 characters", "input": self.first_name })

    def validate_last_name(self) -> None:
        if not isinstance(self.last_name, str) or not self.last_name or not len(self.last_name) >= 3:
            self.errors.append({ "type": "str", "loc": "User, last_name", "msg": "Attribute must be str and have at least 3 characters", "input": self.last_name })

    def validate_email(self) -> None:
        #TODO: Implement email validity verification algorithm
        if not isinstance(self.email, str) or not self.email:
            self.errors.append({ "type": "str", "loc": "User, email", "msg": "Attribute must be non-empty str and a valid email", "input": self.email })

    def validate_phone(self) -> None:
        #TODO: Implement better validation for phone numbers
        if not isinstance(self.phone, str) or not self.phone:
            self.errors.append({ "type": "str", "loc": "User, phone", "msg": "Attribute must be non-empty str", "input": self.phone })

    def validate_password(self) -> None:
        if not isinstance(self.password, str) or not len(self.password) >= 8:
            self.errors.append({ "type": "str", "loc": "User, password", "msg": "Attribute must be str and have at least 8 characters", "input": self.password })

    def validate_email_verified_at(self) -> None:
        if not self.email_verified_at == None and not DateTimeUtil.is_valid_date(self.email_verified_at):
            self.errors.append({ "type": "datetime | None", "loc": "User, email_verified_at", "msg": "Attribute must be 'None' or a valid date", "input": self.email_verified_at })

    def validate_phone_verified_at(self) -> None:
        if not self.phone_verified_at == None and not DateTimeUtil.is_valid_date(self.phone_verified_at):
            self.errors.append({ "type": "datetime | None", "loc": "User, phone_verified_at", "msg": "Attribute must be 'None' or a valid date", "input": self.phone_verified_at })

    def validate_ID_document_verified_at(self) -> None:
        if not self.ID_document_verified_at == None and not DateTimeUtil.is_valid_date(self.ID_document_verified_at):
            self.errors.append({ "type": "datetime | None", "loc": "User, ID_document_verified_at", "msg": "Attribute must be 'None' or a valid date", "input": self.ID_document_verified_at })

    def validate_is_active(self) -> None:
        if not isinstance(self.is_active, bool):
            self.errors.append({ "type": "bool", "loc": "User, is_active", "msg": "Attribute must be bool", "input": self.is_active })

    def lazy_validation(self) -> None:
        self.validate_first_name()
        self.validate_last_name()
        self.validate_email()
        self.validate_phone()
        self.validate_password()
        self.validate_email_verified_at()
        self.validate_phone_verified_at()
        self.validate_ID_document_verified_at()
        self.validate_is_active()
        super().lazy_validation()


