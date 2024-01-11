import pytest
from datetime import datetime, timedelta

from src.domain.base.entity import Entity
from src.domain.product.product import Product
from src.domain.product.product_attribute import ProductAttribute
from src.domain.product.product_image import ProductImage
from src.domain.product.product_metadata import ProductMetadata


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
        updated_at=now
    )
