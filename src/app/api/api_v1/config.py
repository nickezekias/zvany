import os
from pydantic_settings import BaseSettings
from src.app.config import Settings

class MariaDbSettings(BaseSettings):
    connection: str = os.getenv("DB_CONNECTION", "mariadb")
    host: str = os.getenv("DB_HOST", "0.0.0.0")
    port: str = os.getenv("DB_PORT", 3306)
    database: str = os.getenv("DB_DATABASE", "c8gd2s")
    username: str = os.getenv("DB_USERNAME", "root")
    password: str = os.getenv("DB_PASSWORD", "")

class Settings(Settings):
    db: MariaDbSettings = MariaDbSettings()
