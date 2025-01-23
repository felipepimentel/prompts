---
description: Comprehensive style guide for writing clean, maintainable, and efficient
  PostgreSQL queries
path: developer/database/postgresql-style-guide
prompt_type: Instruction-based prompting
tags:
- postgresql
- sql
- database
- style-guide
- best-practices
title: PostgreSQL Style Guide
---

# PostgreSQL Style Guide

## General Principles

### 1. Formatting
- Use consistent indentation (2 or 4 spaces)
- Use lowercase for SQL keywords
- Break long lines at logical points
- Align related statements vertically
- Use white space to improve readability

### 2. Naming Conventions
- Use `snake_case` for all identifiers
- Avoid SQL reserved words
- Keep names under 63 characters
- Make names descriptive and clear
- Use English language names

## Schema Design

### 1. Table Naming
```sql
-- Use plural nouns for tables
create table users (
  id bigint generated always as identity primary key,
  email text not null unique,
  created_at timestamptz not null default now()
);

-- Add descriptive comments
comment on table users is 'System users including both customers and staff';
```

### 2. Column Naming
```sql
-- Use singular nouns for columns
create table orders (
  id bigint generated always as identity primary key,
  user_id bigint references users(id),  -- Foreign key pattern: table_id
  status order_status not null,         -- Enum type
  total_amount decimal(10,2) not null,  -- Money pattern
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
```

### 3. Constraints
```sql
-- Name constraints explicitly
create table products (
  id bigint generated always as identity,
  sku text not null,
  name text not null,
  price decimal(10,2) not null,
  
  constraint products_pkey primary key (id),
  constraint products_sku_key unique (sku),
  constraint products_price_positive check (price > 0)
);
```

## Query Style

### 1. Simple Queries
```sql
-- Single-line for very simple queries
select * from users where active = true;

-- Multi-line for better readability
select 
  id,
  email,
  created_at
from 
  users
where 
  created_at >= now() - interval '7 days';
```

### 2. Joins
```sql
-- Align join conditions
select
  orders.id as order_id,
  users.email as user_email,
  orders.total_amount
from
  orders
  inner join users on users.id = orders.user_id
  left join payments on payments.order_id = orders.id
where
  orders.status = 'pending'
  and orders.created_at > now() - interval '24 hours';
```

### 3. Complex Queries
```sql
-- Use CTEs for complex queries
with monthly_sales as (
  -- Calculate sales per month
  select
    date_trunc('month', created_at) as month,
    sum(total_amount) as total_sales
  from
    orders
  where
    status = 'completed'
  group by
    date_trunc('month', created_at)
),
sales_growth as (
  -- Calculate month-over-month growth
  select
    month,
    total_sales,
    lag(total_sales) over (order by month) as prev_month_sales,
    (total_sales - lag(total_sales) over (order by month)) / 
      lag(total_sales) over (order by month) * 100 as growth_percent
  from
    monthly_sales
)
select
  month,
  total_sales,
  round(growth_percent, 2) as growth_percent
from
  sales_growth
order by
  month desc;
```

## Functions and Procedures

### 1. Function Style
```sql
create or replace function get_user_stats(
  user_id bigint,
  start_date date default current_date - interval '30 days',
  end_date date default current_date
) returns table (
  total_orders bigint,
  total_spent decimal(10,2),
  average_order decimal(10,2)
) as $$
begin
  return query
    select
      count(*) as total_orders,
      sum(total_amount) as total_spent,
      avg(total_amount) as average_order
    from
      orders
    where
      orders.user_id = get_user_stats.user_id
      and orders.created_at::date between start_date and end_date;
end;
$$ language plpgsql;
```

### 2. Trigger Functions
```sql
create or replace function update_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

create trigger set_updated_at
  before update on products
  for each row
  execute function update_updated_at();
```

## Indexes

### 1. Index Naming
```sql
-- Pattern: table_column_type_idx
create index users_email_btree_idx 
  on users using btree (email);

create index products_name_gin_idx 
  on products using gin (name gin_trgm_ops);
```

### 2. Partial Indexes
```sql
-- Add where clause in name
create index orders_status_pending_btree_idx 
  on orders using btree (created_at)
  where status = 'pending';
```

## Security

### 1. Row Level Security
```sql
-- Enable RLS
alter table orders enable row level security;

-- Create policies
create policy "Users can view their own orders"
  on orders for select
  using (user_id = auth.uid());

create policy "Admin can view all orders"
  on orders for select
  using (auth.role() = 'admin');
```

### 2. Grants
```sql
-- Grant minimal required privileges
grant select on table products to web_anon;
grant select, insert, update on table orders to authenticated;
grant usage on sequence orders_id_seq to authenticated;
```

## Performance

### 1. Query Optimization
- Use explain analyze for performance testing
- Consider partial indexes for filtered queries
- Use appropriate index types (btree, gin, gist)
- Optimize join conditions
- Use materialized views for complex reports

### 2. Maintenance
- Regular vacuum and analyze
- Monitor index usage
- Archive old data
- Use appropriate data types
- Partition large tables

## Best Practices

1. Data Integrity
   - Use appropriate constraints
   - Implement foreign keys
   - Add check constraints
   - Use transactions

2. Code Organization
   - Group related changes
   - Comment complex logic
   - Use migrations
   - Version control schemas

3. Security
   - Implement RLS
   - Use prepared statements
   - Minimal privilege grants
   - Regular audits

4. Maintenance
   - Document changes
   - Regular backups
   - Monitor performance
   - Update statistics

Remember: Consistency in style and naming makes databases easier to maintain and understand. Always prioritize clarity and maintainability over brevity. 