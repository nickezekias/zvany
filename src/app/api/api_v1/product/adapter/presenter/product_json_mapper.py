from datetime import datetime

from src.domain.util.date_time_util import DateTimeUtil

from src.domain.base.mapper import Mapper
from src.domain.product.product import Product
from src.domain.product.product_attribute import ProductAttribute
from src.domain.product.product_image import ProductImage
from src.domain.product.product_metadata import ProductMetadata

from src.app.api.api_v1.product.adapter.request.product_request import (
    ProductPostRequest,
)
from src.app.api.api_v1.product.adapter.response.product_response import (
    ProductPostResponse,
)
from src.app.api.api_v1.product.adapter.response.product_attribute_response import (
    ProductAttributeResponse,
)
from src.app.api.api_v1.product.adapter.response.product_image_response import (
    ProductImageResponse,
)
from src.app.api.api_v1.product.adapter.response.product_metadata_response import (
    ProductMetadataResponse,
)


class ProductJsonMapper(Mapper[ProductPostRequest, Product | ProductPostResponse]):
    def map_to_domain(self, param: ProductPostRequest) -> Product:
        now = datetime.now()

        product_attributes: list[ProductAttribute] = []
        product_images: list[ProductImage] = []
        product_metadata: list[ProductMetadata] = []
        for product_attr_req in param.attributes:
            product_attributes.append(
                ProductAttribute(
                    id="",
                    name=product_attr_req.name,
                    values=product_attr_req.values,
                    created_at=now,
                    updated_at=now,
                )
            )
        for product_img_req in param.images:
            product_images.append(
                ProductImage(
                    id="",
                    alt=product_img_req.alt,
                    height=product_img_req.height,
                    name=product_img_req.name,
                    src=product_img_req.src,
                    width=product_img_req.width,
                    created_at=now,
                    updated_at=now,
                )
            )
        for product_meta_req in param.metadata:
            product_metadata.append(
                ProductMetadata(
                    id="", key=product_meta_req.key, value=product_meta_req.value
                )
            )

        # converting dates from string to datetime
        sale_start_date = param.saleStartDate
        sale_end_date = param.saleEndDate
        if sale_start_date is not None:
            sale_start_date = DateTimeUtil.string_to_date(sale_start_date)
        if sale_end_date is not None:
            sale_end_date = DateTimeUtil.string_to_date(sale_end_date)

        return Product(
            id="",
            name=param.name,
            slug=param.slug,
            sku=param.sku,
            type=param.type,
            status=param.status,
            catalog_visibility=param.catalogVisibility,
            long_description=param.longDescription,
            short_description=param.shortDescription,
            price=param.price,
            regular_price=param.regularPrice,
            sale_price=param.salePrice,
            sale_start_date=sale_start_date,
            sale_end_date=sale_end_date,
            on_sale=param.onSale,
            total_sales=param.totalSales,
            virtual=param.virtual,
            quantity=param.quantity,
            sold_individually=param.soldIndividually,
            weight=param.weight,
            shipping_taxable=param.shippingTaxable,
            reviews_allowed=param.reviewsAllowed,
            average_rating=param.averageRating,
            rating_count=param.ratingCount,
            related_ids=param.relatedIds,
            upsells_ids=param.upsellsIds,
            cross_sells_ids=param.crossSellIds,
            parent_id=param.parentId,
            purchase_note=param.purchaseNote,
            categories=param.categories,
            tags=param.tags,
            images=product_images,
            attributes=product_attributes,
            variations=param.variations,
            menu_order=param.menuOrder,
            metadata=product_metadata,
            created_at=now,
            updated_at=now,
        )

    def map_to_domain_list(self, params: list[ProductPostRequest]) -> list[Product | ProductPostResponse]:
        return super().map_to_domain_list(params)

    def map_from_domain(self, param: Product) -> ProductPostResponse:
        # sale_start_date = param.sale_start_date
        # sale_end_date = param.sale_end_date
        # if sale_start_date is not None:
        #     sale_start_date = DateTimeUtil.date_to_string(sale_start_date)
        # if sale_end_date is not None:
        #     sale_end_date = DateTimeUtil.date_to_string(sale_end_date)

        product_attributes: list[ProductAttributeResponse] = []
        product_images: list[ProductImageResponse] = []
        product_metadata: list[ProductMetadataResponse] = []
        for product_attr in param.attributes:
            product_attributes.append(
                ProductAttributeResponse(
                    id="",
                    name=product_attr.name,
                    position=product_attr.position,
                    values=product_attr.values,
                    variation=product_attr.variation,
                    visible=product_attr.visible,
                    createdAt=product_attr.created_at,
                    updatedAt=product_attr.updated_at,
                )
            )
        for product_img in param.images:
            product_images.append(
                ProductImageResponse(
                    id="",
                    alt=product_img.alt,
                    height=product_img.height,
                    name=product_img.name,
                    position=product_img.position,
                    src=product_img.src,
                    width=product_img.width,
                    createdAt=product_img.created_at,
                    updatedAt=product_img.updated_at,
                )
            )

        for product_meta in param.metadata:
            product_metadata.append(
                ProductMetadataResponse(
                    id="", key=product_meta.key, value=product_meta.value
                )
            )

        return ProductPostResponse(
            id=param.id,
            name=param.name,
            slug=param.slug,
            sku=param.sku,
            type=param.type,
            status=param.status,
            catalogVisibility=param.catalog_visibility,
            longDescription=param.long_description,
            shortDescription=param.short_description,
            price=param.price,
            regularPrice=param.regular_price,
            salePrice=param.sale_price,
            saleStartDate=param.sale_start_date,
            saleEndDate=param.sale_end_date,
            onSale=param.on_sale,
            totalSales=param.total_sales,
            virtual=param.virtual,
            quantity=param.quantity,
            soldIndividually=param.sold_individually,
            weight=param.weight,
            shippingTaxable=param.shipping_taxable,
            reviewsAllowed=param.reviews_allowed,
            averageRating=param.average_rating,
            ratingCount=param.rating_count,
            relatedIds=param.related_ids,
            upsellsIds=param.upsells_ids,
            crossSellIds=param.cross_sells_ids,
            parentId=param.parent_id,
            purchaseNote=param.purchase_note,
            categories=param.categories,
            tags=param.tags,
            images=product_images,
            attributes=product_attributes,
            variations=param.variations,
            menuOrder=param.menu_order,
            metadata=product_metadata,
            createdAt=param.created_at,
            updatedAt=param.updated_at,
        )
    
    def map_from_domain_list(self, params: list[Product | ProductPostResponse]) -> list[ProductPostRequest]:
        return super().map_from_domain_list(params)
