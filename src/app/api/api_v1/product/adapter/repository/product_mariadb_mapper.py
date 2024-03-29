import json
from src.domain.util.date_time_util import DateTimeUtil

from src.domain.base.mapper import Mapper
from src.domain.product.product import Product
from src.domain.product.product_attribute import ProductAttribute
from src.domain.product.product_image import ProductImage
from src.domain.product.product_metadata import ProductMetadata
from src.app.db.models.product_orm import ProductORM


class ProductMariaDbMapper(Mapper[ProductORM, Product]):

    def map_to_domain(
        self, param: ProductORM
    ) -> Product:
        created_at = param.created_at
        updated_at = param.updated_at
        sale_start_date = param.sale_start_date
        sale_end_date = param.sale_end_date
        if created_at is not None and isinstance(created_at, str):
            created_at = DateTimeUtil.string_to_date(created_at)
        if updated_at is not None and isinstance(updated_at, str):
            updated_at = DateTimeUtil.string_to_date(updated_at)
        if sale_start_date is not None:
            sale_start_date = DateTimeUtil.string_to_date(str(sale_start_date))
        if sale_end_date is not None:
            sale_end_date = DateTimeUtil.string_to_date(str(sale_end_date))

        related_ids: list[str] = list(str(param.related_ids).split(','))
        upsells_ids: list[str] = list(str(param.upsells_ids).split(','))
        cross_sells_ids: list[str] = list(str(param.cross_sells_ids).split(','))

        metadata: dict = json.loads(str(param.product_metadata))
        metadata_objects: list[ProductMetadata] = []
        for key, value in metadata.items():
            metadata_objects.append(ProductMetadata(id="", key=str(key), value=str(value)))

        return Product(
            id=str(param.id),
            name=str(param.name),
            slug=str(param.slug),
            sku=str(param.sku),
            type=str(param.type),
            status=str(param.status),
            catalog_visibility=str(param.catalog_visibility),
            long_description=str(param.long_description),
            short_description=str(param.short_description),
            price=str(param.price),
            regular_price=str(param.regular_price),
            sale_price=str(param.sale_price),
            sale_start_date=sale_start_date,
            sale_end_date=sale_end_date,
            on_sale=param.on_sale,
            total_sales=param.total_sales,
            virtual=param.virtual,
            quantity=param.quantity,
            sold_individually=param.sold_individually,
            weight=param.weight,
            shipping_taxable=param.shipping_taxable,
            reviews_allowed=param.reviews_allowed,
            average_rating=param.average_rating,
            rating_count=param.rating_count,
            related_ids=related_ids,
            upsells_ids=upsells_ids,
            cross_sells_ids=cross_sells_ids,
            parent_id=param.parent_id,
            purchase_note=param.purchase_note,
            categories=param.categories,
            tags=param.tags,
            images=[],
            attributes=[],
            variations=param.variations,
            menu_order=param.menu_order,
            metadata=metadata_objects,
            created_at=created_at,
            updated_at=updated_at
        )

    def map_to_domain_list(self, params: list[ProductORM]) -> list[Product]:
        products: list[Product] = []
        for orm in params:
            products.append(self.map_to_domain(orm))
        return products

    def map_from_domain(self, param: Product) -> ProductORM:
        sale_start_date = param.sale_start_date
        sale_end_date = param.sale_end_date
        if sale_start_date is not None:
            sale_start_date = DateTimeUtil.date_to_string(sale_start_date)
        if sale_end_date is not None:
            sale_end_date = DateTimeUtil.date_to_string(sale_end_date)

        related_ids = param.related_ids
        if related_ids is not None and len(related_ids) > 0:
            related_ids = ''.join(related_ids)
        elif related_ids is not None and len(related_ids) == 0:
            related_ids = ''

        cross_sells_ids = param.cross_sells_ids
        if cross_sells_ids is not None and len(cross_sells_ids) > 0:
            cross_sells_ids = ''.join(cross_sells_ids)
        elif cross_sells_ids is not None and len(cross_sells_ids) == 0:
            cross_sells_ids = ''

        upsells_ids = param.upsells_ids
        if upsells_ids is not None and len(upsells_ids) > 0:
            upsells_ids = ''.join(upsells_ids)
        elif upsells_ids is not None and len(upsells_ids) == 0:
            upsells_ids = ''

        categories = param.categories
        if len(categories) > 0:
            categories = ''.join(param.categories)
        else:
            categories = ''

        tags = param.tags
        if tags is not None and len(tags) > 0:
            tags = str(''.join(tags))
        elif tags is not None and len(tags) == 0:
            tags = '' 

        attributes: str = ""
        images: str = ""
        metadata: dict = {}

        for product_attr in param.attributes:
            attributes += product_attr.id      

        for product_img in param.images:
            images += product_img.id

        for product_meta in param.metadata:
            metadata[f"{product_meta.key}"] = product_meta.value

        return ProductORM(
            id=param.id,
            name=param.name,
            slug=param.slug,
            sku=param.sku,
            type=param.type,
            status=param.status,
            catalog_visibility=param.catalog_visibility,
            long_description=param.long_description,
            short_description=param.short_description,
            price=param.price,
            regular_price=param.regular_price,
            sale_price=param.sale_price,
            sale_start_date=sale_start_date,
            sale_end_date=sale_end_date,
            on_sale=param.on_sale,
            total_sales=param.total_sales,
            virtual=param.virtual,
            quantity=param.quantity,
            sold_individually=param.sold_individually,
            weight=param.weight,
            shipping_taxable=param.shipping_taxable,
            reviews_allowed=param.reviews_allowed,
            average_rating=param.average_rating,
            rating_count=param.rating_count,
            related_ids=related_ids,
            upsells_ids=upsells_ids,
            cross_sells_ids=cross_sells_ids,
            parent_id=param.parent_id,
            purchase_note=param.purchase_note,
            categories=categories,
            tags=tags,
            images=images,
            attributes=attributes,
            variations=param.variations,
            menu_order=param.menu_order,
            product_metadata=json.dumps(metadata),
            created_at = DateTimeUtil.date_to_string(param.created_at),
            updated_at = DateTimeUtil.date_to_string(param.updated_at)
        ) # type: ignore


    def map_from_domain_list(self, params: list[Product]) -> list[ProductORM]:
        return super().map_from_domain_list(params)
