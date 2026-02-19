from sqlmodel import SQLModel, Field
from sqlalchemy import String
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None, index=True)
    password: str = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: int = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id")
    title: str = Field(default=None, sa_type=String)
    description: str | None = Field(default=None, sa_type=String)
    is_completed: bool = Field(default=False)
    due_date: datetime | None = Field(default=None)
    create_at: datetime = Field(default_factory=datetime.utcnow)