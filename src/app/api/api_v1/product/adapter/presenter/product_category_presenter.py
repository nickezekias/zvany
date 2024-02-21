from fastapi import HTTPException, status
from src.app.api.api_v1.product.adapter.presenter.product_category_json_mapper import (
    ProductCategoryJsonMapper,
)
from src.app.api.api_v1.product.adapter.response.product_category_response import (
    ProductCategoryResponse,
)

from src.app.core.adapter.presenter import Presenter
from src.domain.base.mapper import Mapper
from src.domain.product.i_product_category_presenter import IProductCategoryPresenter
from src.domain.product.product_category import ProductCategory


class ProductCategoryPresenter(Presenter, IProductCategoryPresenter):
    mapper: Mapper

    def __init__(self) -> None:
        self.mapper = ProductCategoryJsonMapper()

    def output(self, data: ProductCategory) -> ProductCategoryResponse:
        return self.mapper.map_from_domain(data)

    def output_index(
        self, data: list[ProductCategory]
    ) -> list[ProductCategoryResponse]:
        return self.mapper.map_from_domain_list(data)

    def output_create(self, data: ProductCategory) -> ProductCategoryResponse:
        return self.mapper.map_from_domain(data)

    def output_update(self, data: ProductCategory) -> ProductCategoryResponse:
        return self.mapper.map_from_domain(data)

    def output_delete(self) -> dict:
        return {"success": True}

    def output_error_invalid_data(self, error: ValueError) -> None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "message": "ProductCategory.create.error.invalidData",
                "detail": str(error),
            },
        )

    def output_error_duplicate_name(self) -> None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": "ProductCategory.create.error.duplicateName"},
        )
