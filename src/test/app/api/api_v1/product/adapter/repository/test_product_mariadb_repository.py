

from src.domain.product.i_product_repository import IProductRepository
from src.domain.product.product import Product


class TestProductMariaDbRepository(IProductRepository):

    #TODO: add tests for get method
    def get(self, id):
        pass

    #FIXME: redefine get_all to actually mock getting all products
    def get_all(self) -> list[Product]:
        return []
    
    #TODO: add tests
    def find(self, query: str):
        pass

    #TODO: add tests
    def add(self, entity: Product):
        pass
    
    #TODO: add tests
    def add_range(self, entities: list[Product]):
        pass

    #TODO: add tests
    def update(self, entity: Product):
        pass

    #TODO: add tests
    def remove(self, product: Product):
        pass

    #TODO: add tests
    def remove_range(self, entities: list[Product]):
        pass

    #TODO: add tests
    def commit(self):
        pass

    #TODO: add tests
    def refresh(self):
        pass

    #TODO: add tests
    def test_get_all(self):
        products: list[Product] = []
        if len(products) > 0:
            assert isinstance(products[0], Product)
        assert isinstance(products, list)
