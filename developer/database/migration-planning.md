---
title: "Database Migration Planning Guide"
path: "developer/database/migration-planning"
tags: ["database", "migration", "data-transformation", "schema-evolution"]
description: "A comprehensive guide for planning and executing database migrations while ensuring data integrity and minimal downtime"
prompt_type: "Planning Framework"
---

<purpose>
To provide a structured approach for planning and executing database migrations, ensuring data integrity and minimizing service disruption.
</purpose>

<context>
Use this template when planning database migrations, whether for schema changes, data transformations, or platform migrations.
</context>

<instructions>
Provide the following migration planning information:

1. Migration Context
   - Current Environment
     * Database type/version
     * Data size/volume
     * Schema complexity
     * Usage patterns

   - Target Environment
     * Database type/version
     * Infrastructure changes
     * Performance requirements
     * Compliance needs

2. Migration Analysis
   - Schema Changes
     * Table structures
     * Data types
     * Constraints
     * Indexes

   - Data Transformation
     * Data mapping
     * Type conversions
     * Default values
     * Data cleanup

3. Migration Strategy
   - Implementation Plan
     * Migration phases
     * Rollback points
     * Data validation
     * Performance testing

   - Risk Mitigation
     * Data backup
     * Downtime planning
     * Error handling
     * Recovery procedures

4. Execution Framework
   - Migration Steps
     * Pre-migration tasks
     * Core migration
     * Post-migration tasks
     * Verification steps

   - Monitoring Plan
     * Progress tracking
     * Performance metrics
     * Error logging
     * Success criteria

</instructions>

<variables>
- database_type: Source and target database details
- data_volume: Size and complexity metrics
- time_constraints: Migration window details
- risk_tolerance: Acceptable downtime/issues
</variables>

<examples>
Example 1:
Input: PostgreSQL version upgrade with schema changes
Output:
```markdown
# Database Migration Plan: PostgreSQL 12 to 14

## Migration Overview
- **Source:** PostgreSQL 12.7
- **Target:** PostgreSQL 14.1
- **Data Size:** 500GB
- **Tables:** 150
- **Active Users:** 10,000
- **Downtime Window:** 4 hours

## Pre-Migration Tasks

### 1. Environment Setup
```sql
-- Create test environment
CREATE DATABASE migration_test WITH TEMPLATE production;

-- Verify space requirements
SELECT pg_size_pretty(pg_database_size('production'));
SELECT pg_size_pretty(pg_total_relation_size(relname)) AS total_size
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relname) DESC;
```

### 2. Schema Changes
```sql
-- Example schema modification
BEGIN;

-- Add new columns with defaults
ALTER TABLE users 
  ADD COLUMN last_login_at timestamp,
  ADD COLUMN login_count integer DEFAULT 0;

-- Create new indexes
CREATE INDEX CONCURRENTLY idx_users_last_login 
ON users(last_login_at);

COMMIT;

-- Verify constraints
SELECT conname, contype, conrelid::regclass
FROM pg_constraint
WHERE conrelid = 'users'::regclass;
```

## Migration Execution

### 1. Backup Process
```bash
# Full backup
pg_dump -Fc -f pre_migration_backup.dump production

# Verify backup
pg_restore -l pre_migration_backup.dump > backup_contents.txt
```

### 2. Data Migration
```sql
-- Update statistics
ANALYZE VERBOSE;

-- Migrate data
INSERT INTO users_new 
SELECT 
  id,
  username,
  COALESCE(last_login, created_at) as last_login_at,
  COALESCE(login_count, 0) as login_count,
  created_at
FROM users;

-- Verify counts
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM users_new;
```

### 3. Post-Migration Validation
```sql
-- Check data integrity
SELECT COUNT(*) as mismatches
FROM users u
LEFT JOIN users_new un ON u.id = un.id
WHERE un.id IS NULL;

-- Verify indexes
SELECT schemaname, tablename, indexname, indexdef
FROM pg_indexes
WHERE tablename = 'users_new';
```

## Rollback Plan

### 1. Schema Rollback
```sql
-- Revert schema changes
BEGIN;
ALTER TABLE users DROP COLUMN last_login_at;
ALTER TABLE users DROP COLUMN login_count;
DROP INDEX IF EXISTS idx_users_last_login;
COMMIT;
```

### 2. Data Restoration
```bash
# Restore from backup if needed
pg_restore -d production pre_migration_backup.dump
```

## Monitoring Queries
```sql
-- Monitor progress
SELECT pid, state, wait_event_type, wait_event,
       query_start, xact_start, backend_start
FROM pg_stat_activity
WHERE state != 'idle';

-- Check for locks
SELECT blocked_locks.pid AS blocked_pid,
       blocking_locks.pid AS blocking_pid,
       blocked_activity.usename AS blocked_user,
       blocking_activity.usename AS blocking_user,
       blocked_activity.query AS blocked_statement
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks 
    ON blocking_locks.locktype = blocked_locks.locktype
    AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
    AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
    AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page
    AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
    AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
    AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
    AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
    AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
    AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
    AND blocking_locks.pid != blocked_locks.pid
JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;
```

## Success Criteria
1. All data migrated with integrity
2. Performance matches or exceeds baseline
3. No data loss or corruption
4. All applications functional
5. Backup verified and accessible

## Communication Plan
1. T-24h: Final notification to stakeholders
2. T-1h: Begin migration window
3. T+0: Migration starts
4. T+2h: Progress update
5. T+4h: Completion notice
```

Example 2:
Input: MySQL to PostgreSQL migration
Output:
```markdown
# Database Migration Plan: MySQL to PostgreSQL

## Migration Overview
- **Source:** MySQL 8.0
- **Target:** PostgreSQL 14
- **Data Size:** 200GB
- **Tables:** 75
- **Active Users:** 5,000
- **Downtime Window:** 6 hours

## Pre-Migration Tasks

### 1. Schema Conversion
```sql
-- MySQL schema
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    status ENUM('pending', 'completed', 'cancelled'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    KEY `idx_user_status` (user_id, status)
);

-- PostgreSQL equivalent
CREATE TYPE order_status AS ENUM ('pending', 'completed', 'cancelled');

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    status order_status,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_user_status ON orders(user_id, status);
```

### 2. Data Type Mapping
```python
type_mapping = {
    'INT': 'INTEGER',
    'BIGINT': 'BIGINT',
    'VARCHAR': 'VARCHAR',
    'DATETIME': 'TIMESTAMP',
    'TINYINT(1)': 'BOOLEAN',
    'TEXT': 'TEXT',
    'DECIMAL': 'NUMERIC',
    'BLOB': 'BYTEA'
}

def convert_data_types(mysql_schema):
    pg_schema = mysql_schema
    for mysql_type, pg_type in type_mapping.items():
        pg_schema = pg_schema.replace(mysql_type, pg_type)
    return pg_schema
```

## Migration Execution

### 1. Data Export (MySQL)
```bash
# Export data in compatible format
mysqldump --compatible=postgresql \
          --default-character-set=utf8 \
          --skip-extended-insert \
          --compact \
          database_name > mysql_dump.sql

# Convert to PostgreSQL format
pgloader mysql://user:pass@host/dbname \
         postgresql://user:pass@host/dbname
```

### 2. Data Import (PostgreSQL)
```bash
# Import using pgloader
pgloader --type csv \
         --with "fields terminated by ','" \
         --with "fields enclosed by '\"'" \
         --with "lines terminated by '\n'" \
         data.csv \
         postgresql://user:pass@host/dbname

# Verify sequence values
SELECT setval('orders_id_seq', 
             (SELECT MAX(id) FROM orders));
```

### 3. Data Verification
```sql
-- Check row counts
SELECT COUNT(*) FROM orders;

-- Verify data integrity
SELECT status, COUNT(*) 
FROM orders 
GROUP BY status;

-- Check foreign keys
SELECT
    tc.table_schema, 
    tc.constraint_name, 
    tc.table_name, 
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name 
FROM 
    information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kcu
      ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
WHERE constraint_type = 'FOREIGN KEY';
```

## Performance Testing

### 1. Query Performance
```sql
-- Test common queries
EXPLAIN ANALYZE
SELECT o.*, u.email
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.status = 'pending'
  AND o.created_at >= NOW() - INTERVAL '24 hours';

-- Check index usage
SELECT schemaname, tablename, indexname, 
       idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes;
```

### 2. Load Testing
```python
async def simulate_load():
    async with asyncpg.create_pool(dsn=DATABASE_URL) as pool:
        async with pool.acquire() as conn:
            for _ in range(1000):
                await conn.execute("""
                    INSERT INTO orders (user_id, status)
                    VALUES ($1, $2)
                """, random.randint(1, 1000), 'pending')
```

## Monitoring Setup

### 1. Performance Metrics
```sql
-- Create monitoring views
CREATE VIEW performance_metrics AS
SELECT
    relname as table_name,
    seq_scan,
    idx_scan,
    n_tup_ins,
    n_tup_upd,
    n_tup_del,
    n_live_tup,
    n_dead_tup
FROM pg_stat_user_tables;

-- Monitor query performance
CREATE EXTENSION pg_stat_statements;

SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;
```

### 2. Alert Setup
```sql
-- Create alert function
CREATE OR REPLACE FUNCTION alert_on_high_load()
RETURNS trigger AS $$
BEGIN
    IF (SELECT count(*) FROM pg_stat_activity) > 100 THEN
        PERFORM pg_notify(
            'high_load',
            json_build_object(
                'connection_count', count(*),
                'timestamp', now()
            )::text
        )
        FROM pg_stat_activity;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

## Rollback Procedures

### 1. Quick Rollback
```bash
# Stop applications
systemctl stop application

# Restore MySQL data
mysql -u root -p database_name < backup.sql

# Update connection strings
sed -i 's/postgresql/mysql/' config/database.yml

# Restart applications
systemctl start application
```

### 2. Verification Queries
```sql
-- Verify data consistency
SELECT COUNT(*) as total_orders,
       COUNT(DISTINCT user_id) as unique_users,
       COUNT(DISTINCT status) as status_count
FROM orders;

-- Check recent modifications
SELECT created_at::date as date,
       COUNT(*) as orders
FROM orders
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY 1
ORDER BY 1;
```
```

</examples>

<notes>
- Test thoroughly
- Backup everything
- Plan for rollback
- Monitor performance
- Document changes
- Validate data
- Communicate clearly
- Review security
</notes> 