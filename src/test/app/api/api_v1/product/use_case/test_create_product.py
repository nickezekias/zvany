import pytest

# from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
# from src.app.api.api_v1.product.use_case.create_product import CreateProduct
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.i_product_repository import IProductRepository
from src.test.app.api.api_v1.product.adapter.presenter.test_product_presenter import TestProductPresenter
from src.test.app.api.api_v1.product.adapter.repository.test_product_mariadb_repository import TestProductMariaDbRepository

class TestCreateProduct:
    repository: IProductRepository = TestProductMariaDbRepository()
    presenter: IProductPresenter = TestProductPresenter()

    @pytest.mark.asyncio
    async def test_execute(self) -> None:
        #TODO: write test once we have a test database
        pass
