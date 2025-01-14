---
title: "Next.js 14 Development Guide"
path: "developer/frameworks/nextjs/nextjs-14-setup-guide"
tags: ["nextjs", "typescript", "tailwind", "seo", "development", "best-practices", "app-router"]
description: "A comprehensive guide for developing Next.js 14 applications with TypeScript, Tailwind CSS, and SEO optimization, following modern best practices."
---

# Next.js 14 Development Guide

## Overview
This guide provides comprehensive development guidelines for building modern web applications using Next.js 14, TypeScript, and Tailwind CSS, with a focus on performance, SEO, and best practices.

## Core Requirements

### 1. App Router Architecture
- Use the `app` directory structure
- Implement server components by default
- Use client components only when necessary
- Follow Next.js 14 routing conventions

### 2. TypeScript Integration
- Use modern TypeScript syntax
- Implement proper type definitions
- Enable strict type checking
- Follow type inference best practices

### 3. Responsive Design
- Utilize Tailwind CSS for styling
- Implement mobile-first approach
- Ensure cross-device compatibility
- Optimize for various screen sizes

## Project Structure

### Directory Organization
```
app/
  ├── (routes)/           # Route groups
  │   ├── about/         # About page route
  │   ├── blog/         # Blog routes
  │   └── shop/        # Shop routes
  ├── api/             # API routes
  ├── components/     # Shared components
  │   ├── ui/        # UI components
  │   └── layout/   # Layout components
  ├── lib/          # Utility functions
  ├── styles/      # Global styles
  └── types/      # TypeScript types
```

## Component Development

### Server Components
```typescript
// app/blog/page.tsx
import { Post } from '@/types';

async function getPosts(): Promise<Post[]> {
  const res = await fetch('https://api.example.com/posts', {
    next: { revalidate: 3600 } // Cache for 1 hour
  });
  
  if (!res.ok) {
    throw new Error('Failed to fetch posts');
  }
  
  return res.json();
}

export default async function BlogPage() {
  const posts = await getPosts();
  
  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6">Blog Posts</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {posts.map(post => (
          <PostCard key={post.id} post={post} />
        ))}
      </div>
    </div>
  );
}
```

### Client Components
```typescript
// components/ui/ThemeToggle.tsx
'use client';

import { useState, useEffect } from 'react';
import { useTheme } from 'next-themes';

export function ThemeToggle() {
  const [mounted, setMounted] = useState(false);
  const { theme, setTheme } = useTheme();

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return (
    <button
      className="p-2 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800"
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
    >
      {theme === 'dark' ? '🌞' : '🌙'}
    </button>
  );
}
```

## Data Fetching

### Server-Side Data Fetching
```typescript
// lib/api.ts
export async function fetchData<T>(
  url: string,
  options: RequestInit = {}
): Promise<T> {
  const defaultOptions: RequestInit = {
    next: { revalidate: 3600 },
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  };

  const res = await fetch(url, { ...defaultOptions, ...options });
  
  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }
  
  return res.json();
}

// Usage in a server component
import { fetchData } from '@/lib/api';
import type { User } from '@/types';

export default async function UserProfile({ userId }: { userId: string }) {
  const user = await fetchData<User>(`/api/users/${userId}`);
  
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">{user.name}</h1>
      <p className="text-gray-600">{user.email}</p>
    </div>
  );
}
```

## Error Handling

### Error Boundaries
```typescript
// app/error.tsx
'use client';

interface ErrorBoundaryProps {
  error: Error & { digest?: string };
  reset: () => void;
}

export default function Error({ error, reset }: ErrorBoundaryProps) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[400px]">
      <h2 className="text-2xl font-bold mb-4">Something went wrong!</h2>
      <p className="text-gray-600 mb-4">{error.message}</p>
      <button
        onClick={reset}
        className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
      >
        Try again
      </button>
    </div>
  );
}
```

## Loading States

### Loading UI
```typescript
// app/loading.tsx
export default function Loading() {
  return (
    <div className="flex items-center justify-center min-h-[400px]">
      <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500" />
    </div>
  );
}
```

## SEO Optimization

### Metadata Configuration
```typescript
// app/layout.tsx
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: {
    default: 'My App',
    template: '%s | My App',
  },
  description: 'A modern Next.js application',
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://myapp.com',
    siteName: 'My App',
  },
  robots: {
    index: true,
    follow: true,
  },
  twitter: {
    card: 'summary_large_image',
    site: '@myapp',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

## Performance Optimization

### Image Optimization
```typescript
// components/ui/OptimizedImage.tsx
import Image from 'next/image';

interface OptimizedImageProps {
  src: string;
  alt: string;
  width: number;
  height: number;
  priority?: boolean;
}

export function OptimizedImage({
  src,
  alt,
  width,
  height,
  priority = false,
}: OptimizedImageProps) {
  return (
    <div className="relative aspect-w-16 aspect-h-9">
      <Image
        src={src}
        alt={alt}
        width={width}
        height={height}
        priority={priority}
        className="object-cover rounded-lg"
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      />
    </div>
  );
}
```

## API Routes

### Route Handlers
```typescript
// app/api/posts/route.ts
import { NextResponse } from 'next/server';
import type { Post } from '@/types';

export async function GET() {
  try {
    const posts = await prisma.post.findMany({
      orderBy: { createdAt: 'desc' },
    });
    
    return NextResponse.json(posts);
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch posts' },
      { status: 500 }
    );
  }
}

export async function POST(request: Request) {
  try {
    const json = await request.json();
    const post = await prisma.post.create({
      data: json,
    });
    
    return NextResponse.json(post, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create post' },
      { status: 500 }
    );
  }
}
```

## Resources
- [Next.js Documentation](https://nextjs.org/docs)
- [TypeScript Documentation](https://www.typescriptlang.org/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [React Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components) 