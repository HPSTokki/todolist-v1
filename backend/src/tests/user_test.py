from sqlmodel import create_engine, SQLModel, Session, select
import pytest

from src.services.user_services import UserService        
from src.dto.todolist_dtos import InsertUser
from src.models.todolist_models import User
from src.error import UserExistsError, UserDoesNotExistsError

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
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

def test_register_user_dupe_error(session):
    service = UserService(session)
    
    user_data = InsertUser(
        email="test@gmail.com",
        password="password123"
    )
    
    service.register_user(user_data)
    
    duplicate_user = InsertUser(
        email="test@gmail.com",
        password="password123"
    )
    
    with pytest.raises(UserExistsError) as exc_info:
        service.register_user(duplicate_user)
        
    assert str(exc_info.value) == "User Exists" 
    
def test_get_all_user(session):
    service = UserService(session)
    
    user_data = InsertUser(
        email="test@gmail.com",
        password="password123"
    )
    
    user_data2 = InsertUser(
        email="test2@gmail.com",
        password="password123"
    )
    
    service.register_user(user_data)
    service.register_user(user_data2)
    
    stmt = select(User)
    result = session.exec(stmt).all()
    
    assert len(result) == 2
    assert result[0].email == "test@gmail.com"
    assert result[0].id is not None
    assert result[1].email == "test2@gmail.com"
    assert result[1].email is not None
    
def test_get_one_user(session):
    service = UserService(session)
    
    user_data = InsertUser(
        email="test@gmail.com",
        password="password123"
    )
    
    user_data2 = InsertUser(
        email="test2@gmail.com",
        password="password123"
    )
    
    service.register_user(user_data)
    service.register_user(user_data2)
    
    result = service.get_one_user_by_id(1)
    
    assert result.id == 1
    assert result.email == "test@gmail.com"
    
def test_get_one_user_error(session):
    service = UserService(session)
    
    user_data = InsertUser(
        email="test@gmail.com",
        password="password123"
    )
    
    user_data2 = InsertUser(
        email="test2@gmail.com",
        password="password123"
    )
    
    service.register_user(user_data)
    service.register_user(user_data2)
    
    with pytest.raises(UserDoesNotExistsError) as exc_info:
        result = service.get_one_user_by_id(3)
        
    assert str(exc_info.value) == "User doesn't exists"    
    