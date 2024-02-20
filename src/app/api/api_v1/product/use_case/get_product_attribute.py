from src.app.api.api_v1.product.adapter.response.product_attribute_response import (
    ProductAttributeResponse,
)
from src.domain.product.i_product_attribute_repository import (
    IProductAttributeRepository,
)
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_attribute_presenter import IProductAttributePresenter
from src.domain.product.product_attribute import ProductAttribute


class GetProductAttribute(IUseCase):
    repository: IProductAttributeRepository
    presenter: IProductAttributePresenter

    def __init__(
        self,
        repository: IProductAttributeRepository,
        presenter: IProductAttributePresenter,
    ) -> None:
        self.repository = repository
        self.presenter = presenter

    async def execute(self, payload: dict[str, str]) -> ProductAttributeResponse | None:
        product_attr: ProductAttribute = self.repository.get(id=payload["id"])
        if product_attr:
            return self.presenter.output(product_attr)
        return self.presenter.output_error_object_not_found(
            "productAttribute.get.error.objectWithIdNotFound"
        )
