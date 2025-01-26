---
category: Developer
description: A comprehensive guide for building modern web applications using TypeScript,
  React, NextUI components, and Supabase backend services
model: GPT-4
path: developer/frameworks/react/nextui-supabase-guide
prompt_type: Instruction-based prompting
tags:
- typescript
- react
- nextui
- supabase
- frontend
title: NextUI and Supabase Integration Guide
version: '1.0'
---

# NextUI and Supabase Integration Guide

## Core Principles
- Modern UI components
- Type-safe backend
- Real-time features
- Authentication
- Database management

## Project Setup

### Environment Configuration
```typescript
// .env.local
NEXT_PUBLIC_SUPABASE_URL=your-project-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

### NextUI Setup
```typescript
// app/providers.tsx
'use client'

import { NextUIProvider } from '@nextui-org/react'
import { ThemeProvider as NextThemesProvider } from 'next-themes'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <NextUIProvider>
      <NextThemesProvider attribute="class" defaultTheme="system">
        {children}
      </NextThemesProvider>
    </NextUIProvider>
  )
}

// app/layout.tsx
import { Providers } from './providers'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head />
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
```

### Supabase Client
```typescript
// lib/supabase.ts
import { createClient } from '@supabase/supabase-js'
import { Database } from '@/types/supabase'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!

export const supabase = createClient<Database>(supabaseUrl, supabaseKey)

// types/supabase.ts
export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

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
          created_at?: string
        }
        Update: {
          id?: string
          username?: string
          full_name?: string
          avatar_url?: string
          created_at?: string
        }
      }
    }
  }
}
```

## Authentication

### Auth Components
```typescript
// components/auth/SignInForm.tsx
'use client'

import { useState } from 'react'
import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Input,
  Button,
} from '@nextui-org/react'
import { supabase } from '@/lib/supabase'

export function SignInForm() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSignIn = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const { error } = await supabase.auth.signInWithPassword({
        email,
        password,
      })

      if (error) throw error
    } catch (error) {
      console.error('Error signing in:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <Card className="max-w-sm mx-auto">
      <CardHeader>
        <h2 className="text-2xl font-bold">Sign In</h2>
      </CardHeader>
      <CardBody>
        <form onSubmit={handleSignIn} className="space-y-4">
          <Input
            type="email"
            label="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <Input
            type="password"
            label="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <Button
            type="submit"
            color="primary"
            isLoading={loading}
            className="w-full"
          >
            Sign In
          </Button>
        </form>
      </CardBody>
    </Card>
  )
}
```

### Auth Provider
```typescript
// contexts/AuthContext.tsx
'use client'

import {
  createContext,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from 'react'
import { User } from '@supabase/supabase-js'
import { supabase } from '@/lib/supabase'

interface AuthContextType {
  user: User | null
  loading: boolean
}

const AuthContext = createContext<AuthContextType>({
  user: null,
  loading: true,
})

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check active sessions
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null)
      setLoading(false)
    })

    // Listen for auth changes
    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null)
      setLoading(false)
    })

    return () => subscription.unsubscribe()
  }, [])

  return (
    <AuthContext.Provider value={{ user, loading }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}
```

## Database Integration

### Data Hooks
```typescript
// hooks/useProfiles.ts
import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'
import type { Database } from '@/types/supabase'

type Profile = Database['public']['Tables']['profiles']['Row']

export function useProfiles() {
  const [profiles, setProfiles] = useState<Profile[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    const fetchProfiles = async () => {
      try {
        const { data, error } = await supabase
          .from('profiles')
          .select('*')
          .order('created_at', { ascending: false })

        if (error) throw error

        setProfiles(data)
      } catch (error) {
        setError(error as Error)
      } finally {
        setLoading(false)
      }
    }

    fetchProfiles()

    // Subscribe to changes
    const subscription = supabase
      .channel('profiles')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'profiles',
        },
        (payload) => {
          console.log('Change received!', payload)
          fetchProfiles()
        }
      )
      .subscribe()

    return () => {
      subscription.unsubscribe()
    }
  }, [])

  return { profiles, loading, error }
}
```

### Data Components
```typescript
// components/ProfileList.tsx
'use client'

import {
  Card,
  CardBody,
  Avatar,
  Spinner,
} from '@nextui-org/react'
import { useProfiles } from '@/hooks/useProfiles'

export function ProfileList() {
  const { profiles, loading, error } = useProfiles()

  if (loading) {
    return (
      <div className="flex justify-center">
        <Spinner />
      </div>
    )
  }

  if (error) {
    return (
      <div className="text-center text-red-500">
        Error loading profiles: {error.message}
      </div>
    )
  }

  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      {profiles.map((profile) => (
        <Card key={profile.id}>
          <CardBody className="flex flex-row items-center gap-4">
            <Avatar
              src={profile.avatar_url}
              name={profile.full_name}
              size="lg"
            />
            <div>
              <h3 className="text-lg font-semibold">
                {profile.full_name}
              </h3>
              <p className="text-sm text-gray-500">
                @{profile.username}
              </p>
            </div>
          </CardBody>
        </Card>
      ))}
    </div>
  )
}
```

## File Storage

### Storage Hooks
```typescript
// hooks/useStorage.ts
import { useState } from 'react'
import { supabase } from '@/lib/supabase'

