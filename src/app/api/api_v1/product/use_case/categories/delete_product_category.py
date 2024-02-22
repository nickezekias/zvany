from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_category_presenter import IProductCategoryPresenter
from src.domain.product.i_product_category_repository import IProductCategoryRepository


class DeleteProductCategory(IUseCase):
    repository: IProductCategoryRepository
    presenter: IProductCategoryPresenter

    def __init__(
        self,
        repository: IProductCategoryRepository,
        presenter: IProductCategoryPresenter,
    ) -> None:
        self.repository = repository
        self.presenter = presenter

    async def execute(self, payload: dict[str, str]) -> dict | None:
        res = self.repository.remove(payload["id"])
        if res:
            try:
                self.repository.commit()
                return self.presenter.output_delete()
            except Exception as e:
                return self.presenter.output_error_server_db_commit(str(e))
        else:
            return self.presenter.output_error_object_not_found(
                "productCategory.get.error.objectWithIdNotFound"
            )
