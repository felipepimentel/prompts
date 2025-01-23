---
description: A comprehensive guide for developing and deploying applications using
  Docker, covering containerization best practices, multi-container applications,
  and production deployment strategies.
path: developer/frameworks/docker/docker-development-guide
prompt_type: Instruction-based prompting
tags:
- docker
- containerization
- devops
- deployment
- infrastructure
title: Docker Development Guide
---

# Docker Development Guide

## Core Principles
1. Isolation - Keep applications and dependencies self-contained
2. Portability - Ensure consistent behavior across environments
3. Efficiency - Optimize resource usage and build times
4. Security - Follow security best practices for containers

## Docker Setup

### 1. Development Environment
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker --version
docker-compose --version
```

### 2. Project Structure
```
project/
├── docker/              # Docker-related files
│   ├── development/    # Development configurations
│   └── production/     # Production configurations
├── src/                # Application source code
├── .dockerignore       # Files to exclude
├── docker-compose.yml  # Service definitions
└── Dockerfile          # Main Dockerfile
```

## Dockerfile Development

### 1. Base Dockerfile
```dockerfile
# Use multi-stage builds
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build application
RUN npm run build

# Production stage
FROM node:18-alpine

WORKDIR /app

# Copy built assets from builder
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./

# Install production dependencies
RUN npm ci --only=production

# Set environment variables
ENV NODE_ENV=production

# Expose port
EXPOSE 3000

# Start application
CMD ["npm", "start"]
```

### 2. Development Dockerfile
```dockerfile
# docker/development/Dockerfile
FROM node:18-alpine

WORKDIR /app

# Install development dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Enable hot reloading
ENV NODE_ENV=development
CMD ["npm", "run", "dev"]
```

## Docker Compose Configuration

### 1. Development Setup
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: docker/development/Dockerfile
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgres://user:pass@db:5432/dbname
    depends_on:
      - db
      - redis

  db:
    image: postgres:14-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### 2. Production Setup
```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgres://user:pass@db:5432/dbname
    depends_on:
      - db
      - redis
    networks:
      - app_network

  db:
    image: postgres:14-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app_network

  redis:
    image: redis:alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data
    networks:
      - app_network

  nginx:
    image: nginx:alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/nginx/certs:ro
    depends_on:
      - app
    networks:
      - app_network

networks:
  app_network:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
```

## Development Workflow

### 1. Building Images
```bash
# Build development environment
docker-compose build

# Build production image
docker-compose -f docker-compose.prod.yml build
```

### 2. Running Containers
```bash
# Start development environment
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

## Production Deployment

### 1. Container Registry
```bash
# Log in to registry
docker login registry.example.com

# Tag image
docker tag myapp:latest registry.example.com/myapp:latest

# Push image
docker push registry.example.com/myapp:latest
```

### 2. Deployment Script
```bash
#!/bin/bash
# deploy.sh

# Pull latest images
docker-compose -f docker-compose.prod.yml pull

# Deploy new containers
docker-compose -f docker-compose.prod.yml up -d

# Clean up old images
docker image prune -f
```

## Optimization Techniques

### 1. Image Optimization
```dockerfile
# Use .dockerignore
node_modules
npm-debug.log
Dockerfile
.dockerignore
.git
.gitignore
README.md

# Layer caching
COPY package*.json ./
RUN npm ci
COPY . .

# Multi-stage builds
FROM node:18-alpine AS builder
# ... build stage ...

FROM node:18-alpine
# ... production stage ...
```

### 2. Resource Management
```yaml
# docker-compose.yml with resource limits
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

## Monitoring and Logging

### 1. Container Monitoring
```yaml
# docker-compose.yml with monitoring
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    depends_on:
      - prometheus
```

### 2. Logging Configuration
```yaml
# docker-compose.yml with logging
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Security Best Practices

### 1. Container Security
- Use official base images
- Run containers as non-root
- Scan images for vulnerabilities
- Implement least privilege principle
- Keep base images updated

### 2. Network Security
- Use custom networks
- Limit exposed ports
- Implement TLS
- Use secrets management
- Monitor container communications

### 3. Access Control
- Implement RBAC
- Use secrets for sensitive data
- Rotate credentials regularly
- Audit container access
- Monitor user activities

## Best Practices

### 1. Development
- Use multi-stage builds
- Optimize layer caching
- Implement health checks
- Document configurations
- Use version control

### 2. Deployment
- Use orchestration tools
- Implement rolling updates
- Monitor resource usage
- Back up persistent data
- Plan for scalability

### 3. Maintenance
- Regular security updates
- Monitor performance
- Implement logging
- Document procedures
- Test disaster recovery

## Resources
1. [Docker Documentation](https://docs.docker.com/)
2. [Docker Compose Documentation](https://docs.docker.com/compose/)
3. [Docker Security](https://docs.docker.com/engine/security/)
4. [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
5. [Container Security Guide](https://snyk.io/learn/container-security/) 