---
category: Developer
description: A comprehensive guide for maintaining high code quality in GitHub repositories,
  including workflows, automation, and best practices
model: GPT-4
path: developer/guidelines/github/github-code-quality-guide
prompt_type: Instruction-based prompting
tags:
- github
- code-quality
- best-practices
- ci-cd
- automation
- git
- development
- workflow
title: GitHub Code Quality Guidelines
version: '1.0'
---

# GitHub Code Quality Guidelines

## Overview
This guide provides comprehensive standards and best practices for maintaining high code quality in GitHub repositories, focusing on automation, workflows, and collaborative development.

## Repository Setup

### 1. Branch Protection Rules
```json
{
  "protection": {
    "required_status_checks": {
      "strict": true,
      "contexts": [
        "continuous-integration/ci-name",
        "code-quality/linter",
        "security/dependency-check"
      ]
    },
    "required_pull_request_reviews": {
      "required_approving_review_count": 1,
      "dismiss_stale_reviews": true,
      "require_code_owner_reviews": true
    },
    "enforce_admins": true,
    "restrictions": null
  }
}
```

### 2. CODEOWNERS Configuration
```yaml
# .github/CODEOWNERS

# Default owners for everything
* @org/core-team

# Frontend code owners
/src/frontend/ @org/frontend-team
/src/components/ @org/frontend-team

# Backend code owners
/src/backend/ @org/backend-team
/src/api/ @org/backend-team

# Documentation owners
/docs/ @org/docs-team
*.md @org/docs-team
```

## Workflow Automation

### 1. GitHub Actions CI/CD
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Type check
        run: npm run type-check
      
      - name: Test
        run: npm run test
      
      - name: Build
        run: npm run build

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Security scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

### 2. Pull Request Template
```markdown
# .github/pull_request_template.md

## Description
<!-- Describe your changes in detail -->

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
<!-- Describe the tests you ran -->

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where needed
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
```

## Code Quality Tools

### 1. ESLint Configuration
```javascript
// .eslintrc.js
module.exports = {
  root: true,
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    'prettier',
  ],
  plugins: ['@typescript-eslint', 'react', 'prettier'],
  rules: {
    'prettier/prettier': 'error',
    'no-console': 'warn',
    'no-unused-vars': 'error',
    '@typescript-eslint/explicit-function-return-type': 'error',
    'react/prop-types': 'off',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
}
```

### 2. Prettier Configuration
```json
// .prettierrc
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
```

### 3. Husky Pre-commit Hooks
```json
// .husky/pre-commit
{
  "hooks": {
    "pre-commit": "lint-staged",
    "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
  }
}

// .lintstagedrc
{
  "*.{js,jsx,ts,tsx}": [
    "eslint --fix",
    "prettier --write",
    "jest --findRelatedTests"
  ],
  "*.{json,md}": [
    "prettier --write"
  ]
}
```

## Code Review Guidelines

### 1. Pull Request Size
- Keep PRs small (< 400 lines)
- Focus on single responsibility
- Split large changes into smaller PRs
- Include relevant tests

### 2. Review Checklist
```markdown
## Code Review Checklist

### Functionality
- [ ] Code works as described in requirements
- [ ] Edge cases are handled
- [ ] Error states are managed
- [ ] Performance implications considered

### Code Quality
- [ ] Code follows project style guide
- [ ] No unnecessary complexity
- [ ] No duplicate code
- [ ] Proper error handling

### Testing
- [ ] Unit tests added/updated
- [ ] Integration tests if needed
- [ ] Edge cases covered
- [ ] Proper mocking used

### Security
- [ ] Input validation
- [ ] Authentication/Authorization
- [ ] Data sanitization
- [ ] No sensitive data exposed
```

## Automated Testing

### 1. Jest Configuration
```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
  },
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
    '!src/mocks/**',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
}
```

### 2. GitHub Actions Test Workflow
```yaml
# .github/workflows/test.yml
name: Test

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [16.x, 18.x]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm run test:ci
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
```

## Security Measures

### 1. Dependency Scanning
```yaml
# .github/workflows/security.yml
name: Security

on:
  schedule:
    - cron: '0 0 * * *'
  push:
    branches: [main]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Snyk to check for vulnerabilities
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      
      - name: Run OWASP Dependency-Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'My Project'
          path: '.'
          format: 'HTML'
```

### 2. Secret Scanning
```yaml
# .github/secret_scanning.yml
paths-ignore:
  - 'node_modules/**'
  - 'dist/**'
  - '*.test.{js,ts}'

patterns:
  - name: AWS Access Key
    pattern: 'AKIA[0-9A-Z]{16}'
  - name: Private Key
    pattern: '-----BEGIN.*PRIVATE KEY-----'
```

## Documentation Standards

### 1. README Template
```markdown
# Project Name

## Overview
Brief description of the project

## Prerequisites
- Required dependencies
- Environment setup

## Installation
```bash
npm install
```

## Development
```bash
npm run dev
```

## Testing
```bash
npm run test
```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md)

## License
This project is licensed under the MIT License
```

### 2. Contributing Guidelines
```markdown
# Contributing Guidelines

## Code Style
- Follow ESLint rules
- Use Prettier formatting
- Write meaningful commit messages

## Pull Request Process
1. Update documentation
2. Add/update tests
3. Update CHANGELOG.md
4. Get review approval

## Branch Naming
- feature/feature-name
- fix/bug-description
- docs/documentation-update
```

## Performance Monitoring

### 1. Lighthouse CI
```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI

on:
  pull_request:
    branches: [main]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Lighthouse CI
        uses: treosh/lighthouse-ci-action@v9
        with:
          urls: |
            https://staging.myapp.com/
          uploadArtifacts: true
          temporaryPublicStorage: true
```

### 2. Performance Budgets
```json
// .lighthouserc.json
{
  "ci": {
    "collect": {
      "numberOfRuns": 3
    },
    "assert": {
      "assertions": {
        "categories:performance": ["error", {"minScore": 0.9}],
        "first-contentful-paint": ["error", {"maxNumericValue": 2000}],
        "interactive": ["error", {"maxNumericValue": 3500}],
        "largest-contentful-paint": ["error", {"maxNumericValue": 2500}]
      }
    }
  }
}
```

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
- [ESLint Documentation](https://eslint.org/docs/user-guide)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)