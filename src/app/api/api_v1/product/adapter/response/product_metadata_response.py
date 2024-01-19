from pydantic import BaseModel

class ProductMetadataResponse(BaseModel):
    id: str
    key: str
    value: str
