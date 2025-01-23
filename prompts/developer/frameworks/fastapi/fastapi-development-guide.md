---
description: A comprehensive guide for developing modern web APIs with FastAPI, covering
  best practices, patterns, and advanced features
path: developer/frameworks/fastapi/fastapi-development-guide
prompt_type: Instruction-based prompting
tags:
- python
- fastapi
- api
- web-development
- backend
title: FastAPI Development Guide
---

# FastAPI Development Guide

## Core Principles
- Modern Python features
- Type safety
- Performance optimization
- API documentation
- Security best practices

## Project Setup

### Basic Structure
```
fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   └── dependencies.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── domain/
│   └── services/
│       ├── __init__.py
│       └── business/
├── tests/
│   ├── __init__.py
│   └── api/
├── alembic/
│   └── versions/
├── pyproject.toml
└── README.md
```

### Dependencies Setup
```toml
# pyproject.toml
[project]
name = "fastapi-project"
version = "0.1.0"
description = "FastAPI project"
requires-python = ">=3.12"

dependencies = [
    "fastapi>=0.104.0",
    "uvicorn>=0.24.0",
    "pydantic>=2.5.0",
    "sqlalchemy>=2.0.23",
    "alembic>=1.12.1",
    "python-jose>=3.3.0",
    "passlib>=1.7.4",
    "python-multipart>=0.0.6",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "httpx>=0.25.0",
    "pytest-asyncio>=0.21.1",
]
```

## Application Configuration

### Settings Management
```python
# app/core/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Annotated

class Settings(BaseSettings):
    """Application settings."""
    
    APP_NAME: str = "FastAPI Application"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str
    
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
```

### Database Setup
```python
# app/core/database.py
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)
from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
```

## API Implementation

### Router Organization
```python
# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    db: Annotated[AsyncSession, Depends(get_db)]
) -> User:
    """Create new user."""
    db_user = await get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return await create_user_in_db(db, user)
```

### Dependency Injection
```python
# app/api/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.core.config import settings
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)]
) -> User:
    """Get current authenticated user."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise credentials_exception
    return user
```

## Data Models

### SQLAlchemy Models
```python
# app/models/base.py
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from typing import Any

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    id: Any
    created_at: datetime
    updated_at: datetime

# app/models/user.py
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.models.base import Base

class User(Base):
    """User model."""
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
```

### Pydantic Schemas
```python
# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr

class UserCreate(UserBase):
    """User creation schema."""
    password: str

class UserResponse(UserBase):
    """User response schema."""
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
```

## Security

### Authentication
```python
# app/core/security.py
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Get password hash."""
    return pwd_context.hash(password)

def create_access_token(
    subject: int | str,
    expires_delta: timedelta | None = None
) -> str:
    """Create access token."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode = {"exp": expire, "sub": str(subject)}
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
```

## Testing

### Test Configuration
```python
# tests/conftest.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app
from app.core.database import get_db

@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Test client fixture."""
    async with AsyncClient(
        app=app,
        base_url="http://test"
    ) as client:
        yield client

@pytest.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Database session fixture."""
    async with AsyncSessionLocal() as session:
        yield session
        await session.rollback()
```

### API Tests
```python
# tests/api/test_users.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

async def test_create_user(
    client: AsyncClient,
    db_session: AsyncSession
) -> None:
    """Test user creation."""
    response = await client.post(
        "/api/v1/users/",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
```

## Best Practices

### Development
1. Use type hints
2. Implement validation
3. Handle errors properly
4. Document APIs
5. Write tests

### Performance
- Use async operations
- Implement caching
- Optimize queries
- Profile endpoints
- Monitor performance

### Security
1. Validate input
2. Use authentication
3. Implement CORS
4. Rate limiting
5. Error handling

### Documentation
- Use OpenAPI
- Add descriptions
- Include examples
- Document errors
- Keep updated

## Resources
- FastAPI documentation
- SQLAlchemy guides
- Pydantic documentation
- Testing guides
- Security best practices 