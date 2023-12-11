from fastapi import APIRouter, BackgroundTasks, Form, Depends
from datetime import timedelta
from datetime import datetime
from pydantic import EmailStr

from typing import Any

from src.app.api.api_v1.config import Settings
from src.domain.account.user import User

from src.domain.account.i_authenticator import IAuthenticator
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_account_presenter import IAccountPresenter
from src.app.api.api_v1.account.adapter.presenter.account_presenter import AccountPresenter

from src.app.api.api_v1.account.adapter.request.login_request import LoginRequest
from src.app.api.api_v1.account.adapter.response.login_response import LoginResponse
from src.app.api.api_v1.account.adapter.controller.login_controller import LoginController

from src.app.api.api_v1.account.adapter.request.register_request import RegisterRequest
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse
from src.app.api.api_v1.account.adapter.controller.register_controller import RegisterController
from src.app.api.api_v1.account.adapter.presenter.register_presenter import RegisterPresenter

from src.app.api.api_v1.account.use_case.send_email_verification_link import SendEmailVerificationLink as SendEmailVerificationLinkUseCase
from src.app.api.api_v1.account.adapter.request.verify_email_request import VerifyEmailRequest
from src.app.api.api_v1.account.use_case.verify_email import VerifyEmail as VerifyEmailUseCase

from src.app.api.api_v1.account.adapter.notification.forgot_password_notification import ForgotPasswordNotification
from src.app.api.api_v1.account.use_case.forgot_password import ForgotPassword as ForgotPasswordUseCase

from src.app.api.api_v1.account.use_case.reset_password import ResetPassword as ResetPasswordUseCase



from src.domain.notification.notification import Notification
from src.app.api.api_v1.account.adapter.notification.verify_email_notification import VerifyEmailNotification

from src.app.core.util.crypto import Crypto


from src.app.api.api_v1.deps import get_settings
from src.app.api.api_v1.deps import get_account_mariadb_repository
from src.app.api.api_v1.deps import get_authenticator


router = APIRouter(
    tags=["auth"]
)

@router.get("/test", response_model=Any)
async def test(settings: Settings = Depends(get_settings)):
    token = Crypto.generate_token(
                data={"sub": "nickezekias@gmail.com"},
                expires_after=timedelta(minutes=30)
            )
    return token

@router.post("/login", response_model=LoginResponse, status_code=200)
async def login(
    form_data: LoginRequest,
    settings: Settings = Depends(get_settings),
    repository: IAccountRepository = Depends(get_account_mariadb_repository),
    authenticator=Depends(get_authenticator)
) -> dict | None:
    controller = LoginController(repository, authenticator)
    return await controller.login(form_data)

@router.post("/register", response_model=RegisterResponse, status_code=201)
async def register(
    form_data: RegisterRequest,
    background_tasks: BackgroundTasks,
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository),
    authenticator=Depends(get_authenticator)
) -> RegisterResponse | None:
    notification: Notification = VerifyEmailNotification(background_tasks)
    controller = RegisterController(
        account_repository=account_repository,
        register_presenter=RegisterPresenter(),
        account_presenter=AccountPresenter(),
        authenticator=authenticator,
        notification=notification,
        crypto=Crypto
    )
    return await controller.register(form_data)


@router.get("/resend-email-verification", response_model=dict, status_code=200)
async def resend_email_verification(
    email: str,
    background_tasks: BackgroundTasks,
    repository: IAccountRepository = Depends(get_account_mariadb_repository),
) -> dict:
    presenter: IAccountPresenter = AccountPresenter()
    try:
        notification: Notification = VerifyEmailNotification(background_tasks)
    except:
        return { "success": False }
    return await SendEmailVerificationLinkUseCase(crypto=Crypto, repository=repository, presenter=presenter, notification=notification).execute(email=email)

@router.post("/verify-email", response_model=dict, status_code=200)
async def verify_email(
    payload: VerifyEmailRequest,
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository)
) -> dict | None:
    presenter: IAccountPresenter = AccountPresenter()
    return await VerifyEmailUseCase(account_repository, presenter, Crypto()).execute(payload)

@router.post("/forgot-password", response_model=dict, status_code=200)
async def forgot_password(
    background_tasks: BackgroundTasks,
    email: EmailStr = Form(),
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository),
) -> dict | None:
    notification: Notification = ForgotPasswordNotification(background_tasks)
    presenter: IAccountPresenter = AccountPresenter()
    return await ForgotPasswordUseCase(account_repository, presenter, Crypto, notification).execute(email)

@router.post("/reset-password", response_model=ResetPasswordUseCase.Response, status_code=200)
async def reset_password(
    payload: ResetPasswordUseCase.Request,
    repository: IAccountRepository = Depends(get_account_mariadb_repository),
    authenticator = Depends(get_authenticator)
) -> ResetPasswordUseCase.Response:
    presenter: IAccountPresenter = AccountPresenter()
    return await ResetPasswordUseCase(
        repository=repository,
        presenter=presenter,
        crypto=Crypto,
        authenticator=authenticator
    ).execute(payload)

# check no user with same email exists
@router.post("/check-email-unicity", response_model=dict, status_code=200)
async def check_email(
    email: str = Form(),
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository)
) -> dict | None:
    found_user: User = account_repository.get_by_email(email = email)
    if found_user:
        return { "success": False, "detail": "app.account.register.errors.emailExists" }
    else: return { "success": True, "detail": "app.account.register.success.emailIsUnique" }

# check no user with same phone exists
@router.post("/check-phone-unicity", response_model=dict, status_code=200)
async def check_phone(
    phone: str = Form(),
    account_repository: IAccountRepository = Depends(get_account_mariadb_repository)
) -> dict | None:
    found_user: User = account_repository.get_by_phone(phone = phone)
    # return { "phone": phone }
    if found_user:
        return { "success": False, "detail": "app.account.register.errors.phoneExists" }
    else: return { "success": True, "detail": "app.account.register.success.phoneIsUnique" }