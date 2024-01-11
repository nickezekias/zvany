from pydantic import BaseModel

class ProductMetadataRequest(BaseModel):
    id: str = ""
    key: str
    value: str
