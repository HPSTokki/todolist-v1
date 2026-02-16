from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import select
from src.models.todolist_model import User
from src.services.auth_service import decode_token
from src.engine import SessionDep

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(session: SessionDep, token: str = Depends(oauth2_scheme)) -> User:
    payload = decode_token(token)

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid Token Payload")
    
    stmt = select(User).where(
        User.user_id == int(user_id)
    )
    user = session.exec(stmt).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user