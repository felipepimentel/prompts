---
description: Comprehensive guide for implementing FastAPI best practices with Python
  3.12, focusing on modern patterns, performance, and maintainability
path: developer/frameworks/fastapi/fastapi-best-practices-guide
prompt_type: Instruction-based prompting
tags:
- python
- fastapi
- best-practices
- api
- web-development
title: FastAPI Best Practices Guide with Python 3.12
---

# FastAPI Best Practices Guide

## Core Principles
- Type safety and validation
- Performance optimization
- Clean architecture
- Security best practices
- Modern Python features

## Project Organization

### Directory Structure
```
project/
├── app/
│   ├── api/
│   │   ├── deps.py
│   │   ├── errors.py
│   │   └── routes/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── events.py
│   │   └── session.py
│   ├── models/
│   │   └── domain/
│   └── services/
│       └── domain/
├── tests/
│   ├── conftest.py
│   └── api/
└── main.py
```

## Type Safety

### Pydantic Models
```python
# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Annotated

class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    email: Annotated[
        EmailStr,
        Field(description="User's email address")
    ]
    full_name: Annotated[
        str,
        Field(min_length=1, max_length=100)
    ]
    is_active: Annotated[
        bool,
        Field(default=True)
    ]

class UserCreate(UserBase):
    password: Annotated[
        str,
        Field(min_length=8, pattern=r"^(?=.*[A-Za-z])(?=.*\d)")
    ]

class UserResponse(UserBase):
    id: int
```

### Type Hints
```python
# app/services/user.py
from collections.abc import Sequence
from typing import Annotated, TypeVar, Generic

T = TypeVar("T")

class Repository(Generic[T]):
    async def get_by_id(
        self,
        id: Annotated[int, Field(gt=0)]
    ) -> T | None:
        ...
    
    async def get_all(
        self,
        skip: Annotated[int, Field(ge=0)] = 0,
        limit: Annotated[int, Field(gt=0)] = 100
    ) -> Sequence[T]:
        ...
```

## Dependency Injection

### Dependencies
```python
# app/api/deps.py
from typing import Annotated
from fastapi import Depends, Security
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import oauth2_scheme
from app.db.session import async_session
from app.services.user import UserService

async def get_db() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def get_current_user(
    token: Annotated[str, Security(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(get_db)]
) -> User:
    return await UserService(db).get_current_user(token)

DBDep = Annotated[AsyncSession, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]
```

## Error Handling

### Exception Classes
```python
# app/api/errors.py
from fastapi import HTTPException, status
from typing import Any

class APIError(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
        headers: dict[str, Any] | None = None
    ) -> None:
        super().__init__(status_code, detail, headers)

class NotFoundError(APIError):
    def __init__(self, resource: str, id: int) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} with id {id} not found"
        )

class ValidationError(APIError):
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail
        )
```

### Error Handlers
```python
# app/api/errors/handlers.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

def add_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(APIError)
    async def api_error_handler(
        request: Request,
        exc: APIError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
            headers=exc.headers
        )
    
    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(
        request: Request,
        exc: IntegrityError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": "Database integrity error"}
        )
```

## Performance Optimization

### Async Database Operations
```python
# app/db/session.py
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)

from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_pre_ping=True
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)
```

### Caching
```python
# app/core/cache.py
from functools import wraps
from typing import Any, Callable
import redis.asyncio as redis
from pydantic import BaseModel

from app.core.config import settings

redis_client = redis.from_url(
    settings.REDIS_URL,
    encoding="utf-8",
    decode_responses=True
)

class CacheConfig(BaseModel):
    prefix: str
    ttl: int = 3600
    
    def get_key(self, *args, **kwargs) -> str:
        return f"{self.prefix}:{str(args)}:{str(kwargs)}"

def cached(config: CacheConfig):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = config.get_key(*args, **kwargs)
            
            # Try cache
            if cached_data := await redis_client.get(key):
                return cached_data
            
            # Get fresh data
            result = await func(*args, **kwargs)
            
            # Cache result
            await redis_client.setex(
                key,
                config.ttl,
                result
            )
            
            return result
        return wrapper
    return decorator
```

## Security

### Authentication
```python
# app/core/security.py
from datetime import datetime, timedelta
from typing import Any
from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def create_access_token(
    subject: str | Any,
    expires_delta: timedelta | None = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode = {
        "exp": expire,
        "sub": str(subject),
        "type": "access"
    }
    
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
```

## Testing

### Fixtures
```python
# tests/conftest.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

from app.main import app
from app.db.session import async_session

@pytest.fixture
async def db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        app=app,
        base_url="http://test"
    ) as client:
        yield client

@pytest.fixture
def auth_headers(user: User) -> dict[str, str]:
    token = create_access_token(user.id)
    return {"Authorization": f"Bearer {token}"}
```

### API Tests
```python
# tests/api/test_users.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

pytestmark = pytest.mark.asyncio

async def test_create_user(
    client: AsyncClient,
    db: AsyncSession
):
    response = await client.post(
        "/api/v1/users",
        json={
            "email": "test@example.com",
            "password": "password123",
            "full_name": "Test User"
        }
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
```

## Middleware

### Request ID
```python
# app/middleware/request_id.py
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next
    ):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        
        return response
```

## Logging

### Logger Setup
```python
# app/core/logging.py
import logging
import sys
from typing import Any

from app.core.config import settings

def setup_logging() -> None:
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format=(
            "%(asctime)s - %(name)s - %(levelname)s - "
            "%(message)s [%(request_id)s]"
        ),
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

class RequestIDFilter(logging.Filter):
    def filter(self, record: Any) -> bool:
        record.request_id = getattr(
            record,
            "request_id",
            "no_request_id"
        )
        return True

logger = logging.getLogger("app")
logger.addFilter(RequestIDFilter())
```

## Best Practices

### Code Organization
1. Clear module boundaries
2. Dependency injection
3. Service layer pattern
4. Repository pattern
5. Unit of work pattern

### Performance
- Async operations
- Connection pooling
- Proper indexing
- Query optimization
- Caching strategy

### Security
1. Input validation
2. Authentication
3. Authorization
4. Rate limiting
5. CORS configuration

### Development
- Type hints
- Documentation
- Testing
- Error handling
- Logging

## Resources
- FastAPI documentation
- Python 3.12 features
- SQLAlchemy guides
- Testing strategies
- Security best practices 