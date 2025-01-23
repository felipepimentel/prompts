---
description: A comprehensive guide for integrating and customizing shadcn/ui components
  in Next.js applications with Tailwind CSS
path: developer/frameworks/nextjs/shadcn-ui-guide
prompt_type: Instruction-based prompting
tags:
- nextjs
- tailwind
- shadcn-ui
- components
- frontend
title: shadcn/ui Integration Guide
---

# shadcn/ui Integration Guide

## Core Principles
- Component customization
- Design system integration
- Accessibility patterns
- Performance optimization
- Maintainable architecture

## Project Setup

### Installation
```bash
# Initialize shadcn/ui in your Next.js project
npx shadcn-ui@latest init

# Follow the CLI prompts:
# ✓ Would you like to use TypeScript (recommended)? yes
# ✓ Which style would you like to use? Default
# ✓ Which color would you like to use as base color? Slate
# ✓ Where is your global CSS file? app/globals.css
# ✓ Would you like to use CSS variables for colors? yes
# ✓ Where is your tailwind.config.js located? tailwind.config.js
# ✓ Configure the import alias for components: @/components
# ✓ Configure the import alias for utils: @/lib/utils
```

### Configuration
```typescript
// tailwind.config.ts
import { type Config } from 'tailwindcss'
import { shadcnPlugin } from './shadcn-plugin'

const config: Config = {
  darkMode: ['class'],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  plugins: [
    require('tailwindcss-animate'),
    shadcnPlugin({
      prefix: 'ui',
    }),
  ],
}

export default config
```

### Theme Setup
```typescript
// lib/themes.ts
export const themes = {
  light: {
    background: 'hsl(0 0% 100%)',
    foreground: 'hsl(222.2 84% 4.9%)',
    card: 'hsl(0 0% 100%)',
    'card-foreground': 'hsl(222.2 84% 4.9%)',
    popover: 'hsl(0 0% 100%)',
    'popover-foreground': 'hsl(222.2 84% 4.9%)',
    primary: 'hsl(222.2 47.4% 11.2%)',
    'primary-foreground': 'hsl(210 40% 98%)',
    secondary: 'hsl(210 40% 96.1%)',
    'secondary-foreground': 'hsl(222.2 47.4% 11.2%)',
    muted: 'hsl(210 40% 96.1%)',
    'muted-foreground': 'hsl(215.4 16.3% 46.9%)',
    accent: 'hsl(210 40% 96.1%)',
    'accent-foreground': 'hsl(222.2 47.4% 11.2%)',
    destructive: 'hsl(0 84.2% 60.2%)',
    'destructive-foreground': 'hsl(210 40% 98%)',
    border: 'hsl(214.3 31.8% 91.4%)',
    input: 'hsl(214.3 31.8% 91.4%)',
    ring: 'hsl(222.2 84% 4.9%)',
  },
  dark: {
    background: 'hsl(222.2 84% 4.9%)',
    foreground: 'hsl(210 40% 98%)',
    card: 'hsl(222.2 84% 4.9%)',
    'card-foreground': 'hsl(210 40% 98%)',
    popover: 'hsl(222.2 84% 4.9%)',
    'popover-foreground': 'hsl(210 40% 98%)',
    primary: 'hsl(210 40% 98%)',
    'primary-foreground': 'hsl(222.2 47.4% 11.2%)',
    secondary: 'hsl(217.2 32.6% 17.5%)',
    'secondary-foreground': 'hsl(210 40% 98%)',
    muted: 'hsl(217.2 32.6% 17.5%)',
    'muted-foreground': 'hsl(215 20.2% 65.1%)',
    accent: 'hsl(217.2 32.6% 17.5%)',
    'accent-foreground': 'hsl(210 40% 98%)',
    destructive: 'hsl(0 62.8% 30.6%)',
    'destructive-foreground': 'hsl(210 40% 98%)',
    border: 'hsl(217.2 32.6% 17.5%)',
    input: 'hsl(217.2 32.6% 17.5%)',
    ring: 'hsl(212.7 26.8% 83.9%)',
  },
}
```

