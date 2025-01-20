---
title: Supabase Database Migration Guide
path: developer/supabase/database-create-migration.md
tags:
  - supabase
  - postgresql
  - migrations
  - database
  - security
  - rls
description: Comprehensive guide for creating and managing database migrations in Supabase projects using best practices
---

# Supabase Database Migration Guide

## Migration File Structure

### 1. File Naming Convention
Files must be named in the format `YYYYMMDDHHmmss_short_description.sql` using UTC time:

```
20240315143000_create_users_table.sql
20240315143100_add_user_profiles.sql
20240315143200_create_auth_policies.sql
```

### 2. Migration Header Template
```sql
/*
 * Migration: [Short Description]
 * 
 * Purpose:
 * - Detailed explanation of what this migration does
 * - List major changes and their impact
 * 
 * Tables Affected:
 * - table_name1: [changes made]
 * - table_name2: [changes made]
 * 
 * Security Considerations:
 * - RLS policies added/modified
 * - Permission changes
 * - Data access implications
 * 
 * Dependencies:
 * - List any migration dependencies
 * - Required extensions or configurations
 * 
 * Author: [Your Name]
 * Date: YYYY-MM-DD
 */
```

## Common Migration Patterns

### 1. Creating New Tables
```sql
-- Create enum type if needed
create type user_role as enum ('admin', 'staff', 'customer');

-- Create the table with proper constraints
create table users (
  id bigint generated always as identity primary key,
  email text not null unique,
  role user_role not null default 'customer',
  full_name text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  deleted_at timestamptz,
  version integer not null default 1,
  
  -- Add constraints with meaningful names
  constraint users_email_format check (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Add table comment
comment on table users is 'User accounts with authentication and role information';

-- Add column comments
comment on column users.role is 'User role determining access permissions';
comment on column users.version is 'Optimistic locking version number';

-- Enable RLS
alter table users enable row level security;

-- Create RLS policies for authenticated users
create policy "Users can view their own data"
  on users
  for select
  to authenticated
  using (auth.uid() = id);

create policy "Users can update their own data"
  on users
  for update
  to authenticated
  using (auth.uid() = id)
  with check (
    auth.uid() = id
    and deleted_at is null
    -- Prevent role escalation
    and (role = 'customer' or auth.jwt() ->> 'role' = 'admin')
  );

-- Create RLS policies for anonymous users if needed
create policy "Public can view basic user info"
  on users
  for select
  to anon
  using (
    deleted_at is null
    -- Only allow viewing specific columns via security definer function
  );

-- Create indexes for common query patterns
create index users_email_idx on users (email) where deleted_at is null;
create index users_role_idx on users (role) where deleted_at is null;
```

### 2. Adding Columns
```sql
-- Add new columns with clear comments
alter table users 
  -- Add nullable column
  add column phone_number text,
  -- Add column with default
  add column is_verified boolean not null default false,
  -- Add column with constraint
  add column country_code text 
    constraint users_country_code_length 
    check (char_length(country_code) = 2);

-- Add column comments
comment on column users.phone_number is 'Optional phone number for 2FA';
comment on column users.is_verified is 'Whether the user has verified their email';
comment on column users.country_code is 'ISO 3166-1 alpha-2 country code';

-- Update RLS policies if needed
drop policy if exists "Users can update their own data" on users;
create policy "Users can update their own data"
  on users
  for update
  to authenticated
  using (auth.uid() = id)
  with check (
    auth.uid() = id
    and deleted_at is null
    and (
      role = 'customer' 
      or auth.jwt() ->> 'role' = 'admin'
    )
  );
```

### 3. Creating Join Tables
```sql
-- Create join table with proper naming
create table user_organizations (
  user_id bigint not null references users(id),
  organization_id bigint not null references organizations(id),
  role user_role not null default 'member',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  
  -- Always include primary key
  constraint user_organizations_pkey 
    primary key (user_id, organization_id),
    
  -- Add any additional constraints
  constraint user_organizations_valid_dates
    check (updated_at >= created_at)
);

-- Enable RLS
alter table user_organizations enable row level security;

-- Create RLS policies
create policy "Users can view their organization memberships"
  on user_organizations
  for select
  to authenticated
  using (auth.uid() = user_id);

create policy "Organization admins can manage memberships"
  on user_organizations
  for all
  to authenticated
  using (
    exists (
      select 1 
      from user_organizations
      where user_id = auth.uid()
        and organization_id = user_organizations.organization_id
        and role = 'admin'
    )
  );
```

### 4. Adding Indexes
```sql
-- Create indexes for common query patterns
create index users_search_idx on users 
  using gin(to_tsvector('english', full_name));

-- Create partial indexes for better performance
create index active_users_idx 
  on users (created_at)
  where deleted_at is null;

-- Create composite indexes for join conditions
create index user_orgs_lookup_idx 
  on user_organizations (user_id, organization_id, role)
  where deleted_at is null;
```

### 5. Data Migrations
```sql
-- Add clear warning for destructive operations
/* WARNING: This migration modifies existing data */

-- Always use transactions for data migrations
begin;

-- Update existing data
update users
set 
  country_code = 'US',
  updated_at = now()
where 
  country_code is null
  and deleted_at is null;

-- Verify the changes
do $$
declare
  invalid_count integer;
begin
  select count(*)
  into invalid_count
  from users
  where country_code is null
    and deleted_at is null;
    
  if invalid_count > 0 then
    raise exception 'Found % users without country code', invalid_count;
  end if;
end $$;

commit;
```

### 6. Creating Functions
```sql
-- Create helper functions with proper security
create or replace function get_user_organizations(
  p_user_id bigint
)
returns table (
  organization_id bigint,
  organization_name text,
  user_role user_role
)
language sql
security definer
set search_path = public
stable
as $$
  select
    o.id as organization_id,
    o.name as organization_name,
    uo.role as user_role
  from
    organizations o
  join
    user_organizations uo on uo.organization_id = o.id
  where
    uo.user_id = p_user_id
    and uo.deleted_at is null
    and o.deleted_at is null;
$$;

-- Add function comment
comment on function get_user_organizations is 'Get all organizations a user belongs to with their roles';
```

## Best Practices

### 1. Security
- Always enable RLS on new tables
- Create granular policies for each operation
- Use security definer functions carefully
- Document security implications
- Validate inputs and handle edge cases

### 2. Performance
- Add appropriate indexes
- Consider query patterns
- Use partial indexes when possible
- Monitor index usage
- Document performance considerations

### 3. Maintainability
- Use clear, descriptive names
- Add thorough comments
- Follow consistent formatting
- Document dependencies
- Include rollback procedures

### 4. Data Integrity
- Use appropriate constraints
- Implement proper foreign keys
- Add validation checks
- Handle NULL values explicitly
- Use transactions for data changes

Remember:
- Test migrations thoroughly
- Document security implications
- Consider performance impact
- Handle errors gracefully
- Follow naming conventions
- Keep migrations atomic
- Include rollback procedures 