---
title: "Database Performance Optimization Guide"
path: "developer/database/performance-optimization"
tags: ["database", "performance", "optimization", "tuning"]
description: "A comprehensive guide for optimizing database performance through configuration, indexing, and architecture improvements"
prompt_type: "Optimization Framework"
---

<purpose>
To provide a systematic approach for identifying and implementing database performance optimizations across all aspects of the system.
</purpose>

<context>
Use this guide when looking to improve overall database performance, whether addressing specific issues or conducting general optimization.
</context>

<instructions>
Provide the following system information:

1. System Overview
   - Database Details
     * Database system and version
     * Current database size
     * Growth rate
     * Hardware specifications

   - Usage Patterns
     * Peak load times
     * Read/write ratio
     * Concurrent users
     * Batch operations

2. Performance Analysis
   - Current State
     * Table sizes and growth
     * Query patterns
     * Pain points
     * Resource utilization

   - Monitoring Data
     * Slow query logs
     * System metrics
     * IO statistics
     * Connection stats

3. Optimization Areas
   - Configuration Tuning
     * Memory allocation
     * Connection settings
     * Buffer sizes
     * Worker processes
     * Logging levels

   - Query Optimization
     * Index review
     * Query rewriting
     * Join optimization
     * Execution plans

   - Schema Optimization
     * Table structure
     * Data types
     * Partitioning
     * Normalization level

4. Implementation Strategy
   - Priority Actions
     * Quick wins
     * Major changes
     * Long-term improvements
     * Maintenance tasks

   - Resource Planning
     * Hardware upgrades
     * Software updates
     * Monitoring tools
     * Testing environment
</instructions>

<variables>
- database_system: Database type and version
- database_size: Current data volume
- usage_patterns: Typical usage characteristics
- performance_metrics: Current performance data
</variables>

<examples>
Example 1:
Input: E-commerce database optimization
```yaml
System:
  Type: PostgreSQL 13
  Size: 500GB
  Tables:
    - products: 1M rows
    - orders: 10M rows
    - order_items: 50M rows
  Pain Points:
    - Slow product search
    - Order processing delays
```
Output:
```sql
-- Configuration Adjustments
ALTER SYSTEM SET shared_buffers = '4GB';
ALTER SYSTEM SET work_mem = '16MB';
ALTER SYSTEM SET maintenance_work_mem = '512MB';

-- Indexing Strategy
CREATE INDEX CONCURRENTLY idx_products_search 
ON products USING gin (to_tsvector('english', name || ' ' || description));

CREATE INDEX CONCURRENTLY idx_orders_processing 
ON orders (status, created_at) 
WHERE status IN ('pending', 'processing');

-- Partitioning Strategy
CREATE TABLE orders_partitioned (LIKE orders)
PARTITION BY RANGE (created_at);

-- Caching Solution
CREATE MATERIALIZED VIEW mv_product_stats AS
SELECT category_id, 
       COUNT(*) as product_count,
       AVG(price) as avg_price
FROM products 
GROUP BY category_id;
```

Example 2:
Input: Analytics database optimization
```yaml
System:
  Type: MySQL 8.0
  Size: 1TB
  Tables:
    - events: 100M rows
    - metrics: 500M rows
  Pain Points:
    - Slow aggregation queries
    - Poor write performance
```
Output:
```sql
-- Configuration Optimization
SET GLOBAL innodb_buffer_pool_size = 12G;
SET GLOBAL innodb_log_file_size = 1G;
SET GLOBAL innodb_flush_log_at_trx_commit = 2;

-- Table Partitioning
ALTER TABLE events
PARTITION BY RANGE (UNIX_TIMESTAMP(event_date)) (
    PARTITION p_2023_01 VALUES LESS THAN (UNIX_TIMESTAMP('2023-02-01')),
    PARTITION p_2023_02 VALUES LESS THAN (UNIX_TIMESTAMP('2023-03-01'))
);

-- Aggregation Optimization
CREATE TABLE daily_metrics (
    date DATE,
    metric_type VARCHAR(50),
    value DECIMAL(10,2),
    PRIMARY KEY (date, metric_type)
)
AS
SELECT 
    DATE(timestamp) as date,
    metric_type,
    SUM(value) as value
FROM metrics
GROUP BY DATE(timestamp), metric_type;
```
</examples>

<notes>
- Test changes in staging
- Monitor impact carefully
- Consider maintenance windows
- Document all changes
- Plan for scalability
- Balance improvements
- Regular review needed
</notes>