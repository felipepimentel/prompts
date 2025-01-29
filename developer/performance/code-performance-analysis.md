---
title: "Code Performance Analysis Guide"
path: "developer/performance/code-performance-analysis"
tags: ["performance", "optimization", "profiling", "best-practices"]
description: "A comprehensive guide for analyzing and optimizing code performance through systematic review and improvements"
prompt_type: "Analysis Framework"
---

<purpose>
To provide a structured approach for analyzing code performance, identifying bottlenecks, and implementing effective optimizations.
</purpose>

<context>
Use this template when conducting performance analysis of code to identify optimization opportunities and improve overall system efficiency.
</context>

<instructions>
Provide the following analysis information:

1. Performance Context
   - System Overview
     * Code environment
     * Runtime platform
     * Resource constraints
     * Performance targets

   - Analysis Scope
     * Critical paths
     * Performance metrics
     * Load patterns
     * Bottleneck areas

2. Performance Analysis
   - Time Complexity
     * Algorithm efficiency
     * Loop optimizations
     * Recursive patterns
     * Data structure usage

   - Resource Usage
     * Memory allocation
     * CPU utilization
     * I/O operations
     * Network calls

3. Optimization Areas
   - Code Level
     * Algorithmic improvements
     * Caching strategies
     * Parallel processing
     * Async operations

   - Resource Management
     * Memory optimization
     * Connection pooling
     * Resource cleanup
     * Load balancing

4. Implementation Strategy
   - Optimization Plan
     * Priority areas
     * Expected gains
     * Implementation steps
     * Verification methods

   - Trade-offs
     * Complexity vs speed
     * Memory vs CPU
     * Maintainability
     * Scalability

</instructions>

<variables>
- runtime_environment: Execution platform details
- performance_targets: Performance goals
- resource_constraints: System limitations
- optimization_priorities: Key areas for improvement
</variables>

<examples>
Example 1:
Input: Database query optimization
Output:
```markdown
# Performance Analysis Report: Database Queries

## System Context
- **Database:** PostgreSQL 13
- **Load:** 1000 req/min peak
- **Data Size:** 500GB
- **Current Response:** avg 2.5s

## Performance Analysis

### 1. Query Performance
#### Original Query
```sql
SELECT p.*, c.name as category_name, COUNT(r.id) as review_count
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
LEFT JOIN reviews r ON p.id = r.product_id
WHERE p.price > 100
  AND p.status = 'active'
GROUP BY p.id, c.name
ORDER BY p.created_at DESC;
```

#### Issues Identified
1. **Full Table Scan**
   - No index on price column
   - Sequential scan on large products table
   - Impact: O(n) complexity

2. **Inefficient Joins**
   - Cartesian product with reviews
   - Missing indexes on foreign keys
   - Impact: Exponential growth with data

3. **Memory Usage**
   - Large result set
   - Unnecessary columns
   - Impact: High memory consumption

### Optimizations

1. **Index Optimization**
```sql
-- Add composite index for common filters
CREATE INDEX idx_products_status_price 
ON products(status, price);

-- Add index for sorting
CREATE INDEX idx_products_created_at
ON products(created_at DESC);

-- Add indexes for foreign keys
CREATE INDEX idx_reviews_product_id
ON reviews(product_id);
```

2. **Query Rewrite**
```sql
-- Optimized query
WITH product_reviews AS (
  SELECT product_id, COUNT(*) as review_count
  FROM reviews
  GROUP BY product_id
)
SELECT 
  p.id,
  p.name,
  p.price,
  c.name as category_name,
  COALESCE(pr.review_count, 0) as review_count
FROM products p
LEFT JOIN categories c 
  ON p.category_id = c.id
LEFT JOIN product_reviews pr 
  ON p.id = pr.product_id
WHERE p.price > 100
  AND p.status = 'active'
ORDER BY p.created_at DESC;
```

3. **Caching Strategy**
```python
def get_product_details(product_id):
    # Check cache first
    cache_key = f"product:{product_id}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    # If not in cache, fetch and store
    product_data = fetch_product_data(product_id)
    cache.set(cache_key, product_data, timeout=3600)
    return product_data
```

### Performance Impact
- Query time: 2.5s → 200ms
- Memory usage: -40%
- CPU load: -30%
- Cache hit ratio: 85%

## Recommendations

### Immediate Actions
1. Implement optimized query
2. Add suggested indexes
3. Enable query caching
4. Monitor query plans

### Long-term Improvements
1. Consider data partitioning
2. Implement connection pooling
3. Add query timeout limits
4. Regular index maintenance
```

