---
title: "Git Merge Conflict Resolution Guide"
path: "developer/git/merge-conflict"
tags: ["git", "version-control", "collaboration", "conflict-resolution"]
description: "A systematic approach to analyzing and resolving Git merge conflicts while maintaining code integrity"
prompt_type: "Problem-Solving Framework"
---

<purpose>
To provide a structured approach for analyzing and resolving Git merge conflicts while ensuring code functionality and maintaining project integrity.
</purpose>

<context>
Use this guide when encountering merge conflicts in Git and needing to determine the best resolution strategy while understanding the implications.
</context>

<instructions>
Provide the following information about the merge conflict:

1. Conflict Details
   - Conflicting code sections
   ```
   <<<<<<<< HEAD
   [Current branch code]
   ========
   [Incoming branch code]
   >>>>>>>> feature-branch
   ```
   - Feature purpose/context
   - Related functionality

2. Analysis Process
   - Code Comparison
     * Identify differences
     * Understand intentions
     * Check dependencies
     * Review functionality

   - Context Evaluation
     * Feature requirements
     * Business logic
     * Dependencies
     * Side effects

3. Resolution Strategy
   - Choose Approach
     * Keep current version
     * Keep incoming version
     * Combine changes
     * Create new solution

   - Implementation Steps
     * Code modification
     * Dependency updates
     * Test adjustments
     * Documentation updates

4. Verification Plan
   - Testing Strategy
     * Unit tests
     * Integration tests
     * Functionality verification
     * Regression testing

   - Review Points
     * Code style
     * Best practices
     * Performance impact
     * Security implications
</instructions>

<variables>
- conflict_code: The conflicting code sections
- feature_description: Purpose of the feature being merged
- current_version: Current branch version
- incoming_version: Incoming branch version
</variables>

<examples>
Example 1:
Input: Configuration file conflict
```git
<<<<<<< HEAD
port: 3000
debug: false
=======
port: 8080
debug: true
logging: verbose
>>>>>>> feature/logging
```
Output:
```yaml
# Combined configuration with both features
port: 3000  # Keep production port
debug: true  # Enable debug for new logging
logging: verbose  # Add new logging feature
```

Example 2:
Input: Function implementation conflict
```git
<<<<<<< HEAD
def process_data(data):
    validate_input(data)
    return transform_data(data)
=======
def process_data(data):
    if not data:
        return None
    return enhance_data(data)
>>>>>>> feature/null-check
```
Output:
```python
def process_data(data):
    # Combine null check with validation
    if not data:
        return None
    validate_input(data)
    # Combine both transformations
    processed = transform_data(data)
    return enhance_data(processed)
```
</examples>

<notes>
- Understand both versions thoroughly
- Consider all stakeholders
- Test thoroughly after resolution
- Document resolution decisions
- Update related tests
- Check for side effects
- Consider creating new tests
</notes>