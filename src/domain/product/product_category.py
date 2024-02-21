from dataclasses import dataclass
from datetime import datetime

from src.domain.base.entity import Entity


@dataclass
class ProductCategory(Entity):
    name: str  # must be unique
    position: int
    parent: str  # parent category's name
    description: str
    slug: str  # unique not empty
    visible: bool
    created_at: datetime
    updated_at: datetime
    id: str

    def __init__(
        self,
        id: str,
        name: str,
        parent: str,
        slug: str,
        created_at: datetime,
        updated_at: datetime,
        description: str = "",
        position: int = 0,
        visible: bool = True,
    ) -> None:
        super().__init__(id)

        self.name = name
        self.parent = parent
        self.description = description
        self.slug = slug
        self.created_at = created_at
        self.updated_at = updated_at
        self.position = position
        self.visible = visible

        self.validate_is_non_empty_string("name", self.name)
        self.validate_is_non_empty_string("parent", self.parent)
        self.validate_is_non_empty_string("slug", self.slug)
        self.validate_is_datetime("created_at", self.created_at)
        self.validate_is_datetime_gte_min(
            "updated_at", self.updated_at, self.created_at
        )
