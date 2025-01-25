---
category: Developer
description: Comprehensive guide for building modern web applications using TypeScript,
  React, NextUI, and Supabase, focusing on best practices and full-stack integration
model: GPT-4
path: developer/frameworks/react/typescript-react-nextui-supabase-guide.md
prompt_type: Instruction-based prompting
tags:
- typescript
- react
- nextui
- supabase
- frontend
title: TypeScript React NextUI Supabase Integration Guide
version: '1.0'
---

# TypeScript React NextUI Supabase Integration Guide

## Overview
This guide provides a comprehensive approach to building full-stack applications using TypeScript, React, NextUI for UI components, and Supabase for backend services.

## Project Setup

### 1. Initial Setup
```bash
# Create new React project with TypeScript
npx create-react-app my-app --template typescript

# Navigate to project
cd my-app

# Install dependencies
npm install @nextui-org/react framer-motion @supabase/supabase-js
```

### 2. Supabase Configuration
```typescript
// lib/supabase.ts
import { createClient } from '@supabase/supabase-js'
import { Database } from './database.types'

const supabaseUrl = process.env.REACT_APP_SUPABASE_URL!
const supabaseKey = process.env.REACT_APP_SUPABASE_ANON_KEY!

export const supabase = createClient<Database>(supabaseUrl, supabaseKey)
```

### 3. NextUI Setup
```typescript
// App.tsx
import { NextUIProvider } from '@nextui-org/react'

function App() {
  return (
    <NextUIProvider>
      {/* Your app content */}
    </NextUIProvider>
  )
}
```

## Authentication

### 1. Auth Context
```typescript
// contexts/AuthContext.tsx
import { createContext, useContext, useEffect, useState } from 'react'
import { User } from '@supabase/supabase-js'
import { supabase } from '@/lib/supabase'

interface AuthContextType {
  user: User | null
  loading: boolean
  signIn: (email: string, password: string) => Promise<void>
  signOut: () => Promise<void>
}

const AuthContext = createContext<AuthContextType>({} as AuthContextType)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check active sessions and subscribe to auth changes
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null)
      setLoading(false)
    })

    const { data: { subscription } } = supabase.auth.onAuthStateChange(
      (_event, session) => {
        setUser(session?.user ?? null)
        setLoading(false)
      }
    )

    return () => subscription.unsubscribe()
  }, [])

  const signIn = async (email: string, password: string) => {
    const { error } = await supabase.auth.signInWithPassword({
      email,
      password,
    })
    if (error) throw error
  }

  const signOut = async () => {
    const { error } = await supabase.auth.signOut()
    if (error) throw error
  }

  return (
    <AuthContext.Provider value={{ user, loading, signIn, signOut }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)
```

### 2. Auth Components
```typescript
// components/auth/SignInForm.tsx
import { useState } from 'react'
import { Button, Input } from '@nextui-org/react'
import { useAuth } from '@/contexts/AuthContext'

export function SignInForm() {
  const { signIn } = useAuth()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      await signIn(email, password)
    } catch (error) {
      console.error('Error signing in:', error)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <Input
        type="email"
        label="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <Input
        type="password"
        label="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <Button type="submit">Sign In</Button>
    </form>
  )
}
```

## Data Management

### 1. Database Types
```typescript
// lib/database.types.ts
export interface Database {
  public: {
    Tables: {
      profiles: {
        Row: {
          id: string
          username: string
          full_name: string
          avatar_url: string
          created_at: string
        }
        Insert: {
          id: string
          username: string
          full_name?: string
          avatar_url?: string
        }
        Update: {
          username?: string
          full_name?: string
          avatar_url?: string
        }
      }
      posts: {
        Row: {
          id: number
          title: string
          content: string
          author_id: string
          created_at: string
        }
        Insert: {
          title: string
          content: string
          author_id: string
        }
        Update: {
          title?: string
          content?: string
        }
      }
    }
  }
}
```

### 2. Data Hooks
```typescript
// hooks/useProfiles.ts
import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'
import type { Database } from '@/lib/database.types'

type Profile = Database['public']['Tables']['profiles']['Row']

export function useProfile(userId: string) {
  const [profile, setProfile] = useState<Profile | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function fetchProfile() {
      try {
        const { data, error } = await supabase
          .from('profiles')
          .select('*')
          .eq('id', userId)
          .single()

        if (error) throw error
        setProfile(data)
      } catch (error) {
        console.error('Error fetching profile:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchProfile()
  }, [userId])

  return { profile, loading }
}
```

## UI Components

### 1. Layout Components
```typescript
// components/layout/AppLayout.tsx
import { Navbar, Container } from '@nextui-org/react'
import { useAuth } from '@/contexts/AuthContext'

interface AppLayoutProps {
  children: React.ReactNode
}

export function AppLayout({ children }: AppLayoutProps) {
  const { user, signOut } = useAuth()

  return (
    <div>
      <Navbar>
        <Navbar.Brand>
          <h1>My App</h1>
        </Navbar.Brand>
        <Navbar.Content>
          {user ? (
            <Navbar.Item>
              <Button onClick={signOut}>Sign Out</Button>
            </Navbar.Item>
          ) : (
            <Navbar.Item>
              <Button as={Link} href="/signin">Sign In</Button>
            </Navbar.Item>
          )}
        </Navbar.Content>
      </Navbar>
      <Container>
        {children}
      </Container>
    </div>
  )
}
```

