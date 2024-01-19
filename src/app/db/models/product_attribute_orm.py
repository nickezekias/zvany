from sqlalchemy import Boolean, Column, DateTime, String, SmallInteger

from src.app.db.base_class import Base

class ProductAttributeORM(Base):
    __tablename__="product_attributes" # type: ignore

    id=Column(String(36), primary_key=True, index=True)
    name = Column(String)
    position = Column(SmallInteger)
    values = Column(String)
    variation = Column(Boolean())
    visible = Column(Boolean())
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
