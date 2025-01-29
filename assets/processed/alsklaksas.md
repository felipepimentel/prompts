---
title: "Git Ignore Configuration Guide"
path: "developer/git/gitignore-setup"
tags: ["git", "configuration", "best-practices", "security"]
description: "A comprehensive guide for creating and maintaining .gitignore files that effectively exclude unnecessary and sensitive files"
prompt_type: "Configuration Framework"
---

<purpose>
To provide a structured approach for creating comprehensive .gitignore files that properly exclude build artifacts, system files, and sensitive information.
</purpose>

<context>
Use this guide when setting up a new project or updating the .gitignore configuration for an existing project to ensure proper file exclusion.
</context>

<instructions>
Specify your project details:

1. Project Information
   - Development Language
     * Primary language
     * Framework(s)
     * Build tools
     * Package managers

   - Development Environment
     * IDEs in use
     * Operating systems
     * Development tools
     * Deployment platforms

2. File Categories to Ignore
   - System Files
     * OS-specific files
     * Temporary files
     * Thumbnail caches
     * System logs

   - Development Files
     * IDE configurations
     * Editor settings
     * Local tooling
     * Debug files

   - Build Artifacts
     * Compiled files
     * Build directories
     * Generated code
     * Cache files

   - Dependencies
     * Package directories
     * Vendor folders
     * Library files
     * Module caches

   - Sensitive Information
     * Configuration files
     * Environment files
     * API keys
     * Credentials

3. Configuration Structure
   - Global Patterns
     * Common exclusions
     * Directory patterns
     * File extensions
     * Path specifications

   - Project-Specific Rules
     * Custom build outputs
     * Local configurations
     * Project artifacts
     * Test outputs
</instructions>

<variables>
- project_language: Primary development language
- frameworks: Development frameworks in use
- development_tools: IDEs and tools in use
- operating_systems: Target OS platforms
</variables>

<examples>
Example 1:
Input: Node.js web application
Output:
```gitignore
# Dependencies
node_modules/
npm-debug.log
yarn-debug.log
yarn-error.log

# Build output
dist/
build/
.next/
out/

# Environment variables
.env
.env.local
.env*.local

# IDE files
.idea/
.vscode/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Debug logs
debug.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Testing
coverage/
.nyc_output/

# Misc
*.log
*.pid
*.seed
*.pid.lock
```

Example 2:
Input: Python Django project
Output:
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.env/
.venv/
ENV/

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/
static/
staticfiles/

# Development
.idea/
.vscode/
*.swp
.DS_Store
Thumbs.db

# Secrets
.env
.env.local
secrets.json
credentials.json

# Testing
.coverage
htmlcov/
.tox/
.pytest_cache/
pytest.ini

# Build
*.egg-info/
dist/
build/
eggs/
parts/
bin/
var/
sdist/
develop-eggs/
```
</examples>

<notes>
- Keep patterns specific
- Document non-obvious exclusions
- Consider global gitignore
- Review regularly
- Test exclusions
- Share with team
- Update as needed
</notes>