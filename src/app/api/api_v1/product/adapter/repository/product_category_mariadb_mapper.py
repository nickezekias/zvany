from src.app.db.models.product_category_orm import ProductCategoryORM
from src.domain.base.mapper import Mapper
from src.domain.product.product_category import ProductCategory
from src.domain.util.date_time_util import DateTimeUtil


class ProductCategoryMariaDbMapper(Mapper[ProductCategoryORM, ProductCategory]):
    def map_to_domain(self, param: ProductCategoryORM) -> ProductCategory:
        created_at = param.created_at
        updated_at = param.updated_at
        if created_at is not None and isinstance(created_at, str):
            created_at = DateTimeUtil.string_to_date(created_at)
        if updated_at is not None and isinstance(updated_at, str):
            updated_at = DateTimeUtil.string_to_date(updated_at)

        return ProductCategory(
            id=str(param.id),
            name=str(param.name),
            parent=str(param.parent),
            slug=str(param.slug),
            created_at=created_at,  # type: ignore
            updated_at=updated_at,  # type: ignore
            description=str(param.description),
            position=param.position,  # type: ignore
            visible=param.visible,  # type: ignore
        )

    def map_to_domain_list(
        self, params: list[ProductCategoryORM]
    ) -> list[ProductCategory]:
        entities: list[ProductCategory] = []

        for param in params:
            entities.append(self.map_to_domain(param))

        return entities

    def map_from_domain(self, param: ProductCategory) -> ProductCategoryORM:
        return ProductCategoryORM(
            id=param.id,
            name=param.name,
            parent=param.parent,
            slug=param.slug,
            created_at=DateTimeUtil.date_to_string(param.created_at),
            updated_at=DateTimeUtil.date_to_string(param.updated_at),
            description=param.description,
            position=param.position,
            visible=param.visible,
        )  # type: ignore

    def map_from_domain_list(
        self, params: list[ProductCategory]
    ) -> list[ProductCategoryORM]:
        orm_list: list[ProductCategoryORM] = []

        for param in params:
            orm_list.append(self.map_from_domain(param))

        return orm_list
