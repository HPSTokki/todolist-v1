from sqlmodel import create_engine, SQLModel, Session
import pytest

from src.services.user_services import UserService        
from src.dto.todolist_dtos import InsertUser
from src.models.todolist_models import User

engine = create_engine("sqlite:///:memory:")

@pytest.fixture
def session():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
        
def test_register_user(session):
    service = UserService(session)
    
    user_data = InsertUser(
        email="test@gmail.com",
        password="password123"
    )
    
    new_user = service.register_user(user_data)
    
    assert new_user.email == "test@gmail.com"
    assert new_user.password != "password123"
    assert new_user.id is not None
    