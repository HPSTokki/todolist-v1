from pydantic import BaseModel

class InsertUser(BaseModel):
    email: str
    password: str