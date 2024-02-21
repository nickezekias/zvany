from abc import abstractmethod
from src.app.db.models.product_category_orm import ProductCategoryORM

from src.domain.base.i_repository import IRepository
from src.domain.product.product_category import ProductCategory


class IProductCategoryRepository(IRepository[ProductCategoryORM, ProductCategory]):
    @abstractmethod
    def get_by_name(self, name: str) -> ProductCategory | None:
        pass
