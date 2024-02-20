from src.app.api.api_v1.product.adapter.response.product_attribute_response import (
    ProductAttributeResponse,
)
from src.domain.product.i_product_attribute_repository import (
    IProductAttributeRepository,
)
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_attribute_presenter import IProductAttributePresenter
from src.domain.product.product_attribute import ProductAttribute


class CreateProductAttribute(IUseCase):
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
        product_attr: ProductAttribute = payload["product_attribute"]
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
