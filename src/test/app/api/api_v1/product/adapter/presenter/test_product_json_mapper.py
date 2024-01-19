from src.app.api.api_v1.product.adapter.presenter.product_json_mapper import ProductJsonMapper
from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.domain.base.mapper import Mapper
from src.domain.product.product import Product

class TestProductJsonMapper:
    mapper: Mapper = ProductJsonMapper()

    #FIXME: Add tests for map_to_domain after I create a product
    def test_map_to_domain(self):
        pass

    def test_map_from_domain(self, product: Product):
        m_product_json: ProductPostResponse = self.mapper.map_from_domain(product)
        assert m_product_json.name == "Iphone 8"