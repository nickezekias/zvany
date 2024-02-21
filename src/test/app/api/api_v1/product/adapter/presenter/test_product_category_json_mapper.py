from datetime import datetime

import pytest

from src.app.api.api_v1.product.adapter.presenter.product_category_json_mapper import (
    ProductCategoryJsonMapper,
)
from src.domain.base.mapper import Mapper
from src.domain.product.product_category import ProductCategory


class TestProductCategoryJsonMapper:
    mapper: Mapper = ProductCategoryJsonMapper()

    def test_map_to_domain(self, product_category: ProductCategory):

        assert isinstance(product_category, ProductCategory)

        product_category.lazy_validation()
        assert len(product_category.errors) == 0

        assert product_category.id != ""
        assert product_category.name != ""
        assert product_category.slug != ""
        assert isinstance(product_category.created_at, datetime) is True
        assert isinstance(product_category.updated_at, datetime) is True

    def test_map_to_domain_error_name_is_empty(self, product_category: ProductCategory):
        product_category.name = ""
        product_category.slug = ""
        with pytest.raises(ValueError):
            product_category.lazy_validation()
            print(product_category)
