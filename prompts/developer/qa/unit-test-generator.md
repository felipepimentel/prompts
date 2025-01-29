---
title: "Unit Test Generator"
path: "developer/qa/unit-test-generator"
tags: ["testing", "unit-tests", "qa", "test-coverage"]
description: "A comprehensive guide for generating thorough unit tests covering normal cases, edge cases, and error handling"
prompt_type: "Code Generation Framework"
---

<purpose>
To assist in creating comprehensive unit tests that ensure code reliability and proper handling of various scenarios.
</purpose>

<context>
Use this prompt when you need to generate unit tests for functions or classes, ensuring thorough test coverage and proper error handling.
</context>

<instructions>
Generate unit tests for the following function:
[paste function here]

Create test cases covering these categories:

1. Normal Case Testing
   - Test with typical expected inputs
   - Verify expected outputs
   - Test different valid input combinations
   - Verify state changes if applicable

2. Edge Case Testing
   - Boundary values
   - Empty/null inputs
   - Minimum/maximum values
   - Type limits
   - Resource limits

3. Error Case Testing
   - Invalid inputs
   - Malformed data
   - Out-of-range values
   - Type mismatches
   - Resource unavailability

4. Integration Points
   - Mock dependencies
   - Stub external services
   - Test async behavior
   - Verify callbacks/promises

Use [preferred testing framework] syntax and follow testing best practices:
- Clear test descriptions
- Proper setup and teardown
- Meaningful assertions
- Isolated tests
</instructions>

<variables>
- function_code: The function/class to test
- testing_framework: Preferred testing framework
- language: Programming language
- dependencies: Required testing libraries/tools
</variables>

<examples>
Example 1:
Input: String validation function
```javascript
function validateEmail(email) {
    // Implementation
}
```
Output:
```javascript
describe('validateEmail', () => {
    test('valid email returns true', () => {
        expect(validateEmail('user@example.com')).toBe(true);
    });
    
    test('invalid email returns false', () => {
        expect(validateEmail('invalid-email')).toBe(false);
    });
    
    test('empty string returns false', () => {
        expect(validateEmail('')).toBe(false);
    });
});
```

Example 2:
Input: Number processing function
```python
def calculate_average(numbers):
    // Implementation
```
Output:
```python
def test_calculate_average():
    assert calculate_average([1, 2, 3]) == 2
    assert calculate_average([]) == 0
    with pytest.raises(TypeError):
        calculate_average(None)
```
</examples>

<notes>
- Follow testing framework conventions
- Ensure tests are maintainable
- Include meaningful error messages
- Consider performance implications
- Document test assumptions
- Use appropriate test doubles
</notes>