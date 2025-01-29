---
title: "SQL Injection Security Review Guide"
path: "developer/security/sql-injection"
tags: ["security", "sql", "database", "code-review", "best-practices"]
description: "A comprehensive guide for identifying and fixing SQL injection vulnerabilities in database interaction code"
prompt_type: "Security Analysis Framework"
---

<purpose>
To assist in identifying and remedying SQL injection vulnerabilities in database interaction code while promoting secure coding practices.
</purpose>

<context>
Use this guide when reviewing database interaction code for security vulnerabilities, particularly SQL injection risks, or when implementing new database queries.
</context>

<instructions>
Review the provided database interaction code:
[Paste your database interaction code]

Analyze for the following security concerns:

1. Input Validation
   - Direct string concatenation
   - Dynamic SQL generation
   - User input handling
   - Type conversion issues
   - Character encoding risks

2. Query Construction
   - Parameterized queries usage
   - Stored procedures implementation
   - Dynamic SQL alternatives
   - Query builder patterns
   - ORM integration

3. Access Control
   - User privilege levels
   - Database user permissions
   - Connection pooling security
   - Resource limitations
   - Transaction isolation

4. Common Vulnerabilities
   - UNION-based injection
   - Boolean-based injection
   - Time-based injection
   - Error-based injection
   - Second-order injection

For each identified vulnerability:
1. Risk Assessment
   - Attack vector description
   - Potential impact
   - Exploitation difficulty
   - Detection methods

2. Secure Implementation
   - Code refactoring approach
   - Security library usage
   - Best practice implementation
   - Testing methodology

3. Prevention Strategies
   - Input sanitization methods
   - Query parameterization
   - Error handling
   - Logging and monitoring
</instructions>

<variables>
- database_code: Code to review
- database_type: Type of database system
- framework: Development framework in use
- security_libraries: Available security tools
</variables>

<examples>
Example 1:
Input: Direct string concatenation
```python
query = "SELECT * FROM users WHERE username = '" + username + "'"
```
Output:
```python
# Using parameterized query
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```

Example 2:
Input: Dynamic SQL generation
```javascript
const query = `DELETE FROM orders WHERE id = ${orderId}`;
```
Output:
```javascript
// Using prepared statement
const query = 'DELETE FROM orders WHERE id = ?';
await db.execute(query, [orderId]);
```
</examples>

<notes>
- Always use parameterized queries
- Implement proper input validation
- Use appropriate security libraries
- Follow principle of least privilege
- Implement proper error handling
- Consider using ORMs when appropriate
- Maintain security patches and updates
</notes>