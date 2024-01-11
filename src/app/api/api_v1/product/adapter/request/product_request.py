from pydantic import BaseModel

from src.app.api.api_v1.product.adapter.request.product_attribute_request import ProductAttributeRequest
from src.app.api.api_v1.product.adapter.request.product_image_request import ProductImageRequest
from src.app.api.api_v1.product.adapter.request.product_metadata_request import ProductMetadataRequest

class ProductPostRequest(BaseModel):
    id: str = ""
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
    saleStartDate: str | None = None
    saleEndDate: str | None = None
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
    relatedIds: list[str] | None = None
    upsellsIds: list[str] | None = None
    crossSellIds: list[str] | None = None
    parentId: str = ""
    purchaseNote: str
    categories: list[str]
    tags: list[str] | None = None
    images: list[ProductImageRequest]
    attributes: list[ProductAttributeRequest]
    variations: list[str] | None = None
    menuOrder: int = 0
    metadata: list[ProductMetadataRequest]
    createdAt: str
    updatedAt: str
