# from abc import abstractmethod

from src.domain.base.i_repository import IRepository
from src.domain.product.product import Product
from src.app.db.models.product_orm import ProductORM

class IProductRepository(IRepository[ProductORM, Product]):
    """Product Repository Interface"""
