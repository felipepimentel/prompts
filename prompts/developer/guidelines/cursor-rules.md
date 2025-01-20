---
title: "Cursor Rules Configuration Guide"
path: "developer/guidelines/cursor-rules"
tags: ["cursor", "development", "configuration", "rules", "best-practices", "guidelines", "ai-assistant"]
description: "A comprehensive guide for configuring and maintaining Cursor AI rules, focusing on project organization, code quality, and development workflows"
---

# Cursor Rules Configuration Guide

## Overview
This guide provides detailed instructions for configuring and maintaining Cursor AI rules (.cursorrules files) to ensure consistent, high-quality code generation and development workflows.

## Core Configuration

### 1. Project-Level Rules
```json
{
  "rules": {
    "naming": {
      "components": "PascalCase",
      "functions": "camelCase",
      "variables": "camelCase",
      "constants": "UPPER_SNAKE_CASE",
      "types": "PascalCase",
      "files": "kebab-case"
    },
    "structure": {
      "components": "src/components",
      "pages": "src/pages",
      "utils": "src/utils",
      "types": "src/types",
      "styles": "src/styles",
      "tests": "tests",
      "docs": "docs"
    },
    "patterns": {
      "imports": "absolute",
      "exports": "named",
      "state": "hooks",
      "styling": "module-based",
      "testing": "component-level"
    },
    "documentation": {
      "components": "jsdoc",
      "functions": "jsdoc",
      "types": "tsdoc",
      "readme": "required"
    }
  }
}
```

### 2. Language-Specific Rules

#### TypeScript/JavaScript
```json
{
  "typescript": {
    "strict": true,
    "types": {
      "props": "interface",
      "state": "type",
      "utils": "type",
      "generics": "preferred"
    },
    "patterns": {
      "async": "promise",
      "errors": "typed",
      "imports": "type-imports"
    },
    "style": {
      "functions": "arrow",
      "components": "functional",
      "declarations": "const"
    }
  }
}
```

#### Python
```json
{
  "python": {
    "style": {
      "formatting": "black",
      "imports": "isort",
      "docstrings": "google"
    },
    "typing": {
      "annotations": "required",
      "generics": "preferred",
      "protocols": "when-needed"
    },
    "patterns": {
      "classes": "dataclass",
      "exceptions": "custom",
      "async": "asyncio"
    }
  }
}
```

#### Go
```json
{
  "go": {
    "style": {
      "formatting": "gofmt",
      "imports": "goimports",
      "comments": "godoc"
    },
    "patterns": {
      "errors": "wrapped",
      "context": "required",
      "interfaces": "small"
    },
    "testing": {
      "framework": "testing",
      "coverage": "required",
      "benchmarks": "when-needed"
    }
  }
}
```

## Framework-Specific Rules

### 1. React
```json
{
  "react": {
    "components": {
      "style": "functional",
      "props": "typed",
      "state": "hooks",
      "effects": "cleanup-required",
      "memoization": "when-needed"
    },
    "patterns": {
      "context": "global-state",
      "refs": "minimal",
      "events": "typed-handlers"
    },
    "performance": {
      "splitting": "route-based",
      "loading": "suspense",
      "rendering": "selective"
    }
  }
}
```

### 2. Next.js
```json
{
  "nextjs": {
    "routing": {
      "style": "app-router",
      "dynamic": "generateStaticParams",
      "loading": "suspense"
    },
    "data": {
      "fetching": "server-components",
      "mutations": "server-actions",
      "caching": "required"
    },
    "optimization": {
      "images": "next/image",
      "fonts": "next/font",
      "scripts": "next/script"
    }
  }
}
```

### 3. FastAPI
```json
{
  "fastapi": {
    "routing": {
      "versioning": "path",
      "responses": "typed",
      "validation": "pydantic"
    },
    "security": {
      "auth": "jwt",
      "cors": "configured",
      "middleware": "required"
    },
    "documentation": {
      "openapi": "detailed",
      "examples": "required",
      "schemas": "documented"
    }
  }
}
```

## Testing Rules

### 1. Unit Testing
```json
{
  "unit-testing": {
    "coverage": {
      "minimum": 80,
      "reports": "required",
      "critical-paths": 100
    },
    "patterns": {
      "arrange-act-assert": true,
      "mocking": "minimal",
      "fixtures": "typed"
    },
    "naming": {
      "files": "*.test.ts",
      "functions": "should_*",
      "describes": "feature_based"
    }
  }
}
```

### 2. Integration Testing
```json
{
  "integration-testing": {
    "scope": {
      "api": "required",
      "database": "required",
      "external-services": "mocked"
    },
    "environment": {
      "setup": "docker",
      "cleanup": "required",
      "isolation": "per-suite"
    },
    "data": {
      "seeding": "fixtures",
      "cleanup": "automated",
      "transactions": "rollback"
    }
  }
}
```

## Code Quality Rules

### 1. Linting
```json
{
  "linting": {
    "tools": {
      "typescript": "eslint",
      "python": "ruff",
      "go": "golangci-lint"
    },
    "rules": {
      "complexity": "warn",
      "duplication": "error",
      "formatting": "error",
      "naming": "error"
    },
    "automation": {
      "pre-commit": "required",
      "ci": "blocking",
      "fixes": "automated"
    }
  }
}
```

### 2. Documentation
```json
{
  "documentation": {
    "code": {
      "functions": "required",
      "types": "required",
      "components": "required",
      "apis": "openapi"
    },
    "project": {
      "readme": "required",
      "setup": "required",
      "architecture": "required",
      "decisions": "adr"
    },
    "generation": {
      "api": "swagger",
      "typescript": "typedoc",
      "python": "sphinx"
    }
  }
}
```

## Development Workflow Rules

### 1. Version Control
```json
{
  "version-control": {
    "branching": {
      "main": "protected",
      "develop": "integration",
      "features": "short-lived"
    },
    "commits": {
      "style": "conventional",
      "scope": "required",
      "linking": "required"
    },
    "reviews": {
      "approvals": 1,
      "checks": "required",
      "templates": "enforced"
    }
  }
}
```

### 2. CI/CD
```json
{
  "ci-cd": {
    "pipelines": {
      "lint": "required",
      "test": "required",
      "build": "required",
      "deploy": "automated"
    },
    "environments": {
      "development": "auto-deploy",
      "staging": "manual-approval",
      "production": "protected"
    },
    "artifacts": {
      "images": "versioned",
      "assets": "hashed",
      "docs": "versioned"
    }
  }
}
```

## Maintenance Guidelines

### Regular Updates
- Review and update rules quarterly
- Keep documentation synchronized
- Validate rule effectiveness
- Gather team feedback
- Monitor rule impact on development velocity

### Version Control
- Track rule changes in version control
- Document significant updates
- Maintain change history
- Review impact of changes
- Automate rule validation

## Resources
- [Cursor AI Documentation](https://cursor.sh/docs)
- [TypeScript Guidelines](https://www.typescriptlang.org/docs/handbook/declaration-files/do-and-dont.html)
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)
- [React Best Practices](https://reactjs.org/docs/hooks-rules.html)
- [Next.js Documentation](https://nextjs.org/docs)
- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/) 