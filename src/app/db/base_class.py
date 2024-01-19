from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
import uuid

@as_declarative()
class Base:
    id = Column(String(36), primary_key=True, index=True, default=uuid.uuid4)
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"
