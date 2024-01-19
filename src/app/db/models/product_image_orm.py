from sqlalchemy import Column, DateTime, String, SmallInteger

from src.app.db.base_class import Base

class ProductImageORM(Base):
    __tablename__ = "product_images" # type: ignore

    id=Column(String(36), primary_key=True, index=True)
    alt = Column(String)
    height = Column(SmallInteger)
    name = Column(String)
    position = Column(SmallInteger)
    src = Column(String)
    width = Column(SmallInteger)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
