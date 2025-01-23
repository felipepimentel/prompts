---
description: Comprehensive guide for building modern web applications with HTMX, focusing
  on basic concepts and best practices
path: developer/frameworks/htmx/htmx-basic-development-guide.md
prompt_type: Instruction-based prompting
tags:
- htmx
- web-development
- javascript
- frontend
title: HTMX Basic Development Guide
---

# HTMX Basic Development Guide

## Overview
This guide provides instructions for developing web applications using HTMX, a modern approach to building dynamic web interfaces without heavy JavaScript frameworks.

## Key Concepts

### 1. HTMX Attributes
- `hx-get`: Make GET request
- `hx-post`: Make POST request
- `hx-put`: Make PUT request
- `hx-delete`: Make DELETE request
- `hx-trigger`: Define when to trigger the request
- `hx-target`: Where to place the response
- `hx-swap`: How to swap the response

### 2. Basic Setup
```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
</head>
<body>
    <!-- Your HTMX-enhanced HTML here -->
</body>
</html>
```

### 3. Common Patterns

#### Simple Button Click
```html
<button hx-post="/api/action" 
        hx-trigger="click"
        hx-target="#result">
    Click Me
</button>
<div id="result"></div>
```

#### Form Submission
```html
<form hx-post="/api/submit" 
      hx-target="#response">
    <input type="text" name="username">
    <button type="submit">Submit</button>
</form>
<div id="response"></div>
```

#### Dynamic Loading
```html
<div hx-get="/api/data" 
     hx-trigger="load"
     hx-swap="outerHTML">
    Loading...
</div>
```

## Best Practices

1. Progressive Enhancement
   - Always provide fallback behavior for non-JavaScript environments
   - Use semantic HTML elements
   - Ensure core functionality works without HTMX

2. Performance Optimization
   - Use appropriate swap strategies
   - Implement proper caching headers
   - Minimize payload size

3. Error Handling
   - Implement proper error responses
   - Provide user feedback
   - Handle network failures gracefully

4. Security Considerations
   - Validate all inputs server-side
   - Implement CSRF protection
   - Use appropriate Content Security Policy

## Common Use Cases

1. Infinite Scroll
```html
<div hx-get="/api/more" 
     hx-trigger="revealed"
     hx-swap="beforeend">
    <!-- Content -->
</div>
```

2. Live Search
```html
<input type="search" 
       name="q" 
       hx-get="/api/search" 
       hx-trigger="keyup changed delay:500ms"
       hx-target="#search-results">
<div id="search-results"></div>
```

3. Form Validation
```html
<input type="text" 
       name="email" 
       hx-get="/api/validate/email" 
       hx-trigger="change"
       hx-target="next .error">
<div class="error"></div>
```

## Debugging Tips

1. Use `htmx.logAll()` for debugging
2. Check Network tab in DevTools
3. Verify response headers
4. Test with different swap strategies

## Integration Guidelines

1. Backend Integration
   - Return HTML fragments
   - Use proper status codes
   - Implement proper headers

2. CSS Integration
   - Use transition classes
   - Implement loading states
   - Handle swap animations

3. JavaScript Integration
   - Use event listeners
   - Implement custom extensions
   - Handle edge cases

## Resources

1. Official Documentation
2. Community Examples
3. Best Practices Guide
4. Security Guidelines

## Troubleshooting

1. Common Issues
2. Solutions
3. Performance Optimization
4. Browser Compatibility

Remember to always test thoroughly and follow web standards for the best user experience. 