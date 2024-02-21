import pytest
from datetime import datetime
from src.domain.product.product_category import ProductCategory


class TestProductCategory:
    now = datetime.now()

    product_cat = ProductCategory(
        id="fsadfdasfasd",
        name="default",
        parent="default",
        slug="default",
        created_at=now,
        updated_at=now,
        description="",
        position=1,
        visible=True,
    )

    def test_correct_instantiation(self):
        assert self.product_cat.id != ""
        self.product_cat.lazy_validation()
        assert len(self.product_cat.errors) == 0
