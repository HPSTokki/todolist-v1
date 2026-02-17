from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.core.security import hash_password, verify_password
from src.models.todolist_models import User
from src.dto.todolist_dto import InsertUser
from fastapi import HTTPException, status

class UserService():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def register_user(self, user_data: InsertUser) -> User:
        
        stmt = await self.session.execute(
            select(User).where(
                User.email == user_data.email
            )
        )

        existing_user = stmt.scalar_one_or_none()

        if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email Already Exists")
        
        hashed_password = hash_password(user_data.password)

        user_dict = user_data.model_dump()

        user_dict["password"] = hashed_password

        new_user = User.model_validate(user_dict)

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user