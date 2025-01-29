---
title: "Class/Module Design Template"
path: "developer/guidelines/class-design"
tags: ["oop", "class-design", "code-structure", "best-practices"]
description: "A template for creating well-structured classes and modules with proper OOP principles and documentation"
prompt_type: "Template-Based"
---

<purpose>
To provide a structured template for creating well-designed classes and modules that follow object-oriented programming principles.
</purpose>

<context>
Use this prompt when you need to create a new class or module and want to ensure it follows best practices in terms of structure, documentation, and object-oriented design.
</context>

<instructions>
Create a [class/module] for [specific functionality] in [programming language] following these guidelines:

1. Constructor/Initialization
   - Define required parameters and their types
   - Initialize instance variables
   - Add validation if necessary

2. Main Public Methods
   - Include clear method signatures
   - Write comprehensive docstrings
   - Define parameter types and return types
   - Document exceptions/error cases

3. Private Helper Methods
   - Implement necessary utility functions
   - Keep methods focused and single-purpose
   - Use appropriate naming conventions

4. Object-Oriented Principles
   - Ensure proper encapsulation
   - Follow SOLID principles
   - Implement appropriate inheritance/composition
   - Define clear interfaces

Include comprehensive documentation and type hints where applicable.
</instructions>

<variables>
- class_name: Name of the class or module
- functionality: Specific purpose or functionality
- language: Target programming language
- dependencies: Required external dependencies or imports
</variables>

<examples>
Example 1:
Input: Create a UserManager class in Python for handling user authentication
Output:
```python
class UserManager:
    def __init__(self, db_connection):
        self._db = db_connection
        self._active_users = {}
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate a user with given credentials."""
        # Implementation
```

Example 2:
Input: Create a DataProcessor module in TypeScript for CSV handling
Output:
```typescript
class DataProcessor {
    private readonly filePath: string;
    
    constructor(filePath: string) {
        this.filePath = filePath;
    }
    
    public async processData(): Promise<ProcessedData> {
        // Implementation
    }
}
```
</examples>

<notes>
- Follow language-specific conventions and best practices
- Consider performance implications of design choices
- Include error handling and edge cases
- Write clear and maintainable code
- Consider thread safety if applicable
</notes>