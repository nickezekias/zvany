

from src.domain.product.product import Product


class TestProductMariaDbRepository:
    def get_all(self) -> list[Product]:
        return []

    def test_get_all(self):
        products: list[Product] = []
        if len(products) > 0:
            assert isinstance(products[0], Product)
        assert isinstance(products, list)
