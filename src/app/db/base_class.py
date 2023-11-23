from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr
import uuid

@as_declarative()
class Base:
    id = Column(String(36), primary_key=True, index=True, default=uuid.uuid4)
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
