from sqlalchemy import Boolean, Column, DateTime, String, SmallInteger

from src.app.db.base_class import Base


class ProductAttributeORM(Base):
    __tablename__ = "product_attributes"  # type: ignore

    id = Column(String(36), primary_key=True, index=True)
    name = Column(String, unique=True)
    position = Column(SmallInteger)
    values = Column(String)
    variation = Column(Boolean())
    visible = Column(Boolean())
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "values": self.values,
            "variation": self.variation,
            "visible": self.visible,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def as_dict_update(self) -> dict:
        return {
            "name": self.name,
            "position": self.position,
            "values": self.values,
            "variation": self.variation,
            "visible": self.visible,
            "updated_at": self.updated_at,
        }
