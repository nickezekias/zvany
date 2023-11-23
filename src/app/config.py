import os
import sys
import json
import logging
from typing import Any
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

from loguru import logger


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO  # logging levels are ints

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "zvany-backend"),
    API_V1_STR: str = "/api/v1"
    APP_DEBUG: bool = os.getenv("APP_DEBUG", False)

    APP_KEY: str = os.getenv("APP_KEY", "randf877568978yugfdi8398238xkl48x8")
    CRYPT_ALGORITHM: str = "HS256"

    # 60 minutes * 24 hours = 1 day
    #[]FIXME:set it for one hour
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    #email
    EMAIL_TEMPLATES_DIR: str="src/app/email/templates"
    MAIL_VERIFY_TOKEN_EXPIRE_MINUTES: int = os.getenv("MAIL_VERIFY_TOKEN_EXPIRE_MINUTES", "1440")
    MAIL_PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = os.getenv("MAIL_PASSWORD_RESET_TOKEN_EXPIRE_MINUTES", "60")
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD", "")
    MAIL_FROM_NAME: str = os.getenv("APP_NAME")
    MAIL_FROM_ADDRESS: str = os.getenv("MAIL_FROM_ADDRESS", "admin@noenv.com")
    MAIL_PORT: str = os.getenv("MAIL_PORT", "")
    MAIL_HOST: str = os.getenv("MAIL_HOST", "")

    # logging
    logging: LoggingSettings = LoggingSettings()

    DOMAIN: str = f"{os.getenv('APP_HOST', '0.0.0.0')}:{os.getenv('APP_PORT', '8000')}"
    # logger.debug(os.getenv("APP_URL", "http://localhost:8000"))
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"  # type: ignore

    # BACKEND_CORS_ORIGINS is a comma-separated list of origins
    # e.g: http://localhost,http://localhost:4200,http://localhost:3000
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost:8000",
        "https://localhost:8000",
        "http://localhost:8080",  # type: ignore
        "http://localhost:5173",  # type: ignore
        "https://localhost:8080",  # type: ignore
        "https://localhost:5173",  # type: ignore
    ]

    class Config:
        case_sensitive = True

settings = Settings()