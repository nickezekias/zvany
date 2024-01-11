from pydantic import BaseModel

class ProductImageRequest(BaseModel):
    """DTO for ProductImage requests validation"""
    id: str = ""
    alt: str = ""
    name: str
    height: int
    position: int
    src: str
    width: int
    createdAt: str
    updatedAt: str
