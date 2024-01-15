from abc import abstractmethod
from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.domain.base.i_presenter import IPresenter
from src.domain.product.product import Product

class IProductPresenter(IPresenter):
    """Product Presenter Interface"""

    @abstractmethod
    def output(self, data: list[Product]) -> list[ProductPostResponse]:
        pass
