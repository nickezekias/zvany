from datetime import datetime, timedelta
from typing import Any

from jose import jwt
from passlib.context import CryptContext

from src.app.config import settings
from src.domain.account.user import User
from src.domain.account.i_authenticator import IAuthenticator
from src.domain.util.i_crypto import ICrypto


class Authenticator(IAuthenticator):
    pwd_context: CryptContext
    crypto: ICrypto

    def __init__(self, crypto: ICrypto) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.crypto = crypto

    def create_access_token(self, data: dict) -> str:
        expires_after = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        encoded_jwt = self.crypto.generate_token(data=data, expires_after=expires_after)
        return encoded_jwt

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def user() -> User:
        pass

