from datetime import datetime

from sqlalchemy.orm import Session

from src.app.api.api_v1.product.adapter.repository.product_attribute_mariadb_mapper import (
    ProductAttributeMariaDbMapper,
)
from src.app.db.models.product_attribute_orm import ProductAttributeORM
from src.app.db.repository import Repository
from src.domain.base.mapper import Mapper
from src.domain.product.i_product_attribute_repository import (
    IProductAttributeRepository,
)
from src.domain.product.product_attribute import ProductAttribute


class ProductAttributeMariaDbRepository(
    Repository[ProductAttributeORM, ProductAttribute], IProductAttributeRepository
):
    db: Session
    mapper: Mapper

    def __init__(
        self, db: Session, mapper: Mapper = ProductAttributeMariaDbMapper()
    ) -> None:
        super().__init__(db, mapper)
        self.db = db
        self.mapper = mapper

    # pylint: disable=W0622
    def get(self, id: str) -> None:
        orm: ProductAttributeORM | None = self.db.query(ProductAttributeORM).get(id)
        if orm:
            return self.mapper.map_to_domain(orm)
        else:
            return None

    def get_by_name(self, name: str) -> ProductAttribute | None:
        orm = (
            self.db.query(ProductAttributeORM)
            .filter(ProductAttributeORM.name == name)
            .one_or_none()
        )
        if orm:
            return self.mapper.map_to_domain(orm)
        return None

    def get_all(self) -> list[ProductAttribute]:
        orm_list: list[ProductAttributeORM] = self.db.query(ProductAttributeORM).all()
        return self.mapper.map_to_domain_list(orm_list)

    def update(self, entity: ProductAttribute) -> ProductAttribute | None:
        entity.updated_at = datetime.now()
        payload_orm: ProductAttributeORM = self.mapper.map_from_domain(entity)

        # check if orm object with payload.id exists
        found_orm = self.db.query(ProductAttributeORM).filter_by(id=entity.id)
        if found_orm:
            found_orm.update(payload_orm.as_dict_update())
        else:
            return None

        result = self.get(entity.id)
        if result:
            return result
        else:
            return None

    def remove(self, id: str) -> bool:
        orm_to_delete: ProductAttributeORM | None = self.db.get(ProductAttributeORM, id)
        if orm_to_delete:
            self.db.delete(orm_to_delete)
            return True
        else:
            return False
