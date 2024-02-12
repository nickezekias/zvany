from fastapi import APIRouter, Depends
from src.app.api.api_v1.deps import get_db, get_product_mariadb_repository
from src.app.api.api_v1.product.adapter.presenter.product_json_mapper import ProductJsonMapper
from src.app.api.api_v1.product.adapter.presenter.product_presenter import ProductPresenter
from src.app.api.api_v1.product.adapter.request.product_request import ProductPostRequest

from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.app.api.api_v1.product.use_case.create_product import CreateProduct
from src.app.api.api_v1.product.use_case.get_all_products import GetAllProducts
from src.app.db.models.product_orm import ProductORM
from src.domain.base.mapper import Mapper
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.i_product_repository import IProductRepository

import sqlalchemy as sa

router = APIRouter(
    tags=["product"]
)

@router.get("/test", status_code=200)
async def test(db=Depends(get_db)):
    return db.execute(sa.select(ProductORM)).all()


@router.get("/", response_model=list[ProductPostResponse], status_code=200)
async def index(
    repository: IProductRepository = Depends(get_product_mariadb_repository),
) -> list[ProductPostResponse]:
    presenter: IProductPresenter = ProductPresenter()
    return await GetAllProducts(repository, presenter).execute()

@router.post("/", response_model=ProductPostResponse | None, status_code=200)
async def create(
    product_req: ProductPostRequest,
    repository: IProductRepository = Depends(get_product_mariadb_repository),
) -> ProductPostResponse | None:
    presenter: IProductPresenter = ProductPresenter()
    mapper: Mapper = ProductJsonMapper()

    try:
        product = mapper.map_to_domain(product_req)
    except ValueError as e:
        return presenter.output_error_domain_validation(str(e))

    return await CreateProduct(repository, presenter).execute({ "product": product })
