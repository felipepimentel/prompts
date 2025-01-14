---
title: Next.js and Supabase Integration Guide
path: developer/supabase/supabase-2.md
tags:
  - nextjs
  - supabase
  - typescript
  - react
  - server-components
  - tailwind
  - development
description: Comprehensive guide for building modern web applications using Next.js 14 App Router with Supabase, focusing on best practices and performance
---

# Next.js and Supabase Integration Guide

## Project Setup

### 1. Initial Configuration
```bash
# Create new Next.js project
npx create-next-app@latest my-app --typescript --tailwind --eslint

# Install Supabase dependencies
npm install @supabase/supabase-js @supabase/auth-helpers-nextjs
```

### 2. Environment Setup
```env
# .env.local
NEXT_PUBLIC_SUPABASE_URL=your-project-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

### 3. Supabase Client Configuration
```typescript
// lib/supabase.ts
import { createClient } from '@supabase/supabase-js'
import { Database } from '@/types/supabase'

export const supabase = createClient<Database>(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)
```

## Core Components

### 1. Authentication Component
```typescript
// components/auth/auth-form.tsx
'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs'

export function AuthForm() {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const router = useRouter()
  const supabase = createClientComponentClient()

  async function onSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setIsLoading(true)
    setError(null)

    try {
      const formData = new FormData(event.currentTarget)
      const email = formData.get('email') as string
      const password = formData.get('password') as string

      const { error } = await supabase.auth.signInWithPassword({
        email,
        password,
      })

      if (error) throw error

      router.refresh()
      router.push('/dashboard')
    } catch (error) {
      setError(error instanceof Error ? error.message : 'An error occurred')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <form onSubmit={onSubmit} className="space-y-4">
      {error && (
        <div className="p-4 bg-red-50 text-red-500 rounded">
          {error}
        </div>
      )}
      <div>
        <label htmlFor="email" className="block text-sm font-medium">
          Email
        </label>
        <input
          id="email"
          name="email"
          type="email"
          required
          className="mt-1 block w-full rounded border-gray-300"
        />
      </div>
      <div>
        <label htmlFor="password" className="block text-sm font-medium">
          Password
        </label>
        <input
          id="password"
          name="password"
          type="password"
          required
          className="mt-1 block w-full rounded border-gray-300"
        />
      </div>
      <button
        type="submit"
        disabled={isLoading}
        className="w-full py-2 px-4 bg-blue-600 text-white rounded disabled:opacity-50"
      >
        {isLoading ? 'Signing in...' : 'Sign In'}
      </button>
    </form>
  )
}
```

### 2. Data Fetching Component
```typescript
// components/data/user-posts.tsx
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs'
import { cookies } from 'next/headers'

async function getPosts() {
  const supabase = createServerComponentClient({ cookies })
  
  const { data: posts, error } = await supabase
    .from('posts')
    .select('id, title, content, created_at, users(name)')
    .order('created_at', { ascending: false })
    .limit(10)

  if (error) throw error
  return posts
}

export async function UserPosts() {
  const posts = await getPosts()

  return (
    <div className="space-y-4">
      {posts.map((post) => (
        <article key={post.id} className="p-4 border rounded">
          <h2 className="text-xl font-bold">{post.title}</h2>
          <p className="mt-2">{post.content}</p>
          <div className="mt-2 text-sm text-gray-500">
            By {post.users?.name} on {new Date(post.created_at).toLocaleDateString()}
          </div>
        </article>
      ))}
    </div>
  )
}
```

### 3. Real-time Subscription Component
```typescript
// components/data/real-time-messages.tsx
'use client'

import { useEffect, useState } from 'react'
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs'
import type { Message } from '@/types'

