from dataclasses import dataclass
from datetime import datetime

from src.domain.base.entity import Entity


@dataclass
class ProductImage(Entity):
    """Class to hold product images"""

    alt: str
    height: int
    name: str
    position: int
    src: str
    width: int
    created_at: datetime
    updated_at: datetime
    id: str

    def __init__(
        self,
        # pylint: disable=W0622
        id: str,
        # pylint: enable=W0622
        height: int,
        name: str,
        src: str,
        width: int,
        created_at: datetime,
        updated_at: datetime,
        alt: str = "",
        position: int = 0,
    ) -> None:
        super().__init__(id)

        self.alt = alt
        self.height = height

        self.name = name
        self.validate_is_non_empty_string("name", self.name)

        self.position = position

        self.src = src
        self.validate_is_non_empty_string("src", self.src)

        self.width = width

        self.created_at = created_at
        self.validate_is_datetime("created_at", self.created_at)

        self.updated_at = updated_at
        self.validate_is_datetime_gte_min(
            "updated_at", self.updated_at, self.created_at
        )
