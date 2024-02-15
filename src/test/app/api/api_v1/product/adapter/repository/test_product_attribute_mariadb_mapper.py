from src.app.api.api_v1.product.adapter.repository.product_attribute_mariadb_mapper import ProductAttributeMariaDbMapper
from src.app.db.models.product_attribute_orm import ProductAttributeORM
from src.domain.base.mapper import Mapper
from src.domain.product.product_attribute import ProductAttribute

class TestProductMariaDbMapper:
    mapper: Mapper = ProductAttributeMariaDbMapper()

    def test_map_from_domain(self, product_attribute: ProductAttribute):
        product_attr_orm = self.mapper.map_from_domain(product_attribute)
        assert isinstance(product_attr_orm, ProductAttributeORM)

    def test_map_to_domain(self, product_attribute_orm: ProductAttributeORM):
        product_attr = self.mapper.map_to_domain(product_attribute_orm)
        assert isinstance(product_attr, ProductAttribute)

    def test_map_from_domain_list(self, product_attribute: ProductAttribute):
        array: list[ProductAttribute] = [product_attribute, product_attribute]
        array_orm: list[ProductAttributeORM] = self.mapper.map_from_domain_list(array)
        assert len(array_orm) > 0
        assert isinstance(array_orm[0], ProductAttributeORM) is True
        assert isinstance(array_orm[1], ProductAttributeORM) is True

    def test_map_from_domain_list_empty_params_array(self):
        array = []
        array_orm = self.mapper.map_from_domain_list(array)
        assert len(array_orm) == 0
