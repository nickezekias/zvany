from fastapi import HTTPException

from src.domain.account.i_register_presenter import IRegisterPresenter
from src.domain.account.user import User

from src.app.core.adapter.presenter import Presenter

from src.app.api.api_v1.account.adapter.presenter.account_json_mapper import AccountJsonMapper
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse

class RegisterPresenter(Presenter, IRegisterPresenter):

    def output(self, user: User) -> RegisterResponse:
        user_res = AccountJsonMapper().mapFromDomain(user)
        return {
            "user": user_res,
            "token": user.token
        }

    def output_error_email_exists(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.errors.emailExists"
        )
    
    def output_error_phone_exists(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.errors.phoneExists"
        )
    
    def output_error_user_data_duplicate(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.errors.userDataDuplicate"
        )
    
    def output_error_invalid_data(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.errors.invalidData"
        )