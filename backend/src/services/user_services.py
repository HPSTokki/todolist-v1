from sqlmodel import Session, select
from fastapi import HTTPException, status

from src.dto.todolist_dtos import InsertUser, ResponseUser, ListResponseUser
from src.models.todolist_models import User
from src.core.security import hash_password, verify_password
from src.error import UserExistsError, UserDoesNotExistsError

class UserService():
    def __init__(self, session: Session):
        self.session = session
        
    def register_user(self, user_data: InsertUser) -> User:
        stmt = select(User).where(
            User.email == user_data.email
        )
        
        result = self.session.exec(stmt).first()
                
        if result:
            raise UserExistsError("User Exists")
        
        hashed_password = hash_password(user_data.password)        
        
        new_user = User.model_validate(user_data)
        new_user.password = hashed_password
        
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user
    
    def get_all_user(self) -> ListResponseUser:
        stmt = select(User)
        return self.session.exec(stmt).all()
    
    def get_one_user_by_id(self, user_id: int) -> User:
        stmt = select(User).where(
            User.id == user_id
        )
        
        result = self.session.exec(stmt).first()
        
        if not result:
            raise UserDoesNotExistsError("User doesn't exists")
        
        return result