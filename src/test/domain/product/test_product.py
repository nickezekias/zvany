import pytest
from datetime import datetime, timedelta

from src.domain.product.product import Product

now = datetime.now()


class TestProduct:
    def test_correct_product_instantiation(self, product: Product):
        assert product.name == "Iphone 8"
        assert len(product.errors) == 0
        product.clear_validations()

    def test_name_must_have_3_char(self, product: Product):
        with pytest.raises(ValueError):
            product.name = "hi"
            product.lazy_validation()

    def test_no_empty_sku(self, product: Product):
        with pytest.raises(ValueError):
            product.sku = ""
            product.lazy_validation()

    def test_product_type_correct_values(self, product: Product):
        product_types = ["simple", "grouped", "external", "variable"]
        for pt in product_types:
            product.type = pt
            product.lazy_validation()
            assert len(product.errors) == 0
        assert len(product.errors) == 0

    def test_invalid_product_type(self, product: Product):
        with pytest.raises(ValueError):
            product.type = "mj"
            product.lazy_validation()

    def test_product_status_correct_values(self, product: Product):
        statuses = ["draft", "pending", "private", "published"]
        for status in statuses:
            product.status = status
            product.lazy_validation()
            assert len(product.errors) == 0
        assert len(product.errors) == 0

    def test_invalid_product_status(self, product: Product):
        with pytest.raises(ValueError):
            product.status = "drafted"
            product.lazy_validation()

    def test_catalog_visibility_correct_values(self, product: Product):
        visibility = ["visible", "catalog", "search", "hidden"]
        for val in visibility:
            product.catalog_visibility = val
            product.lazy_validation()
            assert len(product.errors) == 0
        assert len(product.errors) == 0

    def test_invalid_catalog_visibility(self, product: Product):
        with pytest.raises(ValueError):
            product.catalog_visibility = "dunno"
            product.lazy_validation()

    def test_short_description_error_empty_value(self, product: Product):
        with pytest.raises(ValueError):
            product.short_description = ""
            product.lazy_validation()

    def test_price_error_value_empty_price(self, product: Product):
        with pytest.raises(ValueError):
            product.price = ""
            product.lazy_validation()

    def test_price_error_value_eq_zero(self, product: Product):
        with pytest.raises(ValueError):
            product.price = "0"
            product.lazy_validation()

    def test_price_error_value_lt_0(self, product: Product):
        with pytest.raises(ValueError):
            product.price = "-1"
            product.lazy_validation()

    def test_price_value_decimal(self, product: Product):
        product.price = "9.99"
        product.lazy_validation()
        assert len(product.errors) == 0

    def test_price_error_value_neg_decimal(self, product: Product):
        product.price = "-9.99"
        with pytest.raises(ValueError):
            product.lazy_validation()

    def test_regular_price_error_value_empty_price(self, product: Product):
        with pytest.raises(ValueError):
            product.regular_price = ""
            product.lazy_validation()

    def test_regular_price_error_value_eq_zero(self, product: Product):
        with pytest.raises(ValueError):
            product.regular_price = "0"
            product.lazy_validation()

    def test_regular_price_error_value_lt_0(self, product: Product):
        with pytest.raises(ValueError):
            product.regular_price = "-1"
            product.lazy_validation()

    def test_valid_sale_price(self, product: Product):
        product.sale_price = "830"
        product.sale_start_date = datetime.now()
        product.sale_end_date = datetime.now() + timedelta(minutes=60)
        product.lazy_validation()
        assert len(product.errors) == 0

    def test_valid_empty_sale_price(self, product: Product):
        product.sale_start_date = None
        product.sale_end_date = None
        product.sale_price = ""
        product.lazy_validation()
        assert len(product.errors) == 0

    def test_sale_price_error_value_not_empty(self, product: Product):
        with pytest.raises(ValueError):
            product.sale_start_date = None
            product.sale_end_date = None
            product.sale_price = "0"
            product.lazy_validation()

    def test_sale_price_error_empty_value(self, product: Product):
        with pytest.raises(ValueError):
            product.sale_price = ""
            product.lazy_validation()

    def test_sale_price_error_value_eq_zero(self, product: Product):
        with pytest.raises(ValueError):
            product.price = "0"
            product.lazy_validation()

    def test_valid_sale_start_date_and_sale_end_date(self, product: Product):
        product.sale_start_date = datetime.now()
        product.sale_end_date = datetime.now() + timedelta(hours=1)
        product.lazy_validation()
        assert len(product.errors) == 0

    def test_sale_start_date_error_value_lt_2023_12_31(self, product: Product):
        with pytest.raises(ValueError):
            product.sale_start_date = datetime(2023, 12, 30)
            product.lazy_validation()

    def test_sale_end_date_error_lt_1_hour_from_sale_start_date(self, product: Product):
        with pytest.raises(ValueError):
            product.sale_start_date = datetime.now()
            product.sale_end_date = datetime.now() + timedelta(minutes=59)
            product.lazy_validation()

    def test_quantity_error_value_lt_minus_1(self, product: Product):
        with pytest.raises(ValueError):
            product.quantity = -2
            product.lazy_validation()

    def test_valid_created_at(self, product: Product):
        product.created_at = datetime.now()
        product.updated_at = datetime.now()
        product.lazy_validation()
        assert len(product.errors) == 0

    def test_created_at_error_invalid_type(self, product: Product):
        with pytest.raises(ValueError):
            product.created_at = None  # type: ignore - setting wrong type for test purposes
            product.lazy_validation()

    def test_valid_updated_at(self, product: Product):
        product.updated_at = datetime.now()
        product.lazy_validation()
        assert len(product.errors) == 0

    def test_updated_at_error_value_lt_created_at(self, product: Product):
        with pytest.raises(ValueError):
            product.created_at = datetime.now()
            product.updated_at = datetime.now() - timedelta(minutes=1)
            product.lazy_validation()
