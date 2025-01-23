---
description: A comprehensive guide for writing clear, informative, and standardized
  git commit messages
path: developer/instructions/git-commit-guidelines.md
prompt_type: Instruction-based prompting
tags:
- git
- version-control
- best-practices
- documentation
- collaboration
title: Git Commit Message Guidelines
---

# Git Commit Message Guidelines

## 1. Message Structure
### 1.1 Format
```
<type>(<scope>): <gitmoji> <subject>

<body>

<footer>
```

### 1.2 Components
- Type: Describes the kind of change
- Scope: Component or area affected (optional)
- Gitmoji: Relevant emoji for visual categorization
- Subject: Concise description
- Body: Detailed explanation (optional)
- Footer: References and breaking changes (optional)

## 2. Type Categories
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes
- refactor: Code refactoring
- perf: Performance improvements
- test: Adding/modifying tests
- chore: Maintenance tasks
- ci: CI/CD changes
- build: Build system changes
- revert: Reverting changes

## 3. Writing Guidelines
### 3.1 Subject Line
- Use imperative mood ("Add" not "Added")
- Keep under 50 characters
- Capitalize first letter
- No period at the end
- Be specific and clear
- Use present tense

### 3.2 Message Body
- Wrap at 72 characters
- Explain what and why, not how
- Use bullet points for multiple items
- Include context and motivation
- Reference issues and PRs
- Describe side effects

## 4. Gitmoji Usage
### 4.1 Common Emojis
- ✨ (sparkles): New feature
- 🐛 (bug): Bug fix
- 📚 (books): Documentation
- 💄 (lipstick): UI/style
- ♻️ (recycle): Refactor
- ⚡️ (zap): Performance
- ✅ (check): Tests
- 🔧 (wrench): Configuration
- 👷 (construction): CI
- 📦 (package): Dependencies

### 4.2 Guidelines
- Use relevant emoji
- Place before subject
- Limit to one primary emoji
- Be consistent in usage
- Follow team conventions
- Document emoji meanings

## 5. Best Practices
1. Write clear, atomic commits
2. Separate logical changes
3. Reference relevant issues
4. Document breaking changes
5. Follow team conventions
6. Be consistent in style
7. Review before committing

## Examples

### Feature Addition
```
feat(auth): ✨ Add OAuth2 authentication support

Implement OAuth2 authentication flow with Google provider.
- Add OAuth2 client configuration
- Create user authentication endpoints
- Implement token validation
- Add user session management

Closes #123
```

### Bug Fix
```
fix(api): 🐛 Fix race condition in user session handling

Resolve concurrent session creation issues by adding
proper locking mechanisms and validation checks.

Fixes #456
```

### Documentation Update
```
docs(readme): 📚 Update installation instructions

Add detailed steps for development environment setup
and troubleshooting guidelines.
```

Remember: Good commit messages are crucial for project maintainability and team collaboration. They should tell a story of how and why the code has evolved. 