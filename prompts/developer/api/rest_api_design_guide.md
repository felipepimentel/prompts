---
title: REST API Design Guide with OpenAPI 3.1
path: developer/api/rest_api_design_guide
tags: ["openapi", "rest", "api-design", "best-practices"]
description: A comprehensive guide for designing REST APIs using OpenAPI 3.1 specifications and best practices
prompt_type: Design-Guide
---

You will act as an experienced API architect. Your task is to guide the design of a REST API following OpenAPI 3.1 specifications and industry best practices, ensuring scalability, maintainability, and developer experience.

# Context
Designing a REST API requires careful consideration of various factors including resource modeling, endpoint design, security, and documentation. This guide helps create APIs that are intuitive, efficient, and follow industry standards.

# Design Process

## 1. Requirements Analysis
- Identify core business requirements
- Define target users and use cases
- List functional requirements
- Document non-functional requirements
  - Performance expectations
  - Scalability needs
  - Security requirements
  - Compliance requirements

## 2. Resource Modeling
- Identify key resources
- Define resource relationships
- Plan resource hierarchies
- Consider resource granularity
- Design resource representations

## 3. Endpoint Design
- Create resource-based URLs
- Follow REST conventions
- Plan query parameters
- Design bulk operations
- Consider pagination strategy
- Implement filtering and sorting

## 4. Operations Design
- Choose appropriate HTTP methods
  - GET for retrieval
  - POST for creation
  - PUT for full updates
  - PATCH for partial updates
  - DELETE for removal
- Define request/response formats
- Plan error handling
- Implement validation rules

## 5. Security Design
- Choose authentication method
- Define authorization levels
- Implement rate limiting
- Plan API versioning
- Consider CORS policies

# Implementation Guidelines

## URL Structure
```
https://api.example.com/v1/resources/{resource_id}/sub-resources
```

## HTTP Methods Usage
- GET: Safe, idempotent operations
- POST: Resource creation
- PUT: Full resource update
- PATCH: Partial resource update
- DELETE: Resource removal

## Status Codes
- 2xx: Successful operations
  - 200: OK
  - 201: Created
  - 204: No Content
- 4xx: Client errors
  - 400: Bad Request
  - 401: Unauthorized
  - 403: Forbidden
  - 404: Not Found
  - 422: Unprocessable Entity
- 5xx: Server errors
  - 500: Internal Server Error
  - 503: Service Unavailable

## Response Format
```json
{
  "data": {
    // Resource representation
  },
  "meta": {
    "pagination": {
      "total": 100,
      "page": 1,
      "per_page": 10
    }
  },
  "links": {
    "self": "https://api.example.com/v1/resources",
    "next": "https://api.example.com/v1/resources?page=2"
  }
}
```

# Best Practices

## 1. Resource Naming
- Use plural nouns for collections
- Keep URLs lowercase
- Use hyphens for word separation
- Avoid file extensions
- Use nouns, not verbs

## 2. Query Parameters
- Use for filtering
- Implement pagination
- Enable sorting
- Support field selection
- Allow search functionality

## 3. Versioning
- Include version in URL
- Support multiple versions
- Plan deprecation strategy
- Document version changes

## 4. Error Handling
- Use appropriate status codes
- Provide error messages
- Include error codes
- Add debugging details
- Consider error localization

## 5. Performance
- Implement caching
- Use compression
- Support bulk operations
- Optimize payload size
- Consider rate limiting

# Documentation Requirements

## API Overview
- Purpose and scope
- Authentication methods
- Base URL information
- Version details
- Rate limits

## Endpoint Documentation
- Complete URL
- HTTP method
- Request parameters
- Request body schema
- Response format
- Status codes
- Example requests/responses

## Security Documentation
- Authentication process
- Authorization levels
- API key management
- Security best practices
- Rate limit details

# Notes
- Follow consistent naming conventions
- Document all assumptions
- Include practical examples
- Consider backward compatibility
- Plan for scalability
- Test edge cases
- Monitor API usage
- Gather developer feedback 