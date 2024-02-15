import pytest
from fastapi import HTTPException, status
from src.app.api.api_v1.product.adapter.presenter.product_json_mapper import ProductJsonMapper

from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.app.core.adapter.presenter import Presenter
from src.domain.base.mapper import Mapper
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.product import Product


class TestProductPresenter(Presenter, IProductPresenter):
    mapper: Mapper = ProductJsonMapper()
     
    #FIXME: Actually return list of product_response
    def output_index(self, data: list[Product]) -> list[ProductPostResponse]:
        return []

    def output_create(self, data: Product) -> ProductPostResponse:
        return self.mapper.map_from_domain(data)

    def output_error_invalid_data(self, error: ValueError) -> None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"message": "product.create.error.invalidData", "detail": str(error)}
        )

    def test_output_create_error_invalid_param_type(self) -> None:
        data = { "name": "Ezekiel" }
        with pytest.raises(ValueError):
            self.output_create(data) # type: ignore - testing wrong type
