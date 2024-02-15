import pydantic_core
import pytest

from datetime import datetime
from src.app.api.api_v1.product.adapter.presenter.product_attribute_json_mapper import ProductAttributeJsonMapper
from src.app.api.api_v1.product.adapter.request.product_attribute_request import ProductAttributeRequest
from src.app.api.api_v1.product.adapter.response.product_attribute_response import ProductAttributeResponse
from src.domain.base.mapper import Mapper
from src.domain.product.product_attribute import ProductAttribute


class TestProductJsonMapper:
    mapper: Mapper = ProductAttributeJsonMapper()

    def test_map_to_domain_correct_instantiation(self, product_attribute_req: ProductAttributeRequest):
        product_attr = self.mapper.map_to_domain(product_attribute_req)
        assert isinstance(product_attr, ProductAttribute) is True
        product_attr.lazy_validation()
        assert len(product_attr.errors) == 0
        assert product_attr.id != ""
        assert isinstance(product_attr.values, set) is True
        assert isinstance(product_attr.created_at, datetime) is True
        assert isinstance(product_attr.updated_at, datetime) is True

    """Test Map To Domain error when product_attribute_request data is invalid"""
    def test_map_to_domain_error_wrong_param_type(self):
        data = {
            "id": "",
            "name": "color",
            "position": 0,
        }
        with pytest.raises(pydantic_core.ValidationError):
            product_attr_req = ProductAttributeRequest(**data)
            product_attr = self.mapper.map_to_domain(product_attr_req)
            assert len(product_attr.errors) == 0

    def test_map_from_domain(self, product_attribute: ProductAttribute):
        product_attr_res: ProductAttributeResponse = self.mapper.map_from_domain(product_attribute)
        assert isinstance(product_attr_res, ProductAttributeResponse)
