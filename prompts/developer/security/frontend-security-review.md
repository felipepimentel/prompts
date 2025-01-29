---
title: "Frontend Security Review Guide"
path: "developer/security/frontend-security-review"
tags: ["security", "frontend", "web", "best-practices"]
description: "A comprehensive guide for reviewing and improving frontend code security through best practices and preventive measures"
prompt_type: "Security Framework"
---

<purpose>
To provide a structured approach for reviewing frontend code security, identifying vulnerabilities, and implementing appropriate security measures.
</purpose>

<context>
Use this guide when reviewing frontend code for security vulnerabilities or implementing security best practices in web applications.
</context>

<instructions>
Provide the following information:

1. Code Overview
   - Application Details
     * Frontend framework
     * Libraries used
     * Authentication method
     * API integration approach

   - Security Context
     * Sensitive data handling
     * User input processing
     * External integrations
     * Asset management

2. Security Analysis
   - XSS Prevention
     * Input sanitization
     * Output encoding
     * Content Security Policy
     * Framework protections

   - Data Protection
     * Sensitive data handling
     * Local storage usage
     * Session management
     * Form security

3. Communication Security
   - API Security
     * Authentication tokens
     * Request validation
     * Error handling
     * CORS configuration

   - CSRF Protection
     * Token implementation
     * Cookie security
     * Request validation
     * Framework features

4. Implementation Review
   - Security Features
     * Authentication flow
     * Authorization checks
     * Input validation
     * Error handling

   - Best Practices
     * Dependency security
     * Code minification
     * Asset integrity
     * Security headers

</instructions>

<variables>
- frontend_framework: Framework and version
- authentication_method: Authentication approach
- api_integration: API communication method
- security_requirements: Specific security needs
</variables>

<examples>
Example 1:
Input: React application with JWT authentication
Output:
```javascript
// Security Improvements

// 1. XSS Prevention
// Use React's built-in XSS protection
const UserInput = ({ content }) => {
  // Safe: React automatically escapes content
  return <div>{content}</div>;
};

// For cases where you need dangerouslySetInnerHTML
const SafeHTML = ({ content }) => {
  const sanitizedContent = DOMPurify.sanitize(content);
  return <div dangerouslySetInnerHTML={{ __html: sanitizedContent }} />;
};

// 2. Secure Data Handling
// Store sensitive data in memory, not localStorage
const useSecureState = () => {
  const [token, setToken] = useState(null);
  
  const secureLogin = async (credentials) => {
    try {
      const response = await api.post('/login', credentials);
      setToken(response.data.token); // Stored in memory only
    } catch (error) {
      console.error('Login failed:', error);
    }
  };
  
  return { token, secureLogin };
};

// 3. CSRF Protection
// Add CSRF token to API requests
const api = axios.create({
  baseURL: '/api',
  headers: {
    'X-CSRF-Token': document.querySelector('meta[name="csrf-token"]').content
  }
});

// 4. Secure API Communication
const secureApiCall = async () => {
  try {
    const response = await api.get('/data', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      // Validate response type
      responseType: 'json'
    });
    return response.data;
  } catch (error) {
    // Secure error handling
    console.error('API error:', error.message);
    throw new Error('An error occurred');
  }
};
```

Example 2:
Input: Vue.js application with OAuth
Output:
```javascript
// Security Implementation

// 1. Content Security Policy
// Add CSP meta tag
const SecurityHeaders = {
  template: `
    <meta http-equiv="Content-Security-Policy" 
          content="default-src 'self'; 
                   script-src 'self' 'unsafe-inline' 'unsafe-eval'; 
                   style-src 'self' 'unsafe-inline';">
  `
};

// 2. Secure Input Handling
const SecureForm = {
  data() {
    return {
      input: '',
      errors: []
    };
  },
  methods: {
    validateInput(value) {
      // Input validation
      const sanitized = this.$sanitize(value);
      if (sanitized !== value) {
        this.errors.push('Invalid characters detected');
        return false;
      }
      return true;
    },
    async submitForm() {
      if (!this.validateInput(this.input)) {
        return;
      }
      // Secure form submission
      try {
        await this.$http.post('/api/data', {
          data: this.input
        }, {
          headers: {
            'X-CSRF-Token': this.$csrf
          }
        });
      } catch (error) {
        this.handleError(error);
      }
    }
  }
};

// 3. OAuth Implementation
const auth = {
  methods: {
    async initializeAuth() {
      // Configure OAuth client
      const client = await this.$auth.initialize({
        client_id: process.env.VUE_APP_OAUTH_CLIENT_ID,
        redirect_uri: `${window.location.origin}/callback`,
        scope: 'read write',
        response_type: 'code'
      });
      
      // Secure token storage
      client.on('tokens', (tokens) => {
        // Store tokens securely in memory
        this.$auth.setTokens(tokens);
      });
    }
  }
};

// 4. Secure Router Navigation
const router = {
  beforeEach(to, from, next) {
    // Check authentication and authorization
    if (to.matched.some(record => record.meta.requiresAuth)) {
      if (!auth.isAuthenticated()) {
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        });
      } else {
        // Verify user permissions
        if (auth.hasPermission(to.meta.permission)) {
          next();
        } else {
          next({ path: '/403' });
        }
      }
    } else {
      next();
    }
  }
};
```
</examples>

<notes>
- Always sanitize user input
- Use framework security features
- Keep dependencies updated
- Implement proper CORS
- Use secure communication
- Handle errors securely
- Follow security headers
- Regular security audits
</notes> 