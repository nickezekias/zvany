import pytest
from datetime import datetime
from src.app.api.api_v1.product.adapter.presenter.product_attribute_json_mapper import ProductAttributeJsonMapper
from src.app.api.api_v1.product.adapter.presenter.product_json_mapper import (
    ProductJsonMapper,
)
from src.app.api.api_v1.product.adapter.repository.product_attribute_mariadb_mapper import ProductAttributeMariaDbMapper
from src.app.api.api_v1.product.adapter.repository.product_mariadb_mapper import (
    ProductMariaDbMapper,
)
from src.app.api.api_v1.product.adapter.request.product_attribute_request import ProductAttributeRequest

from src.app.api.api_v1.product.adapter.request.product_request import (
    ProductPostRequest,
)
from src.app.api.api_v1.product.adapter.response.product_response import (
    ProductPostResponse,
)
from src.app.db.models.product_attribute_orm import ProductAttributeORM

from src.app.db.models.product_orm import ProductORM

from src.domain.base.entity import Entity
from src.domain.base.mapper import Mapper
from src.domain.product.product import Product
from src.domain.product.product_attribute import ProductAttribute

now = datetime.now()

mariadb_mapper: Mapper = ProductMariaDbMapper()
json_mapper: Mapper = ProductJsonMapper()


@pytest.fixture(scope="class")
def entity():
    return Entity()

@pytest.fixture(scope="function")
def product_attribute_req() -> ProductAttributeRequest:
    data = {
            "id": "",
            "name": "color",
            "position": 0,
            "values": ["white", "silver", "black", "gold"],
            "variation": True,
            "visible": True,
            "createdAt": "2024-02-12T23:04:11.559172",
            "updatedAt": "2024-02-12T23:04:11.559172"
        }
    return ProductAttributeRequest(**data)

@pytest.fixture(scope="function")
def product_attribute(product_attribute_req: ProductAttributeRequest) -> ProductAttribute:
    return ProductAttributeJsonMapper().map_to_domain(product_attribute_req)

@pytest.fixture(scope="function")
def product_attribute_orm(product_attribute: ProductAttribute) -> ProductAttributeORM:
    return ProductAttributeMariaDbMapper().map_from_domain(product_attribute)

@pytest.fixture(scope="function")
def product_req() -> ProductPostRequest:
    data =  {
        "id": "",
        "name": "Iphone 8",
        "slug": "iphone-8",
        "sku": "IPHONE-8",
        "type": "simple",
        "status": "draft",
        "catalogVisibility": "visible",
        "longDescription": "",
        "shortDescription": "The best iPhone ever, with 3gb RAM and 64 GB ROM. Glass back, apple touch and siri",
        "price": "9.99",
        "regularPrice": "9.99",
        "salePrice": "",
        "saleStartDate": None,
        "saleEndDate": None,
        "onSale": False,
        "totalSales": 0,
        "virtual": False,
        "quantity": -1,
        "soldIndividually": True,
        "weight": "",
        "shippingTaxable": False,
        "reviewsAllowed": True,
        "averageRating": 0,
        "ratingCount": 0,
        "relatedIds": [],
        "upsellsIds": [],
        "crossSellIds": [],
        "parentId": "no-parent",
        "purchaseNote": "Purchase Note",
        "categories": [],
        "tags": ["bags"],
        "images": [
            {
                "id": "",
                "alt": "Iphone 8 image",
                "name": "Iphone 8",
                "height": 480,
                "position": 0,
                "src": "https://pexels.com/some-iphone-image",
                "width": 480,
                "createdAt": "{{currentDate}}",
                "updatedAt": "{{currentDate}}",
            }
        ],
        "attributes": [
            {
                "id": "",
                "name": "color",
                "position": 0,
                "values": ["white", "silver", "black", "gold"],
                "variation": True,
                "visible": True,
                "createdAt": "{{currentDate}}",
                "updatedAt": "{{currentDate}}",
            }
        ],
        "variations": None,
        "menuOrder": 0,
        "metadata": [{"key": "title", "value": "Iphone 8"}],
        "createdAt": "{{currentDate}}",
        "updatedAt": "{{currentDate}}",
    }
    return ProductPostRequest(**data)


@pytest.fixture(scope="function")
def product(product_req: ProductPostRequest) -> Product:
    return json_mapper.map_to_domain(product_req)

    """   return Product(
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
        sale_start_date=now,
        sale_end_date=datetime.now() + timedelta(hours=1),
        categories=["default"],
        images=[
            ProductImage(
                id="",
                height=250,
                name="iphone8",
                src="iphone8.png",
                width=250,
                created_at=now,
                updated_at=now,
            )
        ],
        attributes=[
            ProductAttribute(
                id="",
                name="color",
                values={"black", "red"},
                created_at=now,
                updated_at=now,
            )
        ],
        metadata=[ProductMetadata(id="", key="slug", value="iphone-8")],
        created_at=now,
        updated_at=now + timedelta(minutes=60),
    )

 """
@pytest.fixture(scope="function")
def product_orm(product: Product) -> ProductORM:
    return mariadb_mapper.map_from_domain(product)


@pytest.fixture(scope="function")
def product_post_response(product: Product) -> ProductPostResponse:
    return json_mapper.map_from_domain(product)
