from datetime import datetime, timedelta

from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.util.i_crypto import ICrypto
from src.domain.notification.notification import Notification
from src.domain.account.user import User
from src.domain.account.pr_token import PRToken
from src.app.core.constants import TokenLabels



class ForgotPassword(IUseCase):
    repository: IAccountRepository
    presenter: IAccountPresenter
    crypto: ICrypto
    notification: Notification
    FORGOT_PASSWORD_TOKEN_EXP = 60

    def __init__(
        self,
        repository: IAccountRepository,
        presenter: IAccountPresenter,
        crypto: ICrypto,
        notification: Notification
    ) -> None:
        self.repository = repository
        self.presenter = presenter
        self.crypto = crypto
        self.notification = notification

    async def execute(self, email: str) -> dict:
        user: User = self.repository.get_by_email(email)
        if not user:
            self.presenter.output_error_user_not_found()

        token = self.crypto.generate_token(
            data={"nbf": datetime.utcnow(), "sub": user.id, "label": TokenLabels.RESET_PASSWORD},
            expires_after=timedelta(minutes=self.FORGOT_PASSWORD_TOKEN_EXP)
        )
        # add token to pr (password reset) tokens table
        pr_token = PRToken(
            id="",
            email=user.email,
            token=token,
            created_at=datetime.now(),
            used_at=None, ip_address=None,
            user_agent=None
        )
        self.repository.add_pr_token(pr_token)
        try:
            self.repository.commit()
        except Exception as e:
            self.presenter.output_error_invalid_password_reset_token(error=str(e))


        # init and send  notification
        self.notification.notifiable = user
        self.notification.token = token
        await self.notification.send()

        return self.presenter.output_forgot_password()
