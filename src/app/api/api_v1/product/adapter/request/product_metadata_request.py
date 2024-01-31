from pydantic import BaseModel

class ProductMetadataRequest(BaseModel):
    key: str
    value: str
