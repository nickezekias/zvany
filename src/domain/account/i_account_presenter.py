from abc import abstractmethod
from src.domain.base.i_presenter import IPresenter

class IAccountPresenter(IPresenter):
    #shared
    @abstractmethod
    def output_error_user_not_found(self) -> None:
        pass

    @abstractmethod
    def output_error_user_with_credentials_not_found(self) -> None:
        pass

    @abstractmethod
    def output_error_account_with_email_not_found(self) -> None:
        pass

    @abstractmethod
    def output_error_inactive_account(self) -> None:
        pass

    @abstractmethod
    def output_error_email_already_verified(self) -> None:
        pass

    @abstractmethod
    def output_error_invalid_auth_token(self) -> None:
        pass


    # verify email outputs -----------------------------------------------
    @abstractmethod
    def output_verify_email(self) -> dict:
        pass

    @abstractmethod
    def output_resend_email_verification(self) -> dict:
        pass

    @abstractmethod
    def output_error_login_to_verify_email(self) -> None:
        pass
    
    @abstractmethod
    def output_error_invalid_email_verification_link(self) -> None:
        pass


    # forgot password
    @abstractmethod
    def output_forgot_password(self) -> None:
        pass

    # reset password
    @abstractmethod
    def output_error_invalid_password_reset_token(self) -> None:
        pass

    @abstractmethod
    def output_error_passwords_not_same(self) -> None:
        pass

    @abstractmethod
    def output_reset_password(self) -> dict:
        pass