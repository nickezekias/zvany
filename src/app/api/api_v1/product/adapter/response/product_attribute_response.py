from datetime import datetime
from pydantic import BaseModel

class ProductAttributeResponse(BaseModel):
    id: str
    name: str
    position: int
    values: set[str]
    variation: bool
    visible: bool
    createdAt: datetime
    updatedAt: datetime
