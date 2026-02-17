from fastapi import APIRouter
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.deps.session import SessionDep
from src.models.todolist_models import User
from src.dto.todolist_dto import InsertUser
from src.services.user_services import UserService

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(session: SessionDep, user_data: InsertUser):
    service = UserService(session)
    user = await service.register_user(user_data)
    return user