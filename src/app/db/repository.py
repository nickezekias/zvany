from typing import Generic, TypeVar
from src.domain.base.i_repository import IRepository
from src.domain.base.mapper import Mapper

from src.app.db.base_class import Base as BaseORM


import sqlalchemy as sa
from sqlalchemy.orm import Session
from loguru import logger

TEntity = TypeVar("TEntity")
ORMEntity = TypeVar("ORMEntity")
DbContext = TypeVar("DbContext")
TQuery = TypeVar("TQuery")


class Repository(Generic[ORMEntity, TEntity], IRepository[ORMEntity, TEntity]):
    db: Session
    mapper: Mapper

    def __init__(self, db: Session, mapper: Mapper) -> None:
        self.db = db
        self.mapper = mapper

    def get(self, id: int | str):
        pass

    def get_all(self) -> list[TEntity]:
        # orms: list[ORMEntity] = self.db.scalars(sa.select(ProductORM).order_by(ProductORM.id)).all()
        orms = self.db.query(ORMEntity).all()
        entities = self.mapper.map_to_domain_list(orms)
        return entities

    def find(self, query: TQuery) -> list[TEntity]:
        orms: list[ORMEntity] = self.db.query.filter(query).all()
        entities = self.mapper.map_to_domain_list(orms)
        return entities

    def add(self, entity: TEntity) -> None:
        orm = self.mapper.map_from_domain(entity)
        self.db.add(orm)

    def update(self, entity: TEntity) -> TEntity:
        pass

    # TODO: Return refreshed entities instead of input entities
    def add_range(self, entities: list[TEntity]) -> list[TEntity]:
        orms: list[ORMEntity] = self.mapper.map_from_domain_list(entities)
        self.db.add_all(orms)
        return entities

    def remove(self, id: str | int) -> None:
        pass

    def remove_range(self, entities: list[TEntity]) -> None:
        return super().remove_range()

    def commit(self) -> None:
        try:
            self.db.commit()
        except sa.exc.SQLAlchemyError as e:
            error = str(e.__dict__["orig"])
            logger.error(error)
            raise Exception(error)

    def refresh(self, entity: TEntity) -> None:
        self.db.refresh(entity)