export function RealTimeMessages() {
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const supabase = createClientComponentClient()

  useEffect(() => {
    // Initial fetch
    async function fetchMessages() {
      try {
        const { data, error } = await supabase
          .from('messages')
          .select('*')
          .order('created_at', { ascending: false })
          .limit(50)

        if (error) throw error
        setMessages(data)
      } catch (error) {
        console.error('Error fetching messages:', error)
      } finally {
        setIsLoading(false)
      }
    }

    fetchMessages()

    // Set up real-time subscription
    const channel = supabase
      .channel('messages')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'messages'
        },
        (payload) => {
          if (payload.eventType === 'INSERT') {
            setMessages((prev) => [payload.new as Message, ...prev])
          }
        }
      )
      .subscribe()

    return () => {
      supabase.removeChannel(channel)
    }
  }, [supabase])

  if (isLoading) {
    return <div>Loading messages...</div>
  }

  return (
    <div className="space-y-4">
      {messages.map((message) => (
        <div key={message.id} className="p-4 border rounded">
          <p>{message.content}</p>
          <span className="text-sm text-gray-500">
            {new Date(message.created_at).toLocaleString()}
          </span>
        </div>
      ))}
    </div>
  )
}
```

## Server Actions

### 1. Database Operations
```typescript
// app/actions/posts.ts
'use server'

import { createServerActionClient } from '@supabase/auth-helpers-nextjs'
import { cookies } from 'next/headers'
import { revalidatePath } from 'next/cache'

export async function createPost(formData: FormData) {
  const supabase = createServerActionClient({ cookies })
  
  const title = formData.get('title') as string
  const content = formData.get('content') as string

  try {
    const { error } = await supabase
      .from('posts')
      .insert({ title, content })

    if (error) throw error

    revalidatePath('/posts')
    return { success: true }
  } catch (error) {
    return { 
      success: false, 
      error: error instanceof Error ? error.message : 'An error occurred' 
    }
  }
}
```

### 2. File Upload
```typescript
// app/actions/storage.ts
'use server'

import { createServerActionClient } from '@supabase/auth-helpers-nextjs'
import { cookies } from 'next/headers'

export async function uploadFile(formData: FormData) {
  const supabase = createServerActionClient({ cookies })
  const file = formData.get('file') as File

  try {
    const fileExt = file.name.split('.').pop()
    const fileName = `${Math.random()}.${fileExt}`

    const { error } = await supabase.storage
      .from('uploads')
      .upload(fileName, file)

    if (error) throw error

    return { 
      success: true, 
      path: fileName 
    }
  } catch (error) {
    return { 
      success: false, 
      error: error instanceof Error ? error.message : 'Upload failed' 
    }
  }
}
```

## Middleware

### 1. Authentication Middleware
```typescript
// middleware.ts
import { createMiddlewareClient } from '@supabase/auth-helpers-nextjs'
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export async function middleware(req: NextRequest) {
  const res = NextResponse.next()
  const supabase = createMiddlewareClient({ req, res })

  const {
    data: { session },
  } = await supabase.auth.getSession()

  // Protected routes
  if (req.nextUrl.pathname.startsWith('/dashboard')) {
    if (!session) {
      return NextResponse.redirect(new URL('/login', req.url))
    }
  }

  // Public routes
  if (req.nextUrl.pathname.startsWith('/login')) {
    if (session) {
      return NextResponse.redirect(new URL('/dashboard', req.url))
    }
  }

  return res
}

export const config = {
  matcher: ['/dashboard/:path*', '/login']
}
```

## Error Handling

### 1. Error Boundary
```typescript
// app/error.tsx
'use client'

import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    console.error(error)
  }, [error])

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold text-red-600">
        Something went wrong!
      </h2>
      <button
        onClick={reset}
        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
      >
        Try again
      </button>
    </div>
  )
}
```

### 2. Loading States
```typescript
// app/loading.tsx
export default function Loading() {
  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-blue-500" />
    </div>
  )
}
```

## Best Practices

### 1. Component Organization
- Use Server Components by default
- Move client-side logic to leaf components
- Implement proper loading and error states
- Use semantic HTML elements

### 2. Data Fetching
- Prefer Server Components for data fetching
- Use real-time subscriptions sparingly
- Implement proper caching strategies
- Handle loading and error states

### 3. Authentication
- Use middleware for route protection
- Implement proper session management
- Handle auth state changes
- Provide clear error messages

### 4. Performance
- Minimize client-side JavaScript
- Use proper caching strategies
- Implement proper loading states
- Optimize images and assets

### 5. Security
- Validate all user inputs
- Use proper auth checks
- Implement rate limiting
- Follow security best practices

Remember:
- Keep components focused and small
- Use TypeScript for better type safety
- Follow React Server Components patterns
- Implement proper error handling
- Use proper loading states
- Follow security best practices 