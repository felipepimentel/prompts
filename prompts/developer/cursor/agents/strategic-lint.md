---
title: "Comprehensive Linting Directives Guide"
author: "Claude"
date: "`r Sys.Date()`"
output:
  html_document:
    toc: true
    toc_float: true
    toc_depth: 3
    theme: united
    highlight: tango
    code_folding: show
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

# Linting Directive Guide & Cheatsheet

## Quick Reference Syntax

```
ENFORCE: <rule>=<level>
CHECK: <category>=<strictness>
OPTIMIZE: <target>=<strategy>
```

## Project-Specific Linting Tables

### Web Development

| Context | Directive | Purpose | Example |
|---------|-----------|----------|---------|
| **Frontend** | `ENFORCE: style=airbnb jsx=strict` | React/Vue code quality | Ensures component best practices |
| **Backend** | `CHECK: security=high async=true` | Server code safety | Prevents common API vulnerabilities |
| **Full Stack** | `OPTIMIZE: bundle=size cache=check` | Performance | Reduces bundle size, improves caching |

### Data Engineering

| Context | Directive | Purpose | Example |
|---------|-----------|----------|---------|
| **ETL** | `CHECK: data=sanitize null=strict` | Data integrity | Validates transformations |
| **ML** | `OPTIMIZE: memory=efficient tensor=validate` | Model performance | Prevents memory leaks |
| **Analytics** | `ENFORCE: docs=required tests=coverage:80` | Reproducibility | Ensures documented analysis |

### Mobile Development

| Context | Directive | Purpose | Example |
|---------|-----------|----------|---------|
| **iOS** | `CHECK: memory=arc ui=main` | Swift optimization | Prevents retain cycles |
| **Android** | `ENFORCE: null=strict compose=true` | Kotlin safety | Ensures null safety |
| **Cross-Platform** | `OPTIMIZE: platform=both` | Compatibility | Validates cross-platform code |

## Common Directive Patterns

### Security Focus
```
SECURE:
  input=sanitize
  auth=validate
  sql=parameterize
  csrf=check
```

### Performance Focus
```
OPTIMIZE:
  complexity=O(n)
  memory=linear
  async=true
  cache=recommended
```

### Code Quality Focus
```
ENFORCE:
  style=standard
  types=strict
  docs=required
  tests=unit:required,e2e:recommended
```

## Language-Specific Directives

### Python
```python
# Directive: ENFORCE: pep8=true typing=strict
def process_data(data: List[Dict]) -> DataFrame:
    """
    Process input data into DataFrame.
    Args:
        data: List of dictionaries
    Returns:
        DataFrame: Processed data
    """
    return pd.DataFrame(data)
```

### TypeScript
```typescript
// Directive: CHECK: types=strict null=strict
interface UserData {
  id: number;
  name: string;
  email: string | null;
}

function processUser(user: UserData): void {
  // Type-safe processing
}
```

### Java/Kotlin
```kotlin
// Directive: ENFORCE: null=strict coroutines=best_practice
suspend fun fetchData(): Result<Data> = withContext(Dispatchers.IO) {
    try {
        // Fetch implementation
    } catch (e: Exception) {
        Result.failure(e)
    }
}
```

## Best Practices

### 1. Combining Directives
```
# Basic Development
ENFORCE: style=standard
CHECK: basic

# Production Release
ENFORCE: style=strict
CHECK: all
OPTIMIZE: performance
SECURE: high
```

### 2. Environment-Specific Rules
```
ENV: development
  ENFORCE: relaxed
  CHECK: basic

ENV: production
  ENFORCE: strict
  CHECK: comprehensive
  SECURE: high
```

### 3. Documentation Requirements
```
DOCUMENT:
  public=required
  private=recommended
  examples=true
  updates=required
```

## Linting Implementation Guide

### Setup Process

1. **Project Initialization**
```bash
# Install linting tools
npm install eslint prettier --save-dev
# or
pip install flake8 mypy black
```

2. **Configuration Files**
```json
{
  "extends": ["eslint:recommended"],
  "rules": {
    "max-len": ["error", { "code": 80 }],
    "indent": ["error", 4]
  }
}
```

3. **Integration Steps**
```yaml
# CI/CD Integration
lint:
  script:
    - npm run lint
    - npm run type-check
```

## Advanced Usage

### Custom Rule Sets
```
CUSTOM:
  rules:
    - name: "max-complexity"
      level: "warning"
      threshold: 10
    - name: "doc-coverage"
      level: "error"
      minimum: 80
```

### Automated Fixes
```
FIX:
  style=auto
  imports=organize
  unused=remove
```

### Performance Monitoring
```
MONITOR:
  complexity=track
  coverage=report
  dependencies=audit
```

## Troubleshooting Guide

| Issue | Directive | Solution |
|-------|-----------|----------|
| False Positives | `IGNORE: rule_id` | Disable specific rule |
| Performance Impact | `OPTIMIZE: parse=lazy` | Lazy rule evaluation |
| Configuration Conflicts | `PRIORITY: tool1>tool2` | Set tool precedence |

## Resources

- [ESLint Documentation](https://eslint.org/docs/latest/)
- [Python Black](https://black.readthedocs.io/)
- [SwiftLint](https://realm.github.io/SwiftLint/)
- [ktlint](https://ktlint.github.io/)

## Notes

- Always test linting configurations in isolation
- Regular updates to linting rules recommended
- Consider team feedback for rule adjustments
- Document rule exceptions with clear reasoning

---

*This guide is maintained and updated regularly. Last update: `r Sys.Date()`*