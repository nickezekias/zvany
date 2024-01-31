import pytest

from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.app.api.api_v1.product.use_case.get_all_products import GetAllProducts
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.i_product_repository import IProductRepository
from src.test.app.api.api_v1.product.adapter.presenter.test_product_presenter import TestProductPresenter
from src.test.app.api.api_v1.product.adapter.repository.test_product_mariadb_repository import TestProductMariaDbRepository


class TestGetAllProducts:
    repository: IProductRepository = TestProductMariaDbRepository()
    presenter: IProductPresenter = TestProductPresenter()

    @pytest.mark.asyncio
    async def test_execute(self, filter_query: str = ""):
        #FIXME: define tests for when there is a filter_query
        if filter_query:
            pass
        res = await GetAllProducts(self.repository, self.presenter).execute(filter_query)
        if len(res) > 0:
            assert isinstance(res[0], ProductPostResponse)
        assert isinstance(res, list)