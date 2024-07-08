import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager
from src.config.settings import settings
from typing import AsyncGenerator

DATABASE_URL = settings.database_url

# Configuration du logging
logging.basicConfig(filename='var/logs/database.log', level=logging.INFO)

# Créer un moteur de base de données asynchrone
async_engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=100,  # Nombre de connexions dans le pool
    max_overflow=800  # Connexions supplémentaires possibles au-delà du pool_size
)

# Créer une session asynchrone
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Fournit un générateur de session asynchrone."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()

Base = declarative_base()
