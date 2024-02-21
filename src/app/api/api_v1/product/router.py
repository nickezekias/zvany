from fastapi import APIRouter, Depends

from src.app.api.api_v1 import deps

# from src.app.api.api_v1.deps import get_db, get_product_mariadb_repository
from src.app.api.api_v1.product.adapter.presenter.product_attribute_json_mapper import (
    ProductAttributeJsonMapper,
)
from src.app.api.api_v1.product.adapter.presenter.product_attribute_presenter import (
    ProductAttributePresenter,
)
from src.app.api.api_v1.product.adapter.presenter.product_category_json_mapper import (
    ProductCategoryJsonMapper,
)
from src.app.api.api_v1.product.adapter.presenter.product_category_presenter import (
    ProductCategoryPresenter,
)
from src.app.api.api_v1.product.adapter.presenter.product_json_mapper import (
    ProductJsonMapper,
)
from src.app.api.api_v1.product.adapter.presenter.product_presenter import (
    ProductPresenter,
)
from src.app.api.api_v1.product.adapter.request.product_attribute_request import (
    ProductAttributeRequest,
)
from src.app.api.api_v1.product.adapter.request.product_category_request import (
    ProductCategoryRequest,
)
from src.app.api.api_v1.product.adapter.request.product_request import (
    ProductPostRequest,
)
from src.app.api.api_v1.product.adapter.response.product_attribute_response import (
    ProductAttributeResponse,
)
from src.app.api.api_v1.product.adapter.response.product_category_response import (
    ProductCategoryResponse,
)

from src.app.api.api_v1.product.adapter.response.product_response import (
    ProductPostResponse,
)
from src.app.api.api_v1.product.use_case.attributes.delete_product_attribute import (
    DeleteProductAttribute,
)
from src.app.api.api_v1.product.use_case.attributes.get_all_product_attributes import (
    GetAllProductAttributes,
)
from src.app.api.api_v1.product.use_case.attributes.update_product_attribute import (
    UpdateProductAttribute,
)
from src.app.api.api_v1.product.use_case.categories.create_product_category import (
    CreateProductCategory,
)
from src.app.api.api_v1.product.use_case.categories.get_product_category import (
    GetProductCategory,
)
from src.app.api.api_v1.product.use_case.categories.update_product_category import (
    UpdateProductCategory,
)
from src.app.api.api_v1.product.use_case.create_product import CreateProduct
from src.app.api.api_v1.product.use_case.attributes.create_product_attribute import (
    CreateProductAttribute,
)
from src.app.api.api_v1.product.use_case.get_all_products import GetAllProducts
from src.app.api.api_v1.product.use_case.attributes.get_product_attribute import (
    GetProductAttribute,
)
from src.app.db.models.product_orm import ProductORM
from src.domain.product.i_product_attribute_repository import (
    IProductAttributeRepository,
)
from src.domain.base.mapper import Mapper
from src.domain.product.i_product_attribute_presenter import IProductAttributePresenter
from src.domain.product.i_product_category_presenter import IProductCategoryPresenter
from src.domain.product.i_product_category_repository import IProductCategoryRepository
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.i_product_repository import IProductRepository

import sqlalchemy as sa

from src.domain.product.product_attribute import ProductAttribute
from src.domain.product.product_category import ProductCategory

router = APIRouter(tags=["product"])


@router.get("/test", status_code=200)
async def test(db=Depends(deps.get_db)):
    return db.execute(sa.select(ProductORM)).all()


@router.get("/", response_model=list[ProductPostResponse], status_code=200)
async def index(
    repository: IProductRepository = Depends(deps.get_product_mariadb_repository),
) -> list[ProductPostResponse]:
    presenter: IProductPresenter = ProductPresenter()
    return await GetAllProducts(repository, presenter).execute()


@router.post("/", response_model=ProductPostResponse | None, status_code=201)
async def create(
    product_req: ProductPostRequest,
    repository: IProductRepository = Depends(deps.get_product_mariadb_repository),
) -> ProductPostResponse | None:
    presenter: IProductPresenter = ProductPresenter()
    mapper: Mapper = ProductJsonMapper()
    try:
        product = mapper.map_to_domain(product_req)
    except ValueError as e:
        return presenter.output_error_domain_validation(str(e))

    return await CreateProduct(repository, presenter).execute({"product": product})


"""
        ******************** PRODUCT ATTRIBUTES *********************
"""


