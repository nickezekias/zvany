from pydantic import BaseModel

class ProductAttributeRequest(BaseModel):
    id: str = ""
    name: str
    position: int
    values: set[str]
    variation: bool
    visible: bool
    createdAt: str
    updatedAt: str
