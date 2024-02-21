from pydantic import BaseModel, Field


class ProductCategoryRequest(BaseModel):
    id: str
    name: str = Field(min_length=3)
    position: int
    parent: str
    description: str
    slug: str = Field(min_length=3)
    visible: bool
    createdAt: str
    updatedAt: str
