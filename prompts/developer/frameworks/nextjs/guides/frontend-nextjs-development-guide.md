---
title: "Next.js Frontend Development Guide"
path: "developer/frameworks/nextjs/guides/frontend-nextjs-development-guide"
tags: ["nextjs", "frontend", "react", "typescript", "development", "guide", "web-development", "best-practices", "patterns"]
description: "A comprehensive guide for developing frontend applications with Next.js, focusing on modern development patterns, component architecture, and best practices"
---

# Next.js Frontend Development Guide

## Overview
This guide provides comprehensive patterns and best practices for developing frontend applications using Next.js, focusing on modern development approaches, component architecture, and maintainable code structure.

## Core Concepts

### 1. Component Architecture

#### Atomic Design Pattern
```typescript
src/
  components/
    atoms/         # Basic building blocks
      Button/
        index.tsx
        types.ts
        styles.module.css
    molecules/     # Simple component combinations
      SearchBar/
        index.tsx
        types.ts
    organisms/     # Complex component combinations
      Header/
        index.tsx
        types.ts
    templates/     # Page layouts
      DashboardLayout/
        index.tsx
        types.ts
```

### 2. State Management

#### Local State with Hooks
```typescript
// src/components/molecules/Counter/index.tsx
'use client'

import { useState, useCallback } from 'react'
import { Button } from '@/components/atoms/Button'

export function Counter() {
  const [count, setCount] = useState(0)
  
  const increment = useCallback(() => {
    setCount(prev => prev + 1)
  }, [])
  
  return (
    <div className="flex items-center gap-4">
      <span className="text-lg font-bold">{count}</span>
      <Button onClick={increment}>Increment</Button>
    </div>
  )
}
```

#### Global State with Zustand
```typescript
// src/store/auth.ts
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

interface AuthState {
  user: User | null
  token: string | null
  login: (credentials: Credentials) => Promise<void>
  logout: () => void
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      token: null,
      login: async (credentials) => {
        const { user, token } = await loginApi(credentials)
        set({ user, token })
      },
      logout: () => set({ user: null, token: null }),
    }),
    {
      name: 'auth-storage',
    }
  )
)
```

### 3. Data Fetching

#### Server Components
```typescript
// src/app/posts/page.tsx
import { PostCard } from '@/components/molecules/PostCard'
import { getPosts } from '@/lib/api'

export default async function PostsPage() {
  const posts = await getPosts()
  
  return (
    <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  )
}
```

#### Client Components with SWR
```typescript
// src/components/organisms/PostList/index.tsx
'use client'

import useSWR from 'swr'
import { PostCard } from '@/components/molecules/PostCard'
import { Spinner } from '@/components/atoms/Spinner'

export function PostList() {
  const { data: posts, error, isLoading } = useSWR('/api/posts')
  
  if (isLoading) return <Spinner />
  if (error) return <div>Failed to load posts</div>
  
  return (
    <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  )
}
```

### 4. Form Handling

#### Form Management with React Hook Form
```typescript
// src/components/organisms/ContactForm/index.tsx
'use client'

import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { Button } from '@/components/atoms/Button'
import { Input } from '@/components/atoms/Input'

const schema = z.object({
  name: z.string().min(2, 'Name must be at least 2 characters'),
  email: z.string().email('Invalid email address'),
  message: z.string().min(10, 'Message must be at least 10 characters'),
})

type FormData = z.infer<typeof schema>

export function ContactForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormData>({
    resolver: zodResolver(schema),
  })
  
  const onSubmit = async (data: FormData) => {
    try {
      await fetch('/api/contact', {
        method: 'POST',
        body: JSON.stringify(data),
      })
    } catch (error) {
      console.error('Failed to submit form:', error)
    }
  }
  
  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      <Input
        label="Name"
        error={errors.name?.message}
        {...register('name')}
      />
      <Input
        label="Email"
        type="email"
        error={errors.email?.message}
        {...register('email')}
      />
      <Input
        label="Message"
        as="textarea"
        error={errors.message?.message}
        {...register('message')}
      />
      <Button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Sending...' : 'Send Message'}
      </Button>
    </form>
  )
}
```

### 5. Routing and Navigation

