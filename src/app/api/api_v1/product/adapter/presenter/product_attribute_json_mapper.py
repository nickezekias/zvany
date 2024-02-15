from datetime import datetime

from src.app.api.api_v1.product.adapter.request.product_attribute_request import ProductAttributeRequest
from src.app.api.api_v1.product.adapter.response.product_attribute_response import ProductAttributeResponse
from src.domain.base.mapper import Mapper
from src.domain.product.product_attribute import ProductAttribute

class ProductAttributeJsonMapper(Mapper[ProductAttributeRequest | ProductAttribute, ProductAttribute | ProductAttributeResponse]):

    def map_to_domain(self, param: ProductAttributeRequest) -> ProductAttribute:
        now = datetime.now()
        
        return ProductAttribute(
            id=param.id,
            name=param.name,
            values=set(param.values),
            created_at=now,
            updated_at=now,
            position=param.position,
            variation=param.variation,
            visible=param.visible
        )
    
    def map_to_domain_list(self, params: list[ProductAttributeRequest]) -> list[ProductAttribute]:
        product_attributes: list[ProductAttribute] = []
        
        for param in params:
            product_attributes.append(self.map_to_domain(param))

        return product_attributes

    def map_from_domain(self, param: ProductAttribute) -> ProductAttributeResponse:
        return ProductAttributeResponse(
            id=param.id,
            name=param.name,
            values=param.values,
            createdAt=param.created_at,
            updatedAt=param.updated_at,
            position=param.position,
            variation=param.variation,
            visible=param.visible
        )

    def map_from_domain_list(self, params: list[ProductAttribute]) -> list[ProductAttributeResponse]:
        product_attr_res: list[ProductAttributeResponse] = []

        for param in params:
            product_attr_res.append(self.map_from_domain(param))

        return product_attr_res
