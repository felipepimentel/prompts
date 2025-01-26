---
category: Developer
description: A comprehensive guide for building robust LLM applications using TypeScript
  and modern AI development practices
model: GPT-4
path: developer/frameworks/typescript/typescript-llm-stack-guide
prompt_type: Instruction-based prompting
tags:
- typescript
- llm
- ai
- development
- backend
title: TypeScript LLM Tech Stack Guide
version: '1.0'
---

# TypeScript LLM Tech Stack Guide

## Core Principles
- Type safety
- Scalability
- Maintainability
- Performance
- Security

## Project Setup

### Environment Configuration
```typescript
// config/env.ts
import { z } from 'zod'
import { config } from 'dotenv'

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  PORT: z.string().transform(Number),
  OPENAI_API_KEY: z.string(),
  ANTHROPIC_API_KEY: z.string().optional(),
  PINECONE_API_KEY: z.string().optional(),
  REDIS_URL: z.string().optional(),
})

config()

export const env = envSchema.parse(process.env)
```

### Project Structure
```bash
src/
├── config/
│   ├── env.ts
│   └── constants.ts
├── lib/
│   ├── llm/
│   │   ├── openai.ts
│   │   ├── anthropic.ts
│   │   └── types.ts
│   ├── vectorstore/
│   │   ├── pinecone.ts
│   │   └── types.ts
│   └── cache/
│       ├── redis.ts
│       └── types.ts
├── services/
│   ├── completion/
│   │   ├── service.ts
│   │   └── types.ts
│   ├── embedding/
│   │   ├── service.ts
│   │   └── types.ts
│   └── rag/
│       ├── service.ts
│       └── types.ts
└── api/
    ├── routes/
    │   ├── completion.ts
    │   ├── embedding.ts
    │   └── rag.ts
    └── middleware/
        ├── rateLimit.ts
        └── validation.ts
```

## LLM Integration

### OpenAI Client
```typescript
// lib/llm/openai.ts
import OpenAI from 'openai'
import { env } from '@/config/env'
import { ChatMessage, CompletionOptions } from './types'

export class OpenAIClient {
  private client: OpenAI

  constructor() {
    this.client = new OpenAI({
      apiKey: env.OPENAI_API_KEY,
    })
  }

  async complete(
    messages: ChatMessage[],
    options: CompletionOptions = {}
  ) {
    const response = await this.client.chat.completions.create({
      model: options.model || 'gpt-4-turbo-preview',
      messages: messages.map(msg => ({
        role: msg.role,
        content: msg.content,
      })),
      temperature: options.temperature || 0.7,
      max_tokens: options.maxTokens,
      stream: options.stream,
    })

    return response
  }

  async embed(text: string) {
    const response = await this.client.embeddings.create({
      model: 'text-embedding-3-small',
      input: text,
    })

    return response.data[0].embedding
  }
}
```

### Anthropic Client
```typescript
// lib/llm/anthropic.ts
import Anthropic from '@anthropic-ai/sdk'
import { env } from '@/config/env'
import { ChatMessage, CompletionOptions } from './types'

export class AnthropicClient {
  private client: Anthropic

  constructor() {
    this.client = new Anthropic({
      apiKey: env.ANTHROPIC_API_KEY,
    })
  }

  async complete(
    messages: ChatMessage[],
    options: CompletionOptions = {}
  ) {
    const response = await this.client.messages.create({
      model: options.model || 'claude-3-opus-20240229',
      messages: messages.map(msg => ({
        role: msg.role,
        content: msg.content,
      })),
      temperature: options.temperature || 0.7,
      max_tokens: options.maxTokens,
      stream: options.stream,
    })

    return response
  }
}
```

### Type Definitions
```typescript
// lib/llm/types.ts
export interface ChatMessage {
  role: 'system' | 'user' | 'assistant'
  content: string
}

export interface CompletionOptions {
  model?: string
  temperature?: number
  maxTokens?: number
  stream?: boolean
}

export interface CompletionResponse {
  id: string
  choices: Array<{
    message: ChatMessage
    finishReason: string
  }>
  usage: {
    promptTokens: number
    completionTokens: number
    totalTokens: number
  }
}
```

## Vector Store Integration

### Pinecone Setup
```typescript
// lib/vectorstore/pinecone.ts
import { Pinecone } from '@pinecone-database/pinecone'
import { env } from '@/config/env'
import { Document, QueryOptions } from './types'

export class PineconeStore {
  private client: Pinecone
  private index: string

  constructor(index: string) {
    this.client = new Pinecone({
      apiKey: env.PINECONE_API_KEY!,
    })
    this.index = index
  }

  async upsert(documents: Document[]) {
    const index = this.client.index(this.index)
    
    await index.upsert(
      documents.map(doc => ({
        id: doc.id,
        values: doc.embedding,
        metadata: doc.metadata,
      }))
    )
  }

  async query(
    embedding: number[],
    options: QueryOptions = {}
  ) {
    const index = this.client.index(this.index)
    
    const results = await index.query({
      vector: embedding,
      topK: options.topK || 5,
      includeMetadata: true,
    })

    return results.matches
  }
}
```

### Vector Store Types
```typescript
// lib/vectorstore/types.ts
export interface Document {
  id: string
  embedding: number[]
  metadata?: Record<string, any>
}

export interface QueryOptions {
  topK?: number
  filter?: Record<string, any>
}

export interface QueryResult {
  id: string
  score: number
  metadata?: Record<string, any>
}
```

## Caching Layer

