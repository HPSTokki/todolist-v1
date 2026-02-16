from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends
from typing import Generator, Annotated
from pathlib import Path

BASE_PATH = Path(__file__).resolve()
LOCAL_DB_PATH = BASE_PATH / "local.db"

sqlite_url = f"sqlite:///{LOCAL_DB_PATH}"

connect_args = {
    "check_same_thread": False
}

engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session() -> Generator[SQLModel, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]