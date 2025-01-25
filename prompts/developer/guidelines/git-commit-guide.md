---
category: Developer
description: Comprehensive guide for creating clear and effective Git commits, focusing
  on best practices, conventions, and workflow optimization
model: GPT-4
path: developer/guidelines/git-commit-guide.md
prompt_type: Instruction-based prompting
tags:
- git
- version-control
- best-practices
- workflow
- collaboration
title: Git Commit Guide
version: '1.0'
---

# Git Commit Guide

## Overview
This guide provides a structured approach to creating effective Git commits that enhance collaboration, maintainability, and project history clarity.

## Commit Message Structure

### 1. Conventional Commits
```bash
# Format
<type>(<scope>): <description>

[optional body]

[optional footer(s)]

# Examples
feat(auth): add OAuth2 authentication
fix(api): handle null response from user service
docs(readme): update installation instructions
style(components): format according to style guide
refactor(database): optimize query performance
test(auth): add unit tests for login flow
chore(deps): update dependencies
```

### 2. Type Definitions
```bash
# Common types
feat     # New feature
fix      # Bug fix
docs     # Documentation changes
style    # Code style changes (formatting, etc.)
refactor # Code changes that neither fix bugs nor add features
test     # Adding or modifying tests
chore    # Maintenance tasks

# Examples
feat: add user registration
fix: prevent crash when email is null
docs: add API documentation
style: format code according to guidelines
refactor: simplify authentication logic
test: add integration tests for API
chore: update npm packages
```

## Commit Best Practices

### 1. Atomic Commits
```bash
# Bad: Multiple unrelated changes
git commit -m "fix login bug, update styles, add new feature"

# Good: Separate commits for each change
git commit -m "fix: handle invalid credentials in login"
git commit -m "style: update button styles to match design"
git commit -m "feat: add password reset functionality"
```

### 2. Clear Descriptions
```bash
# Bad: Vague description
git commit -m "fix bug"

# Good: Clear and specific
git commit -m "fix: handle edge case when user email is not verified"

# Better: With body for more context
git commit -m "fix: handle edge case when user email is not verified

When a user attempts to log in with an unverified email address,
the system now displays a proper error message and sends a new
verification email instead of silently failing.

Closes #123"
```

## Workflow Integration

### 1. Pre-commit Hooks
```bash
# .git/hooks/commit-msg
#!/bin/sh

commit_msg_file=$1
commit_msg=$(cat "$commit_msg_file")

# Check conventional commit format
if ! echo "$commit_msg" | grep -qE '^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+$'; then
    echo "Error: Commit message does not follow conventional commit format"
    echo "Format: <type>(<scope>): <description>"
    exit 1
fi
```

### 2. Commit Template
```bash
# .gitmessage
# <type>(<scope>): <description>
# |<----  Using a Maximum Of 50 Characters  ---->|

# [optional body]
# |<----   Try To Limit Each Line to a Maximum Of 72 Characters   ---->|

# [optional footer(s)]
# Closes #123

# Types: feat, fix, docs, style, refactor, test, chore
# Scope: auth, api, ui, etc.
# Description: imperative, present tense, no period
# Body: explain what and why vs. how
# Footer: reference issues, breaking changes
```

## Branch Integration

### 1. Feature Branches
```bash
# Create feature branch
git checkout -b feature/user-authentication

# Make atomic commits
git commit -m "feat(auth): add login form component"
git commit -m "feat(auth): implement login API integration"
git commit -m "test(auth): add login form tests"
git commit -m "docs(auth): add login documentation"

# Prepare for merge
git checkout main
git pull
git merge feature/user-authentication
```

### 2. Pull Requests
```markdown
# Pull Request Template

## Description
[Describe the changes and their purpose]

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that causes existing functionality to change)
- [ ] Documentation update

## Commits
- feat(auth): add login form component
- feat(auth): implement login API integration
- test(auth): add login form tests
- docs(auth): add login documentation

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests passing
- [ ] Commits follow conventions
```

## Maintenance

### 1. History Clean-up
```bash
# Interactive rebase to clean up commits
git rebase -i HEAD~3

# Commands available in rebase
pick   # Use commit
reword # Edit commit message
edit   # Edit commit
squash # Combine with previous commit
fixup  # Combine and discard message
drop   # Remove commit
```

### 2. Commit Fixes
```bash
# Amend last commit
git commit --amend -m "feat(auth): add OAuth2 authentication"

# Add forgotten files
git add forgotten-file.js
git commit --amend --no-edit

# Fix author information
git commit --amend --author="John Doe <john@example.com>"
```

## Best Practices

1. Commit Organization
   - Make atomic commits
   - Use clear messages
   - Follow conventions
   - Include context

2. Message Structure
   - Use imperative mood
   - Be concise but clear
   - Reference issues
   - Add detailed body when needed

3. Workflow
   - Use feature branches
   - Review before commit
   - Run tests
   - Update documentation

4. Maintenance
   - Clean history regularly
   - Fix mistakes promptly
   - Keep branches updated
   - Archive old branches

Remember to:
1. Write meaningful messages
2. Make atomic commits
3. Follow team conventions
4. Include necessary context
5. Keep history clean