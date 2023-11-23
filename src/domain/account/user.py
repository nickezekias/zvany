from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar

from src.domain.base.entity import Entity

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
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password
        self.token = token
        self.email_verified_at = email_verified_at
        self.phone_verified_at = phone_verified_at
        self.ID_document = ID_document
        self.ID_document_verified_at = ID_document_verified_at
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        super().__init__()

    def verify_email() -> bool:
        pass

    def check_verification_status() -> bool:
        pass

    def full_name(self, locale: str = 'en') -> str:
        if locale == 'en':
            return f'{self.first_name} {self.last_name}'
                
    def active(self) -> bool:
        return self.is_active
