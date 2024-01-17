import pytest
from src.app.db.models.product_orm import ProductORM
from src.app.api.api_v1.product.adapter.repository.product_mariadb_mapper import ProductMariaDbMapper
from src.domain.base.mapper import Mapper
from src.domain.product.product import Product




class TestProductMariaDbMapper:
    mapper: Mapper = ProductMariaDbMapper()
    def test_map_to_domain(self, product_orm: ProductORM):
        m_product: Product = self.mapper.map_to_domain(product_orm)
        assert len(m_product.errors) == 0

    def test_map_from_domain(self, product: Product):
        m_product_orm: ProductORM = self.mapper.map_from_domain(product)
        print(isinstance(m_product_orm.product_metadata, str))
        assert str(m_product_orm.name) != "Iphone 8"
