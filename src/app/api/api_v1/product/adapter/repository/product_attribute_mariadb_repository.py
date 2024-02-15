from sqlalchemy.orm import Session

from src.app.api.api_v1.product.adapter.repository.product_attribute_mariadb_mapper import ProductAttributeMariaDbMapper
from src.app.db.models.product_attribute_orm import ProductAttributeORM
from src.app.db.repository import Repository
from src.domain.base.mapper import Mapper
from src.domain.product.product_attribute import ProductAttribute

class ProductAttributeMariaDbRepository(Repository[ProductAttributeORM, ProductAttribute]):
    db: Session
    mapper: Mapper

    def __init__(self, db: Session, mapper: Mapper = ProductAttributeMariaDbMapper()) -> None:
        super().__init__(db, mapper)
        self.db = db
        self.mapper = mapper

    # pylint: disable=W0622
    def get(self, id: str) -> None:
        orm: ProductAttributeORM | None = self.db.query(ProductAttributeORM).get(id)
        if orm:
            return self.mapper.map_to_domain(orm)
        else: return None

    def get_all(self) -> list[ProductAttribute]:
        orm_list: list[ProductAttributeORM] = self.db.query(ProductAttributeORM).all()
        return self.mapper.map_to_domain_list(orm_list)
