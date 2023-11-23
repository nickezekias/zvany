from pydantic import BaseModel

from src.app.api.api_v1.account.adapter.response.user_response import UserPostResponse

class RegisterResponse(BaseModel):
    user: UserPostResponse
    token: str