from src.app.db.models.product_attribute_orm import ProductAttributeORM
from src.domain.base.mapper import Mapper
from src.domain.product.product_attribute import ProductAttribute
from src.domain.util.date_time_util import DateTimeUtil

class ProductAttributeMariaDbMapper(Mapper[ProductAttributeORM, ProductAttribute]):

    def map_to_domain(self, param: ProductAttributeORM) -> ProductAttribute:
        created_at = param.created_at
        updated_at = param.updated_at
        if created_at is not None and isinstance(created_at, str):
            created_at = DateTimeUtil.string_to_date(created_at)
        if updated_at is not None and isinstance(updated_at, str):
            updated_at = DateTimeUtil.string_to_date(updated_at)

        values: set[str] = set(str(param.values).split(','))

        return ProductAttribute(
            id=str(param.id),
            name=str(param.name),
            position=param.position, # type: ignore
            values=values,
            variation=param.variation, # type: ignore
            visible=param.visible, # type: ignore
            created_at=created_at, #type: ignore
            updated_at=updated_at #type: ignore
        )

    def map_to_domain_list(self, params: list[ProductAttributeORM]) -> list[ProductAttribute]:
        product_attributes: list[ProductAttribute] = []

        for param in params:
            product_attributes.append(self.map_to_domain(param))

        return product_attributes
    
    def map_from_domain(self, param: ProductAttribute) -> ProductAttributeORM:
        values = ''.join(param.values)

        return ProductAttributeORM(
            id=param.id,
            name=param.name,
            position=param.position,
            values=values,
            variation=param.variation,
            visible=param.visible,
            created_at = DateTimeUtil.date_to_string(param.created_at),
            updated_at = DateTimeUtil.date_to_string(param.updated_at)
        ) #type: ignore

    def map_from_domain_list(self, params: list[ProductAttribute]) -> list[ProductAttributeORM]:
        product_attr_orm_list: list[ProductAttributeORM] = []

        for param in params:
            product_attr_orm_list.append(self.map_from_domain(param))

        return product_attr_orm_list
