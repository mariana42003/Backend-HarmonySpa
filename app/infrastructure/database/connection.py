from sqlalchemy import create_engine

from app.core.config import settings


def build_engine():
    return create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
        pool_recycle=1800,
    )


engine = build_engine()