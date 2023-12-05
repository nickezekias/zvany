from datetime import timedelta
from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_authenticator import IAuthenticator
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_login_presenter import ILoginPresenter
from src.app.api.api_v1.account.adapter.request.login_request import LoginRequest
from src.app.api.api_v1.account.adapter.response.login_response import LoginResponse

class Login(IUseCase):
    repository: IAccountRepository
    presenter: ILoginPresenter
    authenticator: IAuthenticator

    def __init__(self, repository: IAccountRepository, presenter: ILoginPresenter, authenticator: IAuthenticator) -> None:
        super().__init__()
        self.repository = repository
        self.presenter = presenter
        self.authenticator = authenticator

    async def execute(self, data: LoginRequest, access_token_expires: timedelta) -> dict | None:
        user = self.repository.get_by_email(data.username)
        if not user:
            self.presenter.output_error_user_not_found()

        if not self.authenticator.verify_password(data.password, user.password):
            self.presenter.output_error_user_not_found()

        token = self.authenticator.create_access_token({ "user_id":user.id }, expires_after=access_token_expires)
        return self.presenter.output(LoginResponse(token=token, type="bearer"))
