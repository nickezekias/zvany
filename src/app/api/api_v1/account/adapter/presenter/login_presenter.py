from fastapi import HTTPException

from src.domain.account.i_login_presenter import ILoginPresenter
from src.app.api.api_v1.account.adapter.response.login_response import LoginResponse

class LoginPresenter(ILoginPresenter):
    def output(self, data: LoginResponse) -> dict:
        return data.dict()

    def output_error_user_not_found(self) -> None:
        raise HTTPException(
            status_code = 404,
            detail = "account.login.errors.userNotFound"
        )
