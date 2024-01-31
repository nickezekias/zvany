from dataclasses import dataclass
from datetime import datetime

from src.domain.util.validator import Validator
from src.domain.product.product_attribute import ProductAttribute
from src.domain.product.product_image import ProductImage
from src.domain.product.product_metadata import ProductMetadata

from src.domain.base.entity import Entity


@dataclass
class Product(Entity):
    """Main Product class - has 38 attrs"""

    name: str
    slug: str
    sku: str
    type: str
    status: str
    catalog_visibility: str
    long_description: str
    short_description: str
    price: str
    regular_price: str
    sale_price: str
    sale_start_date: datetime | None
    sale_end_date: datetime | None
    on_sale: bool
    total_sales: int
    virtual: bool
    quantity: int
    sold_individually: bool
    weight: str
    shipping_taxable: bool
    reviews_allowed: bool
    average_rating: int
    rating_count: int
    related_ids: list[str] | None
    upsells_ids: list[str] | None
    cross_sells_ids: list[str] | None
    parent_id: str
    purchase_note: str
    categories: list[str]
    tags: list[str] | None
    images: list[ProductImage]
    attributes: list[ProductAttribute]
    variations: list[str] | None
    """menu_order: Menu order, to custom sort the resource"""
    menu_order: int
    metadata: list[ProductMetadata]
    created_at: datetime
    updated_at: datetime
    id: str

    CATALOG_VISIBILITY = {
        "VISIBLE": "visible",
        "CATALOG": "catalog",
        "SEARCH": "search",
        "HIDDEN": "hidden",
    }
    CATEGORY_DEFAULT = "default"
    PRODUCT_TYPES = {
        "SIMPLE": "simple",
        "GROUPED": "grouped",
        "EXTERNAL": "external",
        "VARIABLE": "variable",
    }
    PRODUCT_STATUS = {
        "DRAFT": "draft",
        "PENDING": "pending",
        "PRIVATE": "private",
        "PUBLISHED": "published",
    }

    def __init__(
        self,
        # pylint: disable=W0622
        id: str,
        # pylint: enable=W0622
        name: str,
        slug: str,
        sku: str,
        long_description: str,
        short_description: str,
        price: str,
        regular_price: str,
        sale_price: str,
        categories: list[str],
        images: list[ProductImage],
        attributes: list[ProductAttribute],
        metadata: list[ProductMetadata],
        created_at: datetime,
        updated_at: datetime,
        status: str = PRODUCT_STATUS["DRAFT"],
        catalog_visibility: str = CATALOG_VISIBILITY["VISIBLE"],
        # pylint: disable=W0622
        type: str = PRODUCT_TYPES["SIMPLE"],
        # pylint: disable=W0622
        sale_start_date: datetime | None = None,
        sale_end_date: datetime | None = None,
        on_sale: bool = False,
        total_sales: int = 0,
        virtual: bool = False,
        quantity: int = -1,
        sold_individually: bool = True,
        weight: str = "",
        shipping_taxable: bool = True,
        reviews_allowed: bool = True,
        average_rating: int = 0,
        rating_count: int = 0,
        related_ids: list[str] | None = None,
        upsells_ids: list[str] | None = None,
        cross_sells_ids: list[str] | None = None,
        parent_id: str = "",
        purchase_note: str = "",
        tags: list[str] | None = None,
        variations: list[str] | None = None,
        menu_order: int = 0,
    ) -> None:
        self.id = id

        super().__init__()

        self.name = name
        self.slug = slug
        self.sku = sku
        self.type = type
        self.status = status
        self.catalog_visibility = catalog_visibility
        self.long_description = long_description
        self.short_description = short_description
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.sale_start_date = sale_start_date
        self.sale_end_date = sale_end_date
        self.on_sale = on_sale
        self.total_sales = total_sales
        self.virtual = virtual
        self.quantity = quantity
        self.sold_individually = sold_individually
        self.weight = weight
        self.shipping_taxable = shipping_taxable
        self.reviews_allowed = reviews_allowed
        self.average_rating = average_rating
        self.rating_count = rating_count
        self.related_ids = related_ids
        self.upsells_ids = upsells_ids
        self.cross_sells_ids = cross_sells_ids
        self.parent_id = parent_id
        self.purchase_note = purchase_note
        self.categories = categories
        self.tags = tags
        self.images = images
        self.attributes = attributes
        self.variations = variations
        self.menu_order = menu_order
        self.metadata = metadata
        self.created_at = created_at
        self.updated_at = updated_at

        self.validate_is_string_with_len_gte_min("name", self.name, 3)
        self.validate_is_non_empty_string("sku", self.sku)
        self.validate_type()
        self.validate_status()
        self.validate_catalog_visibility()
        self.validate_is_non_empty_string("short_description", self.short_description)
        self.validate_is_non_empty_price("price", self.price)
        self.validate_is_non_empty_price("regular_price", self.regular_price)
        self.validate_sale_price()
        self.validate_sale_start_date()
        self.validate_sale_end_date()
        self.validate_quantity()
        self.validate_is_datetime("created_at", self.created_at)
        self.validate_is_datetime_gte_min(
            "updated_at", self.updated_at, self.created_at
        )

        self.validate()

    def validate_type(self) -> bool:
        """Checks if attr and returns True if valid and False if not"""
        if (
            Validator.is_non_empty_string(self.type)
            and self.type in self.PRODUCT_TYPES.values()
        ):
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": "Product, type",
                    "msg": "Attribute must be a non empty str and an item of Product.PRODUCT_TYPES list",
                    "input": self.type,
                }
            )
            return False

    def validate_status(self) -> bool:
        """Checks if attr and returns True if valid and False if not"""
        if (
            Validator.is_non_empty_string(self.status)
            and self.status in self.PRODUCT_STATUS.values()
        ):
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": "Product, status",
                    "msg": "Attribute must be a non empty str and a and an item of Product.PRODUCT_STATUS list",
                    "input": self.status,
                }
            )
            return False

    def validate_catalog_visibility(self) -> bool:
        """Checks if attr and returns True if valid and False if not"""
        if (
            Validator.is_non_empty_string(self.catalog_visibility)
            and self.catalog_visibility in self.CATALOG_VISIBILITY.values()
        ):
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": "Product, catalog_visibility",
                    "msg": "Attribute must be a non empty str and an item of Product.CATALOG_VISIBILITY list",
                    "input": self.catalog_visibility,
                }
            )
            return False

    def validate_is_non_empty_price(self, attr_name: str, attr_value: str) -> bool:
        """
        Checks if attr and returns True if valid and False if not
            Parameters:
                attr_name (str): A string representing the name of the var
                attr_value (str): The actual variable representing it's value

            Returns:
                is_valid (bool): Validation status, if valid returns True, if not False
        """
        if Validator.is_non_empty_string(attr_value) and float(attr_value) > 0:
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": f"{self.get_class_name()}, {attr_name}",
                    "msg": "Attribute must be a non-empty str with a value gt than 0",
                    "input": attr_value,
                }
            )
            return False

    def validate_sale_price(self) -> bool:
        if (
            Validator.is_string(self.sale_price)
            and self.sale_start_date is None
            and self.sale_price == ""
        ):
            return True
        elif (
            Validator.is_non_empty_string(self.sale_price)
            and self.sale_start_date is not None
            and float(self.sale_price) > 0
        ):
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": f"{self.get_class_name()}, sale_price",
                    "msg": "Attribute must be a non-empty str with a value gt than 0 when sale_start_date is set, otherwise it should an empty str",
                    "input": self.sale_price,
                }
            )
            return False

    def validate_sale_start_date(self) -> bool:
        """Check sale_start_date is valid date >= 2023-12-31"""
        if self.sale_start_date is None:
            return True
        elif Validator.is_valid_datetime(
            self.sale_start_date
        ) and self.sale_start_date > datetime(2023, 12, 31):
            return True
        else:
            self.errors.append(
                {
                    "type": "datetime",
                    "loc": f"{self.get_class_name()}, sale_start_date",
                    "msg": "attribute should be a valid datetime and >= 2023-12-31",
                    "input": self.sale_start_date,
                }
            )
            return False

    def validate_sale_end_date(self) -> bool:
        """Check sale_end_date is valid date > sale_start_date"""
        if self.sale_end_date is None and self.sale_start_date is None:
            return True
        elif (
            self.sale_end_date
            and Validator.is_valid_datetime(self.sale_end_date)
            and self.sale_start_date
            and Validator.is_valid_datetime(self.sale_start_date)
        ):
            time_diff = self.sale_end_date - self.sale_start_date
            if time_diff.seconds >= 3600:
                return True
            else:
                self.errors.append(
                    {
                        "type": "datetime",
                        "loc": f"{self.get_class_name()}, sale_start_date",
                        "msg": "sale_end_date should be at least 1 hour gt sale_start_date",
                        "input": self.sale_end_date,
                    }
                )
                return False
        else:
            self.errors.append(
                {
                    "type": "datetime",
                    "loc": f"{self.get_class_name()}, sale_start_date",
                    "msg": "attribute should be a valid datetime",
                    "input": self.sale_end_date,
                }
            )
            return False

    def validate_quantity(self) -> bool:
        """ "Checks quantity is a non-empty string with a min of -1"""
        if Validator.is_int_gte_min(self.quantity, -1):
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": f"{self.get_class_name()}, quantity",
                    "msg": "Attribute must be a non-empty str with a value gt than 0",
                    "input": self.quantity,
                }
            )
            return False

    def lazy_validation(self) -> None:
        self.validate_is_string_with_len_gte_min("name", self.name, 3)
        self.validate_is_non_empty_string("sku", self.sku)
        self.validate_type()
        self.validate_status()
        self.validate_catalog_visibility()
        self.validate_is_non_empty_string("short_description", self.short_description)
        self.validate_is_non_empty_price("price", self.price)
        self.validate_is_non_empty_price("regular_price", self.regular_price)
        self.validate_sale_price()
        self.validate_sale_start_date()
        self.validate_sale_end_date()
        self.validate_quantity()
        self.validate_is_datetime("created_at", self.created_at)
        self.validate_is_datetime_gte_min(
            "updated_at", self.updated_at, self.created_at
        )
        self.validate()
