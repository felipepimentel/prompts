---
title: "Git Branch Naming Convention Guide"
path: "developer/git/branch-naming"
tags: ["git", "best-practices", "development", "version-control", "collaboration"]
description: "A comprehensive guide for establishing consistent and meaningful Git branch naming conventions across development teams"
prompt_type: "Guidelines"
---

<purpose>
To establish a standardized branch naming convention that improves code organization, collaboration, and project management in Git repositories.
</purpose>

<context>
Use this guide when setting up branch naming conventions for a new project or standardizing naming across existing repositories.
</context>

<instructions>
Follow these guidelines for naming Git branches:

1. Branch Type Prefix
   - feature/ : For new features
   - bugfix/ : For bug fixes
   - hotfix/ : For urgent production fixes
   - release/ : For release branches
   - refactor/ : For code refactoring
   - test/ : For testing branches
   - docs/ : For documentation updates

2. Issue Reference
   - Include ticket/issue number after prefix
   - Use hyphen as separator
   - Example: feature/JIRA-123

3. Description
   - Add brief description after issue number
   - Use hyphens between words
   - Keep it concise but meaningful
   - Use lowercase letters

4. Complete Pattern:
   [type]/[ticket-number]-[brief-description]

Branch naming rules:
- Use lowercase letters
- Use hyphens (-) as word separators
- No spaces or underscores
- Keep descriptions concise
- Include relevant ticket numbers
- Use only ASCII characters
</instructions>

<variables>
- branch_type: Type of work being done
- ticket_number: Reference to issue tracker
- description: Brief description of the work
</variables>

<examples>
Example 1: New feature development
Input: Creating a user authentication feature, ticket ABC-123
Output: feature/ABC-123-user-authentication

Example 2: Bug fix implementation
Input: Fixing login page crash, ticket BUG-456
Output: bugfix/BUG-456-fix-login-crash

Example 3: Urgent production fix
Input: Critical security patch, ticket SEC-789
Output: hotfix/SEC-789-security-vulnerability-fix

Example 4: Documentation update
Input: Updating API documentation, ticket DOC-321
Output: docs/DOC-321-update-api-docs
</examples>

<notes>
- Maintain consistency across all repositories
- Document conventions in project README
- Consider automated branch name validation
- Keep descriptions meaningful but concise
- Ensure ticket numbers are accurate
- Consider CI/CD pipeline requirements
- Make conventions easily searchable
</notes>