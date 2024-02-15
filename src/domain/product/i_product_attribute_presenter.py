from abc import abstractmethod

from src.app.api.api_v1.product.adapter.response.product_attribute_response import ProductAttributeResponse
from src.domain.base.i_presenter import IPresenter
from src.domain.product.product_attribute import ProductAttribute

class IProductAttributePresenter(IPresenter):

    @abstractmethod
    def output(self, data: ProductAttribute) -> ProductAttributeResponse:
        pass

    @abstractmethod
    def output_index(self, data: list[ProductAttribute]) -> list[ProductAttributeResponse]:
        pass

    @abstractmethod
    def output_create(self, data: ProductAttribute) -> ProductAttributeResponse:
        pass

    @abstractmethod
    def output_update(self, data: ProductAttribute) -> ProductAttributeResponse:
        pass


    @abstractmethod
    def output_error_invalid_data(self, error: ValueError) -> None:
        pass
