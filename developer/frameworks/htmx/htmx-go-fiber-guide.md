---
title: "HTMX with Go Fiber Development Guide"
path: "developer/frameworks/htmx/htmx-go-fiber-guide"
tags: ["htmx", "go", "fiber", "web-development", "backend", "best-practices"]
description: "A comprehensive guide for building modern web applications using HTMX with Go Fiber, focusing on high-performance server-side rendering and best practices."
---

# HTMX with Go Fiber Development Guide

## Overview
This guide provides best practices and patterns for modern web development using HTMX with Go Fiber, combining Fiber's high-performance web framework with HTMX's elegant approach to dynamic web interfaces.

## Core Technologies
- Go (1.22+)
- Fiber (latest version)
- HTMX (latest version)
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
.env                # Environment variables
```

## Server Setup

### Basic Server Configuration
```go
package main

import (
    "github.com/gofiber/fiber/v2"
    "github.com/gofiber/template/html/v2"
    "github.com/gofiber/fiber/v2/middleware/logger"
    "github.com/gofiber/fiber/v2/middleware/csrf"
    "os"
)

func main() {
    // Initialize template engine
    engine := html.New("./internal/templates", ".html")
    
    // Create Fiber app
    app := fiber.New(fiber.Config{
        Views: engine,
        ViewsLayout: "layouts/base",
    })
    
    // Middleware
    app.Use(logger.New())
    app.Use(csrf.New())
    
    // Static files
    app.Static("/static", "./static")
    
    // Setup routes
    setupRoutes(app)
    
    // Start server
    port := os.Getenv("PORT")
    if port == "" {
        port = "3000"
    }
    app.Listen(":" + port)
}
```

### Route Setup
```go
func setupRoutes(app *fiber.App) {
    // API routes
    api := app.Group("/api")
    api.Get("/users", handleGetUsers)
    api.Get("/users/:id", handleGetUser)
    api.Post("/users", handleCreateUser)
    
    // HTML routes
    app.Get("/", handleHome)
    app.Get("/users", handleUsersPage)
}
```

## Handlers and Templates

### Handler Implementation
```go
// Handler with HTMX support
func handleGetUsers(c *fiber.Ctx) error {
    users, err := getUsers()
    if err != nil {
        return c.Status(fiber.StatusInternalServerError).
            JSON(fiber.Map{"error": "Failed to fetch users"})
    }
    
    // Check if it's an HTMX request
    if c.Get("HX-Request") == "true" {
        // Return partial template for HTMX
        return c.Render("partials/users-list", fiber.Map{
            "Users": users,
        })
    }
    
    // Return full page
    return c.Render("pages/users", fiber.Map{
        "Title": "Users List",
        "Users": users,
    })
}

// API handler example
func handleCreateUser(c *fiber.Ctx) error {
    user := new(models.User)
    if err := c.BodyParser(user); err != nil {
        return c.Status(fiber.StatusBadRequest).
            JSON(fiber.Map{"error": "Invalid request body"})
    }
    
    if err := user.Create(); err != nil {
        return c.Status(fiber.StatusInternalServerError).
            JSON(fiber.Map{"error": "Failed to create user"})
    }
    
    // Return updated list for HTMX
    if c.Get("HX-Request") == "true" {
        users, _ := getUsers()
        return c.Render("partials/users-list", fiber.Map{
            "Users": users,
        })
    }
    
    return c.JSON(user)
}
```

### Template Structure
```html
<!-- layouts/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{.Title}}</title>
    <script src="/static/js/htmx.min.js"></script>
    <meta name="csrf-token" content="{{.CSRFToken}}">
</head>
<body>
    {{embed}}
</body>
</html>

<!-- partials/users-list.html -->
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
```

## CSRF Protection

### Middleware Configuration
```go
app.Use(csrf.New(csrf.Config{
    KeyLookup:      "header:X-CSRF-Token",
    CookieName:     "csrf_",
    CookieSameSite: "Lax",
    Expiration:     1 * time.Hour,
    KeyGenerator:   utils.UUID,
}))
```

### CSRF in Templates
```html
<!-- Form with CSRF protection -->
<form hx-post="/api/submit"
      hx-headers='{"X-CSRF-Token": "{{.CSRFToken}}"}'>
    <input type="text" name="data">
    <button type="submit">Submit</button>
</form>
```

## Error Handling

### Custom Error Handler
```go
app.Use(func(c *fiber.Ctx) error {
    return c.Next()
})

app.Use(func(c *fiber.Ctx) error {
    if err := c.Next(); err != nil {
        // Handle HTMX requests differently
        if c.Get("HX-Request") == "true" {
            return c.Render("partials/error", fiber.Map{
                "Error": err.Error(),
            })
        }
        
        code := fiber.StatusInternalServerError
        if e, ok := err.(*fiber.Error); ok {
            code = e.Code
        }
        
        return c.Status(code).JSON(fiber.Map{
            "error": err.Error(),
        })
    }
    return nil
})
```

### Error Templates
```html
<!-- partials/error.html -->
<div class="error-message"
     role="alert"
     hx-swap-oob="true">
    {{.Error}}
</div>
```

## Performance Optimization

### Response Compression
```go
app.Use(compress.New(compress.Config{
    Level: compress.LevelBestSpeed,
}))
```

### Template Caching
```go
// Enable template caching in production
if os.Getenv("GO_ENV") == "production" {
    engine := html.New("./internal/templates", ".html", 
        html.Config{
            Reload: false,
        })
    app.Views = engine
}
```

### Static File Configuration
```go
app.Static("/static", "./static", fiber.Static{
    Compress:      true,
    ByteRange:     true,
    Browse:        false,
    CacheDuration: 24 * time.Hour,
    MaxAge:        86400,
})
```

## Environment Configuration
```go
// .env
PORT=3000
DB_URL=postgresql://user:pass@localhost:5432/dbname
GO_ENV=development
```

```go
// config/config.go
type Config struct {
    Port   string
    DBUrl  string
    GoEnv  string
}

func LoadConfig() (*Config, error) {
    if err := godotenv.Load(); err != nil {
        log.Printf("Warning: .env file not found")
    }
    
    return &Config{
        Port:   getEnv("PORT", "3000"),
        DBUrl:  getEnv("DB_URL", ""),
        GoEnv:  getEnv("GO_ENV", "development"),
    }, nil
}
```

## Resources
- [Go Fiber Documentation](https://docs.gofiber.io/)
- [HTMX Documentation](https://htmx.org/docs/)
- [Go Fiber Examples](https://github.com/gofiber/recipes)
- [HTMX + Go Fiber Examples](https://github.com/gofiber/recipes/tree/master/htmx)
- [Go Fiber Community](https://discord.gg/gofiber) 