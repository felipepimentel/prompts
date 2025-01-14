---
title: "FastAPI Development Guide"
path: "developer/frameworks/fastapi/fastapi-development-guide"
tags: ["fastapi", "python", "api", "development", "best-practices", "async", "performance"]
description: "A comprehensive guide for developing scalable APIs using FastAPI and Python, focusing on best practices, performance optimization, and modern development patterns."
---

# FastAPI Development Guide

## Overview
This guide provides comprehensive development guidelines for building scalable APIs using FastAPI and Python, focusing on best practices, performance optimization, and modern development patterns.

## Project Structure

### Directory Organization
```
src/
  ├── api/                # API routes
  │   ├── v1/           # API version 1
  │   └── v2/          # API version 2
  ├── core/            # Core application code
  │   ├── config.py   # Configuration
  │   └── deps.py    # Dependencies
  ├── models/        # Database models
  ├── schemas/      # Pydantic schemas
  ├── services/    # Business logic
  └── utils/      # Utility functions
```

## Code Style

### Function Definitions
```python
# ✅ Good: Clear type hints and async functions
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: str
    is_active: bool = True

async def create_user(
    user: UserCreate,
    db: AsyncSession
) -> User:
    """
    Create a new user in the database.
    
    Args:
        user: User creation data
        db: Database session
        
    Returns:
        Created user instance
        
    Raises:
        HTTPException: If user with email already exists
    """
    if await get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    
    return db_user

# ❌ Bad: Missing type hints and sync function for I/O
def get_user(id, db):
    return db.query(User).filter(User.id == id).first()
```

## API Routes

### Route Organization
```python
# api/v1/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_db
from schemas.user import UserCreate, UserResponse
from services.user import create_user, get_user_by_id

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user_route(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    return await create_user(user, db)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_route(
    user_id: int,
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    user = await get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user
```

## Data Validation

### Pydantic Models
```python
# schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    is_active: bool = True

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
```

## Error Handling

### Exception Handling
```python
# core/exceptions.py
from fastapi import HTTPException
from typing import Any, Dict, Optional

class APIError(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
        headers: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            status_code=status_code,
            detail=detail,
            headers=headers
        )

# Usage in routes
from core.exceptions import APIError

@router.get("/items/{item_id}")
async def get_item(item_id: int) -> Item:
    try:
        item = await get_item_by_id(item_id)
        if not item:
            raise APIError(
                status_code=404,
                detail=f"Item {item_id} not found"
            )
        return item
    except Exception as e:
        raise APIError(
            status_code=500,
            detail="Internal server error"
        )
```

## Dependency Injection

### Database Dependencies
```python
# core/deps.py
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import async_session_maker

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

# Usage in routes
@router.get("/users/", response_model=List[UserResponse])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
) -> List[UserResponse]:
    return await get_user_list(db, skip, limit)
```

## Performance Optimization

### Caching
```python
# services/cache.py
from functools import wraps
from typing import Any, Callable
from redis import asyncio as aioredis

redis = aioredis.from_url("redis://localhost")

def cache_response(
    expire: int = 3600
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Try to get from cache
            cached = await redis.get(cache_key)
            if cached:
                return cached
            
            # Get fresh data
            result = await func(*args, **kwargs)
            
            # Cache the result
            await redis.set(
                cache_key,
                result,
                ex=expire
            )
            
            return result
        return wrapper
    return decorator

# Usage in services
@cache_response(expire=3600)
async def get_popular_items(
    db: AsyncSession,
    limit: int = 10
) -> List[Item]:
    return await db.query(Item)\
        .order_by(Item.views.desc())\
        .limit(limit)\
        .all()
```

### Async Operations
```python
# services/external.py
import httpx
from typing import List, Dict, Any

async def fetch_external_data(
    urls: List[str]
) -> List[Dict[str, Any]]:
    async with httpx.AsyncClient() as client:
        tasks = [
            client.get(url)
            for url in urls
        ]
        responses = await asyncio.gather(*tasks)
        return [
            response.json()
            for response in responses
        ]
```

## Testing

### API Tests
```python
# tests/test_users.py
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/users/",
            json={
                "email": "test@example.com",
                "username": "testuser",
                "password": "password123"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "test@example.com"
        assert data["username"] == "testuser"
        assert "id" in data
```

## Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org)
- [Python Type Hints](https://docs.python.org/3/library/typing.html) 