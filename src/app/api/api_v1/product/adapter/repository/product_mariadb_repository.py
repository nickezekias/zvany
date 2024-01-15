import sqlalchemy as sa
from sqlalchemy.orm import Session
from src.app.api.api_v1.product.adapter.repository.product_mariadb_mapper import ProductMariaDbMapper
from src.app.db.models.product_orm import ProductORM

from src.app.db.repository import Repository
from src.domain.product.i_product_repository import IProductRepository
from src.domain.product.product import Product

class ProductMariaDbRepository(Repository[ProductORM, Product], IProductRepository):
    db: Session
    mapper: ProductMariaDbMapper

    def __init__(self, db: Session, mapper: ProductMariaDbMapper = ProductMariaDbMapper()) -> None:
        super().__init__(db, mapper)
        self.db = db
        self.mapper = mapper

    def get(self, id: int | str) -> Product | None:
        orm: ProductORM | None = self.db.query(ProductORM).get(id)
        if orm:
            return self.mapper.map_to_domain(orm)
        else: return None

    def get_all(self) -> list[Product]:
        orms: list[ProductORM] = self.db.query(ProductORM).all()
        return self.mapper.map_to_domain_list(orms)