### 2. Data Display Components
```typescript
// components/posts/PostCard.tsx
import { Card, Text } from '@nextui-org/react'
import type { Database } from '@/lib/database.types'

type Post = Database['public']['Tables']['posts']['Row']

interface PostCardProps {
  post: Post
}

export function PostCard({ post }: PostCardProps) {
  return (
    <Card>
      <Card.Header>
        <Text h3>{post.title}</Text>
      </Card.Header>
      <Card.Body>
        <Text>{post.content}</Text>
      </Card.Body>
      <Card.Footer>
        <Text small>Posted on {new Date(post.created_at).toLocaleDateString()}</Text>
      </Card.Footer>
    </Card>
  )
}
```

## Real-time Features

### 1. Subscription Setup
```typescript
// hooks/useRealtimePosts.ts
import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'
import type { Database } from '@/lib/database.types'

type Post = Database['public']['Tables']['posts']['Row']

export function useRealtimePosts() {
  const [posts, setPosts] = useState<Post[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Fetch initial data
    fetchPosts()

    // Set up real-time subscription
    const subscription = supabase
      .channel('public:posts')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'posts'
        },
        (payload) => {
          if (payload.eventType === 'INSERT') {
            setPosts((current) => [...current, payload.new as Post])
          } else if (payload.eventType === 'UPDATE') {
            setPosts((current) =>
              current.map((post) =>
                post.id === payload.new.id ? payload.new as Post : post
              )
            )
          } else if (payload.eventType === 'DELETE') {
            setPosts((current) =>
              current.filter((post) => post.id !== payload.old.id)
            )
          }
        }
      )
      .subscribe()

    return () => {
      subscription.unsubscribe()
    }
  }, [])

  async function fetchPosts() {
    try {
      setLoading(true)
      const { data, error } = await supabase
        .from('posts')
        .select('*')
        .order('created_at', { ascending: false })

      if (error) throw error
      setPosts(data)
    } catch (error) {
      console.error('Error fetching posts:', error)
    } finally {
      setLoading(false)
    }
  }

  return { posts, loading }
}
```

## Error Handling

### 1. Error Boundary
```typescript
// components/ErrorBoundary.tsx
import { Component, ErrorInfo, ReactNode } from 'react'
import { Card, Text, Button } from '@nextui-org/react'

interface Props {
  children: ReactNode
}

interface State {
  hasError: boolean
  error: Error | null
}

export class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: null
  }

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error }
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Uncaught error:', error, errorInfo)
  }

  public render() {
    if (this.state.hasError) {
      return (
        <Card>
          <Card.Header>
            <Text h4>Something went wrong</Text>
          </Card.Header>
          <Card.Body>
            <Text>{this.state.error?.message}</Text>
          </Card.Body>
          <Card.Footer>
            <Button
              onClick={() => this.setState({ hasError: false, error: null })}
            >
              Try again
            </Button>
          </Card.Footer>
        </Card>
      )
    }

    return this.props.children
  }
}
```

## Performance Optimization

### 1. Memoization
```typescript
// components/posts/PostList.tsx
import { memo } from 'react'
import { PostCard } from './PostCard'
import type { Database } from '@/lib/database.types'

type Post = Database['public']['Tables']['posts']['Row']

interface PostListProps {
  posts: Post[]
}

export const PostList = memo(function PostList({ posts }: PostListProps) {
  return (
    <div className="grid gap-4">
      {posts.map((post) => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  )
})
```

### 2. Query Optimization
```typescript
// hooks/usePostsWithAuthors.ts
import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'
import type { Database } from '@/lib/database.types'

type Post = Database['public']['Tables']['posts']['Row']
type Profile = Database['public']['Tables']['profiles']['Row']

interface PostWithAuthor extends Post {
  author: Profile
}

export function usePostsWithAuthors() {
  const [posts, setPosts] = useState<PostWithAuthor[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function fetchPosts() {
      try {
        const { data, error } = await supabase
          .from('posts')
          .select(`
            *,
            author:profiles(*)
          `)
          .order('created_at', { ascending: false })

        if (error) throw error
        setPosts(data)
      } catch (error) {
        console.error('Error fetching posts:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchPosts()
  }, [])

  return { posts, loading }
}
```

## Best Practices

1. Authentication
   - Implement proper auth flow
   - Handle session management
   - Secure routes appropriately
   - Manage user state

2. Data Management
   - Use TypeScript types
   - Implement error handling
   - Optimize queries
   - Handle real-time updates

3. UI Components
   - Follow NextUI patterns
   - Maintain consistency
   - Implement accessibility
   - Optimize performance

4. State Management
   - Use context appropriately
   - Implement caching
   - Handle loading states
   - Manage side effects

Remember to:
1. Keep types up to date
2. Handle errors gracefully
3. Optimize performance
4. Follow security best practices
5. Maintain code consistency