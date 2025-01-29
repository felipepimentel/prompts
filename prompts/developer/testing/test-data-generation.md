---
title: "Test Data Generation Guide"
path: "developer/testing/test-data-generation"
tags: ["testing", "data-generation", "database", "test-scenarios"]
description: "A comprehensive guide for generating realistic and diverse test data for database testing and development"
prompt_type: "Testing Framework"
---

<purpose>
To provide a structured approach for generating comprehensive test data that covers various scenarios while maintaining data integrity and realism.
</purpose>

<context>
Use this template when planning and implementing test data generation for database testing, development, or demonstration purposes.
</context>

<instructions>
Provide the following information:

1. Data Requirements
   - Schema Analysis
     * Table structures
     * Field types
     * Constraints
     * Relationships

   - Data Scope
     * Volume needs
     * Data patterns
     * Time ranges
     * Geographic scope

2. Data Categories
   - Standard Cases
     * Common values
     * Typical patterns
     * Normal ranges
     * Expected formats

   - Edge Cases
     * Boundary values
     * Special characters
     * Maximum lengths
     * Minimum values

3. Data Relationships
   - Referential Integrity
     * Foreign keys
     * Cascading effects
     * Circular references
     * Orphaned records

   - Data Dependencies
     * Temporal order
     * Logical sequences
     * Business rules
     * State transitions

4. Generation Strategy
   - Implementation
     * Generation tools
     * Script structure
     * Batch sizes
     * Performance considerations

   - Quality Control
     * Data validation
     * Consistency checks
     * Error scenarios
     * Cleanup procedures

</instructions>

<variables>
- database_type: Database system being used
- data_volume: Amount of test data needed
- schema_complexity: Schema relationship depth
- special_requirements: Specific data needs
</variables>

<examples>
Example 1:
Input: E-commerce database test data
Output:
```sql
-- Test Data Generation Script for E-commerce Database

-- 1. User Data Generation
CREATE OR REPLACE FUNCTION generate_test_users(count INT) RETURNS VOID AS $$
DECLARE
    i INT;
    email_domains TEXT[] := ARRAY['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com'];
    first_names TEXT[] := ARRAY['John', 'Jane', 'Robert', 'Mary', 'William', 'Elizabeth'];
    last_names TEXT[] := ARRAY['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson', 'Taylor'];
BEGIN
    FOR i IN 1..count LOOP
        INSERT INTO users (
            email,
            first_name,
            last_name,
            created_at,
            status
        ) VALUES (
            -- Generate unique email
            LOWER(
                first_names[1 + mod(i, array_length(first_names, 1))] || '.' ||
                last_names[1 + mod(i, array_length(last_names, 1))] ||
                i::TEXT || '@' ||
                email_domains[1 + mod(i, array_length(email_domains, 1))]
            ),
            -- Random first name
            first_names[1 + mod(i, array_length(first_names, 1))],
            -- Random last name
            last_names[1 + mod(i, array_length(last_names, 1))],
            -- Registration date within last year
            NOW() - (random() * interval '365 days'),
            -- Status (mostly active, some inactive)
            CASE WHEN random() < 0.9 THEN 'active' ELSE 'inactive' END
        );
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- 2. Product Data Generation
CREATE OR REPLACE FUNCTION generate_test_products(count INT) RETURNS VOID AS $$
DECLARE
    i INT;
    categories TEXT[] := ARRAY['Electronics', 'Clothing', 'Books', 'Home', 'Sports'];
    product_names TEXT[] := ARRAY['Premium', 'Basic', 'Pro', 'Ultra', 'Essential'];
    product_types TEXT[] := ARRAY['Laptop', 'Phone', 'Tablet', 'Watch', 'Camera'];
BEGIN
    FOR i IN 1..count LOOP
        INSERT INTO products (
            name,
            description,
            category,
            price,
            stock_level,
            created_at,
            status
        ) VALUES (
            -- Generate product name
            product_names[1 + mod(i, array_length(product_names, 1))] || ' ' ||
            product_types[1 + mod(i, array_length(product_types, 1))],
            -- Description
            'High quality ' || product_types[1 + mod(i, array_length(product_types, 1))] ||
            ' for professional use',
            -- Category
            categories[1 + mod(i, array_length(categories, 1))],
            -- Price (random between 10 and 1000)
            10 + (random() * 990)::numeric(10,2),
            -- Stock (random between 0 and 100)
            (random() * 100)::int,
            -- Creation date
            NOW() - (random() * interval '180 days'),
            -- Status (mostly active)
            CASE WHEN random() < 0.95 THEN 'active' ELSE 'discontinued' END
        );
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- 3. Order Data Generation
CREATE OR REPLACE FUNCTION generate_test_orders(count INT) RETURNS VOID AS $$
DECLARE
    i INT;
    user_ids INT[];
    product_ids INT[];
    order_id INT;
    items_count INT;
    selected_product INT;
BEGIN
    -- Get available user and product IDs
    SELECT ARRAY_AGG(id) INTO user_ids FROM users WHERE status = 'active';
    SELECT ARRAY_AGG(id) INTO product_ids FROM products WHERE status = 'active';
    
    FOR i IN 1..count LOOP
        -- Create order
        INSERT INTO orders (
            user_id,
            status,
            created_at,
            total_amount
        ) VALUES (
            -- Random user
            user_ids[1 + mod(i, array_length(user_ids, 1))],
            -- Status (various states)
            CASE (random() * 100)::int % 4
                WHEN 0 THEN 'pending'
                WHEN 1 THEN 'processing'
                WHEN 2 THEN 'completed'
                ELSE 'cancelled'
            END,
            -- Order date
            NOW() - (random() * interval '90 days'),
            0  -- Will be updated after adding items
        ) RETURNING id INTO order_id;

        -- Add 1-5 items to order
        items_count := 1 + (random() * 4)::int;
        FOR j IN 1..items_count LOOP
            selected_product := product_ids[1 + mod((random() * array_length(product_ids, 1))::int, array_length(product_ids, 1))];
            
            INSERT INTO order_items (
                order_id,
                product_id,
                quantity,
                price
            ) VALUES (
                order_id,
                selected_product,
                -- Quantity (1-5)
                1 + (random() * 4)::int,
                -- Get current product price
                (SELECT price FROM products WHERE id = selected_product)
            );
        END LOOP;

        -- Update order total
        UPDATE orders
        SET total_amount = (
            SELECT SUM(quantity * price)
            FROM order_items
            WHERE order_id = orders.id
        )
        WHERE id = order_id;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Generate Test Data
BEGIN;
-- Clean existing data (optional)
TRUNCATE users, products, orders, order_items CASCADE;

-- Generate data
SELECT generate_test_users(1000);    -- 1000 users
SELECT generate_test_products(200);   -- 200 products
SELECT generate_test_orders(5000);    -- 5000 orders

-- Add some edge cases
INSERT INTO users (email, first_name, last_name, status)
VALUES 
    ('', '', '', 'inactive'),        -- Empty strings
    ('test@test.com', 'A', 'B', 'active'),  -- Minimum length
    ('very.long.email.address.that.is.at.the.maximum.length.allowed@really.long.domain.name.com',
     'ThisIsAVeryLongFirstNameThatShouldTestTheLimitsOfTheField',
     'ThisIsAVeryLongLastNameThatShouldTestTheLimitsOfTheField',
     'active');  -- Maximum length

COMMIT;

-- Verify Data
SELECT COUNT(*) as user_count FROM users;
SELECT COUNT(*) as product_count FROM products;
SELECT COUNT(*) as order_count FROM orders;
SELECT COUNT(*) as order_items_count FROM order_items;
```

