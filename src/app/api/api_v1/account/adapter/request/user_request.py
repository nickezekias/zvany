from pydantic import BaseModel, EmailStr, Field, validator

class UserPostRequest(BaseModel):
    id: str = ""
    avatar: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str = Field(unique=True)
    password: str
    password_confirmation: str
    created_at: str
    updated_at: str

    @validator('password_confirmation')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('register.error.passwordMismatch')
        return v
 