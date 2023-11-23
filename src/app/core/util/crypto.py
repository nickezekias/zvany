from datetime import datetime, timedelta
from jose import jwt
from src.domain.util.i_crypto import ICrypto

from src.app.config import settings;

class Crypto(ICrypto):

    @staticmethod
    def generate_token(data: dict, expires_after: timedelta) -> str:
        to_encode = data.copy()

        #check if expires_after is defined, if not use default access_token duration in settings
        if expires_after:
            expire = datetime.utcnow() + expires_after
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, settings.APP_KEY, algorithm=settings.CRYPT_ALGORITHM,
        )
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> dict:
        try:
            decoded_token = jwt.decode(token, settings.APP_KEY, algorithms=[settings.CRYPT_ALGORITHM])
            return decoded_token
        except jwt.JWTError as e:
            from loguru import logger
            logger.error(e)
            return None
