from pydantic import BaseModel
from datetime import datetime

class InsertTask(BaseModel):
    user_id: int | None
    title: str
    description: str | None
    due_date: datetime | None
    is_completed: bool = False
