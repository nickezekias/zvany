from typing import TypeVar
from src.domain.notification.notification import Notification
from src.domain.account.user import User
from src.app.email.email_service import EmailService

class ForgotPasswordNotification(Notification[User]):
    _token: str

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, value) -> None:
        self._token = value


    def via(self, channels: list[Notification.Channels] = [Notification.Channels.EMAIL]) -> list[Notification.Channels]:
        return channels

    async def to_mail(self):
        # []FIXME: Use frontend route
        url = f"/test-reset-password?token={self.token}"
        await EmailService([self.notifiable.email]).sendMail(
            'Zvany Password help',
            'reset_password',
            template_data={ "name": self.notifiable.full_name(), "url": url }   
        )