#### Dynamic Routes
```typescript
// src/app/posts/[slug]/page.tsx
import { notFound } from 'next/navigation'
import { getPost } from '@/lib/api'

interface Props {
  params: { slug: string }
}

export default async function PostPage({ params }: Props) {
  const post = await getPost(params.slug)
  
  if (!post) {
    notFound()
  }
  
  return (
    <article className="prose prose-lg mx-auto">
      <h1>{post.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
    </article>
  )
}
```

#### Client-Side Navigation
```typescript
// src/components/molecules/PostCard/index.tsx
'use client'

import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { type Post } from '@/types'

interface Props {
  post: Post
}

export function PostCard({ post }: Props) {
  const router = useRouter()
  
  return (
    <div className="rounded-lg border p-6">
      <h2 className="text-xl font-bold">
        <Link href={`/posts/${post.slug}`}>{post.title}</Link>
      </h2>
      <p className="mt-2 text-gray-600">{post.excerpt}</p>
      <button
        onClick={() => router.push(`/posts/${post.slug}/edit`)}
        className="mt-4 text-blue-500 hover:underline"
      >
        Edit Post
      </button>
    </div>
  )
}
```

### 6. Authentication

#### Protected Routes
```typescript
// src/middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token')
  
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url))
  }
  
  return NextResponse.next()
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

#### Auth Provider
```typescript
// src/providers/AuthProvider.tsx
'use client'

import { createContext, useContext, useEffect } from 'react'
import { useAuthStore } from '@/store/auth'

const AuthContext = createContext<ReturnType<typeof useAuthStore>>(null!)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const store = useAuthStore()
  
  useEffect(() => {
    // Check token validity on mount
    if (store.token) {
      store.validateToken()
    }
  }, [store])
  
  return (
    <AuthContext.Provider value={store}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)
```

### 7. Error Handling

#### Error Boundaries
```typescript
// src/components/ErrorBoundary.tsx
'use client'

import { Component, type ErrorInfo, type ReactNode } from 'react'

interface Props {
  children: ReactNode
  fallback: ReactNode
}

interface State {
  hasError: boolean
}

export class ErrorBoundary extends Component<Props, State> {
  state = { hasError: false }
  
  static getDerivedStateFromError() {
    return { hasError: true }
  }
  
  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Error caught by boundary:', error, errorInfo)
  }
  
  render() {
    if (this.state.hasError) {
      return this.props.fallback
    }
    
    return this.props.children
  }
}
```

### 8. Performance Optimization

#### Component Memoization
```typescript
// src/components/molecules/ExpensiveList/index.tsx
'use client'

import { memo } from 'react'
import { type Item } from '@/types'

interface Props {
  items: Item[]
  onItemClick: (id: string) => void
}

function ExpensiveListBase({ items, onItemClick }: Props) {
  return (
    <ul className="space-y-4">
      {items.map(item => (
        <li
          key={item.id}
          onClick={() => onItemClick(item.id)}
          className="cursor-pointer p-4 hover:bg-gray-50"
        >
          {item.title}
        </li>
      ))}
    </ul>
  )
}

export const ExpensiveList = memo(ExpensiveListBase)
```

#### Dynamic Imports with Suspense
```typescript
// src/app/dashboard/page.tsx
import { Suspense } from 'react'
import dynamic from 'next/dynamic'
import { Spinner } from '@/components/atoms/Spinner'

const DashboardChart = dynamic(
  () => import('@/components/organisms/DashboardChart'),
  {
    loading: () => <Spinner />,
    ssr: false,
  }
)

export default function DashboardPage() {
  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold">Dashboard</h1>
      <Suspense fallback={<Spinner />}>
        <DashboardChart />
      </Suspense>
    </div>
  )
}
```

## Development Workflow

### 1. Project Organization
```
src/
  ├── app/           # App Router pages
  ├── components/    # UI components
  ├── hooks/         # Custom hooks
  ├── lib/           # Utility functions
  ├── providers/     # Context providers
  ├── store/         # State management
  ├── styles/        # Global styles
  └── types/         # TypeScript types
```

### 2. Code Quality
- Use ESLint and Prettier
- Implement Git hooks with Husky
- Write unit tests with Jest and Testing Library
- Follow TypeScript best practices

### 3. Performance Monitoring
- Use Lighthouse for auditing
- Monitor Core Web Vitals
- Implement error tracking
- Use performance profiling tools

## Resources
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook)
- [Testing Library](https://testing-library.com/docs) 