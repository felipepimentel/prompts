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
Use this guide when planning a database migration, whether it's a schema change, platform migration, or data transformation project.
</context>

<instructions>
Provide the following information:

1. Schema Analysis
   - Source Schema
     * Table definitions
     * Data types
     * Constraints
     * Relationships

   - Target Schema
     * New structure
     * Data types
     * Constraints
     * Relationships

2. Migration Planning
   - Data Mapping
     * Field mappings
     * Type conversions
     * Default values
     * Derived fields

   - Transformation Rules
     * Data cleansing
     * Format changes
     * Business rules
     * Validation rules

3. Migration Strategy
   - Preparation Steps
     * Backup strategy
     * Staging environment
     * Test data
     * Rollback plan

   - Migration Process
     * Pre-migration tasks
     * Data extraction
     * Transformation steps
     * Loading process
     * Post-migration tasks

4. Validation Plan
   - Data Verification
     * Record counts
     * Data integrity
     * Constraint validation
     * Business rules

   - Performance Testing
     * Query performance
     * Load testing
     * Integration testing
     * User acceptance

5. Execution Plan
   - Timeline
     * Preparation phase
     * Testing phase
     * Migration window
     * Verification period

   - Risk Mitigation
     * Backup points
     * Monitoring strategy
     * Rollback procedures
     * Communication plan
</instructions>

<variables>
- source_schema: Current database schema
- target_schema: New database schema
- data_volume: Amount of data to migrate
- time_constraints: Available migration window
</variables>

<examples>
Example 1:
Input: User data migration with schema changes
```sql
-- Old Schema
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(200)
);

-- New Schema
CREATE TABLE users_new (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
);
```
Output:
```sql
-- Migration Steps
-- 1. Create staging table
CREATE TABLE users_staging AS SELECT * FROM users;

-- 2. Split name field
UPDATE users_staging
SET 
    first_name = SUBSTRING_INDEX(name, ' ', 1),
    last_name = SUBSTRING_INDEX(name, ' ', -1);

-- 3. Split contact into email and phone
UPDATE users_staging
SET
    email = CASE WHEN contact LIKE '%@%' 
                 THEN contact 
                 ELSE NULL END,
    phone = CASE WHEN contact NOT LIKE '%@%'
                 THEN contact
                 ELSE NULL END;

-- 4. Validate and transfer
INSERT INTO users_new
SELECT id, first_name, last_name, email, phone
FROM users_staging;
```

Example 2:
Input: Product catalog denormalization
```sql
-- Old Schema
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(200),
    category_id INT
);
CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- New Schema
CREATE TABLE products_new (
    id INT PRIMARY KEY,
    name VARCHAR(200),
    category_name VARCHAR(100)
);
```
Output:
```sql
-- Migration Process
-- 1. Create migration view
CREATE VIEW migration_data AS
SELECT 
    p.id,
    p.name,
    c.name as category_name
FROM products p
LEFT JOIN categories c ON p.category_id = c.id;

-- 2. Validate and transfer
INSERT INTO products_new
SELECT id, name, category_name
FROM migration_data;
```
</examples>

<notes>
- Always create backups
- Test with sample data
- Validate all constraints
- Monitor performance
- Plan for rollback
- Document all steps
- Consider downtime impact
</notes>