Example 2:
Input: API endpoint optimization
Output:
```markdown
# Performance Analysis: API Endpoint

## System Overview
- **Framework:** Node.js/Express
- **Database:** MongoDB
- **Cache:** Redis
- **Load:** 500 req/sec

## Performance Analysis

### 1. Request Processing
#### Original Implementation
```javascript
// Current implementation
app.get('/api/dashboard', async (req, res) => {
  try {
    const userStats = await UserStats.find({});
    const orderStats = await OrderStats.find({});
    const productStats = await ProductStats.find({});
    
    const dashboard = {
      users: processUserStats(userStats),
      orders: processOrderStats(orderStats),
      products: processProductStats(productStats)
    };
    
    res.json(dashboard);
  } catch (error) {
    res.status(500).send(error);
  }
});
```

#### Issues Identified
1. **Sequential Database Queries**
   - Three separate database calls
   - Blocking operations
   - Impact: High latency

2. **Unnecessary Data Loading**
   - Full collection scans
   - Excess data transfer
   - Impact: High memory usage

3. **No Caching**
   - Repeated computations
   - Database pressure
   - Impact: Poor scalability

### Optimizations

1. **Parallel Processing**
```javascript
app.get('/api/dashboard', async (req, res) => {
  try {
    // Parallel database queries
    const [userStats, orderStats, productStats] = await Promise.all([
      UserStats.find({}).lean(),
      OrderStats.find({}).lean(),
      ProductStats.find({}).lean()
    ]);
    
    // Process data concurrently
    const dashboard = await Promise.all([
      processUserStats(userStats),
      processOrderStats(orderStats),
      processProductStats(productStats)
    ]).then(([users, orders, products]) => ({
      users,
      orders,
      products
    }));
    
    res.json(dashboard);
  } catch (error) {
    res.status(500).send(error);
  }
});
```

2. **Data Aggregation**
```javascript
// Optimize database queries
const userStats = await UserStats.aggregate([
  { $match: { date: { $gte: startDate } } },
  { $group: {
      _id: null,
      totalUsers: { $sum: 1 },
      activeUsers: { $sum: { $cond: ["$isActive", 1, 0] } }
    }}
]);
```

3. **Caching Implementation**
```javascript
const CACHE_TTL = 5 * 60; // 5 minutes

async function getDashboardData() {
  const cacheKey = 'dashboard:stats';
  
  // Try cache first
  const cachedData = await redis.get(cacheKey);
  if (cachedData) {
    return JSON.parse(cachedData);
  }
  
  // If not in cache, compute and store
  const dashboard = await computeDashboardStats();
  await redis.setex(cacheKey, CACHE_TTL, JSON.stringify(dashboard));
  
  return dashboard;
}

// Memory-efficient streaming for large datasets
app.get('/api/large-dataset', (req, res) => {
  const cursor = LargeCollection.find().cursor();
  res.type('json');
  res.write('[');
  
  let first = true;
  cursor.on('data', (doc) => {
    if (!first) res.write(',');
    res.write(JSON.stringify(doc));
    first = false;
  });
  
  cursor.on('end', () => {
    res.write(']');
    res.end();
  });
});
```

### Performance Metrics

#### Before Optimization
- Average response time: 1200ms
- Memory usage: 1.2GB
- CPU utilization: 85%
- Max concurrent requests: 200

#### After Optimization
- Average response time: 300ms
- Memory usage: 800MB
- CPU utilization: 60%
- Max concurrent requests: 800

## Implementation Plan

### Phase 1: Quick Wins
1. Implement parallel processing
2. Add basic caching
3. Optimize database queries
4. Add monitoring

### Phase 2: Advanced Optimization
1. Implement data streaming
2. Add cache warming
3. Setup load balancing
4. Implement circuit breakers

### Phase 3: Monitoring
1. Set up performance metrics
2. Configure alerts
3. Implement logging
4. Create dashboards

## Trade-offs Considered
- Cache freshness vs performance
- Memory usage vs CPU load
- Complexity vs maintainability
- Latency vs throughput
```

</examples>

<notes>
- Profile before optimizing
- Measure improvements
- Consider trade-offs
- Test under load
- Document changes
- Monitor impact
- Plan for scalability
- Review regularly
</notes> 