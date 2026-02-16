from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.dto.todolist_dto import InsertUser, UpdateUser, ListResponseUser, Token
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

@router.post("/login", response_model=Token)
def login(
    session: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    service = UserService(session)
    token = service.login(
        form_data.username,
        form_data.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
