---
category: Developer
description: A comprehensive guide for integrating different frameworks and technologies
  in modern applications, focusing on best practices, common patterns, and maintainable
  architecture.
model: GPT-4
path: developer/guidelines/framework-integration-guide
prompt_type: Instruction-based prompting
tags:
- integration
- frameworks
- architecture
- development
- best-practices
title: Framework Integration Guide
version: '1.0'
---

# Framework Integration Guide

## Core Principles
1. Modularity - Keep integrations loosely coupled
2. Maintainability - Ensure code is maintainable and testable
3. Scalability - Design for future growth and changes
4. Compatibility - Handle version conflicts and dependencies

## Integration Patterns

### 1. API Integration
```typescript
// src/lib/api/client.ts
import axios, { type AxiosInstance } from 'axios'

export class ApiClient {
  private client: AxiosInstance

  constructor(baseURL: string) {
    this.client = axios.create({
      baseURL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    })
  }

  async request<T>(config: {
    method: 'GET' | 'POST' | 'PUT' | 'DELETE'
    url: string
    data?: unknown
  }): Promise<T> {
    try {
      const response = await this.client.request(config)
      return response.data
    } catch (error) {
      throw this.handleError(error)
    }
  }

  private handleError(error: unknown): Error {
    if (axios.isAxiosError(error)) {
      return new Error(error.response?.data?.message || 'API Error')
    }
    return new Error('Unknown error occurred')
  }
}
```

### 2. Database Integration
```typescript
// src/lib/db/client.ts
import { Pool, type QueryResult } from 'pg'
import { Redis } from 'ioredis'

export class DatabaseClient {
  private pool: Pool
  private redis: Redis

  constructor(config: {
    postgres: {
      host: string
      port: number
      database: string
      user: string
      password: string
    }
    redis: {
      host: string
      port: number
    }
  }) {
    this.pool = new Pool(config.postgres)
    this.redis = new Redis(config.redis)
  }

  async query<T>(sql: string, params?: unknown[]): Promise<QueryResult<T>> {
    const client = await this.pool.connect()
    try {
      return await client.query(sql, params)
    } finally {
      client.release()
    }
  }

  async cacheGet<T>(key: string): Promise<T | null> {
    const data = await this.redis.get(key)
    return data ? JSON.parse(data) : null
  }

  async cacheSet(key: string, value: unknown, ttl?: number): Promise<void> {
    const data = JSON.stringify(value)
    if (ttl) {
      await this.redis.set(key, data, 'EX', ttl)
    } else {
      await this.redis.set(key, data)
    }
  }
}
```

## Service Integration

### 1. Message Queue Integration
```typescript
// src/lib/queue/client.ts
import { Queue, Worker, QueueScheduler } from 'bullmq'
import { Redis } from 'ioredis'

export class QueueService {
  private queue: Queue
  private worker: Worker
  private scheduler: QueueScheduler

  constructor(
    queueName: string,
    redis: Redis,
    processor: (job: any) => Promise<void>
  ) {
    this.queue = new Queue(queueName, { connection: redis })
    this.worker = new Worker(queueName, processor, { connection: redis })
    this.scheduler = new QueueScheduler(queueName, { connection: redis })
    this.setupListeners()
  }

  private setupListeners(): void {
    this.worker.on('completed', (job) => {
      console.log(`Job ${job.id} completed`)
    })

    this.worker.on('failed', (job, error) => {
      console.error(`Job ${job?.id} failed:`, error)
    })
  }

  async addJob(data: unknown, options?: {
    delay?: number
    priority?: number
  }): Promise<void> {
    await this.queue.add('process', data, options)
  }
}
```

### 2. Search Integration
```typescript
// src/lib/search/client.ts
import { Client } from '@elastic/elasticsearch'

export class SearchService {
  private client: Client

  constructor(config: {
    node: string
    auth: {
      username: string
      password: string
    }
  }) {
    this.client = new Client(config)
  }

  async index(index: string, document: unknown): Promise<void> {
    await this.client.index({
      index,
      document,
    })
  }

  async search<T>(index: string, query: {
    query: unknown
    from?: number
    size?: number
  }): Promise<T[]> {
    const result = await this.client.search({
      index,
      ...query,
    })

    return result.hits.hits.map((hit) => hit._source as T)
  }
}
```

## Frontend Integration

### 1. State Management
```typescript
// src/lib/store/index.ts
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

interface AppState {
  theme: 'light' | 'dark'
  setTheme: (theme: 'light' | 'dark') => void
  user: {
    id: string
    name: string
  } | null
  setUser: (user: AppState['user']) => void
}

export const useStore = create<AppState>()(
  persist(
    (set) => ({
      theme: 'light',
      setTheme: (theme) => set({ theme }),
      user: null,
      setUser: (user) => set({ user }),
    }),
    {
      name: 'app-storage',
    }
  )
)
```

### 2. API Integration
```typescript
// src/lib/api/hooks.ts
import { useQuery, useMutation } from '@tanstack/react-query'
import { ApiClient } from './client'

const api = new ApiClient(process.env.NEXT_PUBLIC_API_URL!)

export function useUser(id: string) {
  return useQuery({
    queryKey: ['user', id],
    queryFn: () => api.request({
      method: 'GET',
      url: `/users/${id}`,
    }),
  })
}

export function useUpdateUser() {
  return useMutation({
    mutationFn: (data: { id: string; name: string }) =>
      api.request({
        method: 'PUT',
        url: `/users/${data.id}`,
        data,
      }),
  })
}
```

## Testing Integration

### 1. Integration Tests
```typescript
// src/tests/integration/api.test.ts
import { describe, test, expect, beforeAll, afterAll } from 'vitest'
import { ApiClient } from '@/lib/api/client'
import { setupTestDatabase } from '../utils/db'
import { startTestServer } from '../utils/server'

describe('API Integration', () => {
  let api: ApiClient
  let cleanup: () => Promise<void>

  beforeAll(async () => {
    const db = await setupTestDatabase()
    const server = await startTestServer()
    api = new ApiClient(server.url)
    cleanup = async () => {
      await db.cleanup()
      await server.close()
    }
  })

  afterAll(async () => {
    await cleanup()
  })

  test('creates and retrieves user', async () => {
    const user = await api.request({
      method: 'POST',
      url: '/users',
      data: { name: 'Test User' },
    })

    expect(user).toHaveProperty('id')

    const retrieved = await api.request({
      method: 'GET',
      url: `/users/${user.id}`,
    })

    expect(retrieved).toEqual(user)
  })
})
```

## Best Practices

### 1. Architecture
- Use dependency injection
- Implement interface segregation
- Follow SOLID principles
- Keep services decoupled
- Use appropriate design patterns

### 2. Error Handling
- Implement proper error boundaries
- Use typed errors
- Handle async errors
- Log errors appropriately
- Provide meaningful error messages

### 3. Performance
- Implement caching strategies
- Optimize database queries
- Use connection pooling
- Monitor memory usage
- Profile application performance

### 4. Security
- Validate input data
- Implement proper authentication
- Use secure communication
- Handle sensitive data properly
- Regular security audits

### 5. Testing
- Write integration tests
- Implement end-to-end tests
- Use proper test isolation
- Mock external services
- Maintain test coverage

## Resources
1. [Next.js Documentation](https://nextjs.org/docs)
2. [Prisma Documentation](https://www.prisma.io/docs)
3. [React Query Documentation](https://tanstack.com/query/latest)
4. [Zustand Documentation](https://github.com/pmndrs/zustand)
5. [Testing Library Documentation](https://testing-library.com/docs/)