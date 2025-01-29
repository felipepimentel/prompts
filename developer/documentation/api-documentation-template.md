---
title: "API Documentation Template Guide"
path: "developer/documentation/api-documentation-template"
tags: ["documentation", "api", "reference", "technical-writing"]
description: "A structured template for creating clear and comprehensive API endpoint documentation"
prompt_type: "Documentation Framework"
---

<purpose>
To provide a standardized template for documenting API endpoints that ensures consistency and completeness in technical documentation.
</purpose>

<context>
Use this template when documenting new API endpoints or updating existing API documentation to maintain consistency across your API reference.
</context>

<instructions>
Provide the following endpoint information:

1. Endpoint Overview
   - Basic Information
     * URL path
     * HTTP method
     * Brief description
     * Authentication requirements

   - Request Details
     * Path parameters
     * Query parameters
     * Headers required
     * Request body schema

2. Request Components
   - Parameters
     * Name and type
     * Required/optional
     * Default values
     * Valid ranges/formats
     * Description

   - Request Body
     * Content type
     * Schema definition
     * Required fields
     * Optional fields
     * Field constraints

3. Response Format
   - Success Response
     * Status code
     * Response body
     * Headers returned
     * Example response

   - Error Responses
     * Status codes
     * Error messages
     * Error types
     * Troubleshooting hints

4. Additional Information
   - Usage Details
     * Rate limits
     * Pagination
     * Caching
     * Versioning

   - Security
     * Authentication methods
     * Authorization scopes
     * Token handling
     * Security considerations

</instructions>

<variables>
- endpoint_path: API endpoint URL
- http_method: HTTP method used
- auth_required: Authentication requirements
- content_type: Request/response content type
</variables>

<examples>
Example 1:
Input: User creation endpoint
Output:
```markdown
# Create User

Creates a new user account in the system.

## Endpoint

\`POST /api/v1/users\`

## Authentication

Requires API key in header: \`X-API-Key: <your_api_key>\`

## Request

### Headers

| Name          | Required | Description           |
|---------------|----------|-----------------------|
| Content-Type  | Yes      | application/json      |
| X-API-Key     | Yes      | Your API key         |

### Body

```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "role": "string"
}
```

### Parameters

| Field    | Type   | Required | Description                    |
|----------|--------|----------|--------------------------------|
| username | string | Yes      | Unique username (3-50 chars)   |
| email    | string | Yes      | Valid email address           |
| password | string | Yes      | Password (min 8 chars)        |
| role     | string | No       | User role (default: "user")   |

## Response

### Success Response

\`\`\`
Status: 201 Created
\`\`\`

```json
{
  "id": "uuid",
  "username": "john_doe",
  "email": "john@example.com",
  "role": "user",
  "created_at": "2023-01-01T00:00:00Z"
}
```

### Error Responses

#### Invalid Request
\`\`\`
Status: 400 Bad Request
\`\`\`

```json
{
  "error": "validation_error",
  "message": "Invalid request parameters",
  "details": {
    "username": "Username is required"
  }
}
```

#### Unauthorized
\`\`\`
Status: 401 Unauthorized
\`\`\`

```json
{
  "error": "unauthorized",
  "message": "Invalid or missing API key"
}
```

## Rate Limiting

- Rate limit: 100 requests per minute
- Rate limit header: \`X-RateLimit-Remaining\`
```

Example 2:
Input: List products endpoint
Output:
```markdown
# List Products

Retrieves a paginated list of products.

## Endpoint

\`GET /api/v1/products\`

## Authentication

No authentication required

## Request

### Query Parameters

| Parameter  | Required | Default | Description                    |
|------------|----------|---------|--------------------------------|
| page       | No       | 1       | Page number                    |
| limit      | No       | 20      | Items per page (max: 100)     |
| category   | No       | null    | Filter by category            |
| sort       | No       | "name"  | Sort field (name, price, date)|
| order      | No       | "asc"   | Sort order (asc, desc)        |

## Response

### Success Response

\`\`\`
Status: 200 OK
\`\`\`

```json
{
  "data": [
    {
      "id": "uuid",
      "name": "Product Name",
      "description": "Product description",
      "price": 99.99,
      "category": "electronics",
      "created_at": "2023-01-01T00:00:00Z"
    }
  ],
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 50,
    "total_pages": 3
  }
}
```

### Error Response

#### Invalid Parameters
\`\`\`
Status: 400 Bad Request
\`\`\`

```json
{
  "error": "validation_error",
  "message": "Invalid query parameters",
  "details": {
    "limit": "Must be between 1 and 100"
  }
}
```

## Caching

- Cache-Control: max-age=300
- ETag support enabled
```
</examples>

<notes>
- Be consistent in formatting
- Include all required fields
- Provide clear examples
- Document error cases
- Keep examples realistic
- Update for changes
- Include authentication details
</notes> 