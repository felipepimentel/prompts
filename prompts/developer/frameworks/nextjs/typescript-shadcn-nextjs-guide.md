---
title: TypeScript Next.js with shadcn/ui Guide
path: developer/frameworks/nextjs/typescript-shadcn-nextjs-guide
tags:
  - typescript
  - nextjs
  - shadcn-ui
  - frontend
  - development
description: A comprehensive guide for building modern web applications using Next.js, TypeScript, and shadcn/ui components
---

# TypeScript Next.js with shadcn/ui Guide

## Core Principles
- Type safety
- Component architecture
- Performance optimization
- Design system integration
- Development workflow

## Project Setup

### Installation
```bash
# Create Next.js project
npx create-next-app@latest my-app --typescript --tailwind --eslint

# Add shadcn/ui
npx shadcn-ui@latest init

# Install additional dependencies
npm install @hookform/resolvers zod react-hook-form @tanstack/react-query
```

### Configuration
```typescript
// next.config.mjs
import { withAxiom } from 'next-axiom'

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['your-domain.com'],
  },
}

export default withAxiom(nextConfig)

// tsconfig.json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

## Component Architecture

### Layout Components
```typescript
// components/layout/Header.tsx
import { ThemeToggle } from '@/components/theme/ThemeToggle'
import { MainNav } from '@/components/layout/MainNav'
import { UserNav } from '@/components/layout/UserNav'

export function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-14 items-center">
        <MainNav />
        <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
          <div className="w-full flex-1 md:w-auto md:flex-none">
            {/* Search component */}
          </div>
          <ThemeToggle />
          <UserNav />
        </div>
      </div>
    </header>
  )
}

// components/layout/MainNav.tsx
import { cn } from '@/lib/utils'
import { Link } from '@/components/ui/link'

interface NavItem {
  title: string
  href: string
  disabled?: boolean
}

export function MainNav({
  className,
  ...props
}: React.HTMLAttributes<HTMLElement>) {
  const items: NavItem[] = [
    {
      title: 'Dashboard',
      href: '/dashboard',
    },
    {
      title: 'Settings',
      href: '/settings',
    },
  ]

  return (
    <nav
      className={cn('flex items-center space-x-4 lg:space-x-6', className)}
      {...props}
    >
      {items.map((item) => (
        <Link
          key={item.href}
          href={item.href}
          className={cn(
            'text-sm font-medium transition-colors hover:text-primary',
            item.disabled && 'cursor-not-allowed opacity-80'
          )}
        >
          {item.title}
        </Link>
      ))}
    </nav>
  )
}
```

### Form Components
```typescript
// components/forms/SignupForm.tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import * as z from 'zod'

import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'

const formSchema = z.object({
  username: z.string().min(2).max(50),
  email: z.string().email(),
  password: z.string().min(8),
})

type FormValues = z.infer<typeof formSchema>

export function SignupForm() {
  const form = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: '',
      email: '',
      password: '',
    },
  })

  async function onSubmit(values: FormValues) {
    try {
      // Handle form submission
      console.log(values)
    } catch (error) {
      console.error(error)
    }
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input placeholder="johndoe" {...field} />
              </FormControl>
              <FormDescription>
                This is your public display name.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        {/* Add more form fields */}
        <Button type="submit">Submit</Button>
      </form>
    </Form>
  )
}
```

### Data Display Components
```typescript
// components/data/DataTable.tsx
import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
} from '@tanstack/react-table'

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
  })

  return (
    <div className="rounded-md border">
      <Table>
        <TableHeader>
          {table.getHeaderGroups().map((headerGroup) => (
            <TableRow key={headerGroup.id}>
              {headerGroup.headers.map((header) => (
                <TableHead key={header.id}>
                  {header.isPlaceholder
                    ? null
                    : flexRender(
                        header.column.columnDef.header,
                        header.getContext()
                      )}
                </TableHead>
              ))}
            </TableRow>
          ))}
        </TableHeader>
        <TableBody>
          {table.getRowModel().rows?.length ? (
            table.getRowModel().rows.map((row) => (
              <TableRow key={row.id}>
                {row.getVisibleCells().map((cell) => (
                  <TableCell key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </TableCell>
                ))}
              </TableRow>
            ))
          ) : (
            <TableRow>
              <TableCell colSpan={columns.length} className="h-24 text-center">
                No results.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </div>
  )
}
```

## State Management

### React Query Setup
```typescript
// lib/query.ts
import { QueryClient } from '@tanstack/react-query'

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000,
      retry: 1,
    },
  },
})

// app/providers.tsx
'use client'

import { QueryClientProvider } from '@tanstack/react-query'
import { ThemeProvider } from 'next-themes'
import { queryClient } from '@/lib/query'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider
        attribute="class"
        defaultTheme="system"
        enableSystem
        disableTransitionOnChange
      >
        {children}
      </ThemeProvider>
    </QueryClientProvider>
  )
}
```

### Custom Hooks
```typescript
// hooks/useAuth.ts
import { useQuery, useMutation } from '@tanstack/react-query'
import { User } from '@/types'

interface LoginCredentials {
  email: string
  password: string
}

export function useAuth() {
  const { data: user, isLoading } = useQuery<User>({
    queryKey: ['user'],
    queryFn: async () => {
      const response = await fetch('/api/auth/me')
      if (!response.ok) throw new Error('Failed to fetch user')
      return response.json()
    },
  })

  const login = useMutation({
    mutationFn: async (credentials: LoginCredentials) => {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials),
      })
      if (!response.ok) throw new Error('Login failed')
      return response.json()
    },
  })

  return {
    user,
    isLoading,
    login: login.mutate,
    isLoggingIn: login.isPending,
  }
}
```

## API Integration

### API Client
```typescript
// lib/api.ts
import axios from 'axios'

export const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized access
    }
    return Promise.reject(error)
  }
)

// Example API service
export const userService = {
  async getProfile() {
    const { data } = await api.get('/users/profile')
    return data
  },

  async updateProfile(profile: any) {
    const { data } = await api.put('/users/profile', profile)
    return data
  },
}
```

## Best Practices

### Type Safety
1. Use TypeScript strict mode
2. Define API response types
3. Validate form inputs
4. Handle error cases
5. Document interfaces

### Performance
- Component memoization
- Image optimization
- Code splitting
- Bundle analysis
- Caching strategies

### Development
1. Code organization
2. Error boundaries
3. Testing strategy
4. Documentation
5. Code review

### Deployment
- Environment variables
- Build optimization
- Error monitoring
- Analytics setup
- CI/CD pipeline

## Resources
- Next.js documentation
- shadcn/ui guides
- TypeScript handbook
- React Query docs
- Design system guides 