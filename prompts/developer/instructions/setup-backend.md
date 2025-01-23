---
description: A comprehensive guide for setting up and configuring a modern backend
  development environment
path: developer/instructions/setup-backend.md
prompt_type: Instruction-based prompting
tags:
- backend
- development
- setup
- infrastructure
- best-practices
title: Backend Development Environment Setup Guide
---

# Backend Development Environment Setup

## 1. Development Environment
### 1.1 Core Tools
- Version control (Git)
- Code editor/IDE
- Terminal emulator
- Package managers
- Docker Desktop
- Database tools

### 1.2 System Requirements
```bash
# Check system resources
CPU: 4+ cores recommended
RAM: 16GB+ recommended
Storage: 256GB+ SSD
OS: Linux/macOS/Windows WSL2
```

## 2. Version Control Setup
### 2.1 Git Configuration
```bash
# Global Git configuration
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main

# SSH key setup
ssh-keygen -t ed25519 -C "your.email@example.com"
```

### 2.2 Repository Structure
```
backend/
├── src/
├── tests/
├── docs/
├── scripts/
├── .gitignore
├── .env.example
├── docker-compose.yml
└── README.md
```

## 3. Development Tools
### 3.1 IDE Configuration
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true
  },
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true
}
```

### 3.2 Extensions
- Language support
- Linting tools
- Debugging tools
- Git integration
- Docker integration
- Database tools

## 4. Docker Environment
### 4.1 Docker Compose
```yaml
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - NODE_ENV=development
    volumes:
      - .:/app
    depends_on:
      - db
      - redis

  db:
    image: postgres:14-alpine
    environment:
      - POSTGRES_USER=dev
      - POSTGRES_PASSWORD=dev
      - POSTGRES_DB=app
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### 4.2 Dockerfile
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 8000

CMD ["npm", "run", "dev"]
```

## 5. Database Setup
### 5.1 Local Development
```bash
# PostgreSQL setup
createdb app_development
createuser -P app_user

# Migration setup
npm install --save-dev sequelize-cli
npx sequelize-cli init
```

### 5.2 Connection Configuration
```javascript
// config/database.js
module.exports = {
  development: {
    username: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    host: process.env.DB_HOST,
    dialect: 'postgres'
  }
};
```

## 6. Environment Configuration
### 6.1 Environment Variables
```bash
# .env.example
NODE_ENV=development
PORT=8000

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=app_development
DB_USER=app_user
DB_PASSWORD=secret

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# JWT
JWT_SECRET=your-secret-key
JWT_EXPIRES_IN=24h

# API Keys
API_KEY=your-api-key
```

### 6.2 Configuration Management
```javascript
// config/index.js
require('dotenv').config();

module.exports = {
  env: process.env.NODE_ENV,
  port: process.env.PORT,
  db: {
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    name: process.env.DB_NAME,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD
  },
  redis: {
    host: process.env.REDIS_HOST,
    port: process.env.REDIS_PORT
  }
};
```

## 7. Testing Environment
### 7.1 Test Configuration
```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'node',
  coverageDirectory: 'coverage',
  collectCoverageFrom: ['src/**/*.js'],
  setupFiles: ['<rootDir>/tests/setup.js']
};
```

### 7.2 Test Database
```bash
# Create test database
createdb app_test

# Run migrations
NODE_ENV=test npm run migrate
```

## 8. Continuous Integration
### 8.1 GitHub Actions
```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: app_test
        ports:
          - 5432:5432

    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm test
```

## Best Practices
1. Use version control from start
2. Document setup procedures
3. Containerize development environment
4. Implement automated testing
5. Configure linting and formatting
6. Secure sensitive information
7. Maintain consistency across environments

Remember: A well-configured development environment is crucial for productive backend development. Keep documentation updated and automate setup processes where possible. 