---
title: FastAPI Scalable API Guide
path: developer/frameworks/fastapi/fastapi-scalable-api-guide
tags:
  - python
  - fastapi
  - scalability
  - performance
  - architecture
description: A comprehensive guide for building highly scalable and maintainable APIs with FastAPI, focusing on architecture patterns, performance optimization, and best practices for large-scale applications
---

# FastAPI Scalable API Guide

## Core Principles
- Scalable architecture
- Performance optimization
- Resource management
- Monitoring and observability
- Maintainable codebase

## Architecture Design

### Domain-Driven Design
```python
# app/domain/models/user.py
from dataclasses import dataclass
from datetime import datetime
from typing import NewType

UserId = NewType("UserId", int)

@dataclass(frozen=True)
class User:
    """User domain model."""
    id: UserId
    email: str
    created_at: datetime
    
    @classmethod
    def create(cls, email: str) -> "User":
        """Create new user."""
        return cls(
            id=UserId(0),  # Placeholder until persisted
            email=email,
            created_at=datetime.utcnow()
        )
```

### Repository Pattern
```python
# app/infrastructure/repositories/user.py
from typing import Protocol, runtime_checkable
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.user import User, UserId

@runtime_checkable
class UserRepository(Protocol):
    """User repository interface."""
    
    async def get_by_id(self, id: UserId) -> User | None:
        """Get user by ID."""
        ...
    
    async def save(self, user: User) -> User:
        """Save user."""
        ...

class SQLAlchemyUserRepository:
    """SQLAlchemy implementation of user repository."""
    
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
    
    async def get_by_id(self, id: UserId) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.id == id)
        )
        user_model = result.scalar_one_or_none()
        return user_model.to_domain() if user_model else None
    
    async def save(self, user: User) -> User:
        user_model = UserModel.from_domain(user)
        self._session.add(user_model)
        await self._session.flush()
        await self._session.refresh(user_model)
        return user_model.to_domain()
```

## Performance Optimization

### Caching Layer
```python
# app/infrastructure/cache/redis.py
from typing import Any, TypeVar, Generic
from redis.asyncio import Redis
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class RedisCache(Generic[T]):
    """Redis cache implementation."""
    
    def __init__(
        self,
        redis: Redis,
        prefix: str,
        model: type[T],
        ttl: int = 3600
    ) -> None:
        self._redis = redis
        self._prefix = prefix
        self._model = model
        self._ttl = ttl
    
    def _key(self, id: str) -> str:
        return f"{self._prefix}:{id}"
    
    async def get(self, id: str) -> T | None:
        """Get item from cache."""
        data = await self._redis.get(self._key(id))
        if not data:
            return None
        return self._model.model_validate_json(data)
    
    async def set(self, id: str, item: T) -> None:
        """Set item in cache."""
        await self._redis.setex(
            self._key(id),
            self._ttl,
            item.model_dump_json()
        )
    
    async def delete(self, id: str) -> None:
        """Delete item from cache."""
        await self._redis.delete(self._key(id))
```

### Database Optimization
```python
# app/infrastructure/database/session.py
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)
from sqlalchemy.pool import AsyncAdaptedQueuePool

def create_engine(url: str, pool_size: int = 5):
    """Create database engine with connection pooling."""
    return create_async_engine(
        url,
        poolclass=AsyncAdaptedQueuePool,
        pool_size=pool_size,
        max_overflow=10,
        pool_timeout=30,
        pool_pre_ping=True,
        pool_recycle=1800
    )

@asynccontextmanager
async def transaction():
    """Transaction context manager."""
    async with AsyncSession() as session:
        async with session.begin():
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
```

## Load Balancing

