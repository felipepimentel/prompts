---
category: Developer
description: A comprehensive prompt for generating OpenAPI 3.1 specifications for
  eCommerce product catalogs
model: GPT-4
path: developer/api/ecommerce_openapi_generator
prompt_type: Template-Based
tags:
- openapi
- api
- ecommerce
- yaml
- specification
- rest
title: eCommerce Product Catalog OpenAPI Generator
version: '1.0'
---

You will act as an API architect specializing in eCommerce systems. Your task is to generate a complete OpenAPI 3.1 specification in YAML format for a product catalog API that follows REST best practices and industry standards.

# Context
Modern eCommerce platforms require well-documented, standardized APIs for product catalog management. This specification will serve as the foundation for building robust, scalable eCommerce systems that can handle product information, categories, and related data.

# Core Requirements

## API Information
- OpenAPI version 3.1.0
- Clear API title and description
- Versioning strategy
- Contact information
- License details
- Server configurations

## Essential Endpoints
1. **Product Operations**
   - List products with pagination and filters
   - Retrieve single product details
   - Search products
   - Product variations handling
   
2. **Category Operations**
   - List categories with hierarchy
   - Retrieve category details
   - Category-product associations

3. **Additional Features**
   - Product image handling
   - Inventory status
   - Price information
   - Product attributes
   - Related products

## Schema Components
Define comprehensive schemas for:
- Products
- Categories
- Prices
- Images
- Attributes
- Inventory
- Error responses

# Output Format
Generate a complete YAML document following OpenAPI 3.1 specifications:

```yaml
openapi: 3.1.0
info:
  title: "eCommerce Product Catalog API"
  description: "REST API for managing eCommerce product catalogs"
  version: "1.0.0"
  contact:
    name: "API Support"
    email: "api@example.com"
servers:
  - url: "https://api.example.com/v1"
    description: "Production server"
paths:
  # Define endpoints here
components:
  schemas:
    # Define data models here
  responses:
    # Define reusable responses here
  parameters:
    # Define reusable parameters here
  securitySchemes:
    # Define security schemes here
```

# Implementation Guidelines

1. **RESTful Design**
   - Use proper HTTP methods
   - Implement consistent URL patterns
   - Include appropriate status codes
   - Support filtering and pagination

2. **Security Considerations**
   - API authentication methods
   - Rate limiting headers
   - CORS policies
   - Data validation rules

3. **Documentation**
   - Clear endpoint descriptions
   - Request/response examples
   - Error scenarios
   - Schema descriptions

4. **Best Practices**
   - Consistent naming conventions
   - Proper status code usage
   - Comprehensive error handling
   - Performance considerations

# Validation Requirements
- Valid OpenAPI 3.1 syntax
- Proper YAML formatting
- Consistent indentation
- Complete schema definitions
- Proper reference usage ($ref)

# Notes
- Include pagination for list endpoints
- Support sorting and filtering
- Handle image URLs and metadata
- Consider cache control headers
- Include rate limiting information
- Document API versioning strategy