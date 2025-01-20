---
title: Python Containerization Guide
path: developer/frameworks/python/python-containerization-guide
tags:
  - python
  - docker
  - containerization
  - devops
  - deployment
description: Comprehensive guide for containerizing Python applications using Docker and modern best practices for deployment and orchestration
---

# Python Containerization Guide

## Core Principles
- Efficient container builds
- Security best practices
- Multi-stage builds
- Resource optimization
- Development workflow

## Docker Configuration

### Base Image Selection
```dockerfile
# Development stage
FROM python:3.12-slim as development

WORKDIR /app

# Install development dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && if [ -f requirements-dev.txt ]; then \
       pip install --no-cache-dir -r requirements-dev.txt; \
    fi

# Production stage
FROM python:3.12-slim as production

WORKDIR /app

# Create non-root user
RUN useradd -m -u 1000 appuser

# Install production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Switch to non-root user
USER appuser

CMD ["python", "main.py"]
```

### Development Setup
```dockerfile
# docker-compose.dev.yml
version: '3.8'

services:
  app:
    build:
      context: .
      target: development
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - PYTHONPATH=/app
      - PYTHONDONTWRITEBYTECODE=1
      - PYTHONUNBUFFERED=1
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Project Structure

### Application Organization
```
project/
├── Dockerfile
├── docker-compose.yml
├── docker-compose.dev.yml
├── requirements.txt
├── requirements-dev.txt
├── scripts/
│   ├── entrypoint.sh
│   └── healthcheck.sh
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── config.py
└── tests/
    └── __init__.py
```

### Configuration Management
```python
# app/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Python Application"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str = "redis://redis:6379/0"
    
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

## Build Optimization

### Multi-stage Builds
```dockerfile
# Production optimized build
FROM python:3.12-slim as builder

WORKDIR /build

# Install build dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy and compile Python code
COPY . .
RUN python -m compileall .

# Final stage
FROM python:3.12-slim

WORKDIR /app

# Copy only necessary files
COPY --from=builder /build/__pycache__ ./__pycache__
COPY --from=builder /build/app ./app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# Create non-root user
RUN useradd -m -u 1000 appuser
USER appuser

CMD ["python", "-m", "app.main"]
```

### Layer Caching
```dockerfile
# Optimize layer caching
FROM python:3.12-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Build-time arguments
ARG BUILD_VERSION
ENV APP_VERSION=$BUILD_VERSION
```

## Resource Management

### Container Resources
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 128M
    healthcheck:
      test: ["CMD", "python", "-c", "import http.client; conn = http.client.HTTPConnection('localhost:8000'); conn.request('GET', '/health'); response = conn.getresponse(); exit(0 if response.status == 200 else 1)"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### Environment Variables
```bash
# .env.example
APP_NAME=Python Application
DEBUG=false
DATABASE_URL=postgresql://user:pass@db:5432/dbname
REDIS_URL=redis://redis:6379/0
```

## Security Practices

### Security Scanning
```yaml
# .github/workflows/security.yml
name: Security Scan

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'your-image:latest'
          format: 'table'
          exit-code: '1'
          ignore-unfixed: true
          severity: 'CRITICAL,HIGH'
```

### Base Image Security
```dockerfile
# Use specific version tags
FROM python:3.12.0-slim@sha256:...

# Update system packages
RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# Remove unnecessary tools
RUN apt-get remove -y curl wget
```

## Development Workflow

### Local Development
```bash
# Start development environment
docker-compose -f docker-compose.dev.yml up -d

# Run tests
docker-compose -f docker-compose.dev.yml run --rm app pytest

# Check code style
docker-compose -f docker-compose.dev.yml run --rm app black .
```

### CI/CD Pipeline
```yaml
# .github/workflows/ci.yml
name: CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build and test
        run: |
          docker-compose build
          docker-compose run --rm app pytest
      
      - name: Push to registry
        if: github.ref == 'refs/heads/main'
        run: |
          docker tag app:latest registry.example.com/app:latest
          docker push registry.example.com/app:latest
```

## Monitoring and Logging

### Logging Configuration
```python
# app/logging.py
import logging
import sys
from pythonjsonlogger import jsonlogger

def setup_logging():
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    
    formatter = jsonlogger.JsonFormatter(
        fmt='%(asctime)s %(levelname)s %(name)s %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
```

### Health Checks
```python
# app/health.py
from fastapi import FastAPI, Response, status
from typing import Dict

app = FastAPI()

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {
        "status": "healthy",
        "version": "1.0.0"
    }
```

## Best Practices

### Development
1. Use multi-stage builds
2. Implement proper logging
3. Handle secrets securely
4. Optimize layer caching
5. Implement health checks

### Security
- Use non-root users
- Scan dependencies
- Update base images
- Remove unnecessary tools
- Implement HTTPS

### Performance
1. Optimize image size
2. Cache dependencies
3. Use appropriate base images
4. Configure resource limits
5. Monitor container health

### Deployment
- Use orchestration tools
- Implement rolling updates
- Configure auto-scaling
- Monitor resources
- Backup strategies

## Resources
- Docker documentation
- Python packaging guides
- Container security best practices
- CI/CD implementation guides
- Monitoring solutions 