### Rate Limiting
```python
# app/api/middleware/rate_limit.py
from fastapi import Request, HTTPException
from redis.asyncio import Redis
import time

class RateLimiter:
    """Rate limiter using sliding window."""
    
    def __init__(
        self,
        redis: Redis,
        window_seconds: int = 60,
        max_requests: int = 100
    ) -> None:
        self._redis = redis
        self._window = window_seconds
        self._max = max_requests
    
    async def check_rate_limit(
        self,
        key: str
    ) -> tuple[bool, int]:
        """Check if request is within rate limit."""
        now = int(time.time())
        window_start = now - self._window
        
        async with self._redis.pipeline() as pipe:
            # Remove old requests
            await pipe.zremrangebyscore(key, 0, window_start)
            # Add new request
            await pipe.zadd(key, {str(now): now})
            # Count requests in window
            await pipe.zcount(key, window_start, now)
            # Set key expiration
            await pipe.expire(key, self._window)
            _, _, count, _ = await pipe.execute()
        
        return count <= self._max, count

class RateLimitMiddleware:
    """Rate limit middleware."""
    
    def __init__(
        self,
        redis: Redis,
        window_seconds: int = 60,
        max_requests: int = 100
    ) -> None:
        self._limiter = RateLimiter(
            redis,
            window_seconds,
            max_requests
        )
    
    async def __call__(
        self,
        request: Request,
        call_next
    ):
        key = f"rate_limit:{request.client.host}"
        allowed, count = await self._limiter.check_rate_limit(key)
        
        if not allowed:
            raise HTTPException(
                status_code=429,
                detail="Too many requests"
            )
        
        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = str(self._limiter._max)
        response.headers["X-RateLimit-Remaining"] = str(
            self._limiter._max - count
        )
        
        return response
```

## Monitoring

### Metrics Collection
```python
# app/infrastructure/metrics/prometheus.py
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest
)
from fastapi import FastAPI, Response
from time import time

# Metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration",
    ["method", "endpoint"]
)

def setup_metrics(app: FastAPI) -> None:
    """Setup metrics collection."""
    
    @app.middleware("http")
    async def metrics_middleware(request, call_next):
        start_time = time()
        
        response = await call_next(request)
        
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code
        ).inc()
        
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(time() - start_time)
        
        return response
    
    @app.get("/metrics")
    def metrics():
        return Response(
            generate_latest(),
            media_type="text/plain"
        )
```

### Logging
```python
# app/infrastructure/logging/config.py
import logging
import json
from datetime import datetime
from typing import Any

class JSONFormatter(logging.Formatter):
    """JSON log formatter."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON."""
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
        
        if record.exc_info:
            log_data["exception"] = self.formatException(
                record.exc_info
            )
        
        return json.dumps(log_data)

def setup_logging() -> None:
    """Setup logging configuration."""
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
```

## Error Handling

### Exception Handling
```python
# app/api/errors/handlers.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Any

class AppError(Exception):
    """Base application error."""
    
    def __init__(
        self,
        message: str,
        code: str,
        status_code: int = 400,
        details: dict[str, Any] | None = None
    ) -> None:
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details or {}

def setup_error_handlers(app: FastAPI) -> None:
    """Setup error handlers."""
    
    @app.exception_handler(AppError)
    async def app_error_handler(
        request: Request,
        error: AppError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=error.status_code,
            content={
                "error": {
                    "code": error.code,
                    "message": error.message,
                    "details": error.details
                }
            }
        )
```

## Best Practices

### Architecture
1. Use domain-driven design
2. Implement clean architecture
3. Follow SOLID principles
4. Use dependency injection
5. Maintain separation of concerns

### Performance
- Implement caching
- Use connection pooling
- Optimize database queries
- Configure rate limiting
- Monitor resource usage

### Scalability
1. Horizontal scaling
2. Load balancing
3. Database sharding
4. Caching strategies
5. Message queues

### Monitoring
- Collect metrics
- Implement logging
- Set up alerts
- Monitor performance
- Track errors

## Resources
- FastAPI documentation
- Database optimization guides
- Caching strategies
- Monitoring solutions
- Architecture patterns 