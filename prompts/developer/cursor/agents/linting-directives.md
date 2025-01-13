# Code Quality and Architecture Directives
> Version: 1.0.1
> Last Updated: 2024-01-10

## Purpose
This document defines comprehensive linting and code quality directives for maintaining consistent, high-quality code across projects. These directives are designed to be actionable, measurable, and automatically enforceable.

## Core Principles
1. **Consistency**: Uniform patterns across codebase
2. **Maintainability**: Easy to understand and modify
3. **Performance**: Optimized for runtime efficiency
4. **Security**: Built-in security practices
5. **Scalability**: Prepared for growth

## Directive Schema
```yaml
DIRECTIVE:
  context: string     # Where this directive applies
  priority: number    # 1 (highest) to 5 (lowest)
  action: string     # enforce | check | optimize
  rules: RuleSet     # Specific rules to apply
  exceptions: Array  # Valid exceptions to rules
```

## Web Development Directives

### Frontend React/TypeScript

#### Component Architecture
```typescript
ENFORCE: {
  style: "airbnb",
  jsx: "strict",
  rules: {
    "component-structure": {
      pattern: "functional",
      hooks: "top-level",
      props: "typed-interface",
      state: "immutable-first"
    },
    "naming-convention": {
      components: "PascalCase",
      hooks: "usePrefix",
      handlers: "handlePrefix",
      props: "camelCase"
    },
    "performance": {
      memoization: "heavy-compute",
      lazyLoading: "routes-components",
      bundleSplitting: "route-based"
    }
  }
}
```

#### State Management
```typescript
CHECK: {
  context: "state",
  rules: {
    "state-updates": {
      pattern: "immutable",
      batching: "required",
      selectors: "memoized"
    },
    "side-effects": {
      cleanup: "required",
      dependencies: "explicit",
      async: "cancelable"
    }
  }
}
```

#### Styling
```typescript
OPTIMIZE: {
  context: "styles",
  rules: {
    "css-in-js": {
      pattern: "atomic",
      bundling: "critical-path",
      specificity: "low"
    },
    "theme": {
      tokens: "design-system",
      variables: "css-custom-props",
      responsive: "mobile-first"
    }
  }
}
```

### Backend Node.js/Express

#### API Architecture
```typescript
ENFORCE: {
  context: "api",
  rules: {
    "rest-patterns": {
      methods: "standard-http",
      responses: "json-api-spec",
      versioning: "url-path"
    },
    "security": {
      auth: "jwt-required",
      validation: "schema-strict",
      sanitization: "auto-escape"
    },
    "performance": {
      caching: "response-headers",
      compression: "dynamic",
      timeout: "configurable"
    }
  }
}
```

#### Database Operations
```typescript
CHECK: {
  context: "database",
  rules: {
    "queries": {
      transactions: "required",
      n-plus-one: "prevent",
      indexes: "analyze"
    },
    "migrations": {
      rollback: "required",
      data-loss: "prevent",
      concurrent: "safe"
    }
  }
}
```

## Data Engineering Directives

### ETL Processes
```python
ENFORCE: {
  context: "etl",
  rules: {
    "data-validation": {
      schema: "strict",
      nulls: "explicit-handle",
      types: "coerce-log"
    },
    "transformations": {
      idempotent: "required",
      logging: "detailed",
      recovery: "checkpoint"
    },
    "loading": {
      batching: "optimized",
      duplicates: "handle",
      consistency: "check"
    }
  }
}
```

### Machine Learning
```python
OPTIMIZE: {
  context: "ml",
  rules: {
    "model-training": {
      memory: "profile",
      gradients: "check",
      batching: "dynamic"
    },
    "inference": {
      quantization: "analyze",
      batching: "optimal",
      caching: "selective"
    },
    "validation": {
      metrics: "comprehensive",
      splits: "stratified",
      leakage: "prevent"
    }
  }
}
```

## Mobile Development Directives

### iOS Swift
```swift
ENFORCE: {
  context: "ios",
  rules: {
    "memory": {
      arc: "analyze",
      cycles: "prevent",
      dealloc: "verify"
    },
    "ui": {
      main-thread: "enforce",
      layout: "constraints",
      responsive: "dynamic"
    },
    "patterns": {
      delegates: "weak",
      closures: "capture-list",
      optionals: "safe-unwrap"
    }
  }
}
```

