from sqlalchemy import Boolean, Column, DateTime, String, SmallInteger

from src.app.db.base_class import Base


class ProductCategoryORM(Base):
    __tablename__ = "product_categories"  # type: ignore

    id = Column(String(36), primary_key=True, index=True)
    name = Column(String, unique=True)
    position = Column(SmallInteger)
    description = Column(String)
    parent = Column(String)
    slug = Column(String, unique=True)
    visible = Column(Boolean())
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "description": self.description,
            "parent": self.parent,
            "slug": self.slug,
            "visible": self.visible,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def as_dict_update(self) -> dict:
        return {
            "name": self.name,
            "position": self.position,
            "description": self.description,
            "parent": self.parent,
            "slug": self.slug,
            "visible": self.visible,
            "updated_at": self.updated_at,
        }
