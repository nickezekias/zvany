from src.app.api.api_v1.product.adapter.response.product_category_response import (
    ProductCategoryResponse,
)
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_category_presenter import IProductCategoryPresenter
from src.domain.product.i_product_category_repository import IProductCategoryRepository
from src.domain.product.product_category import ProductCategory


class CreateProductCategory(IUseCase):
    repository: IProductCategoryRepository
    presenter: IProductCategoryPresenter

    def __init__(
        self,
        repository: IProductCategoryRepository,
        presenter: IProductCategoryPresenter,
    ) -> None:
        self.repository = repository
        self.presenter = presenter

    async def execute(
        self, payload: dict[str, ProductCategory]
    ) -> ProductCategoryResponse | None:
        product_attr: ProductCategory = payload["product_category"]
        if self.repository.get_by_name(product_attr.name) is not None:
            return self.presenter.output_error_duplicate_name()
        try:
            product_attr.lazy_validation()
            self.repository.add(product_attr)
            self.repository.commit()
            return self.presenter.output_create(product_attr)
        except ValueError as e:
            return self.presenter.output_error_invalid_data(e)
        except Exception as e:
            return self.presenter.output_error_server_db_commit(str(e))
