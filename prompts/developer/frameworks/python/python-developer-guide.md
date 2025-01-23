---
description: Comprehensive guide for Python developers, covering development environment
  setup, tools, workflows, and productivity tips
path: developer/frameworks/python/python-developer-guide.md
prompt_type: Instruction-based prompting
tags:
- python
- development
- tools
- productivity
- workflow
title: Python Developer Guide
---

# Python Developer Guide

## Overview
This guide provides a comprehensive overview of Python development tools, workflows, and best practices to help developers be more productive and efficient.

## Development Environment Setup

### 1. Python Installation
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev

# macOS with Homebrew
brew install python@3.12

# Windows with Chocolatey
choco install python --version=3.12
```

### 2. Essential Tools
```bash
# Install development tools
pip install --user pipx
pipx install poetry
pipx install black
pipx install mypy
pipx install ruff
pipx install pytest
```

### 3. IDE Setup (VS Code)
```json
// settings.json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.ruffEnabled": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

## Project Management

### 1. Virtual Environments
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Unix/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Dependency Management with Poetry
```toml
# pyproject.toml
[tool.poetry]
name = "project-name"
version = "0.1.0"
description = "Project description"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.31.0"
pydantic = "^2.5.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
black = "^23.10.0"
mypy = "^1.6.0"
ruff = "^0.1.0"
```

### 3. Project Structure
```
project/
├── src/
│   └── package/
│       ├── __init__.py
│       ├── main.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_main.py
├── docs/
│   └── index.md
├── pyproject.toml
├── README.md
└── .gitignore
```

## Development Workflow

### 1. Version Control
```bash
# Initialize repository
git init

# Create .gitignore
cat > .gitignore << EOL
__pycache__/
*.py[cod]
*$py.class
.env
.venv/
.coverage
htmlcov/
.pytest_cache/
.mypy_cache/
.ruff_cache/
dist/
build/
*.egg-info/
EOL

# Set up pre-commit hooks
pip install pre-commit
cat > .pre-commit-config.yaml << EOL
repos:
  - repo: https://github.com/psf/black
    rev: 23.10.0
    hooks:
      - id: black
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
EOL
```

### 2. Testing
```python
# tests/conftest.py
import pytest
from typing import Generator

@pytest.fixture
def sample_data() -> Generator[dict, None, None]:
    """Provide sample data for tests."""
    data = {"key": "value"}
    yield data

# tests/test_main.py
def test_feature(sample_data: dict) -> None:
    """Test feature functionality."""
    assert sample_data["key"] == "value"
```

### 3. Code Quality Tools
```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ["py312"]

[tool.ruff]
select = ["E", "F", "I", "N", "W"]
ignore = ["E501"]
line-length = 88
target-version = "py312"

[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

## Debugging and Profiling

### 1. Debugging with pdb
```python
def complex_function(data: dict) -> int:
    """Complex function for demonstration."""
    import pdb; pdb.set_trace()  # Start debugger
    result = 0
    for key, value in data.items():
        if isinstance(value, int):
            result += value
    return result
```

### 2. Performance Profiling
```python
import cProfile
import pstats
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T", bound=Callable)

def profile(func: T) -> T:
    """Profile function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            return profile.runcall(func, *args, **kwargs)
        finally:
            stats = pstats.Stats(profile)
            stats.sort_stats("cumulative")
            stats.print_stats()
    return wrapper  # type: ignore

@profile
def expensive_operation() -> None:
    """Expensive operation to profile."""
    result = sum(i * i for i in range(1000000))
```

## Documentation

### 1. Docstring Format
```python
from typing import Optional, List

def process_data(
    data: List[str],
    max_length: Optional[int] = None
) -> List[str]:
    """
    Process a list of strings according to specified criteria.

    Args:
        data: List of strings to process
        max_length: Maximum length for each string (optional)

    Returns:
        List of processed strings

    Raises:
        ValueError: If any string exceeds max_length

    Example:
        >>> process_data(["hello", "world"], max_length=5)
        ['hello', 'world']
    """
    if max_length is not None:
        for item in data:
            if len(item) > max_length:
                raise ValueError(
                    f"String '{item}' exceeds max length of {max_length}"
                )
    return [item.strip() for item in data]
```

### 2. Project Documentation
```markdown
# Project Name

## Overview
Brief description of the project.

## Installation
```bash
poetry install
```

## Usage
Example code showing basic usage.

## Development
Instructions for setting up development environment.

## Testing
Instructions for running tests.

## Contributing
Guidelines for contributing to the project.
```

## Productivity Tips

### 1. Shell Aliases
```bash
# Add to ~/.bashrc or ~/.zshrc
alias py='python'
alias ipy='ipython'
alias pt='pytest'
alias pvenv='python -m venv .venv'
alias activate='source .venv/bin/activate'
```

### 2. IPython Configuration
```python
# ~/.ipython/profile_default/ipython_config.py
c.InteractiveShellApp.extensions = [
    'autoreload'
]
c.InteractiveShellApp.exec_lines = [
    '%autoreload 2'
]
```

### 3. VS Code Snippets
```json
{
    "Python Class": {
        "prefix": "pclass",
        "body": [
            "class ${1:ClassName}:",
            "    \"\"\"${2:Class description.}\"\"\"",
            "",
            "    def __init__(self) -> None:",
            "        ${0:pass}"
        ]
    },
    "Python Function": {
        "prefix": "pfunc",
        "body": [
            "def ${1:function_name}(${2:parameters}) -> ${3:None}:",
            "    \"\"\"${4:Function description.}\"\"\"",
            "    ${0:pass}"
        ]
    }
}
```

## Best Practices

1. Development Environment
   - Use virtual environments
   - Maintain consistent Python versions
   - Configure IDE properly
   - Use version control

2. Code Quality
   - Follow style guides (PEP 8)
   - Use type hints
   - Write tests
   - Document code

3. Workflow
   - Use git effectively
   - Implement CI/CD
   - Review code regularly
   - Keep dependencies updated

4. Productivity
   - Learn keyboard shortcuts
   - Use snippets
   - Automate common tasks
   - Master debugging tools

Remember to:
1. Keep your development environment clean
2. Stay updated with Python features
3. Use appropriate tools for each task
4. Follow security best practices
5. Maintain good documentation 