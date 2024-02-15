from fastapi import HTTPException, status

from src.app.api.api_v1.product.adapter.presenter.product_json_mapper import ProductJsonMapper
from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.app.core.adapter.presenter import Presenter
from src.domain.base.mapper import Mapper
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.product import Product


class ProductPresenter(Presenter, IProductPresenter):
    mapper: Mapper

    def __init__(self) -> None:
        self.mapper = ProductJsonMapper()

    def output_index(self, data: list[Product]) -> list[ProductPostResponse]:
        product_res_list: list[ProductPostResponse] = []
        for product in data:
            product_res_list.append(self.mapper.map_from_domain(product))

        return product_res_list

    def output_create(self, data: Product) -> ProductPostResponse:
        return self.mapper.map_from_domain(data)

    def output_error_invalid_data(self, error: ValueError) -> None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"message": "product.create.error.invalidData", "detail": str(error)}
        )
