---
category: Developer
description: A comprehensive guide for building modern web applications using HTMX,
  focusing on best practices, progressive enhancement, and server-side integration.
model: GPT-4
path: developer/frameworks/htmx/htmx-development-guide
prompt_type: Instruction-based prompting
tags:
- htmx
- web-development
- javascript
- html
- frontend
- best-practices
title: HTMX Development Guide
version: '1.0'
---

# HTMX Development Guide

## Overview
This guide provides best practices and patterns for modern web development using HTMX, a powerful library that allows you to access modern browser features directly from HTML, rather than using JavaScript.

## Core Technologies
- HTMX (latest version)
- HTML5 with semantic markup
- Server-side templating (Jinja2, Handlebars)
- CSS for styling
- Optional JavaScript for enhancements

## Project Structure
```
src/
  templates/          # Server-side templates
    layouts/          # Base templates and layouts
    components/       # Reusable HTMX components
    pages/           # Page-specific templates
  static/
    css/             # Stylesheets
    js/              # Optional JavaScript enhancements
    htmx/            # HTMX extensions
  app.py             # Server application
```

## HTMX Best Practices

### Basic Attributes
```html
<!-- GET Request Example -->
<button hx-get="/api/data"
        hx-target="#result"
        hx-swap="outerHTML"
        hx-trigger="click">
  Load Data
</button>

<!-- POST Request Example -->
<form hx-post="/api/submit"
      hx-target="#response"
      hx-swap="innerHTML"
      hx-indicator="#loading">
  <input type="text" name="username" required>
  <button type="submit">Submit</button>
  <div id="loading" class="htmx-indicator">Loading...</div>
</form>
```

### CSRF Protection
```html
<!-- Add CSRF Token to Headers -->
<meta name="csrf-token" content="{{ csrf_token }}">
<script>
  document.body.addEventListener('htmx:configRequest', function(evt) {
    evt.detail.headers['X-CSRF-Token'] = document.querySelector('meta[name="csrf-token"]').content;
  });
</script>
```

### Loading States
```html
<!-- Using Indicators -->
<div hx-get="/api/data"
     hx-trigger="load"
     hx-indicator="#spinner">
  <div id="spinner" class="htmx-indicator">
    <div class="spinner"></div>
  </div>
  <div class="content"></div>
</div>

<style>
.htmx-indicator {
  display: none;
}
.htmx-request .htmx-indicator {
  display: block;
}
.htmx-request.htmx-indicator {
  display: block;
}
</style>
```

### Progressive Enhancement
```html
<!-- Basic Form with Progressive Enhancement -->
<form action="/submit" method="post"
      hx-post="/submit"
      hx-target="#response"
      hx-swap="outerHTML">
  <!-- Works without JavaScript -->
  <input type="text" name="query" required>
  <button type="submit">Search</button>
</form>

<!-- Enhanced Navigation -->
<a href="/page"
   hx-get="/page"
   hx-push-url="true"
   hx-target="body">
  Navigate with HTMX
</a>
```

### Server-Side Integration (Python/Flask Example)
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    # Check if request is HTMX
    is_htmx = request.headers.get('HX-Request') == 'true'
    
    if is_htmx:
        # Return partial template for HTMX request
        return render_template('partials/data.html', data=data)
    
    # Return full page for regular request
    return render_template('pages/data.html', data=data)
```

### Error Handling
```html
<!-- Client-side Error Handling -->
<div hx-get="/api/data"
     hx-trigger="load"
     hx-target="#content"
     hx-error-target="#error"
     hx-on::after-request="handleError(event)">
  <div id="content"></div>
  <div id="error"></div>
</div>

<script>
function handleError(event) {
  if (event.detail.failed) {
    console.error('Request failed:', event.detail.error);
  }
}
</script>
```

## HTMX Extensions

### Using Extensions
```html
<!-- Include Extension -->
<script src="/static/htmx/ext/json-enc.js"></script>

<!-- Use Extension in Element -->
<form hx-post="/api/submit"
      hx-ext="json-enc">
  <input type="text" name="data">
  <button type="submit">Submit as JSON</button>
</form>
```

### Common Extensions
1. `json-enc` - JSON encoding of form data
2. `loading-states` - Advanced loading state management
3. `morphdom-swap` - Enhanced content swapping
4. `client-side-templates` - Client-side templating
5. `path-deps` - Path-based dependencies

## Performance Optimization

### Request Optimization
```html
<!-- Debounce Input -->
<input type="text"
       name="search"
       hx-get="/api/search"
       hx-trigger="keyup changed delay:500ms"
       hx-target="#search-results">

<!-- Cache GET Requests -->
<div hx-get="/api/data"
     hx-trigger="load"
     hx-target="#content"
     hx-cache="true">
</div>
```

### Content Swapping
```html
<!-- Efficient Content Updates -->
<div hx-get="/api/updates"
     hx-trigger="every 10s"
     hx-target="find .content"
     hx-select=".updated-content"
     hx-swap="outerHTML">
  <div class="content">
    <!-- Content to be updated -->
  </div>
</div>
```

## Resources
- [HTMX Documentation](https://htmx.org/docs/)
- [HTMX Examples](https://htmx.org/examples/)
- [HTMX Extensions](https://htmx.org/extensions/)
- [HTMX Server-Side Integration](https://htmx.org/server-side/)
- [HTMX Discord Community](https://htmx.org/discord)