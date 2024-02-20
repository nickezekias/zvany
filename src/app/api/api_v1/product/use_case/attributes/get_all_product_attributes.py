from src.app.api.api_v1.product.adapter.response.product_attribute_response import (
    ProductAttributeResponse,
)
from src.domain.product.i_product_attribute_repository import (
    IProductAttributeRepository,
)
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_attribute_presenter import IProductAttributePresenter
from src.domain.product.product_attribute import ProductAttribute

class GetAllProductAttributes(IUseCase):
    repository: IProductAttributeRepository
    presenter: IProductAttributePresenter

    def __init__(
        self,
        repository: IProductAttributeRepository,
        presenter: IProductAttributePresenter,
    ) -> None:
        self.repository = repository
        self.presenter = presenter


    async def execute(self, payload: dict[str, dict]) -> list[ProductAttributeResponse]:
        product_attrs: list[ProductAttribute] = self.repository.get_all()
        return self.presenter.output_index(product_attrs)
