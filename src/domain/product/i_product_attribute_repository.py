from abc import abstractmethod

from src.domain.base.i_repository import IRepository
from src.domain.product.product_attribute import ProductAttribute
from src.app.db.models.product_attribute_orm import ProductAttributeORM


class IProductAttributeRepository(IRepository[ProductAttributeORM, ProductAttribute]):
    @abstractmethod
    def get_by_name(self, name: str) -> ProductAttribute | None:
        pass
