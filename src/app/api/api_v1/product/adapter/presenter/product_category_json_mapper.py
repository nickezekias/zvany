from datetime import datetime

from src.app.api.api_v1.product.adapter.request.product_category_request import (
    ProductCategoryRequest,
)
from src.app.api.api_v1.product.adapter.response.product_category_response import (
    ProductCategoryResponse,
)
from src.domain.base.mapper import Mapper
from src.domain.product.product_category import ProductCategory
from src.domain.util.date_time_util import DateTimeUtil


class ProductCategoryJsonMapper(
    Mapper[
        ProductCategoryRequest | ProductCategory,
        ProductCategory | ProductCategoryResponse,
    ]
):
    def map_to_domain(self, param: ProductCategoryRequest) -> ProductCategory:
        now = datetime.now()

        return ProductCategory(
            id=param.id,
            name=param.name,
            parent=param.parent,
            slug=param.slug,
            created_at=now,
            updated_at=now,
            description=param.description,
            position=param.position,
            visible=param.visible,
        )

    def map_to_domain_list(
        self, params: list[ProductCategoryRequest]
    ) -> list[ProductCategory]:
        entities: list[ProductCategory] = []

        for param in params:
            entities.append(self.map_to_domain(param))

        return entities

    def map_from_domain(self, param: ProductCategory) -> ProductCategoryResponse:
        return ProductCategoryResponse(
            id=param.id,
            name=param.name,
            position=param.position,
            parent=param.parent,
            description=param.description,
            slug=param.slug,
            visible=param.visible,
            createdAt=DateTimeUtil.date_to_string(param.created_at),
            updatedAt=DateTimeUtil.date_to_string(param.updated_at),
        )

    def map_from_domain_list(
        self, params: list[ProductCategory]
    ) -> list[ProductCategoryResponse]:
        res_list: list[ProductCategoryResponse] = []

        for param in params:
            res_list.append(self.map_from_domain(param))

        return res_list
