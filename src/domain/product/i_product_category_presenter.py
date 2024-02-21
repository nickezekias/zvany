from abc import abstractmethod

from src.app.api.api_v1.product.adapter.response.product_category_response import (
    ProductCategoryResponse,
)
from src.domain.base.i_presenter import IPresenter
from src.domain.product.product_category import ProductCategory


class IProductCategoryPresenter(IPresenter):

    @abstractmethod
    def output(self, data: ProductCategory) -> ProductCategoryResponse:
        pass

    @abstractmethod
    def output_index(
        self, data: list[ProductCategory]
    ) -> list[ProductCategoryResponse]:
        pass

    @abstractmethod
    def output_create(self, data: ProductCategory) -> ProductCategoryResponse:
        pass

    @abstractmethod
    def output_update(self, data: ProductCategory) -> ProductCategoryResponse:
        pass

    @abstractmethod
    def output_delete(self) -> dict:
        pass

    @abstractmethod
    def output_error_invalid_data(self, error: ValueError) -> None:
        pass

    @abstractmethod
    def output_error_duplicate_name(self) -> None:
        pass
