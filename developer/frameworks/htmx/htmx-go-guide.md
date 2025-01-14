---
title: "HTMX with Go Development Guide"
path: "developer/frameworks/htmx/htmx-go-guide"
tags: ["htmx", "go", "web-development", "html", "backend", "best-practices"]
description: "A comprehensive guide for building modern web applications using HTMX with Go, focusing on server-side rendering, proper error handling, and best practices."
---

# HTMX with Go Development Guide

## Overview
This guide provides best practices and patterns for modern web development using HTMX with Go, combining Go's powerful server-side capabilities with HTMX's elegant approach to dynamic web interfaces.

## Core Technologies
- Go (1.22+)
- HTMX (latest version)
- html/template for server-side rendering
- gorilla/mux for routing (optional)
- Go modules for dependency management

## Project Structure
```
cmd/
  main.go                 # Application entry point
internal/
  handlers/              # HTTP handlers
    home.go
    api.go
  models/               # Data models
    user.go
    response.go
  templates/           # HTML templates
    layouts/
      base.html
    partials/
      form.html
      list.html
static/
  css/                # Stylesheets
  js/                 # JavaScript files (including HTMX)
go.mod               # Go module file
go.sum               # Go module checksum
```

## Server Setup

### Basic Server Configuration
```go
package main

import (
    "context"
    "html/template"
    "log"
    "net/http"
    "os"
    "os/signal"
    "time"
)

func main() {
    // Initialize templates
    tmpl := template.Must(template.ParseGlob("internal/templates/**/*.html"))
    
    // Create server
    srv := &http.Server{
        Addr:         ":8080",
        Handler:      setupRoutes(tmpl),
        ReadTimeout:  15 * time.Second,
        WriteTimeout: 15 * time.Second,
        IdleTimeout:  60 * time.Second,
    }
    
    // Start server in goroutine
    go func() {
        if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
            log.Fatalf("listen: %s\n", err)
        }
    }()
    
    // Wait for interrupt signal
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, os.Interrupt)
    <-quit
    
    // Graceful shutdown
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()
    if err := srv.Shutdown(ctx); err != nil {
        log.Fatal("Server forced to shutdown:", err)
    }
}
```

### Route Setup with Gorilla Mux
```go
func setupRoutes(tmpl *template.Template) http.Handler {
    r := mux.NewRouter()
    
    // Serve static files
    r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", 
        http.FileServer(http.Dir("static"))))
    
    // API routes
    r.HandleFunc("/api/users", handleUsers).Methods("GET")
    r.HandleFunc("/api/users/{id}", handleUser).Methods("GET")
    
    // HTML routes
    r.HandleFunc("/", handleHome(tmpl)).Methods("GET")
    
    // Middleware
    r.Use(csrfMiddleware)
    r.Use(loggingMiddleware)
    
    return r
}
```

## Handlers and Templates

### Handler Implementation
```go
// Handler with HTMX support
func handleUsers(tmpl *template.Template) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        users, err := getUsers()
        if err != nil {
            http.Error(w, "Failed to fetch users", http.StatusInternalServerError)
            return
        }
        
        // Check if it's an HTMX request
        if r.Header.Get("HX-Request") == "true" {
            // Render partial template for HTMX
            tmpl.ExecuteTemplate(w, "users-list.html", users)
            return
        }
        
        // Render full page for regular request
        tmpl.ExecuteTemplate(w, "users-page.html", users)
    }
}
```

### Template Structure
```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{.Title}}</title>
    <script src="/static/js/htmx.min.js"></script>
    <meta name="csrf-token" content="{{.CSRFToken}}">
</head>
<body>
    {{template "content" .}}
</body>
</html>

<!-- users-list.html -->
{{define "users-list"}}
<div id="users-list">
    {{range .Users}}
    <div class="user-item"
         hx-get="/api/users/{{.ID}}"
         hx-trigger="click"
         hx-target="#user-details">
        <h3>{{.Name}}</h3>
    </div>
    {{end}}
</div>
{{end}}
```

## CSRF Protection

### Middleware Implementation
```go
func csrfMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if r.Method != "GET" {
            token := r.Header.Get("X-CSRF-Token")
            if !validateCSRFToken(token) {
                http.Error(w, "Invalid CSRF token", http.StatusForbidden)
                return
            }
        }
        next.ServeHTTP(w, r)
    })
}
```

### CSRF in Templates
```html
<!-- Include CSRF token in forms -->
<form hx-post="/api/submit"
      hx-headers='{"X-CSRF-Token": "{{.CSRFToken}}"}'>
    <input type="text" name="data">
    <button type="submit">Submit</button>
</form>
```

## Error Handling

### Custom Error Types
```go
type APIError struct {
    Status  int    `json:"status"`
    Message string `json:"message"`
}

func (e APIError) Error() string {
    return e.Message
}

func handleError(w http.ResponseWriter, err error) {
    var apiErr APIError
    if errors.As(err, &apiErr) {
        http.Error(w, apiErr.Message, apiErr.Status)
        return
    }
    http.Error(w, "Internal Server Error", http.StatusInternalServerError)
}
```

### Error Response Templates
```html
<!-- error.html -->
{{define "error"}}
<div class="error-message"
     role="alert"
     hx-swap-oob="true">
    {{.Message}}
</div>
{{end}}
```

## Performance Optimization

### Template Caching
```go
type TemplateCache struct {
    templates *template.Template
    mu        sync.RWMutex
}

func (tc *TemplateCache) Get(name string) *template.Template {
    tc.mu.RLock()
    defer tc.mu.RUnlock()
    return tc.templates.Lookup(name)
}

func (tc *TemplateCache) Reload() error {
    tc.mu.Lock()
    defer tc.mu.Unlock()
    
    tmpl, err := template.ParseGlob("internal/templates/**/*.html")
    if err != nil {
        return err
    }
    
    tc.templates = tmpl
    return nil
}
```

### Response Compression
```go
func compressionMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if !strings.Contains(r.Header.Get("Accept-Encoding"), "gzip") {
            next.ServeHTTP(w, r)
            return
        }
        
        gz := gzip.NewWriter(w)
        defer gz.Close()
        
        w.Header().Set("Content-Encoding", "gzip")
        next.ServeHTTP(gzipResponseWriter{Writer: gz, ResponseWriter: w}, r)
    })
}
```

## Resources
- [Go Documentation](https://golang.org/doc/)
- [HTMX Documentation](https://htmx.org/docs/)
- [Gorilla Mux Documentation](https://github.com/gorilla/mux)
- [Go html/template Package](https://golang.org/pkg/html/template/)
- [Go Web Examples](https://gowebexamples.com/) 