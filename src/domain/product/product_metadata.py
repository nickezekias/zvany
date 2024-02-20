from dataclasses import dataclass

from src.domain.base.entity import Entity

@dataclass
class ProductMetadata(Entity):
    """Class to hold product meta for SEO, it's dependent and unique to each product"""
    key: str # meta key
    value: str # meta value
    id: str

    def __init__(
        self,
        # pylint: disable=W0622
        id: str,
        # pylint: enable=W0622
        key: str,
        value: str
    ) -> None:
        super().__init__(id)
        self.key = key
        self.value = value

        self.validate_is_non_empty_string("key", self.key)
        self.validate_is_non_empty_string("value", self.value)
