from dataclasses import dataclass
from datetime import datetime

from src.domain.base.entity import Entity


@dataclass
class PRToken(Entity):
    email: str
    token: str
    created_at: datetime
    used_at: datetime | None
    ip_address: str | None
    user_agent: str | None
    id: str  # this should be last attribute

    def __init__(
        self,
        id: str,
        email: str,
        token: str,
        created_at: datetime,
        used_at: datetime | None,
        ip_address: str | None,
        user_agent: str | None,
    ) -> None:
        super().__init__(id)
        self.email = email
        self.token = token
        self.created_at = created_at
        self.used_at = used_at
        self.ip_address = ip_address
        self.user_agent = user_agent

    def is_used(self) -> bool:
        return self.used_at != None

    def set_as_used(self) -> None:
        self.used_at = datetime.now()
