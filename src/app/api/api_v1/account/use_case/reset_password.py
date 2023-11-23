from dataclasses import dataclass
from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_authenticator import IAuthenticator

from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.user import User
from src.domain.account.pr_token import PRToken
from src.domain.util.i_crypto import ICrypto
from src.app.core.constants import TokenLabels

class ResetPassword(IUseCase):
    repository: IAccountRepository
    presenter: IAccountPresenter
    crypto: ICrypto
    authenticator: IAuthenticator

    def __init__(
        self,
        repository: IAccountRepository,
        presenter: IAccountPresenter,
        crypto: ICrypto,
        authenticator: IAuthenticator
    ) -> None:
        self.repository = repository
        self.presenter = presenter
        self.crypto = crypto
        self.authenticator = authenticator

    @dataclass
    class Request:
        token: str
        email: str
        password: str
        password_confirmation: str

    @dataclass
    class Response:
        success: bool
        message: str

    async def execute(self, payload: Request) -> Response:
        user: User = self.repository.get_by_email(payload.email)
        if not user:
            self.presenter.output_error_user_not_found()

        if not user.active():
            self.presenter.output_error_inactive_account()

        
        if not payload.password == payload.password_confirmation:
            self.presenter.output_error_passwords_not_same()

        token_payload = self.crypto.verify_token(payload.token)
        if not token_payload:
            self.presenter.output_error_invalid_token()

        user_id = token_payload["sub"]

        if not token_payload["label"] == TokenLabels.RESET_PASSWORD and user_id:
            self.presenter.output_error_invalid_token()

        if not user_id == user.id:
            self.presenter.output_error_invalid_token()
            
        #verify token has not been used
        pr_token: PRToken = self.repository.get_pr_token(payload.token)
        if not pr_token:
            self.presenter.output_error_invalid_token()
        if pr_token.is_used():
            self.presenter.output_error_invalid_token("token.used")

        # update user
        password = self.authenticator.get_password_hash(payload.password)
        user.password = password
        self.repository.update(user)
        
        # update token, set as used
        pr_token.set_as_used()
        self.repository.update_pr_token(pr_token)
        
        try:
            self.repository.commit()
        except Exception as e:
            self.presenter.output_error_invalid_token(str(e))
        return self.presenter.output_reset_password()

        


