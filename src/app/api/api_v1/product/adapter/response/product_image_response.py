from datetime import datetime
from pydantic import BaseModel

class ProductImageResponse(BaseModel):
    """DTO for ProductImage response"""
    id: str
    alt: str
    height: int
    name: str
    position: int
    src: str
    width: int
    createdAt: datetime
    updatedAt: datetime
