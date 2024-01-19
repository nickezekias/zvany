

from src.app.api.api_v1.product.adapter.presenter.product_json_mapper import ProductJsonMapper
from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.app.core.adapter.presenter import Presenter
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.product import Product


class ProductPresenter(Presenter, IProductPresenter):
    mapper: ProductJsonMapper

    def __init__(self) -> None:
        self.mapper = ProductJsonMapper()

    def output(self, data: list[Product]) -> list[ProductPostResponse]:
        product_res_list: list[ProductPostResponse] = []
        for product in data:
            product_res_list.append(self.mapper.map_from_domain(product))

        return product_res_list
