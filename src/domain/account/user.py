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

        if not isinstance(first_name, str) and not len(first_name) >= 3:
            raise ValueError("first_name must be str and have at least 3 characters")
        else:
            self.first_name = first_name

        if not isinstance(last_name, str) and not len(last_name) >= 3:
            raise ValueError("last_name must be str and have at least 3 characters")
        else:
            self.last_name = last_name
    
        #TODO: Implement email validity verification algorithm
        if not isinstance(email, str) and not email != "":
            raise ValueError("email must be str")
        else:
            self.email = email

        if not isinstance(phone, str) and not phone != "":
            raise ValueError("phone must be a non-empty str")
        else:
            self.phone = phone

        if not isinstance(password, str) and not len(password) >= 8:
            raise ValueError("password must be str and have at least 8 characters")
        else:
            self.password = password

        self.token = token

        if not email_verified_at == None and DateTimeUtil.is_valid_date(email_verified_at):
            raise ValueError("email_verified_at must be 'None' or a valid date")
        else:
            self.email_verified_at = email_verified_at

        if not not phone_verified_at == None and not DateTimeUtil.is_valid_date(phone_verified_at):
            raise ValueError("phone_verified_at must be 'None' or a valid date")
        else:
            self.phone_verified_at = phone_verified_at

        #TODO: Implement verification algorithm
        self.ID_document = ID_document

        if not ID_document_verified_at == None and not DateTimeUtil.is_valid_date(ID_document_verified_at):
            raise ValueError("ID_document_verified_at must be 'None' or a valid date")
        else:
            self.ID_document_verified_at = ID_document_verified_at

        if not isinstance(is_active, bool):
            raise ValueError("is_active must be a boolean")
        else:
            self.is_active = is_active

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
