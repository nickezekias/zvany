from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.app.api.api_v1.product.adapter.repository.product_category_mariadb_mapper import (
    ProductCategoryMariaDbMapper,
)
from src.app.db.models.product_category_orm import ProductCategoryORM
from src.app.db.repository import Repository
from src.domain.base.mapper import Mapper
from src.domain.product.i_product_category_repository import IProductCategoryRepository
from src.domain.product.product_category import ProductCategory


class ProductCategoryMariaDbRepository(
    Repository[ProductCategoryORM, ProductCategory], IProductCategoryRepository
):
    db: Session
    mapper: Mapper

    def __init__(
        self, db: Session, mapper: Mapper = ProductCategoryMariaDbMapper()
    ) -> None:
        super().__init__(db, mapper)
        self.db = db
        self.mapper = mapper

    # pylint: disable=W0622
    def get(self, id: str) -> None:
        orm: ProductCategoryORM | None = self.db.get(ProductCategoryORM, id)
        if orm:
            return self.mapper.map_to_domain(orm)
        else:
            return None

    def get_by_name(self, name: str) -> ProductCategory | None:
        orm = (
            self.db.query(ProductCategoryORM)
            .filter(ProductCategoryORM.name == name)
            .one_or_none()
        )
        if orm:
            return self.mapper.map_to_domain(orm)
        return None

    def get_all(self) -> list[ProductCategory]:
        orm_list: list[ProductCategoryORM] = self.db.query(ProductCategoryORM).all()
        return self.mapper.map_to_domain_list(orm_list)

    def find(self, query: dict) -> list[ProductCategory]:
        orm_list: list[ProductCategoryORM] = list(
            self.db.scalars(
                select(ProductCategoryORM).where(
                    ProductCategoryORM.name.like(f'%{query["name"]}%')
                )
            ).all()
        )

        return self.mapper.map_to_domain_list(orm_list)

    def update(self, entity: ProductCategory) -> ProductCategory | None:
        entity.updated_at = datetime.now()
        payload_orm: ProductCategoryORM = self.mapper.map_from_domain(entity)

        # check if orm object with payload.id exists
        found_orm = self.db.query(ProductCategoryORM).filter_by(id=entity.id)
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
        orm_to_delete: ProductCategoryORM | None = self.db.get(ProductCategoryORM, id)
        if orm_to_delete:
            self.db.delete(orm_to_delete)
            return True
        else:
            return False
