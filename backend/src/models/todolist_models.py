from sqlmodel import SQLModel, Field
from sqlalchemy import String
from datetime import datetime, timezone

class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None,sa_type=String, index=True)
    password: str = Field(default=None, sa_type=String)
    created_at: datetime = Field(default_factory=datetime.utcnow)