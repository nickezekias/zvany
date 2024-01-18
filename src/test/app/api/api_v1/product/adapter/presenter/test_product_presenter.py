from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.app.core.adapter.presenter import Presenter
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.product import Product


class TestProductPresenter(Presenter, IProductPresenter):
     
    #FIXME: Actually return list of product_response
    def output(self, data: list[Product]) -> list[ProductPostResponse]:
        return []