export function useStorage() {
  const [uploading, setUploading] = useState(false)

  const uploadFile = async (
    bucket: string,
    path: string,
    file: File
  ) => {
    try {
      setUploading(true)

      const { error } = await supabase.storage
        .from(bucket)
        .upload(path, file)

      if (error) throw error

      return supabase.storage
        .from(bucket)
        .getPublicUrl(path)
        .data.publicUrl
    } catch (error) {
      console.error('Error uploading file:', error)
      throw error
    } finally {
      setUploading(false)
    }
  }

  const deleteFile = async (bucket: string, path: string) => {
    try {
      const { error } = await supabase.storage
        .from(bucket)
        .remove([path])

      if (error) throw error
    } catch (error) {
      console.error('Error deleting file:', error)
      throw error
    }
  }

  return {
    uploadFile,
    deleteFile,
    uploading,
  }
}
```

### Upload Component
```typescript
// components/FileUpload.tsx
'use client'

import { useState } from 'react'
import { Button } from '@nextui-org/react'
import { useStorage } from '@/hooks/useStorage'

interface Props {
  bucket: string
  path: string
  onUpload: (url: string) => void
}

export function FileUpload({ bucket, path, onUpload }: Props) {
  const { uploadFile, uploading } = useStorage()
  const [error, setError] = useState<string | null>(null)

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    try {
      const file = e.target.files?.[0]
      if (!file) return

      const url = await uploadFile(bucket, path, file)
      onUpload(url)
    } catch (error) {
      setError((error as Error).message)
    }
  }

  return (
    <div>
      <Button
        as="label"
        color="primary"
        isLoading={uploading}
        className="cursor-pointer"
      >
        {uploading ? 'Uploading...' : 'Upload File'}
        <input
          type="file"
          className="hidden"
          onChange={handleUpload}
          disabled={uploading}
        />
      </Button>
      {error && (
        <p className="mt-2 text-sm text-red-500">{error}</p>
      )}
    </div>
  )
}
```

## Real-time Features

### Presence
```typescript
// hooks/usePresence.ts
import { useEffect, useState } from 'react'
import { useAuth } from '@/contexts/AuthContext'
import { supabase } from '@/lib/supabase'

interface PresenceState {
  [key: string]: {
    user_id: string
    online_at: string
  }
}

export function usePresence() {
  const { user } = useAuth()
  const [presence, setPresence] = useState<PresenceState>({})

  useEffect(() => {
    if (!user) return

    const channel = supabase.channel('online-users')

    channel
      .on('presence', { event: 'sync' }, () => {
        const state = channel.presenceState<{
          user_id: string
          online_at: string
        }>()
        setPresence(state)
      })
      .subscribe(async (status) => {
        if (status === 'SUBSCRIBED') {
          await channel.track({
            user_id: user.id,
            online_at: new Date().toISOString(),
          })
        }
      })

    return () => {
      channel.unsubscribe()
    }
  }, [user])

  return presence
}
```

### Chat Implementation
```typescript
// hooks/useChat.ts
import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'

interface Message {
  id: string
  user_id: string
  content: string
  created_at: string
}

export function useChat(roomId: string) {
  const [messages, setMessages] = useState<Message[]>([])

  useEffect(() => {
    // Fetch existing messages
    const fetchMessages = async () => {
      const { data, error } = await supabase
        .from('messages')
        .select('*')
        .eq('room_id', roomId)
        .order('created_at', { ascending: true })

      if (error) console.error('Error fetching messages:', error)
      else setMessages(data || [])
    }

    fetchMessages()

    // Subscribe to new messages
    const channel = supabase
      .channel(`room:${roomId}`)
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'messages',
          filter: `room_id=eq.${roomId}`,
        },
        (payload) => {
          setMessages((current) => [...current, payload.new as Message])
        }
      )
      .subscribe()

    return () => {
      channel.unsubscribe()
    }
  }, [roomId])

  const sendMessage = async (content: string, userId: string) => {
    const { error } = await supabase.from('messages').insert({
      room_id: roomId,
      user_id: userId,
      content,
    })

    if (error) console.error('Error sending message:', error)
  }

  return {
    messages,
    sendMessage,
  }
}
```

## Best Practices

### Type Safety
1. Use TypeScript generics
2. Define database types
3. Validate API responses
4. Handle edge cases
5. Document type definitions

### Performance
- Optimize queries
- Use connection pooling
- Implement caching
- Batch operations
- Monitor performance

### Security
1. Row Level Security
2. Input validation
3. Access control
4. Error handling
5. Audit logging

### Development
- Code organization
- Error boundaries
- Testing strategy
- Documentation
- Code review

## Resources
- NextUI documentation
- Supabase guides
- TypeScript handbook
- React best practices
- Security guidelines