---
title: "QA Testing Template"
path: "developer/testing/qa-testing-template"
tags: ["testing", "quality-assurance", "software-testing", "bug-reporting"]
description: "A comprehensive template for conducting and documenting software quality assurance testing"
prompt_type: "Testing Framework"
---

<purpose>
To provide a structured approach for conducting thorough software quality assurance testing and documenting findings in a clear, objective manner.
</purpose>

<context>
Use this template when performing QA testing on software features or applications to ensure consistent and comprehensive testing coverage.
</context>

<instructions>
Provide the following testing information:

1. Test Environment
   - System Details
     * Software version
     * Platform/OS
     * Dependencies
     * Test environment

   - Test Scope
     * Features to test
     * Test priorities
     * Excluded items
     * Prerequisites

2. Test Scenarios
   - Functionality Testing
     * Feature workflows
     * Input validation
     * Error handling
     * Edge cases

   - Performance Testing
     * Response times
     * Resource usage
     * Concurrent users
     * Load conditions

3. Test Results
   - Issue Documentation
     * Bug description
     * Steps to reproduce
     * Expected behavior
     * Actual behavior

   - Test Metrics
     * Pass/fail ratio
     * Test coverage
     * Performance data
     * Error rates

4. Recommendations
   - Improvements
     * Critical fixes
     * Enhancements
     * Optimizations
     * Best practices

   - Follow-up
     * Retesting needs
     * Regression tests
     * Documentation updates
     * Training needs

</instructions>

<variables>
- software_version: Version being tested
- test_environment: Testing environment details
- test_scope: Features under test
- tester_info: Tester name and role
</variables>

<examples>
Example 1:
Input: Login functionality testing
Output:
```markdown
# QA Test Report: Login Functionality

## Test Environment
- **Application Version:** 2.1.0
- **Browser:** Chrome 120.0, Firefox 115.0
- **OS:** Windows 11, macOS Ventura
- **Test Date:** March 15, 2024

## Test Scenarios

### 1. Standard Login Flow
#### Test Cases
1. Valid credentials login
   - Steps:
     1. Navigate to login page
     2. Enter valid username/email
     3. Enter valid password
     4. Click login button
   - Expected: Successful login, redirect to dashboard
   - Result: ✅ PASS
   - Response time: 0.8s

2. Remember Me functionality
   - Steps:
     1. Login with "Remember Me" checked
     2. Close browser
     3. Reopen application
   - Expected: Session persisted
   - Result: ✅ PASS

### 2. Input Validation
#### Test Cases
1. Empty fields validation
   - Steps:
     1. Leave username empty
     2. Leave password empty
     3. Click login
   - Expected: Appropriate error messages
   - Result: ❌ FAIL
   - Issue: No error message for empty password

2. Invalid email format
   - Steps:
     1. Enter "invalid.email"
     2. Enter password
     3. Click login
   - Expected: Email format error
   - Result: ✅ PASS

### 3. Error Handling
#### Test Cases
1. Invalid credentials
   - Steps:
     1. Enter wrong username
     2. Enter wrong password
     3. Click login
   - Expected: Generic error message
   - Result: ✅ PASS
   - Note: Error message properly vague

2. Account lockout
   - Steps:
     1. Attempt login with wrong password 5 times
   - Expected: Account temporary lock
   - Result: ⚠️ PARTIAL
   - Issue: Lock duration not displayed

## Issues Found

### Critical Issues
1. **Missing Password Validation**
   - Severity: High
   - Description: No error message when password field is empty
   - Steps to Reproduce:
     1. Enter valid username
     2. Leave password empty
     3. Click login
   - Expected: Error message for empty password
   - Actual: Form submits without validation

### Minor Issues
1. **Lock Duration Display**
   - Severity: Low
   - Description: Account lock duration not shown to user
   - Impact: User experience
   - Recommendation: Add remaining lock time to message

## Recommendations

### Immediate Actions
1. Implement password field validation
2. Add lock duration to account lockout message
3. Add client-side validation for all fields

### Future Improvements
1. Add password strength indicator
2. Implement progressive lockout times
3. Add login attempt notification emails

## Performance Metrics
- Average login time: 0.8s
- 95th percentile: 1.2s
- Error rate: 0.5%
- Test coverage: 95%
```

Example 2:
Input: Payment processing testing
Output:
```markdown
# QA Test Report: Payment Processing

## Test Environment
- **Application Version:** 3.0.0
- **Payment Gateway:** Stripe Test Environment
- **Test Cards:** Visa, Mastercard, AMEX
- **Test Date:** March 16, 2024

## Test Scenarios

### 1. Payment Methods
#### Test Cases
1. Credit Card Payment
   - Steps:
     1. Add items to cart
     2. Proceed to checkout
     3. Enter test card details
     4. Complete purchase
   - Expected: Successful payment
   - Result: ✅ PASS
   - Processing time: 1.2s

2. Saved Cards
   - Steps:
     1. Save card during checkout
     2. Attempt future purchase
   - Expected: Card available for selection
   - Result: ✅ PASS

### 2. Error Handling
#### Test Cases
1. Insufficient Funds
   - Steps:
     1. Use test card for insufficient funds
     2. Attempt purchase
   - Expected: Clear error message
   - Result: ❌ FAIL
   - Issue: Generic error shown

2. Invalid Card Number
   - Steps:
     1. Enter invalid card number
     2. Submit form
   - Expected: Immediate validation
   - Result: ✅ PASS

### 3. Security
#### Test Cases
1. Card Data Handling
   - Steps:
     1. Monitor network requests
     2. Check card data transmission
   - Expected: Encrypted transmission
   - Result: ✅ PASS
   - Note: PCI compliant

## Issues Found

### Critical Issues
1. **Insufficient Funds Error**
   - Severity: High
   - Description: Generic error for insufficient funds
   - Steps to Reproduce:
     1. Use test card 4000000000009995
     2. Attempt purchase
   - Expected: Clear insufficient funds message
   - Actual: "Transaction failed" shown

### Performance Issues
1. **Processing Time Spike**
   - Severity: Medium
   - Description: Occasional 3s+ processing time
   - Impact: User experience
   - Recommendation: Optimize API calls

## Recommendations

### Security Improvements
1. Implement 3D Secure for all transactions
2. Add fraud detection rules
3. Enhance error logging

### User Experience
1. Add clear error messages
2. Implement progress indicators
3. Add payment method icons

## Performance Metrics
- Average processing time: 1.2s
- Error rate: 0.8%
- Success rate: 98.5%
- Test coverage: 92%
```
</examples>

<notes>
- Be objective and thorough
- Document all steps
- Include environment details
- Provide clear reproduction steps
- Focus on facts, not opinions
- Include metrics when possible
- Prioritize issues properly
- Suggest specific improvements
</notes> 