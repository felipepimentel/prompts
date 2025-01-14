---
title: "Go ServeMux REST API Guide"
path: "developer/frameworks/go/go-servemux-rest-guide"
tags: ["go", "rest-api", "servemux", "http", "backend", "best-practices"]
description: "A comprehensive guide for building REST APIs using Go's standard library and ServeMux, focusing on best practices, security, and performance optimization."
---

# Go ServeMux REST API Guide

## Overview
This guide provides comprehensive development guidelines for building REST APIs using Go's standard library and the new ServeMux introduced in Go 1.22+, focusing on best practices, security, and performance optimization.

## Project Structure

### Directory Organization
```
api/
  ├── handlers/        # HTTP handlers
  ├── middleware/     # Middleware functions
  ├── models/        # Data models
  ├── services/     # Business logic
  ├── utils/       # Utility functions
  └── main.go     # Entry point
```

## API Implementation

### Basic Server Setup
```go
package main

import (
    "log"
    "net/http"
    "time"
)

func main() {
    // Create new ServeMux
    mux := http.NewServeMux()

    // Register routes
    registerRoutes(mux)

    // Configure server
    server := &http.Server{
        Addr:         ":8080",
        Handler:      mux,
        ReadTimeout:  15 * time.Second,
        WriteTimeout: 15 * time.Second,
        IdleTimeout:  60 * time.Second,
    }

    // Start server
    log.Printf("Server starting on %s", server.Addr)
    if err := server.ListenAndServe(); err != nil {
        log.Fatalf("Server failed to start: %v", err)
    }
}

func registerRoutes(mux *http.ServeMux) {
    // API routes
    mux.HandleFunc("GET /api/v1/users", handleGetUsers)
    mux.HandleFunc("POST /api/v1/users", handleCreateUser)
    mux.HandleFunc("GET /api/v1/users/{id}", handleGetUser)
    mux.HandleFunc("PUT /api/v1/users/{id}", handleUpdateUser)
    mux.HandleFunc("DELETE /api/v1/users/{id}", handleDeleteUser)
}
```

### Request Handlers
```go
package handlers

import (
    "encoding/json"
    "net/http"
)

type User struct {
    ID    string `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email"`
}

type UserService interface {
    GetUser(id string) (*User, error)
    CreateUser(user *User) error
    UpdateUser(user *User) error
    DeleteUser(id string) error
    ListUsers() ([]*User, error)
}

type UserHandler struct {
    service UserService
}

func NewUserHandler(service UserService) *UserHandler {
    return &UserHandler{service: service}
}

func (h *UserHandler) HandleGetUser(w http.ResponseWriter, r *http.Request) {
    // Extract user ID from path
    id := r.PathValue("id")
    if id == "" {
        http.Error(w, "missing user id", http.StatusBadRequest)
        return
    }

    // Get user from service
    user, err := h.service.GetUser(id)
    if err != nil {
        http.Error(w, err.Error(), http.StatusNotFound)
        return
    }

    // Write response
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(user)
}

func (h *UserHandler) HandleCreateUser(w http.ResponseWriter, r *http.Request) {
    var user User
    if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    defer r.Body.Close()

    if err := h.service.CreateUser(&user); err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusCreated)
    json.NewEncoder(w).Encode(user)
}
```

## Middleware Implementation

### Logging Middleware
```go
package middleware

import (
    "log"
    "net/http"
    "time"
)

func LoggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()

        // Create response wrapper to capture status code
        rw := NewResponseWriter(w)

        // Call next handler
        next.ServeHTTP(rw, r)

        // Log request details
        log.Printf(
            "%s %s %d %s",
            r.Method,
            r.URL.Path,
            rw.statusCode,
            time.Since(start),
        )
    })
}

type ResponseWriter struct {
    http.ResponseWriter
    statusCode int
}

func NewResponseWriter(w http.ResponseWriter) *ResponseWriter {
    return &ResponseWriter{w, http.StatusOK}
}

func (rw *ResponseWriter) WriteHeader(code int) {
    rw.statusCode = code
    rw.ResponseWriter.WriteHeader(code)
}
```

### Authentication Middleware
```go
package middleware

import (
    "context"
    "net/http"
    "strings"
)

type Claims struct {
    UserID string
    Role   string
}

func AuthMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        // Get token from header
        authHeader := r.Header.Get("Authorization")
        if authHeader == "" {
            http.Error(w, "missing authorization header", http.StatusUnauthorized)
            return
        }

        // Extract token
        token := strings.TrimPrefix(authHeader, "Bearer ")
        if token == "" {
            http.Error(w, "invalid token format", http.StatusUnauthorized)
            return
        }

        // Validate token and extract claims
        claims, err := validateToken(token)
        if err != nil {
            http.Error(w, err.Error(), http.StatusUnauthorized)
            return
        }

        // Add claims to context
        ctx := context.WithValue(r.Context(), "claims", claims)
        next.ServeHTTP(w, r.WithContext(ctx))
    })
}

func validateToken(token string) (*Claims, error) {
    // Implement token validation logic
    // Return claims or error
    return nil, nil
}
```

## Error Handling

### Custom Error Types
```go
package errors

import (
    "fmt"
    "net/http"
)

type APIError struct {
    Status  int    `json:"status"`
    Message string `json:"message"`
    Code    string `json:"code"`
}

func (e *APIError) Error() string {
    return e.Message
}

func NewNotFound(resource string) *APIError {
    return &APIError{
        Status:  http.StatusNotFound,
        Message: fmt.Sprintf("%s not found", resource),
        Code:    "NOT_FOUND",
    }
}

func NewBadRequest(message string) *APIError {
    return &APIError{
        Status:  http.StatusBadRequest,
        Message: message,
        Code:    "BAD_REQUEST",
    }
}
```

## Rate Limiting

### Token Bucket Implementation
```go
package middleware

import (
    "net/http"
    "sync"
    "time"
)

type RateLimiter struct {
    tokens     float64
    capacity   float64
    rate       float64
    lastUpdate time.Time
    mu         sync.Mutex
}

func NewRateLimiter(rate float64, capacity float64) *RateLimiter {
    return &RateLimiter{
        tokens:     capacity,
        capacity:   capacity,
        rate:       rate,
        lastUpdate: time.Now(),
    }
}

func (rl *RateLimiter) Allow() bool {
    rl.mu.Lock()
    defer rl.mu.Unlock()

    now := time.Now()
    elapsed := now.Sub(rl.lastUpdate).Seconds()
    rl.tokens = min(rl.capacity, rl.tokens+(elapsed*rl.rate))
    rl.lastUpdate = now

    if rl.tokens >= 1 {
        rl.tokens--
        return true
    }
    return false
}

func RateLimitMiddleware(limiter *RateLimiter) func(http.Handler) http.Handler {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            if !limiter.Allow() {
                http.Error(w, "rate limit exceeded", http.StatusTooManyRequests)
                return
            }
            next.ServeHTTP(w, r)
        })
    }
}
```

## Testing

### Handler Tests
```go
package handlers

import (
    "encoding/json"
    "net/http"
    "net/http/httptest"
    "strings"
    "testing"
)

func TestHandleGetUser(t *testing.T) {
    // Create mock service
    service := &MockUserService{
        users: map[string]*User{
            "1": {ID: "1", Name: "Test User", Email: "test@example.com"},
        },
    }

    // Create handler
    handler := NewUserHandler(service)

    // Create test server
    ts := httptest.NewServer(http.HandlerFunc(handler.HandleGetUser))
    defer ts.Close()

    // Make request
    resp, err := http.Get(ts.URL + "/api/v1/users/1")
    if err != nil {
        t.Fatalf("Failed to make request: %v", err)
    }
    defer resp.Body.Close()

    // Check status code
    if resp.StatusCode != http.StatusOK {
        t.Errorf("Expected status %d, got %d", http.StatusOK, resp.StatusCode)
    }

    // Parse response
    var user User
    if err := json.NewDecoder(resp.Body).Decode(&user); err != nil {
        t.Fatalf("Failed to decode response: %v", err)
    }

    // Verify response
    if user.ID != "1" || user.Name != "Test User" {
        t.Errorf("Unexpected response: %+v", user)
    }
}
```

## Resources
- [Go Documentation](https://golang.org/doc/)
- [net/http Package](https://pkg.go.dev/net/http)
- [ServeMux Documentation](https://pkg.go.dev/net/http#ServeMux)
- [REST API Best Practices](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design) 