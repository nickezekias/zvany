from pydantic import BaseModel

class ProductMetadataResponse(BaseModel):
    key: str
    value: str
