from pydantic import BaseModel
from datetime import datetime

class InsertUser(BaseModel):
    email: str
    password: str

class UpdateUserPassword(BaseModel):
    password: str | None = None
    
class ResponseUser(BaseModel):
    id: int
    email: str
    created_at: datetime
    
class ListResponseUser(BaseModel):
    users: list[ResponseUser]