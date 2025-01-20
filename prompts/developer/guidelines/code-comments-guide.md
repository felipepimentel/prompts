---
title: Code Comments Guide
path: developer/guidelines/code-comments-guide.md
tags:
  - documentation
  - best-practices
  - code-quality
  - readability
  - maintenance
description: Comprehensive guide for writing effective code comments, focusing on best practices, documentation standards, and maintainability
---

# Code Comments Guide

## Overview
This guide provides a structured approach to writing effective code comments that enhance code readability, maintainability, and collaboration.

## Comment Types

### 1. File Headers
```python
"""
Module: user_service.py
Description: Handles user-related operations and authentication
Author: John Doe <john@example.com>
Created: 2024-01-15
Updated: 2024-02-01

This module provides functionality for user management, including:
- User registration and authentication
- Profile management
- Permission handling
- Session management

Dependencies:
- auth_service.py
- database.py
"""
```

### 2. Class Documentation
```python
class UserManager:
    """
    Manages user operations and authentication.

    This class provides a centralized interface for handling user-related
    operations, including registration, authentication, and profile management.

    Attributes:
        db_connection: Database connection instance
        auth_service: Authentication service instance
        cache: Cache manager for user data

    Example:
        >>> manager = UserManager(db, auth, cache)
        >>> user = manager.register_user("john@example.com", "password123")
        >>> is_valid = manager.authenticate_user("john@example.com", "password123")
    """
```

### 3. Function Documentation
```python
def process_user_data(
    user_data: dict,
    validate: bool = True,
    update_existing: bool = False
) -> User:
    """
    Process and validate user data before storage.

    Args:
        user_data: Dictionary containing user information
            Required keys: email, username
            Optional keys: full_name, avatar_url
        validate: Whether to validate data before processing
        update_existing: Whether to update existing user record

    Returns:
        User: Processed user instance

    Raises:
        ValidationError: If user data is invalid
        DuplicateError: If user already exists and update_existing is False

    Example:
        >>> data = {"email": "john@example.com", "username": "john_doe"}
        >>> user = process_user_data(data, validate=True)
    """
```

### 4. Implementation Comments
```python
def calculate_metrics(data: List[float]) -> Dict[str, float]:
    # Initialize result dictionary with default values
    result = {"mean": 0.0, "std": 0.0, "min": 0.0, "max": 0.0}
    
    if not data:
        return result  # Return defaults for empty input
    
    # Calculate basic statistics
    n = len(data)
    total = sum(data)
    mean = total / n
    
    # Calculate standard deviation using two-pass algorithm
    # First pass: calculate mean (done above)
    # Second pass: calculate sum of squared differences
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    std = (squared_diff_sum / n) ** 0.5
    
    return {
        "mean": mean,
        "std": std,
        "min": min(data),
        "max": max(data)
    }
```

### 5. Inline Comments
```python
def validate_password(password: str) -> bool:
    # Check minimum length requirement
    if len(password) < 8:
        return False
    
    # Must contain at least one uppercase letter
    if not any(c.isupper() for c in password):
        return False
    
    # Must contain at least one lowercase letter
    if not any(c.islower() for c in password):
        return False
    
    # Must contain at least one digit
    if not any(c.isdigit() for c in password):
        return False
    
    # Must contain at least one special character
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        return False
    
    return True  # All requirements met
```

## Documentation Standards

### 1. Type Hints and Docstrings
```python
from typing import Optional, List, Dict, Any

def fetch_user_data(
    user_id: str,
    fields: Optional[List[str]] = None,
    include_private: bool = False
) -> Dict[str, Any]:
    """
    Fetch user data from the database.

    Retrieves user information based on the specified fields. If no fields
    are provided, returns all public fields by default.

    Args:
        user_id: Unique identifier for the user
        fields: List of specific fields to retrieve (optional)
        include_private: Whether to include private user data

    Returns:
        Dictionary containing requested user data

    Raises:
        UserNotFoundError: If user_id does not exist
        PermissionError: If requesting private data without proper authorization
    """
```

### 2. Code Examples
```python
class DataProcessor:
    """
    Process and transform data according to specified rules.

    Example:
        Basic usage:
        >>> processor = DataProcessor()
        >>> data = [1, 2, 3, 4, 5]
        >>> result = processor.process(data)
        >>> print(result)
        [2, 4, 6, 8, 10]

        With custom transformation:
        >>> def square(x): return x * x
        >>> result = processor.process(data, transform=square)
        >>> print(result)
        [1, 4, 9, 16, 25]
    """
```

## Best Practices

### 1. Comment Organization
```python
class APIClient:
    """
    Client for interacting with the REST API.
    
    # Architecture Overview
    This client implements the repository pattern and handles:
    - Authentication
    - Request/response processing
    - Error handling
    - Rate limiting
    
    # Usage Guidelines
    1. Initialize with API credentials
    2. Use context manager for automatic cleanup
    3. Handle exceptions appropriately
    
    # Example
    ```python
    with APIClient(credentials) as client:
        data = client.fetch_data()
        client.process_data(data)
    ```
    """
```

### 2. TODO Comments
```python
def process_image(image_path: str) -> bytes:
    """Process and optimize image for web display."""
    # TODO: Implement image resizing (Issue #123)
    # TODO: Add WebP conversion support
    # TODO: Implement metadata stripping
    
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    # FIXME: Memory usage grows with large images
    return image_data
```

## Best Practices

1. Comment Content
   - Explain why, not what
   - Keep comments current
   - Use clear language
   - Add examples when helpful

2. Documentation
   - Use consistent format
   - Include type hints
   - Document exceptions
   - Provide examples

3. Maintenance
   - Update with code changes
   - Remove obsolete comments
   - Fix incorrect comments
   - Keep TODOs current

4. Style
   - Use proper grammar
   - Be concise but clear
   - Follow team standards
   - Maintain consistency

Remember to:
1. Write meaningful comments
2. Keep comments up to date
3. Document complex logic
4. Include usage examples
5. Follow team standards 