Example 2:
Input: Blog system test data
Output:
```python
# Test Data Generation Script for Blog System

import faker
import random
from datetime import datetime, timedelta
from typing import List, Dict
from models import User, Post, Comment, Category, Tag

fake = faker.Faker()

class TestDataGenerator:
    def __init__(self):
        self.users: List[User] = []
        self.categories: List[Category] = []
        self.tags: List[Tag] = []
        self.posts: List[Post] = []
        self.comments: List[Comment] = []

    def generate_users(self, count: int) -> None:
        """Generate test users with various profiles."""
        # Regular users
        for _ in range(count):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                password_hash='$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewYpfQN.Pz1cxjEO',  # 'password123'
                created_at=fake.date_time_between(start_date='-1y'),
                is_active=random.random() < 0.9  # 90% active
            )
            self.users.append(user)

        # Edge cases
        edge_case_users = [
            User(  # Minimal data
                username='a',
                email='a@a.a',
                password_hash='$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewYpfQN.Pz1cxjEO',
                created_at=datetime.now(),
                is_active=True
            ),
            User(  # Maximum lengths
                username='a' * 50,
                email='a' * 240 + '@test.com',
                password_hash='$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewYpfQN.Pz1cxjEO',
                created_at=datetime.now(),
                is_active=True
            ),
            User(  # Special characters
                username='User!@#$%^&*()',
                email='special+chars@test.com',
                password_hash='$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewYpfQN.Pz1cxjEO',
                created_at=datetime.now(),
                is_active=True
            )
        ]
        self.users.extend(edge_case_users)

    def generate_categories(self) -> None:
        """Generate blog categories."""
        standard_categories = [
            'Technology', 'Travel', 'Food', 'Lifestyle', 'Business',
            'Health', 'Sports', 'Entertainment', 'Science', 'Education'
        ]
        
        for name in standard_categories:
            category = Category(
                name=name,
                slug=name.lower().replace(' ', '-'),
                description=fake.text(max_nb_chars=200)
            )
            self.categories.append(category)

        # Edge cases
        edge_categories = [
            Category(name='', slug='empty', description=''),  # Empty
            Category(name='A' * 100, slug='max-length', description='A' * 500),  # Max length
            Category(name='Test & Special < > Characters', slug='special-chars', description='Test description')
        ]
        self.categories.extend(edge_categories)

    def generate_posts(self, count: int) -> None:
        """Generate blog posts with varying content and states."""
        for _ in range(count):
            # Select random author and category
            author = random.choice(self.users)
            category = random.choice(self.categories)
            
            # Generate creation date
            created_at = fake.date_time_between(start_date='-1y')
            
            # Determine post status
            status = random.choices(
                ['draft', 'published', 'archived'],
                weights=[0.1, 0.8, 0.1]
            )[0]

            # Create post
            post = Post(
                title=fake.sentence(),
                slug=fake.slug(),
                content=fake.text(max_nb_chars=2000),
                excerpt=fake.text(max_nb_chars=200),
                author_id=author.id,
                category_id=category.id,
                status=status,
                created_at=created_at,
                published_at=created_at if status == 'published' else None
            )
            
            # Add tags (0-5 random tags)
            post.tags = random.sample(self.tags, random.randint(0, min(5, len(self.tags))))
            
            self.posts.append(post)

        # Add edge cases
        edge_case_posts = [
            Post(  # Minimal content
                title='A',
                slug='a',
                content='A',
                author_id=self.users[0].id,
                category_id=self.categories[0].id,
                status='published'
            ),
            Post(  # Maximum content
                title='A' * 200,
                slug='a' * 100,
                content='A' * 10000,
                author_id=self.users[0].id,
                category_id=self.categories[0].id,
                status='published'
            ),
            Post(  # HTML content
                title='<script>alert("XSS")</script>',
                slug='xss-test',
                content='<p>HTML Content</p><script>alert("XSS")</script>',
                author_id=self.users[0].id,
                category_id=self.categories[0].id,
                status='published'
            )
        ]
        self.posts.extend(edge_case_posts)

    def generate_comments(self, min_per_post: int, max_per_post: int) -> None:
        """Generate comments for posts with varying depth and content."""
        for post in self.posts:
            # Generate random number of top-level comments
            comment_count = random.randint(min_per_post, max_per_post)
            
            for _ in range(comment_count):
                author = random.choice(self.users)
                parent_comment = None
                
                # 30% chance of being a reply to another comment
                if self.comments and random.random() < 0.3:
                    parent_comment = random.choice(self.comments)
                
                comment = Comment(
                    content=fake.text(max_nb_chars=500),
                    author_id=author.id,
                    post_id=post.id,
                    parent_id=parent_comment.id if parent_comment else None,
                    created_at=fake.date_time_between(
                        start_date=post.created_at,
                        end_date='now'
                    ),
                    is_approved=random.random() < 0.9  # 90% approved
                )
                self.comments.append(comment)

        # Add edge cases
        edge_case_comments = [
            Comment(  # Empty content
                content='',
                author_id=self.users[0].id,
                post_id=self.posts[0].id,
                is_approved=True
            ),
            Comment(  # Maximum length
                content='A' * 1000,
                author_id=self.users[0].id,
                post_id=self.posts[0].id,
                is_approved=True
            ),
            Comment(  # HTML/Script content
                content='<script>alert("XSS")</script>',
                author_id=self.users[0].id,
                post_id=self.posts[0].id,
                is_approved=True
            )
        ]
        self.comments.extend(edge_case_comments)

    def generate_all(self) -> None:
        """Generate all test data in proper order."""
        self.generate_users(100)        # 100 users
        self.generate_categories()      # Standard categories + edge cases
        self.generate_posts(200)        # 200 posts
        self.generate_comments(0, 10)   # 0-10 comments per post

    def verify_data(self) -> Dict[str, int]:
        """Verify generated data counts and relationships."""
        return {
            'users': len(self.users),
            'categories': len(self.categories),
            'posts': len(self.posts),
            'comments': len(self.comments),
            'approved_comments': len([c for c in self.comments if c.is_approved]),
            'published_posts': len([p for p in self.posts if p.status == 'published'])
        }

# Usage
generator = TestDataGenerator()
generator.generate_all()
print(generator.verify_data())
```
</examples>

<notes>
- Maintain referential integrity
- Include edge cases
- Generate realistic data
- Consider performance
- Verify data consistency
- Document assumptions
- Include cleanup process
- Test generated data
</notes> 