from pydantic import BaseModel
from datetime import datetime

class InsertTask(BaseModel):
    user_id: int | None
    title: str
    description: str | None
    due_date: datetime | None
    is_completed: bool = False

class ResponseTask(BaseModel):
    task_id: int | None
    title: str
    description: str | None
    due_date: datetime | None
    is_completed: bool

    user_id: int | None
    user_name: str | None
    full_name: str | None


class UpdateTask(BaseModel):
    title: str | None
    description: str | None
    due_date: datetime | None
    is_completed: bool | None = False

class ListResponseTask(BaseModel):
    tasks: list[ResponseTask]

class InsertUser(BaseModel):
    user_name: str
    full_name: str | None
    hashed_password: str
    age: int

class ResponseUser(BaseModel):
    user_id: int
    user_name: str
    full_name: str | None
    age: int

class UpdateUser(BaseModel):
    user_name: str | None
    full_name: str | None
    hashed_password: str | None
    age: int | None

class ListResponseUser(BaseModel):
    users: list[ResponseUser]

