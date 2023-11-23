from typing import Generic, TypeVar
from src.domain.base.i_repository import IRepository
from src.domain.base.mapper import Mapper

import sqlalchemy
from loguru import logger

TEntity = TypeVar('TEntity')
ORMEntity = TypeVar('ORMEntity')
DbContext = TypeVar('DbContext')
TQuery = TypeVar('TQuery')

class Repository(Generic[ORMEntity, TEntity], IRepository[ORMEntity, TEntity]):
    db: DbContext
    mapper: Mapper

    def __init__(self, db: DbContext, mapper: Mapper) -> None:
        self.db = db
        self.mapper = mapper

    def get(self, id: int | str) -> TEntity:
        # orm: ORMEntity = self.db.get(ORMEntity, id)
        orm: ORMEntity = self.db.query(ORMEntity).get(id)
        return self.mapper.mapToDomain(orm)

    def getAll(self) -> list[TEntity]:
        orms: list[ORMEntity] = self.db.query.all()
        entities = self.mapper.mapToDomainList(orms)
        return entities

    def find(self, query: TQuery) -> list[TEntity]:
        orms: list[ORMEntity] = self.db.query.filter(query).all()
        entities = self.mapper.mapToDomainList(orms)
        return entities

    def add(self, entity: TEntity) -> None:
        orm = self.mapper.mapFromDomain(entity)
        self.db.add(orm)

    def update(self, entity: TEntity) -> TEntity:
        pass



    #TODO: Return refreshed entities instead of input entities
    def add_range(self, entities: list[TEntity]) -> list[TEntity]:
        orms: list[ORMEntity] = self.mapper.mapFromDomainList(entities)
        self.db.add_all(orms)
        return entities

    def remove(self, entity: TEntity) -> None:
        orm = self.mapper.mapFromDomain(entity)
        self.db.remove(orm)

    def remove_range(self, entities: list[TEntity]) -> None:
        return super().remove_range()

    def commit(self) -> None:
        try:
            self.db.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            logger.error(error)
            raise Exception(error)

    def refresh(self, entity: TEntity) -> None:
        self.db.refresh(entity)





    
