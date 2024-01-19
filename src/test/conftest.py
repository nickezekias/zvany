import pytest
import json
from datetime import datetime, timedelta

from src.app.db.models.product_orm import ProductORM

from src.domain.base.entity import Entity
from src.domain.product.product import Product
from src.domain.product.product_attribute import ProductAttribute
from src.domain.product.product_image import ProductImage
from src.domain.product.product_metadata import ProductMetadata
from src.domain.util.date_time_util import DateTimeUtil


now = datetime.now()

@pytest.fixture(scope="class")
def entity():
    return Entity()

@pytest.fixture(scope="function")
def product() -> Product:
    return Product(
        id="",
        name="Iphone 8",
        slug="iphone-8",
        sku="IP-8",
        type="simple",
        long_description="",
        short_description="Meet your iPhone 8",
        price="100000",
        regular_price="80000",
        sale_price="2",
        sale_start_date = now,
        sale_end_date = datetime.now() + timedelta(hours=1),
        categories=["default"],
        images=[ProductImage(id="", height=250, name="iphone8", src="iphone8.png", width=250, created_at=now, updated_at=now)],
        attributes=[ProductAttribute(id="", name="color", values={"black", "red"}, created_at=now, updated_at=now)],
        metadata=[ProductMetadata(id="", key="slug", value="iphone-8")],
        created_at=now,
        updated_at=now + timedelta(minutes=60)
    )


@pytest.fixture(scope="function")
def product_orm(product: Product) -> ProductORM:
    param: Product = product
    sale_start_date = param.sale_start_date
    sale_end_date = param.sale_end_date
    if sale_start_date is not None:
        sale_start_date = DateTimeUtil.date_to_string(sale_start_date)
    if sale_end_date is not None:
        sale_end_date = DateTimeUtil.date_to_string(sale_end_date)

    attributes: str = ""
    images: str = ""
    metadata: dict = {}

    for product_attr in param.attributes:
        attributes += product_attr.id      

    for product_img in param.images:
        images += product_img.id

    for product_meta in param.metadata:
        metadata[f'{product_meta.key}'] = f'{product_meta.value}'
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
        related_ids=param.related_ids,
        upsells_ids=param.upsells_ids,
        cross_sells_ids=param.cross_sells_ids,
        parent_id=param.parent_id,
        purchase_note=param.purchase_note,
        categories=param.categories,
        tags=param.tags,
        images=images,
        attributes=attributes,
        variations=param.variations,
        menu_order=param.menu_order,
        product_metadata='{"hello": "world"}',
        created_at = DateTimeUtil.date_to_string(param.created_at),
        updated_at = DateTimeUtil.date_to_string(param.updated_at)
    ) # type: ignore
