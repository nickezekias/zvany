from src.app.api.api_v1.product.adapter.response.product_category_response import (
    ProductCategoryResponse,
)
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_category_presenter import IProductCategoryPresenter
from src.domain.product.i_product_category_repository import IProductCategoryRepository
from src.domain.product.product_category import ProductCategory


class GetAllProductCategories(IUseCase):
    repository: IProductCategoryRepository
    presenter: IProductCategoryPresenter

    def __init__(
        self,
        repository: IProductCategoryRepository,
        presenter: IProductCategoryPresenter,
    ) -> None:
        self.repository = repository
        self.presenter = presenter

    async def execute(self, payload: dict[str, dict]) -> list[ProductCategoryResponse]:
        product_attrs: list[ProductCategory] = self.repository.get_all()
        return self.presenter.output_index(product_attrs)
