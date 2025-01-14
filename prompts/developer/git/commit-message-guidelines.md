---
title: Git Commit Message Guidelines
path: developer/git/commit-message-guidelines
tags:
  - git
  - version-control
  - best-practices
  - collaboration
  - documentation
description: Comprehensive guide for writing clear, semantic, and standardized git commit messages
---

# Git Commit Message Guidelines

## Message Structure

### Format
```
<type>(<scope>): <gitmoji> <subject>

<body>

<footer>
```

### Components
- **Type**: Category of change (required)
- **Scope**: Component affected (optional)
- **Gitmoji**: Visual category indicator (recommended)
- **Subject**: Brief description (required)
- **Body**: Detailed explanation (optional)
- **Footer**: References/breaking changes (optional)

## Type Categories
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style/formatting
- `refactor`: Code restructuring
- `perf`: Performance improvements
- `test`: Adding/updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes
- `build`: Build system changes
- `revert`: Reverting changes

## Writing Guidelines

### Subject Line
- Use imperative mood ("Add" not "Added")
- Maximum 50 characters
- Capitalize first letter
- No period at end
- Be specific and clear
- Use present tense

### Message Body
- Wrap at 72 characters
- Explain what and why, not how
- Use bullet points for multiple points
- Include context and motivation
- Reference issues and PRs
- Describe side effects

## Gitmoji Usage

### Common Emojis
- ✨ New feature
- 🐛 Bug fix
- 📚 Documentation
- 💄 UI/style
- ♻️ Refactor
- ⚡️ Performance
- ✅ Tests
- 🔧 Configuration
- 👷 CI
- 📦 Dependencies

### Guidelines
- Use one primary emoji
- Place before subject
- Follow team conventions
- Be consistent
- Document meanings

## Examples

### Feature Addition
```
feat(auth): ✨ Add OAuth2 authentication

Implement Google OAuth2 provider for user authentication
- Add OAuth2 client configuration
- Create authentication endpoints
- Implement token validation
- Add session management

Closes #123
```

### Bug Fix
```
fix(api): 🐛 Handle null response in user service

Add null checks to prevent crashes when API returns
unexpected null values in user profile responses.

Fixes #456
```

### Breaking Change
```
feat(api)!: 💥 Migrate to v2 API endpoints

BREAKING CHANGE: All v1 API endpoints have been removed.
Clients must update to use new v2 endpoints.

Migration guide: docs/migration-v2.md
```

## Best Practices

1. Write atomic commits
2. Separate logical changes
3. Reference relevant issues
4. Document breaking changes
5. Follow team conventions
6. Be consistent
7. Review before committing

Remember: Good commit messages are crucial for project maintainability and team collaboration. They should tell a story of how and why the code has evolved. 