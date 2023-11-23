from pydantic import BaseModel, EmailStr

class UserPostResponse(BaseModel):
    id: str
    avatar: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    email_verified_at: str | None
    phone_verified_at: str | None
    ID_document: str
    ID_document_verified_at: str | None
    is_active: bool
    created_at: str
    updated_at: str