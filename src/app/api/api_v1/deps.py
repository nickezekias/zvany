from functools import lru_cache
from typing import Generator
from fastapi import Depends

from src.app.api.api_v1.config import Settings
from src.app.core.authenticator import Authenticator
from src.app.core.util.crypto import Crypto
from src.app.db.session import SessionLocal

from src.app.api.api_v1.account.adapter.repository.account_mariadb_repository import AccountMariaDbRepository

@lru_cache()
def get_settings():
    return Settings()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        db.current_user_id = None
        yield db
    finally:
        db.close()

def get_account_mariadb_repository(db=Depends(get_db)):
    return AccountMariaDbRepository(db)

def get_authenticator():
    return Authenticator(Crypto)