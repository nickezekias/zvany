from fastapi import HTTPException, status

from src.domain.account.i_account_presenter import IAccountPresenter
from src.app.core.adapter.presenter import Presenter

class AccountPresenter(Presenter, IAccountPresenter):

    def output_error_user_not_found(self) -> None:
        raise HTTPException(
            status_code = 404,
            detail = "account.shared.errors.userNotFound"
        )

    def output_error_user_with_credentials_not_found(self) -> None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "account.shared.errors.userWithCredentialsNotFound"
        )
    
    def output_error_account_with_email_not_found(self) -> None:
        raise HTTPException(
            status_code = 404,
            detail = "account.shared.errors.accountWithEmailNotFound"
        )

    def output_error_inactive_account(self) -> None:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "account.shared.errors.inactiveAccount"
        )


    def output_error_invalid_auth_token(self) -> None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "account.shared.errors.invalidAuthToken"
        )



    # verify email
    def output_verify_email(self) -> dict:
        return {
            "success": True,
            "message": "account.verifyEmail.success"
        }
        
    def output_resend_email_verification(self) -> dict:
        return {
            "success": True,
            "message": "account.resendEmailVerification.success"
        }

    def output_error_login_to_verify_email(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.verifyEmail.loginToVerifyEmail"
        )

    def output_error_invalid_email_verification_link(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.verifyEmail.invalidVerificationLink"
        )
    
    def output_error_email_already_verified(self) -> None:
        raise HTTPException(
            status_code = 409,
            detail = "account.shared.errors.emailAlreadyVerified"
        )



    # forgot password
    def output_forgot_password(self) -> dict:
        return {
            "success": True,
            "message": "account.forgotPassword.success"
        }

    # reset password
    def output_error_invalid_password_reset_token(self, error: str | None = None) -> dict:
        raise HTTPException(
            status_code=400,
            detail={"message": "account.resetPassword.errors.invalidToken", "details": error }
        )

    def output_error_passwords_not_same(self) -> None:
        raise HTTPException(
            status_code=422,
            detail="account.resetPassword.errors.passwordsNotSame"
        )

    def output_reset_password(self) -> dict:
        return {
            "success": True,
            "message": "account.resetPassword.success"
        }