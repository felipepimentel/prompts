---
title: "Code Security Review Template"
path: "developer/security/code-security-review"
tags: ["security", "code-review", "vulnerabilities", "best-practices"]
description: "A comprehensive guide for conducting security reviews of code to identify and mitigate potential vulnerabilities"
prompt_type: "Security Framework"
---

<purpose>
To provide a structured approach for reviewing code security, identifying potential vulnerabilities, and implementing appropriate security measures.
</purpose>

<context>
Use this template when conducting security reviews of code to ensure thorough coverage of common security concerns and best practices.
</context>

<instructions>
Provide the following review information:

1. Code Overview
   - Basic Information
     * Code type/language
     * Framework/platform
     * Dependencies
     * Security context

   - Application Scope
     * Functionality
     * Data handling
     * User interaction
     * External interfaces

2. Vulnerability Categories
   - Injection Flaws
     * SQL injection
     * Command injection
     * NoSQL injection
     * Template injection

   - Authentication Issues
     * Session management
     * Password handling
     * Token security
     * Access control

3. Data Security
   - Sensitive Data
     * Data encryption
     * Data storage
     * Data transmission
     * Key management

   - Input/Output
     * Input validation
     * Output encoding
     * File handling
     * Error handling

4. Implementation Security
   - Configuration
     * Security settings
     * Environment vars
     * Default values
     * Error messages

   - Dependencies
     * Version security
     * Known vulnerabilities
     * Update strategy
     * Security patches

</instructions>

<variables>
- code_language: Programming language
- security_context: Security requirements
- data_sensitivity: Data classification
- compliance_needs: Compliance requirements
</variables>

<examples>
Example 1:
Input: Web application security review
Output:
```markdown
# Security Review Report

## Application Overview
- **Type:** Web Application
- **Language:** Python/Django
- **Data Sensitivity:** High (handles financial data)
- **User Base:** Public access

## Vulnerability Analysis

### 1. SQL Injection Risk
#### Code Sample
```python
# Vulnerable Code
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)

# Secure Alternative
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = %s"
    return db.execute(query, [user_id])
```

#### Risk Assessment
- **Severity:** High
- **Likelihood:** High
- **Impact:** Data breach, unauthorized access
- **CVSS Score:** 9.8

#### Mitigation Steps
1. Use parameterized queries
2. Implement input validation
3. Apply proper escaping
4. Use ORM when possible

### 2. Authentication Weakness
#### Code Sample
```python
# Vulnerable Code
def verify_password(password, hash):
    return md5(password) == hash

# Secure Alternative
def verify_password(password, hash):
    return pwd_context.verify(password, hash)
```

#### Risk Assessment
- **Severity:** Critical
- **Likelihood:** Medium
- **Impact:** Account compromise
- **CVSS Score:** 8.5

#### Mitigation Steps
1. Use secure hashing (Argon2, bcrypt)
2. Implement password policies
3. Add rate limiting
4. Enable MFA

### 3. Sensitive Data Exposure
#### Code Sample
```python
# Vulnerable Code
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Secure Alternative
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }
```

#### Risk Assessment
- **Severity:** High
- **Likelihood:** Medium
- **Impact:** Data leak
- **CVSS Score:** 7.5

#### Mitigation Steps
1. Explicitly define serialized fields
2. Implement data masking
3. Use encryption for sensitive data
4. Apply proper access controls

## Security Recommendations

### Immediate Actions
1. Update dependency versions
2. Implement input validation
3. Enable security headers
4. Add CSRF protection

### Long-term Improvements
1. Implement security monitoring
2. Regular security training
3. Automated security testing
4. Security documentation
```

Example 2:
Input: API security review
Output:
```markdown
# API Security Review

## Service Overview
- **Type:** REST API
- **Framework:** Node.js/Express
- **Authentication:** JWT
- **Data:** Customer records

## Security Analysis

### 1. Authentication Security
#### Code Sample
```javascript
// Vulnerable Code
const jwt = require('jsonwebtoken');

app.post('/login', (req, res) => {
  const token = jwt.sign(
    { userId: user.id },
    'secret-key'
  );
  res.json({ token });
});

// Secure Alternative
const jwt = require('jsonwebtoken');

app.post('/login', (req, res) => {
  const token = jwt.sign(
    { 
      userId: user.id,
      sessionId: generateSessionId()
    },
    process.env.JWT_SECRET,
    {
      expiresIn: '1h',
      algorithm: 'RS256'
    }
  );
  res.json({ token });
});
```

#### Risk Assessment
- **Severity:** Critical
- **Likelihood:** High
- **Impact:** Session hijacking
- **CVSS Score:** 9.0

#### Security Measures
1. Use environment variables
2. Implement token expiration
3. Use strong algorithms
4. Add refresh token rotation

### 2. Rate Limiting
#### Code Sample
```javascript
// Vulnerable Setup
app.use(express.json());

// Secure Implementation
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  message: 'Too many requests'
});

app.use('/api/', limiter);
```

#### Risk Assessment
- **Severity:** Medium
- **Likelihood:** High
- **Impact:** DoS vulnerability
- **CVSS Score:** 6.5

#### Security Measures
1. Implement rate limiting
2. Add request throttling
3. Monitor usage patterns
4. Set up alerting

## Security Checklist

### Headers and Configuration
- [ ] Use Helmet.js
- [ ] Enable CORS properly
- [ ] Set secure cookies
- [ ] Configure CSP

### Input Validation
- [ ] Sanitize all inputs
- [ ] Validate request body
- [ ] Check content types
- [ ] Limit payload size

### Error Handling
- [ ] Use custom error handler
- [ ] Hide stack traces
- [ ] Log securely
- [ ] Return safe errors
```
</examples>

<notes>
- Check all inputs
- Validate authentication
- Encrypt sensitive data
- Use secure dependencies
- Follow best practices
- Document security measures
- Test security controls
- Monitor for issues
</notes> 