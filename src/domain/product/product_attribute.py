from dataclasses import dataclass
from datetime import datetime

from src.domain.base.entity import Entity


@dataclass
class ProductAttribute(Entity):
    """Class to hold product attributes"""

    name: str
    position: int
    values: set[str]  # values of the attr
    variation: bool  # can attr be used for product variations
    visible: bool  # if attr is visible in additional information tab
    created_at: datetime
    updated_at: datetime
    id: str

    def __init__(
        self,
        # pylint: disable=W0622
        id: str,
        # pylint: enable=W0622
        name: str,
        values: set[str],
        created_at: datetime,
        updated_at: datetime,
        position: int = 0,
        variation: bool = True,
        visible: bool = True,
    ) -> None:
        self.id = id

        self.name = name
        self.validate_is_non_empty_string("name", name)

        self.values = values
        self.validate_is_non_empty_set("values", self.values)

        self.created_at = created_at
        self.validate_is_datetime("created_at", self.created_at)

        self.updated_at = updated_at
        self.validate_is_datetime_gte_min(
            "updated_at", self.updated_at, self.created_at
        )

        self.position = position
        self.variation = variation
        self.visible = visible

        super().__init__()