### Android Kotlin
```kotlin
CHECK: {
  context: "android",
  rules: {
    "lifecycle": {
      leaks: "prevent",
      scope: "structured",
      cleanup: "automatic"
    },
    "compose": {
      recomposition: "minimize",
      side-effects: "launch-effect",
      state: "hoisted"
    },
    "coroutines": {
      scope: "structured",
      cancellation: "cooperative",
      dispatchers: "appropriate"
    }
  }
}
```

## Cross-Platform Development

### React Native
```typescript
OPTIMIZE: {
  context: "react-native",
  rules: {
    "platform-specific": {
      code: "minimal",
      components: "abstract",
      apis: "unified"
    },
    "performance": {
      renders: "minimize",
      images: "optimize",
      animations: "native"
    },
    "navigation": {
      state: "persisted",
      transitions: "smooth",
      deep-links: "handled"
    }
  }
}
```

## Usage Examples

### Component Development
```typescript
// @lint-directive: ENFORCE component-structure
const UserProfile: React.FC<UserProfileProps> = ({ user }) => {
  // Hooks at top level
  const [isEditing, setIsEditing] = useState(false);
  
  // Handlers with prefix
  const handleEditClick = useCallback(() => {
    setIsEditing(true);
  }, []);
  
  // Memoized expensive computations
  const userStats = useMemo(() => computeUserStats(user), [user]);
  
  return (
    <ProfileContainer>
      <UserInfo user={user} stats={userStats} />
      <EditButton onClick={handleEditClick} />
    </ProfileContainer>
  );
};
```

### API Endpoint
```typescript
// @lint-directive: ENFORCE api-security
app.post("/api/v1/users", 
  validateSchema(userSchema),
  sanitizeInput(),
  async (req: Request, res: Response) => {
    try {
      const user = await createUser(req.body);
      res.status(201).json({
        data: { user },
        meta: { timestamp: new Date() }
      });
    } catch (error) {
      handleApiError(error, res);
    }
  }
);
```

### ETL Pipeline
```python
# @lint-directive: ENFORCE etl-validation
def transform_user_data(data: DataFrame) -> DataFrame:
    # Schema validation
    validate_schema(data, USER_SCHEMA)
    
    # Explicit null handling
    data = handle_nulls(data, strategy="fill")
    
    # Type coercion with logging
    data = coerce_types(data, log_errors=True)
    
    return data
```

## Best Practices

1. **Directive Placement**
   - Place directives at the top of files or before specific code blocks
   - Use consistent formatting for directive comments
   - Document any deviations from directive rules

2. **Rule Combinations**
   - Combine related rules under a single directive
   - Avoid conflicting rule combinations
   - Use the most specific context possible

3. **Performance Considerations**
   - Balance strictness with development velocity
   - Consider the impact on build/compile time
   - Use appropriate rules for development vs production

4. **Maintenance**
   - Regularly review and update directives
   - Monitor the impact on code quality metrics
   - Gather feedback from development team

## Common Patterns

### Error Prevention
```yaml
ENFORCE: {
  context: "global",
  rules: {
    "error-handling": {
      async: "try-catch",
      types: "specific",
      recovery: "graceful"
    }
  }
}
```

### Performance Optimization
```yaml
OPTIMIZE: {
  context: "global",
  rules: {
    "resources": {
      memory: "efficient",
      cpu: "minimal",
      network: "batched"
    }
  }
}
```

### Security
```yaml
CHECK: {
  context: "global",
  rules: {
    "security": {
      input: "sanitized",
      output: "escaped",
      auth: "verified"
    }
  }
}
```

## Directive Reference

### Actions
- `ENFORCE`: Strict rules that must be followed
- `CHECK`: Validation rules with warnings
- `OPTIMIZE`: Performance improvement suggestions

### Contexts
- `global`: Applies to all code
- `component`: UI component specific
- `api`: API endpoint specific
- `data`: Data processing specific
- `platform`: Platform-specific code

### Levels
- `strict`: No exceptions allowed
- `moderate`: Warnings for violations
- `loose`: Suggestions only

## Contributing
To propose new directives or modifications:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed explanation

## Version History
- 1.0.0: Initial release
- 1.0.1: Added mobile directives
- 1.0.2: Enhanced ETL rules