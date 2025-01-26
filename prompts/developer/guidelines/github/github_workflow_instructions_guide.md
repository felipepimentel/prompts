---
category: Developer
description: A comprehensive guide for GitHub workflows, including branching strategies,
  commit conventions, and collaboration best practices
model: GPT-4
path: developer/guidelines/github/github-workflow-instructions-guide
prompt_type: Instruction-based prompting
tags:
- github
- workflow
- git
- development
- collaboration
- best-practices
- instructions
- version-control
title: GitHub Workflow Instructions Guide
version: '1.0'
---

# GitHub Workflow Instructions Guide

## Overview
This guide provides detailed instructions and best practices for working with GitHub, focusing on efficient workflows, collaboration patterns, and version control strategies.

## Git Workflow

### 1. Branching Strategy
```bash
# Main branches
main        # Production-ready code
develop     # Integration branch

# Supporting branches
feature/*   # New features
bugfix/*    # Bug fixes
hotfix/*    # Production fixes
release/*   # Release preparation
```

### 2. Branch Management
```bash
# Create new feature branch
git checkout develop
git pull origin develop
git checkout -b feature/new-feature

# Keep branch updated
git fetch origin
git rebase origin/develop

# Clean up after merge
git branch -d feature/new-feature
git remote prune origin
```

## Commit Guidelines

### 1. Conventional Commits
```bash
# Format: <type>(<scope>): <description>
git commit -m "feat(auth): add OAuth2 authentication"
git commit -m "fix(api): handle null response from endpoint"
git commit -m "docs(readme): update installation instructions"

# Types:
# feat:     New feature
# fix:      Bug fix
# docs:     Documentation
# style:    Formatting
# refactor: Code restructuring
# test:     Adding tests
# chore:    Maintenance
```

### 2. Commit Best Practices
```bash
# Atomic commits
git add components/Button.tsx
git commit -m "feat(ui): add primary button component"

# Include tests
git add components/Button.test.tsx
git commit -m "test(ui): add button component tests"

# Link to issues
git commit -m "fix(api): resolve timeout issues (#123)"
```

## Pull Request Workflow

### 1. Creating Pull Requests
```markdown
## Title Format
[Type] Brief description

Example: [Feature] Add user authentication

## Description Template
### Changes Made
- Implemented OAuth2 flow
- Added user profile endpoints
- Created authentication middleware

### Testing
- Unit tests added for auth service
- Integration tests for API endpoints
- Manual testing steps documented

### Checklist
- [ ] Tests passing
- [ ] Documentation updated
- [ ] No linting errors
- [ ] Reviewed by team member
```

### 2. Review Process
```markdown
## Reviewer Guidelines

### Code Quality
- Check for clean code principles
- Verify error handling
- Review performance implications

### Testing
- Run tests locally
- Verify coverage
- Check edge cases

### Documentation
- API documentation complete
- README updates if needed
- Code comments clear
```

## Repository Management

### 1. Project Structure
```
.github/
  workflows/        # GitHub Actions
  CODEOWNERS       # Code ownership
  CONTRIBUTING.md  # Contribution guide
  SECURITY.md      # Security policy
src/
  components/      # UI components
  services/        # Business logic
  utils/          # Helper functions
tests/
  unit/           # Unit tests
  integration/    # Integration tests
docs/             # Documentation
```

### 2. Issue Management
```markdown
## Issue Template

### Bug Report
#### Description
Clear description of the bug

#### Steps to Reproduce
1. Step one
2. Step two
3. Step three

#### Expected Behavior
What should happen

#### Actual Behavior
What actually happens

### Feature Request
#### Problem Statement
What problem does this solve?

#### Proposed Solution
How should it work?

#### Acceptance Criteria
- [ ] Criterion one
- [ ] Criterion two
```

## Collaboration Practices

### 1. Code Review Comments
```markdown
## Comment Guidelines

### Constructive
✅ "Consider using a more descriptive variable name here"
❌ "This is bad code"

### Specific
✅ "This function might fail with null input"
❌ "This needs more error handling"

### Actionable
✅ "We could improve performance by memoizing this value"
❌ "This is slow"
```

### 2. Team Communication
```markdown
## Communication Channels

### Pull Requests
- Technical discussions
- Code review feedback
- Implementation details

### Issues
- Feature requests
- Bug reports
- Project tracking

### Discussions
- Architecture decisions
- Best practices
- Team guidelines
```

## Release Management

### 1. Version Control
```bash
# Semantic Versioning
MAJOR.MINOR.PATCH
# MAJOR: Breaking changes
# MINOR: New features
# PATCH: Bug fixes

# Creating releases
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### 2. Release Process
```markdown
## Release Checklist

### Preparation
- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Run full test suite
- [ ] Update documentation

### Deployment
- [ ] Create release branch
- [ ] Run build process
- [ ] Deploy to staging
- [ ] Run smoke tests

### Publication
- [ ] Create GitHub release
- [ ] Publish release notes
- [ ] Notify stakeholders
```

## Automation

### 1. GitHub Actions Workflow
```yaml
# .github/workflows/main.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Lint
        run: npm run lint
      - name: Test
        run: npm run test
      - name: Build
        run: npm run build

  deploy:
    needs: validate
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        run: npm run deploy
```

### 2. Automated Checks
```yaml
# .github/workflows/checks.yml
name: Code Quality

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - name: Code Coverage
        uses: codecov/codecov-action@v3
      
      - name: Security Scan
        uses: snyk/actions/node@master
      
      - name: Performance Check
        uses: lighthouse-action@v1
```

## Best Practices

### 1. Security
- Use signed commits
- Enable 2FA
- Regular dependency updates
- Secret scanning
- Security policy enforcement

### 2. Performance
- Optimize repository size
- Use Git LFS for large files
- Regular maintenance
- Cache dependencies
- Optimize workflows

### 3. Documentation
- Keep README updated
- Document workflows
- Maintain CHANGELOG
- API documentation
- Contributing guidelines

## Resources
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)