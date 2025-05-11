from sqlmodel import SQLModel
from api.core.settings import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

async_engine = create_async_engine(url=settings.DATABASE_URL, echo=True)


# Initialize database
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# Session creation
async def get_session():
    """Returns an AsyncSession instance"""
    Session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with Session() as session:
        yield session
