from src.dto.todolist_dto import InsertUser, UpdateUser, ListResponseUser
from src.models.todolist_model import User
from sqlmodel import Session, select
from datetime import date, datetime
from fastapi import HTTPException
from src.services.auth_service import hash_password, verify_password, create_access_token

class UserService():
    def __init__(self, session: Session):
        self.session = session

    def register_user(self, user_data: InsertUser) -> User:
        stmt = select(User).where(
            User.user_name == user_data.user_name
        )
        existing_user = self.session.exec(stmt).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Username already taken!")

        user = User(
            user_name=user_data.user_name,
            full_name=user_data.full_name,
            age=user_data.age,
            hashed_password=hash_password(user_data.hashed_password)
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def get_all_users(self) -> ListResponseUser:
        stmt = select(User)
        user = self.session.exec(stmt).all()
        return user

    def login(self, user_name: str, hashed_password: str) -> str:
        user = self.session.exec(
            select(User).where(User.user_name == user_name)
        ).first()

        if not user or not verify_password(hashed_password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return create_access_token(user.user_id)