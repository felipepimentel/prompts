---
title: "SQL Query Optimization Guide"
path: "developer/database/query-optimization"
tags: ["database", "performance", "sql", "optimization"]
description: "A comprehensive guide for analyzing and optimizing SQL queries for better performance on large datasets"
prompt_type: "Optimization Framework"
---

<purpose>
To provide a structured approach for analyzing and optimizing SQL queries to improve performance and resource utilization.
</purpose>

<context>
Use this guide when dealing with slow-performing SQL queries that need optimization, particularly for large datasets or complex operations.
</context>

<instructions>
Provide the following information:

1. Query Details
   - SQL Query
     * Full query text
     * Expected results
     * Current performance
     * Performance targets

   - Database Context
     * Database system (PostgreSQL, MySQL, etc.)
     * Table sizes
     * Hardware constraints
     * Current indexes

2. Performance Analysis
   - Query Plan Analysis
     * Execution plan review
     * Cost analysis
     * Bottleneck identification
     * Resource usage

   - Data Access Patterns
     * Table scan operations
     * Join methods
     * Sort operations
     * Temporary tables

3. Optimization Strategies
   - Query Rewriting
     * Simplify complex queries
     * Optimize JOIN operations
     * Improve WHERE clauses
     * Reduce subqueries

   - Index Optimization
     * Create new indexes
     * Modify existing indexes
     * Remove unused indexes
     * Consider covering indexes

   - Schema Optimization
     * Table denormalization
     * Partitioning strategy
     * Materialized views
     * Caching solutions

4. Implementation Plan
   - Changes Required
     * Query modifications
     * Index changes
     * Schema updates
     * Configuration adjustments

   - Impact Assessment
     * Performance improvement
     * Resource requirements
     * Maintenance overhead
     * Side effects
</instructions>

<variables>
- query: The SQL query to optimize
- database_system: Database management system
- table_sizes: Size of relevant tables
- hardware_constraints: System limitations
</variables>

<examples>
Example 1:
Input: Slow product search query
```sql
SELECT p.*, c.name as category_name
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
WHERE p.price > 100
  AND p.name LIKE '%searchterm%'
ORDER BY p.created_at DESC;
```
Output:
```sql
-- Optimized query with proper indexes
CREATE INDEX idx_products_price_date ON products (price, created_at);
CREATE INDEX idx_products_name_trgm ON products USING gin (name gin_trgm_ops);

-- Rewritten query
SELECT p.*, c.name as category_name
FROM products p
INNER JOIN categories c ON p.category_id = c.id
WHERE p.price > 100
  AND p.name ILIKE '%searchterm%'
ORDER BY p.created_at DESC
LIMIT 100;
```

Example 2:
Input: Slow aggregation query
```sql
SELECT user_id, 
       COUNT(*) as total_orders,
       SUM(amount) as total_amount
FROM orders
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY user_id
HAVING COUNT(*) > 5;
```
Output:
```sql
-- Add composite index
CREATE INDEX idx_orders_date_user ON orders (created_at, user_id);

-- Consider materialized view for frequent access
CREATE MATERIALIZED VIEW mv_user_order_stats AS
SELECT user_id, 
       COUNT(*) as total_orders,
       SUM(amount) as total_amount
FROM orders
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY user_id
HAVING COUNT(*) > 5;
```
</examples>

<notes>
- Always test optimizations
- Consider data growth
- Monitor query plans
- Measure improvements
- Document changes
- Consider maintenance
- Balance optimizations
</notes>