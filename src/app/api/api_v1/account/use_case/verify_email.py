from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.account.i_account_repository import IAccountRepository
from src.app.api.api_v1.account.adapter.request.verify_email_request import VerifyEmailRequest
from src.app.core.constants import TokenLabels

from src.domain.account.user import User
from src.domain.util.i_crypto import ICrypto


class VerifyEmail(IUseCase):
    repository: IAccountRepository
    presenter: IAccountPresenter
    crypto: ICrypto


    def __init__(
            self,
            repository: IAccountRepository,
            presenter: IAccountPresenter,
            crypto: ICrypto
        ) -> None:
        self.repository = repository
        self.presenter = presenter
        self.crypto = crypto

    async def execute(self, payload: VerifyEmailRequest) -> dict:
        user: User = self.repository.get_by_email(payload.email)
        if not user:
            self.presenter.output_error_account_with_email_not_found()

        if user.email_verified_at != None:
            self.presenter.output_error_email_already_verified()

        token_payload = self.crypto.verify_token(payload.token)
        if not token_payload:
            self.presenter.output_error_invalid_email_verification_link()

        user_id = token_payload["sub"]
        
        if not token_payload["label"] == TokenLabels.VERIFY_EMAIL and user_id:
            self.presenter.output_error_invalid_email_verification_link()
        if not user_id == user.id:
            self.presenter.output_error_invalid_email_verification_link()
        else:
            try:
                self.repository.set_email_as_verified(user)
                self.repository.commit()
            except:
                pass
            return self.presenter.output_verify_email()