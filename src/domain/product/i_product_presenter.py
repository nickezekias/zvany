from abc import abstractmethod

from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.domain.base.i_presenter import IPresenter
from src.domain.product.product import Product

class IProductPresenter(IPresenter):
    """Product Presenter Interface"""

    @abstractmethod
    def output_index(self, data: list[Product]) -> list[ProductPostResponse]:
        pass

    @abstractmethod
    def output_create(self, data: Product) -> ProductPostResponse:
        pass

    @abstractmethod
    def output_error_invalid_data(self, error: ValueError) -> None:
        pass
