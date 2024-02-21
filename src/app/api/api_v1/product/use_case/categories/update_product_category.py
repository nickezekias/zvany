from src.app.api.api_v1.product.adapter.response.product_category_response import (
    ProductCategoryResponse,
)
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_category_presenter import IProductCategoryPresenter
from src.domain.product.i_product_category_repository import IProductCategoryRepository
from src.domain.product.product_category import ProductCategory


class UpdateProductCategory(IUseCase):
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
        product_cat_input: ProductCategory = payload["product_category"]

        found_product_cat = self.repository.get(product_cat_input.id)
        if not found_product_cat:
            return self.presenter.output_error_object_not_found(
                "ProductCategory.updateUseCase.error.objectNotFound"
            )

        product_cat = self.repository.update(product_cat_input)

        try:
            self.repository.commit()
        except Exception as e:
            return self.presenter.output_error_server_db_commit(str(e))

        if not product_cat:
            return self.presenter.output_error_server_db_commit(
                "ProductCategory.update_use_case.error.couldNotCommitUpdateToDB"
            )

        return self.presenter.output_update(product_cat)
