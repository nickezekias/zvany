import os
from datetime import datetime, timedelta

from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.base.i_use_case import IUseCase
from src.domain.util.i_crypto import ICrypto
from src.domain.notification.notification import Notification
from src.domain.account.user import User
from src.app.core.constants import TokenLabels

class SendEmailVerificationLink(IUseCase):
    crypto: ICrypto
    notification: Notification
    expire_after: int
    repository: IAccountRepository
    presenter: IAccountPresenter

    def __init__(self, crypto: ICrypto, repository: IAccountRepository, presenter: IAccountPresenter, notification: Notification) -> None:
        self.crypto = crypto
        self.repository = repository
        self.presenter = presenter
        self.notification = notification
        self.expire_after = int(os.getenv("MAIL_VERIFY_TOKEN_EXPIRE_MINUTES", "1440"))

    async def execute(self, email: str):
        user = self.repository.get_by_email(email)
        if not user:
            return self.presenter.output_error_user_not_found()
        if not user.active():
            return self.presenter.output_error_inactive_account()
        if user.is_email_verified():
            return self.presenter.output_error_email_already_verified()
        else:
            token = self.crypto.generate_token(
                data={"nbf": datetime.utcnow(), "sub": user.id, "label": TokenLabels.VERIFY_EMAIL},
                expires_after=timedelta(minutes=self.expire_after)
            )
            self.notification.notifiable = user
            self.notification.token = token
            await self.notification.send()
            return self.presenter.output_resend_email_verification()