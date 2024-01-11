from datetime import datetime
from pydantic import BaseModel

from src.app.api.api_v1.product.adapter.response.product_attribute_response import ProductAttributeResponse
from src.app.api.api_v1.product.adapter.response.product_image_response import ProductImageResponse
from src.app.api.api_v1.product.adapter.response.product_metadata_response import ProductMetadataResponse

class ProductPostResponse(BaseModel):
    id: str
    name: str
    slug: str
    sku: str
    type: str
    status: str
    catalogVisibility: str
    longDescription: str
    shortDescription: str
    price: str
    regularPrice: str
    salePrice: str
    saleStartDate: datetime | None
    saleEndDate: datetime | None
    onSale: bool
    totalSales: int
    virtual: bool
    quantity: int
    soldIndividually: bool
    weight: str
    shippingTaxable: bool
    reviewsAllowed: bool
    averageRating: int
    ratingCount: int
    relatedIds: list[str] | None
    upsellsIds: list[str] | None
    crossSellIds: list[str] | None
    parentId: str
    purchaseNote: str
    categories: list[str]
    tags: list[str] | None
    images: list[ProductImageResponse]
    attributes: list[ProductAttributeResponse]
    variations: list[str] | None
    menuOrder: int
    metadata: list[ProductMetadataResponse]
    createdAt: datetime
    updatedAt: datetime
