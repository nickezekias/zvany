from functools import lru_cache
from typing import Generator
from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from pydantic import ValidationError

from src.app.api.api_v1.config import Settings
from src.app.config import settings as app_settings
from src.app.core.authenticator import Authenticator
from src.app.core.util.crypto import Crypto
from src.app.db.session import SessionLocal

from src.domain.account.user import User;
from src.domain.account.i_account_presenter import IAccountPresenter;
from src.domain.profile.i_profile_presenter import IProfilePresenter;

from src.app.api.api_v1.account.adapter.repository.account_mariadb_repository import AccountMariaDbRepository
from src.app.api.api_v1.account.adapter.presenter.account_presenter import AccountPresenter
from src.app.api.api_v1.profile.adapter.presenter.profile_presenter import ProfilePresenter

@lru_cache()
def get_settings():
    return Settings()

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{app_settings.API_V1_STR}/login/access-token"
)
account_presenter: IAccountPresenter = AccountPresenter()
profile_presenter: IProfilePresenter = ProfilePresenter()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        db.current_user_id = None
        yield db
    finally:
        db.close()

def get_account_mariadb_repository(db=Depends(get_db)):
    return AccountMariaDbRepository(db)

def get_current_user(
    repository: AccountMariaDbRepository=Depends(get_account_mariadb_repository),
    token=Depends(reusable_oauth2)
) -> User | None:
    try:
        payload = Crypto.verify_token(token=token)
    except (jwt.JWTError, ValidationError):
        return account_presenter.output_error_invalid_auth_token()

    if payload and payload["sub"]:
        user: User = repository.get(id=payload["sub"])

        if not user or not user.token == token:
            return account_presenter.output_error_user_with_credentials_not_found()
        return user
    else:
        return account_presenter.output_error_invalid_auth_token()

def get_current_active_user(current_user: User=Depends(get_current_user)) -> User:
    if not current_user.active():
        return account_presenter.output_error_inactive_account()
    return profile_presenter.output_view_current_user(current_user)

def get_authenticator():
    return Authenticator(Crypto)