from src.domain.product.i_product_attribute_repository import (
    IProductAttributeRepository,
)
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_attribute_presenter import IProductAttributePresenter


class DeleteProductAttribute(IUseCase):
    repository: IProductAttributeRepository
    presenter: IProductAttributePresenter

    def __init__(
        self,
        repository: IProductAttributeRepository,
        presenter: IProductAttributePresenter,
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
                "productAttribute.get.error.objectWithIdNotFound"
            )
