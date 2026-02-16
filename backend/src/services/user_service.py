from src.dto.todolist_dto import InsertUser, UpdateUser, ListResponseUser
from src.models.todolist_model import User
from sqlmodel import Session, select
from datetime import date, datetime

class UserService():
    def __init__(self, session: Session):
        self.session = session

    def register_user(self, user_data: InsertUser) -> User:
        user = User.model_validate(user_data)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def get_all_users(self) -> ListResponseUser:
        stmt = select(User)
        user = self.session.exec(stmt).all()
        return user