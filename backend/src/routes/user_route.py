from fastapi import APIRouter
from src.dto.todolist_dto import InsertUser, UpdateUser, ListResponseUser
from src.models.todolist_model import User
from src.services.user_service import UserService
from src.engine import SessionDep

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("/", response_model=ListResponseUser)
def get_all_users(session: SessionDep):
    service = UserService(session)
    user = service.get_all_users()
    return {
        "users": user
    }

@router.post("/register", response_model=User)
def register_user(session: SessionDep, user_data: InsertUser):
    service = UserService(session)
    user = service.register_user(user_data)
    return user
