---
description: Comprehensive guide for integrating HTMX with Go backends, focusing on
  best practices and common patterns
path: developer/frameworks/htmx/htmx-go-integration-guide.md
prompt_type: Instruction-based prompting
tags:
- htmx
- go
- web-development
- backend
- integration
title: HTMX and Go Integration Guide
---

# HTMX and Go Integration Guide

## Overview
This guide demonstrates how to effectively integrate HTMX with Go backends to create dynamic, server-driven web applications with minimal JavaScript.

## Setup

### 1. Go Project Structure
```go
project/
├── main.go
├── handlers/
│   └── htmx_handlers.go
├── templates/
│   └── *.html
└── static/
    └── htmx.min.js
```

### 2. Basic Go Server Setup
```go
package main

import (
    "html/template"
    "log"
    "net/http"
)

func main() {
    mux := http.NewServeMux()
    
    // Serve static files
    fs := http.FileServer(http.Dir("static"))
    mux.Handle("/static/", http.StripPrefix("/static/", fs))
    
    // Setup routes
    mux.HandleFunc("/", handleHome)
    
    log.Fatal(http.ListenAndServe(":8080", mux))
}
```

## Common Patterns

### 1. Partial Template Rendering
```go
func handlePartial(w http.ResponseWriter, r *http.Request) {
    tmpl := template.Must(template.ParseFiles("templates/partial.html"))
    data := map[string]interface{}{
        "Items": []string{"Item 1", "Item 2", "Item 3"},
    }
    tmpl.Execute(w, data)
}
```

### 2. Form Handling
```go
func handleForm(w http.ResponseWriter, r *http.Request) {
    if r.Method != "POST" {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }
    
    // Parse form
    err := r.ParseForm()
    if err != nil {
        http.Error(w, "Error parsing form", http.StatusBadRequest)
        return
    }
    
    // Process form data
    name := r.FormValue("name")
    
    // Return partial template
    tmpl := template.Must(template.ParseFiles("templates/response.html"))
    tmpl.Execute(w, map[string]string{"name": name})
}
```

### 3. Dynamic Content Loading
```go
func handleDynamicContent(w http.ResponseWriter, r *http.Request) {
    // Add HTMX-specific headers
    w.Header().Set("HX-Trigger", "contentLoaded")
    
    tmpl := template.Must(template.ParseFiles("templates/dynamic.html"))
    data := fetchDynamicData()
    tmpl.Execute(w, data)
}
```

## Best Practices

### 1. Response Headers
```go
// Helper function for HTMX responses
func htmxResponse(w http.ResponseWriter) {
    w.Header().Set("Content-Type", "text/html; charset=utf-8")
    // Optional HTMX-specific headers
    w.Header().Set("HX-Push-Url", "false")
}
```

### 2. Error Handling
```go
func handleWithHTMXError(w http.ResponseWriter, err error) {
    w.Header().Set("HX-Retarget", "#error-message")
    w.Header().Set("HX-Reswap", "innerHTML")
    w.WriteHeader(http.StatusBadRequest)
    tmpl := template.Must(template.ParseFiles("templates/error.html"))
    tmpl.Execute(w, map[string]string{"error": err.Error()})
}
```

### 3. Middleware
```go
func htmxMiddleware(next http.HandlerFunc) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        // Check if request is from HTMX
        if r.Header.Get("HX-Request") == "true" {
            // Handle HTMX-specific logic
        }
        next(w, r)
    }
}
```

## Advanced Patterns

### 1. Server-Sent Events
```go
func handleSSE(w http.ResponseWriter, r *http.Request) {
    // Set headers for SSE
    w.Header().Set("Content-Type", "text/event-stream")
    w.Header().Set("Cache-Control", "no-cache")
    w.Header().Set("Connection", "keep-alive")
    
    // Send events
    for {
        fmt.Fprintf(w, "data: %s\n\n", time.Now().String())
        w.(http.Flusher).Flush()
        time.Sleep(1 * time.Second)
    }
}
```

### 2. WebSocket Integration
```go
func handleWebSocket(w http.ResponseWriter, r *http.Request) {
    upgrader := websocket.Upgrader{
        ReadBufferSize:  1024,
        WriteBufferSize: 1024,
    }
    
    conn, err := upgrader.Upgrade(w, r, nil)
    if err != nil {
        log.Println(err)
        return
    }
    defer conn.Close()
    
    // Handle WebSocket communication
}
```

## Security Considerations

1. CSRF Protection
```go
func csrfMiddleware(next http.HandlerFunc) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        // Verify CSRF token
        if !verifyCSRFToken(r) {
            http.Error(w, "Invalid CSRF token", http.StatusForbidden)
            return
        }
        next(w, r)
    }
}
```

2. Input Validation
```go
func validateInput(input string) error {
    if len(input) > 100 {
        return errors.New("input too long")
    }
    // Add more validation rules
    return nil
}
```

## Performance Optimization

1. Template Caching
```go
var templates = template.Must(template.ParseGlob("templates/*.html"))

func renderTemplate(w http.ResponseWriter, name string, data interface{}) {
    templates.ExecuteTemplate(w, name, data)
}
```

2. Response Compression
```go
func compressionMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if strings.Contains(r.Header.Get("Accept-Encoding"), "gzip") {
            gz := gzip.NewWriter(w)
            defer gz.Close()
            w.Header().Set("Content-Encoding", "gzip")
            next.ServeHTTP(gzipResponseWriter{ResponseWriter: w, Writer: gz}, r)
            return
        }
        next.ServeHTTP(w, r)
    })
}
```

## Testing

1. Handler Testing
```go
func TestHTMXHandler(t *testing.T) {
    req := httptest.NewRequest("GET", "/", nil)
    req.Header.Set("HX-Request", "true")
    w := httptest.NewRecorder()
    
    handler := http.HandlerFunc(handleHome)
    handler.ServeHTTP(w, req)
    
    if w.Code != http.StatusOK {
        t.Errorf("Expected status %d, got %d", http.StatusOK, w.Code)
    }
}
```

## Deployment Considerations

1. Environment Configuration
2. Logging Setup
3. Monitoring Integration
4. Error Tracking
5. Performance Metrics

Remember to always follow Go best practices and security guidelines when implementing these patterns. 