### Redis Integration
```typescript
// lib/cache/redis.ts
import { Redis } from 'ioredis'
import { env } from '@/config/env'
import { CacheOptions } from './types'

export class RedisCache {
  private client: Redis

  constructor() {
    this.client = new Redis(env.REDIS_URL!)
  }

  async get<T>(key: string): Promise<T | null> {
    const value = await this.client.get(key)
    return value ? JSON.parse(value) : null
  }

  async set<T>(
    key: string,
    value: T,
    options: CacheOptions = {}
  ) {
    const serialized = JSON.stringify(value)
    
    if (options.ttl) {
      await this.client.setex(key, options.ttl, serialized)
    } else {
      await this.client.set(key, serialized)
    }
  }

  async delete(key: string) {
    await this.client.del(key)
  }
}
```

## Service Layer

### Completion Service
```typescript
// services/completion/service.ts
import { OpenAIClient } from '@/lib/llm/openai'
import { AnthropicClient } from '@/lib/llm/anthropic'
import { RedisCache } from '@/lib/cache/redis'
import {
  CompletionRequest,
  CompletionResponse,
} from './types'

export class CompletionService {
  private openai: OpenAIClient
  private anthropic: AnthropicClient
  private cache: RedisCache

  constructor() {
    this.openai = new OpenAIClient()
    this.anthropic = new AnthropicClient()
    this.cache = new RedisCache()
  }

  async complete(
    request: CompletionRequest
  ): Promise<CompletionResponse> {
    const cacheKey = this.getCacheKey(request)
    const cached = await this.cache.get<CompletionResponse>(cacheKey)

    if (cached) {
      return cached
    }

    const client = request.provider === 'anthropic'
      ? this.anthropic
      : this.openai

    const response = await client.complete(
      request.messages,
      request.options
    )

    await this.cache.set(cacheKey, response, { ttl: 3600 })

    return response
  }

  private getCacheKey(request: CompletionRequest): string {
    return `completion:${JSON.stringify(request)}`
  }
}
```

### RAG Service
```typescript
// services/rag/service.ts
import { OpenAIClient } from '@/lib/llm/openai'
import { PineconeStore } from '@/lib/vectorstore/pinecone'
import { RedisCache } from '@/lib/cache/redis'
import { RAGRequest, RAGResponse } from './types'

export class RAGService {
  private llm: OpenAIClient
  private vectorstore: PineconeStore
  private cache: RedisCache

  constructor() {
    this.llm = new OpenAIClient()
    this.vectorstore = new PineconeStore('your-index-name')
    this.cache = new RedisCache()
  }

  async process(request: RAGRequest): Promise<RAGResponse> {
    const cacheKey = this.getCacheKey(request)
    const cached = await this.cache.get<RAGResponse>(cacheKey)

    if (cached) {
      return cached
    }

    // Generate embedding for the query
    const queryEmbedding = await this.llm.embed(request.query)

    // Retrieve relevant documents
    const results = await this.vectorstore.query(
      queryEmbedding,
      { topK: request.topK }
    )

    // Generate completion with context
    const completion = await this.llm.complete([
      {
        role: 'system',
        content: 'Use the following context to answer the question:\n\n' +
          results.map(r => r.metadata?.text).join('\n\n'),
      },
      {
        role: 'user',
        content: request.query,
      },
    ])

    const response = {
      answer: completion.choices[0].message.content,
      sources: results.map(r => ({
        id: r.id,
        score: r.score,
        metadata: r.metadata,
      })),
    }

    await this.cache.set(cacheKey, response, { ttl: 3600 })

    return response
  }

  private getCacheKey(request: RAGRequest): string {
    return `rag:${JSON.stringify(request)}`
  }
}
```

## API Layer

### Rate Limiting
```typescript
// api/middleware/rateLimit.ts
import rateLimit from 'express-rate-limit'
import RedisStore from 'rate-limit-redis'
import { RedisCache } from '@/lib/cache/redis'

export const createRateLimiter = (
  windowMs: number,
  max: number
) => {
  const cache = new RedisCache()

  return rateLimit({
    windowMs,
    max,
    standardHeaders: true,
    store: new RedisStore({
      sendCommand: (...args: string[]) => cache.client.call(...args),
    }),
  })
}
```

### Validation Middleware
```typescript
// api/middleware/validation.ts
import { z } from 'zod'
import { Request, Response, NextFunction } from 'express'

export const validate = (schema: z.ZodSchema) => {
  return async (
    req: Request,
    res: Response,
    next: NextFunction
  ) => {
    try {
      const validated = await schema.parseAsync({
        body: req.body,
        query: req.query,
        params: req.params,
      })

      req.body = validated.body
      req.query = validated.query
      req.params = validated.params

      next()
    } catch (error) {
      if (error instanceof z.ZodError) {
        res.status(400).json({
          error: 'Validation failed',
          details: error.errors,
        })
      } else {
        next(error)
      }
    }
  }
}
```

## Best Practices

### Error Handling
1. Use custom error classes
2. Implement error boundaries
3. Log errors appropriately
4. Return consistent error responses
5. Handle rate limits gracefully

### Performance
- Implement caching strategies
- Use connection pooling
- Optimize embeddings
- Batch operations
- Monitor resource usage

### Security
1. API key management
2. Input validation
3. Rate limiting
4. Content filtering
5. Audit logging

### Monitoring
- Request metrics
- Error tracking
- Performance monitoring
- Cost tracking
- Usage analytics

## Resources
- OpenAI documentation
- Anthropic documentation
- Pinecone documentation
- TypeScript guides
- Security best practices