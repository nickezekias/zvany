from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app.api.api_v1.config import Settings

settings = Settings()

DATABASE_URL = f"{settings.db.connection}+pymysql://{settings.db.username}:{settings.db.password}@{settings.db.host}:{settings.db.port}/{settings.db.database}?charset=utf8mb4"

engine = create_engine(
    DATABASE_URL,
    echo=settings.APP_DEBUG,
    future=True # full support for v2
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
