---
title: "Database Indexing Strategy Guide"
path: "developer/database/indexing-strategy"
tags: ["database", "performance", "optimization", "indexing"]
description: "A comprehensive guide for designing optimal database indexing strategies to improve query performance"
prompt_type: "Optimization Framework"
---

<purpose>
To provide a structured approach for analyzing database usage patterns and implementing effective indexing strategies that optimize query performance.
</purpose>

<context>
Use this guide when designing or optimizing database indexes to improve query performance while considering the impact on write operations.
</context>

<instructions>
Provide the following information:

1. Schema Analysis
   - Table Structures
     * Table definitions
     * Column types
     * Primary keys
     * Foreign keys

   - Query Patterns
     * Common queries
     * Access patterns
     * Join operations
     * Sort operations

2. Workload Assessment
   - Read Operations
     * Query frequency
     * Result set size
     * Response time requirements
     * Data distribution

   - Write Operations
     * Insert frequency
     * Update patterns
     * Batch operations
     * Concurrency needs

3. Index Design Strategy
   - Single-Column Indexes
     * High selectivity columns
     * Frequently filtered columns
     * Sort keys
     * Join columns

   - Composite Indexes
     * Multi-column queries
     * Column order optimization
     * Filter combinations
     * Index prefix usage

   - Specialized Indexes
     * Covering indexes
     * Partial indexes
     * Expression indexes
     * Full-text indexes

4. Performance Considerations
   - Storage Impact
     * Index size
     * Maintenance overhead
     * Storage requirements
     * Backup implications

   - Operation Impact
     * Write performance
     * Update overhead
     * Lock contention
     * Maintenance windows
</instructions>

<variables>
- table_structure: Database schema details
- query_patterns: Common query patterns
- performance_requirements: Performance targets
- workload_characteristics: Usage patterns
</variables>

<examples>
Example 1:
Input: User activity tracking table
```sql
CREATE TABLE user_activities (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    activity_type VARCHAR(50),
    created_at TIMESTAMP,
    metadata JSONB
);

-- Common queries:
SELECT * FROM user_activities WHERE user_id = ? ORDER BY created_at DESC;
SELECT * FROM user_activities WHERE activity_type = ? AND created_at > ?;
```
Output:
```sql
-- Primary lookup and sort
CREATE INDEX idx_user_activities_user_time ON user_activities (user_id, created_at DESC);

-- Activity type filtering
CREATE INDEX idx_user_activities_type_time ON user_activities (activity_type, created_at)
WHERE activity_type IS NOT NULL;
```

Example 2:
Input: Product inventory table
```sql
CREATE TABLE products (
    id BIGINT PRIMARY KEY,
    category_id INT,
    name VARCHAR(255),
    price DECIMAL(10,2),
    stock_quantity INT
);

-- Common queries:
SELECT * FROM products WHERE category_id = ? AND price BETWEEN ? AND ?;
SELECT * FROM products WHERE stock_quantity < ? AND category_id = ?;
```
Output:
```sql
-- Price range searches by category
CREATE INDEX idx_products_cat_price ON products (category_id, price);

-- Low stock monitoring
CREATE INDEX idx_products_stock_cat ON products (stock_quantity, category_id)
WHERE stock_quantity < 100;
```
</examples>

<notes>
- Consider query frequency
- Monitor index usage
- Balance read/write performance
- Regular maintenance required
- Review execution plans
- Consider storage costs
- Document index purposes
</notes>