@router.post(
    "/attributes", response_model=ProductAttributeResponse | None, status_code=201
)
async def create_attribute(
    product_attr_req: ProductAttributeRequest,
    repository: IProductAttributeRepository = Depends(
        deps.get_product_attribute_mariadb_repository
    ),
) -> ProductAttributeResponse | None:
    presenter: IProductAttributePresenter = ProductAttributePresenter()
    mapper: Mapper = ProductAttributeJsonMapper()
    try:
        product_attr: ProductAttribute = mapper.map_to_domain(product_attr_req)
    except ValueError as e:
        return presenter.output_error_domain_validation(str(e))

    return await CreateProductAttribute(repository, presenter).execute(
        {"product_attribute": product_attr}
    )


@router.get(
    "/attributes/{id}", response_model=ProductAttributeResponse | None, status_code=200
)
async def get_attribute(
    id: str,
    repository: IProductAttributeRepository = Depends(
        deps.get_product_attribute_mariadb_repository
    ),
) -> ProductAttributeResponse | None:
    presenter: IProductAttributePresenter = ProductAttributePresenter()
    return await GetProductAttribute(repository, presenter).execute({"id": id})


@router.get(
    "/attributes", response_model=list[ProductAttributeResponse], status_code=200
)
async def get_attributes(
    repository: IProductAttributeRepository = Depends(
        deps.get_product_attribute_mariadb_repository
    ),
) -> list[ProductAttributeResponse]:
    presenter: IProductAttributePresenter = ProductAttributePresenter()
    return await GetAllProductAttributes(repository, presenter).execute({})


@router.put(
    "/attributes", response_model=ProductAttributeResponse | None, status_code=200
)
async def update_attribute(
    product_attr_req: ProductAttributeRequest,
    repository: IProductAttributeRepository = Depends(
        deps.get_product_attribute_mariadb_repository
    ),
) -> ProductAttributeResponse | None:
    presenter: IProductAttributePresenter = ProductAttributePresenter()
    mapper: Mapper = ProductAttributeJsonMapper()

    try:
        product_attr: ProductAttribute = mapper.map_to_domain(product_attr_req)
    except ValueError as e:
        return presenter.output_error_domain_validation(str(e))

    return await UpdateProductAttribute(repository, presenter).execute(
        {"product_attribute": product_attr}
    )


@router.delete("/attributes/{id}", response_model=dict | None, status_code=200)
async def delete_attribute(
    id: str,
    repository: IProductAttributeRepository = Depends(
        deps.get_product_attribute_mariadb_repository
    ),
) -> dict | None:
    presenter: IProductAttributePresenter = ProductAttributePresenter()
    return await DeleteProductAttribute(repository, presenter).execute({"id": id})


"""

************************** PRODUCT CATEGORIES *****************************

"""


@router.post(
    "/categories", response_model=ProductCategoryResponse | None, status_code=201
)
async def create_category(
    product_cat_req: ProductCategoryRequest,
    repository: IProductCategoryRepository = Depends(
        deps.get_product_category_mariadb_repository
    ),
) -> ProductCategoryResponse | None:
    presenter: IProductCategoryPresenter = ProductCategoryPresenter()
    mapper: Mapper = ProductCategoryJsonMapper()
    try:
        product_cat: ProductCategory = mapper.map_to_domain(product_cat_req)
    except ValueError as e:
        return presenter.output_error_domain_validation(str(e))

    return await CreateProductCategory(repository, presenter).execute(
        {"product_category": product_cat}
    )


@router.get(
    "/categories/{id}", response_model=ProductCategoryResponse | None, status_code=200
)
async def get_category(
    id: str,
    repository: IProductCategoryRepository = Depends(
        deps.get_product_category_mariadb_repository
    ),
) -> ProductCategoryResponse | None:
    presenter: IProductCategoryPresenter = ProductCategoryPresenter()
    return await GetProductCategory(repository, presenter).execute({"id": id})


@router.put(
    "/categories", response_model=ProductCategoryResponse | None, status_code=200
)
async def update_category(
    product_cat_req: ProductCategoryRequest,
    repository: IProductCategoryRepository = Depends(
        deps.get_product_category_mariadb_repository
    ),
) -> ProductCategoryResponse | None:
    presenter: IProductCategoryPresenter = ProductCategoryPresenter()
    mapper: Mapper = ProductCategoryJsonMapper()

    try:
        product_cat: ProductCategory = mapper.map_to_domain(product_cat_req)
    except ValueError as e:
        return presenter.output_error_domain_validation(str(e))

    return await UpdateProductCategory(repository, presenter).execute(
        {"product_category": product_cat}
    )
