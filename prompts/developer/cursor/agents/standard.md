---
title: "Cursor IDE Development Standards"
author: "Cursor Development Team"
date: "`r format(Sys.time(), '%B %d, %Y')`"
output:
  html_document:
    theme: united
    toc: true
    toc_float: true
---

# Cursor Development Standards and Best Practices

## Core Principles
- Write concise, technical responses with accurate Python examples
- Follow PEP 8 style guidelines strictly
- Use descriptive variable names with auxiliary verbs (e.g., is_active, has_permission)
- Implement proper error handling and logging throughout
- Maintain clear separation of concerns in all architectures
- Use type hints consistently across all function signatures
- Prioritize code readability and maintainability

## File Structure and Naming
- Use lowercase with underscores for directories and files (e.g., `blueprints/user_routes.py`)
- Required header comment for all files:
```python
"""
File: {filename}
Version: {semantic_version}
Path: {full_file_path}
Description: {brief_description}
Created: {date}
"""
```

## Documentation Requirements
### RMarkdown Headers
```yaml
---
title: "TITLE: Clear description"
author: "Project Team"
date: "`r format(Sys.time(), '%B %d, %Y')`"
output:
  html_document:
    theme: united
    highlight: tango
    toc: yes
    toc_depth: 3
    toc_float:
      collapsed: no
      smooth_scroll: yes
    code_folding: show
bibliography: references.bib
---
```

### Project Structure Documentation
Every .rmd file must include:
1. Full project directory structure
2. Environment configuration section
3. Database schema diagrams (when applicable)
4. Service connection details
5. Cross-references using absolute paths

### Database Documentation
Required sections:
1. Mermaid diagrams for schema relationships
2. Table of databases and schemas
3. Migration history
4. Performance metrics
5. Maintenance procedures

## Framework-Specific Guidelines
[Framework guidelines as in original file...] 