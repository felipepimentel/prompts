---
category: Developer
description: Comprehensive style guide for writing clean, maintainable, and secure
  PostgreSQL code in Supabase projects
model: GPT-4
path: developer/supabase/code-formal-sql.md
prompt_type: Instruction-based prompting
tags:
- postgresql
- sql
- supabase
- database
- style-guide
- best-practices
title: PostgreSQL SQL Style Guide for Supabase
version: '1.0'
---

# PostgreSQL SQL Style Guide

## Core Principles

### 1. Naming Conventions

#### General Rules
- Use `snake_case` for all identifiers
- Keep names under 63 characters
- Avoid SQL reserved words
- Use descriptive, meaningful names
- Be consistent across the database

#### Specific Rules
```sql
-- Tables: plural nouns
create table users (
  id bigint generated always as identity primary key,
  email text not null unique,
  created_at timestamptz not null default now()
);

-- Columns: singular descriptive names
create table products (
  id bigint generated always as identity primary key,
  name text not null,
  description text,
  price_cents integer not null check (price_cents >= 0),
  category_id bigint references categories(id)
);

-- Foreign keys: referenced_table_id
create table orders (
  id bigint generated always as identity primary key,
  user_id bigint references users(id),
  status order_status not null
);
```

### 2. Table Structure

#### Required Columns
```sql
create table examples (
  -- Primary key: always bigint identity
  id bigint generated always as identity primary key,
  
  -- Timestamps: always use timestamptz
  created_at timestamptz not null default now(),
  updated_at timestamptz,
  
  -- Soft delete if needed
  deleted_at timestamptz,
  
  -- Version control if needed
  version integer not null default 1
);
```

#### Constraints
```sql
create table products (
  id bigint generated always as identity primary key,
  sku text not null,
  name text not null,
  price_cents integer not null,
  
  -- Named constraints for better error messages
  constraint products_sku_unique unique (sku),
  constraint products_price_positive check (price_cents >= 0)
);
```

### 3. Query Style

#### Simple Queries
```sql
-- Single line for very simple queries
select * from users where active = true;

-- Multi-line for better readability
select 
  id,
  email,
  created_at
from 
  users
where 
  created_at >= now() - interval '7 days'
order by 
  created_at desc;
```

#### Complex Queries
```sql
with monthly_sales as (
  -- Calculate monthly sales per product
  select
    date_trunc('month', created_at) as month,
    product_id,
    sum(quantity) as total_quantity,
    sum(price_cents * quantity) as total_cents
  from
    order_items
  join
    orders on orders.id = order_items.order_id
  where
    orders.status = 'completed'
  group by
    date_trunc('month', created_at),
    product_id
),
product_stats as (
  -- Calculate product statistics
  select
    product_id,
    avg(total_quantity) as avg_monthly_quantity,
    percentile_cont(0.5) within group (order by total_quantity) as median_quantity
  from
    monthly_sales
  group by
    product_id
)
select
  products.name as product_name,
  ps.avg_monthly_quantity,
  ps.median_quantity,
  -- Format currency for display
  to_char(
    ms.total_cents::numeric / 100,
    'FM$999,999,999.00'
  ) as total_revenue
from
  product_stats ps
join
  products on products.id = ps.product_id
join
  monthly_sales ms on ms.product_id = ps.product_id
where
  ms.month = date_trunc('month', now())
order by
  ps.avg_monthly_quantity desc;
```

### 4. Security Best Practices

#### Row Level Security
```sql
-- Enable RLS on all tables
alter table users enable row level security;

-- Create policies for different operations
create policy "Users can view their own data"
  on users
  for select
  using (auth.uid() = id);

create policy "Users can update their own data"
  on users
  for update
  using (auth.uid() = id)
  with check (auth.uid() = id);
```

#### Function Security
```sql
-- Always specify security definer/invoker
create function get_user_profile(user_id bigint)
returns json
language sql
security definer
set search_path = public
as $$
  select 
    json_build_object(
      'id', id,
      'email', email,
      'profile', profile
    )
  from 
    users
  where 
    id = user_id
    and deleted_at is null;
$$;
```

### 5. Performance Considerations

#### Indexes
```sql
-- Create indexes for frequently queried columns
create index users_email_idx on users (email);

-- Create partial indexes for filtered queries
create index active_users_idx 
  on users (created_at)
  where deleted_at is null;

-- Create composite indexes for multi-column queries
create index orders_user_status_idx 
  on orders (user_id, status, created_at desc);
```

#### Materialized Views
```sql
create materialized view monthly_revenue as
select
  date_trunc('month', orders.created_at) as month,
  sum(order_items.price_cents * order_items.quantity) as revenue_cents,
  count(distinct orders.user_id) as unique_customers
from
  orders
join
  order_items on order_items.order_id = orders.id
where
  orders.status = 'completed'
group by
  date_trunc('month', orders.created_at)
with data;

-- Create unique index for faster refresh
create unique index monthly_revenue_month_idx on monthly_revenue (month);
```

### 6. Database Functions

#### Function Template
```sql
create or replace function process_order(
  p_order_id bigint,
  p_status text
)
returns boolean
language plpgsql
security definer
set search_path = public
as $$
declare
  v_order orders;
  v_user_id bigint;
begin
  -- Input validation
  if p_order_id is null then
    raise exception 'Order ID cannot be null';
  end if;

  -- Get order details
  select * into v_order
  from orders
  where id = p_order_id
  for update;

  if not found then
    raise exception 'Order not found: %', p_order_id;
  end if;

  -- Process order
  update orders
  set
    status = p_status,
    updated_at = now()
  where id = p_order_id;

  -- Return success
  return true;
exception
  when others then
    -- Log error and re-raise
    raise exception 'Error processing order %: %', p_order_id, sqlerrm;
end;
$$;
```

### 7. Comments and Documentation

#### Table Documentation
```sql
create table subscriptions (
  id bigint generated always as identity primary key,
  user_id bigint not null references users(id),
  plan_id bigint not null references plans(id),
  status subscription_status not null,
  current_period_start timestamptz not null,
  current_period_end timestamptz not null
);

comment on table subscriptions is 'User subscription records with plan details and billing periods';
comment on column subscriptions.status is 'Current status of the subscription (active, canceled, past_due)';
comment on column subscriptions.current_period_start is 'Start date of the current billing period';
comment on column subscriptions.current_period_end is 'End date of the current billing period';
```

#### Function Documentation
```sql
/*
 * Processes a subscription renewal
 *
 * Parameters:
 * - p_subscription_id: ID of the subscription to renew
 * - p_period_end: New period end date
 *
 * Returns:
 * - boolean: true if successful
 *
 * Raises:
 * - If subscription not found
 * - If subscription is not active
 * - If new period end date is invalid
 */
create or replace function renew_subscription(
  p_subscription_id bigint,
  p_period_end timestamptz
)
returns boolean
language plpgsql
security definer
as $$
-- Function body...
$$;
```

Remember:
- Always enable RLS on new tables
- Use proper data types (e.g., timestamptz for timestamps)
- Add appropriate indexes for query patterns
- Document complex SQL with clear comments
- Use transactions for multi-step operations
- Follow consistent formatting for readability
- Consider performance implications of queries
- Implement proper error handling in functions