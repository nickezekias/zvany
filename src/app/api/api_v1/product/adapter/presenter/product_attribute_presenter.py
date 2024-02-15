from fastapi import HTTPException, status

from src.app.api.api_v1.product.adapter.presenter.product_attribute_json_mapper import ProductAttributeJsonMapper
from src.app.api.api_v1.product.adapter.response.product_attribute_response import ProductAttributeResponse
from src.app.core.adapter.presenter import Presenter
from src.domain.base.mapper import Mapper
from src.domain.product.i_product_attribute_presenter import IProductAttributePresenter
from src.domain.product.product_attribute import ProductAttribute

class ProductAttributePresenter(Presenter, IProductAttributePresenter):
    mapper: Mapper

    def __init__(self) -> None:
        self.mapper = ProductAttributeJsonMapper()

    def output(self, data: ProductAttribute) -> ProductAttributeResponse:
        return self.mapper.map_from_domain(data)
    
    def output_index(self, data: list[ProductAttribute]) -> list[ProductAttributeResponse]:
        return self.mapper.map_from_domain_list(data)
    
    def output_create(self, data: ProductAttribute) -> ProductAttributeResponse:
        return self.mapper.map_from_domain(data)
    
    def output_update(self, data: ProductAttribute) -> ProductAttributeResponse:
        return self.mapper.map_from_domain(data)
    
    def output_error_invalid_data(self, error: ValueError) -> None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"message": "productAttribute.create.error.invalidData", "detail": str(error)}
        )
