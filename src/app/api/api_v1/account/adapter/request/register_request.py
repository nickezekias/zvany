from pydantic import BaseModel
from src.app.api.api_v1.account.adapter.request.user_request import UserPostRequest

#TODO:Make it so if request contains anything other than user, the request is not processed
class RegisterRequest(BaseModel):
    user: UserPostRequest