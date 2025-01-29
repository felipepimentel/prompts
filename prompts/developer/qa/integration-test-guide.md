---
title: "Integration Test Design Guide"
path: "developer/qa/integration-testing"
tags: ["testing", "integration-tests", "qa", "test-design"]
description: "A comprehensive guide for designing and implementing effective integration tests for component interactions"
prompt_type: "Testing Framework"
---

<purpose>
To provide a structured approach for creating comprehensive integration tests that verify proper interaction between system components.
</purpose>

<context>
Use this guide when designing integration tests for multiple components that need to work together, ensuring proper communication and error handling.
</context>

<instructions>
Specify the components to test:
[List components and their interactions]

Design integration tests covering these aspects:

1. Component Interaction Scenarios
   - Happy Path Flows
     * Main business workflows
     * Expected data transformations
     * State transitions
     * Event propagation

   - Error Handling
     * Component failures
     * Network issues
     * Timeout scenarios
     * Resource unavailability

   - Edge Cases
     * Boundary conditions
     * Race conditions
     * Load conditions
     * Data consistency

2. Test Environment Setup
   - Dependencies Configuration
     * External services
     * Databases
     * Message queues
     * Cache systems

   - Test Data Preparation
     * Initial state setup
     * Test datasets
     * Mock data
     * Fixtures

3. Test Implementation
   - Test Structure
     * Setup procedures
     * Test execution
     * Verification steps
     * Cleanup procedures

   - Mock Objects
     * Service mocks
     * API stubs
     * Database mocks
     * Event simulators

4. Verification Strategy
   - Assertions
     * State verification
     * Behavior verification
     * Event verification
     * Data integrity checks

   - Monitoring
     * Log analysis
     * Metrics collection
     * Performance monitoring
     * Error tracking
</instructions>

<variables>
- components: List of components to test
- interactions: Component interaction patterns
- environment: Test environment requirements
- dependencies: External dependencies
</variables>

<examples>
Example 1:
Input: Order processing system with payment service
Output:
```python
def test_order_payment_integration():
    # Setup
    order = create_test_order()
    payment_service = MockPaymentService()
    
    # Test execution
    result = process_order_payment(order, payment_service)
    
    # Verification
    assert result.status == "SUCCESS"
    assert order.status == "PAID"
    assert payment_service.was_called_with(order.amount)
```

Example 2:
Input: User authentication with email service
Output:
```python
def test_user_registration_flow():
    # Setup
    email_service = MockEmailService()
    user_data = generate_test_user()
    
    # Test execution
    user = register_new_user(user_data)
    
    # Verification
    assert user.is_registered
    assert email_service.verification_email_sent
    assert user.status == "PENDING_VERIFICATION"
```
</examples>

<notes>
- Focus on component interactions
- Use realistic test data
- Consider system boundaries
- Test failure scenarios
- Monitor test performance
- Maintain test independence
- Document test assumptions
</notes>