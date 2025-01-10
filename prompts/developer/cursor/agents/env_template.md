---
title: "Environment Configuration Template"
author: "Cursor Development Team"
date: "`r format(Sys.time(), '%B %d, %Y')`"
output:
  html_document:
    theme: united
    toc: true
    toc_float: true
---

# Environment Configuration Guide

## Overview
This document outlines the standard environment configuration for Cursor projects.

## Template Structure
```ini
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=project_db
DB_USER=db_user
DB_PASSWORD=<YOUR_PASSWORD>

# Application Settings
DEBUG=False
LOG_LEVEL=INFO
SECRET_KEY=<YOUR_SECRET_KEY>

# Service Connections
REDIS_URL=redis://localhost:6379/0
RABBITMQ_URL=amqp://localhost:5672
MINIO_URL=http://localhost:9000
```

## Configuration Categories

### Database Settings
- `DB_HOST`: Database server hostname
- `DB_PORT`: Database server port
- `DB_NAME`: Database name
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password (never commit actual passwords)

### Application Settings
- `DEBUG`: Development mode flag
- `LOG_LEVEL`: Logging verbosity
- `SECRET_KEY`: Application secret key

### Service Connections
- `REDIS_URL`: Redis connection string
- `RABBITMQ_URL`: RabbitMQ connection string
- `MINIO_URL`: MinIO connection string

## Security Guidelines
1. Never commit `.env` files to version control
2. Use strong, unique passwords
3. Rotate secrets regularly
4. Use different credentials for each environment 