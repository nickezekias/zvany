

from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.i_product_repository import IProductRepository
from src.domain.product.product import Product


class GetAllProducts(IUseCase):
    repository: IProductRepository
    presenter: IProductPresenter

    def __init__(
        self,
        repository: IProductRepository,
        presenter: IProductPresenter,
    ) -> None:
        self.repository = repository
        self.presenter = presenter

    async def execute(self, filter_query: str = "") -> list[ProductPostResponse]:
        if filter_query:
            # add code to filter products list against given query
            pass
        products: list[Product] = self.repository.get_all()
        return self.presenter.output(products)
