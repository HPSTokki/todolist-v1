from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated, AsyncGenerator
from fastapi import Depends
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent.parent
LOCAL_DB_PATH = BASE_PATH / "local.db"

SQLITE_URL = f"sqlite+aiosqlite:///{LOCAL_DB_PATH}"
CONNECT_ARGS = {
    "check_same_thread": False
}

engine = create_async_engine(SQLITE_URL)

async_engine = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_engine() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]