## Component Integration

### Adding Components
```bash
# Add individual components
npx shadcn-ui@latest add button
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
```

### Component Customization
```typescript
// components/ui/button.tsx
import { cva } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        destructive:
          'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        outline:
          'border border-input bg-background hover:bg-accent hover:text-accent-foreground',
        secondary:
          'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        link: 'text-primary underline-offset-4 hover:underline',
        custom: 'bg-gradient-to-r from-blue-500 to-purple-500 text-white hover:opacity-90',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)
```

### Component Composition
```typescript
// components/ui/card.tsx
import { cn } from '@/lib/utils'

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  gradient?: boolean
}

export function Card({
  className,
  gradient = false,
  ...props
}: CardProps) {
  return (
    <div
      className={cn(
        'rounded-lg border bg-card text-card-foreground shadow-sm',
        gradient && 'bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20',
        className
      )}
      {...props}
    />
  )
}

Card.Header = function CardHeader({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn('flex flex-col space-y-1.5 p-6', className)}
      {...props}
    />
  )
}

Card.Title = function CardTitle({
  className,
  ...props
}: React.HTMLAttributes<HTMLHeadingElement>) {
  return (
    <h3
      className={cn(
        'text-2xl font-semibold leading-none tracking-tight',
        className
      )}
      {...props}
    />
  )
}

Card.Description = function CardDescription({
  className,
  ...props
}: React.HTMLAttributes<HTMLParagraphElement>) {
  return (
    <p
      className={cn('text-sm text-muted-foreground', className)}
      {...props}
    />
  )
}

Card.Content = function CardContent({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div className={cn('p-6 pt-0', className)} {...props} />
  )
}
```

## Advanced Patterns

### Form Integration
```typescript
// components/ui/form.tsx
import * as React from 'react'
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

export function SignupForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: '',
      email: '',
      password: '',
    },
  })

  function onSubmit(values: z.infer<typeof formSchema>) {
    console.log(values)
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

### Theme Switching
```typescript
// components/theme-provider.tsx
import { createContext, useContext, useEffect, useState } from 'react'

type Theme = 'dark' | 'light' | 'system'

type ThemeProviderProps = {
  children: React.ReactNode
  defaultTheme?: Theme
  storageKey?: string
}

type ThemeProviderState = {
  theme: Theme
  setTheme: (theme: Theme) => void
}

const ThemeProviderContext = createContext<ThemeProviderState | undefined>(
  undefined
)

export function ThemeProvider({
  children,
  defaultTheme = 'system',
  storageKey = 'ui-theme',
  ...props
}: ThemeProviderProps) {
  const [theme, setTheme] = useState<Theme>(
    () => (localStorage.getItem(storageKey) as Theme) || defaultTheme
  )

  useEffect(() => {
    const root = window.document.documentElement
    root.classList.remove('light', 'dark')

    if (theme === 'system') {
      const systemTheme = window.matchMedia('(prefers-color-scheme: dark)')
        .matches
        ? 'dark'
        : 'light'
      root.classList.add(systemTheme)
      return
    }

    root.classList.add(theme)
  }, [theme])

  const value = {
    theme,
    setTheme: (theme: Theme) => {
      localStorage.setItem(storageKey, theme)
      setTheme(theme)
    },
  }

  return (
    <ThemeProviderContext.Provider {...props} value={value}>
      {children}
    </ThemeProviderContext.Provider>
  )
}
```

## Best Practices

### Component Design
1. Consistent styling
2. Accessibility first
3. Theme support
4. Responsive design
5. Performance

### Development
- Component organization
- Type safety
- Documentation
- Testing
- Code review

### Customization
1. Theme variables
2. Component variants
3. Style overrides
4. Animation
5. Responsive utilities

### Maintenance
- Version control
- Documentation
- Style guide
- Team guidelines
- Updates

## Resources
- shadcn/ui documentation
- Next.js guides
- Tailwind CSS docs
- Accessibility guidelines
- Design system guides 