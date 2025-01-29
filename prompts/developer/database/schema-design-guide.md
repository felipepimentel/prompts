---
title: "Database Schema Design Guide"
path: "developer/database/schema-design"
tags: ["database", "schema-design", "data-modeling", "architecture"]
description: "A comprehensive guide for designing efficient and scalable database schemas based on application requirements"
prompt_type: "Design Framework"
---

<purpose>
To assist in creating well-structured database schemas that meet application requirements while following best practices for performance and scalability.
</purpose>

<context>
Use this prompt when designing a new database schema or restructuring an existing one to meet specific application needs.
</context>

<instructions>
Provide the following information about your application:

1. Application Overview
   - Main purpose and functionality
   - Expected scale and growth
   - Performance requirements

2. Core Entities
   [List main entities and their relationships]

3. Key Requirements
   - Functional requirements
   - Performance requirements
   - Scalability needs
   - Data integrity constraints

Based on this information, you'll receive a schema design including:

1. Table Definitions
   - Table names and purposes
   - Column definitions with data types
   - Primary and foreign keys
   - Constraints and validations

2. Relationship Modeling
   - One-to-one relationships
   - One-to-many relationships
   - Many-to-many relationships
   - Junction tables design

3. Performance Optimization
   - Index recommendations
   - Partitioning strategies
   - Caching considerations
   - Query optimization hints

4. Scalability Considerations
   - Sharding possibilities
   - Replication strategies
   - Backup approaches
   - Growth management
</instructions>

<variables>
- application_description: Overview of the application
- main_entities: List of core entities
- requirements: Key functional and non-functional requirements
- scale_expectations: Expected data volume and growth
</variables>

<examples>
Example 1:
Input: Social media platform with users, posts, and comments
Output:
```sql
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    post_id BIGINT PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_user_posts (user_id, created_at)
);
```

Example 2:
Input: E-commerce platform with products, orders, and inventory
Output:
```sql
CREATE TABLE products (
    product_id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10,2),
    stock_quantity INTEGER,
    INDEX idx_product_search (name, price)
);

CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    user_id BIGINT REFERENCES users(user_id),
    total_amount DECIMAL(10,2),
    status VARCHAR(20),
    INDEX idx_user_orders (user_id, status)
);
```
</examples>

<notes>
- Consider data integrity requirements
- Plan for future scalability
- Follow naming conventions
- Document design decisions
- Consider database engine specific features
- Balance normalization with performance
- Plan for monitoring and maintenance
</notes>