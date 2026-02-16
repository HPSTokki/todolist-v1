from sqlmodel import SQLModel, Field
from sqlalchemy import String
from datetime import datetime

class User(SQLModel, table=True):

    __tablename__ = "users"

    user_id: int = Field(default=None, primary_key=True)
    user_name: str = Field(sa_type=String)
    full_name: str | None = Field(default=None, sa_type=String)
    hashed_password: str = Field(default=None, sa_type=String)
    age: int

class Task(SQLModel, table=True):

    __tablename__ = "tasks"

    task_id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="users.user_id")
    title: str = Field(sa_type=String)
    description: str | None = Field(default=None, sa_type=String)
    due_date: datetime | None
    isCompleted: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)