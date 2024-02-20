from src.app.api.api_v1.product.adapter.response.product_attribute_response import (
    ProductAttributeResponse,
)
from src.domain.product.i_product_attribute_repository import (
    IProductAttributeRepository,
)
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_attribute_presenter import IProductAttributePresenter
from src.domain.product.product_attribute import ProductAttribute


class UpdateProductAttribute(IUseCase):
    repository: IProductAttributeRepository
    presenter: IProductAttributePresenter

    def __init__(
        self,
        repository: IProductAttributeRepository,
        presenter: IProductAttributePresenter,
    ) -> None:
        self.repository = repository
        self.presenter = presenter

    async def execute(
        self, payload: dict[str, ProductAttribute]
    ) -> ProductAttributeResponse | None:
        product_attr_input: ProductAttribute = payload["product_attribute"]

        found_product_attr = self.repository.get(product_attr_input.id)
        if not found_product_attr:
            return self.presenter.output_error_object_not_found(
                "productAttribute.updateUseCase.error.objectNotFound"
            )

        product_attr = self.repository.update(product_attr_input)

        try:
            self.repository.commit()
        except Exception as e:
            return self.presenter.output_error_server_db_commit(str(e))

        if not product_attr:
            return self.presenter.output_error_server_db_commit(
                "productAttribute.update_use_case.error.couldNotCommitUpdateToDB"
            )

        return self.presenter.output_update(product_attr)
