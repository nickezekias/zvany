from src.app.api.api_v1.product.adapter.response.product_response import ProductPostResponse
from src.domain.base.i_use_case import IUseCase
from src.domain.product.i_product_presenter import IProductPresenter
from src.domain.product.i_product_repository import IProductRepository
from src.domain.product.product import Product


class CreateProduct(IUseCase):
    repository: IProductRepository
    presenter: IProductPresenter

    def __init__(
        self,
        repository: IProductRepository,
        presenter: IProductPresenter,
    ) -> None:
        self.repository = repository
        self.presenter = presenter

    async def execute(self, payload: dict[str, Product]) -> ProductPostResponse | None:
        product: Product = payload["product"]
        try:
            product.lazy_validation()
            self.repository.add(product)
            self.repository.commit()
            return self.presenter.output_create(product)
        except ValueError as e:
            return self.presenter.output_error_invalid_data(e)
        except Exception as e:
            return self.presenter.output_error_server_db_commit(str(e))
