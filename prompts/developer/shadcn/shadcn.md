---
description: Comprehensive guide for building modern web applications using ShadCN
  UI components and best practices
path: developer/shadcn/shadcn.md
prompt_type: Instruction-based prompting
tags:
- shadcn
- nextjs
- react
- ui
- tailwind
- typescript
- frontend
title: ShadCN UI Development Guide
---

# ShadCN UI Development Guide

## Core Concepts

### 1. Project Setup
```bash
# Initialize a new Next.js project with TypeScript
npx create-next-app@latest my-app --typescript --tailwind --eslint

# Navigate to project
cd my-app

# Initialize shadcn UI
npx shadcn-ui@latest init
```

### 2. Configuration
```json
// components.json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

## Component Integration

### 1. Adding Components
```bash
# Add individual components
npx shadcn-ui@latest add button
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add form
```

### 2. Component Customization
```typescript
// components/ui/custom-button.tsx
import { cn } from "@/lib/utils"
import { Button } from "./button"

interface CustomButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "default" | "custom"
}

export function CustomButton({ 
  className, 
  variant = "default",
  ...props 
}: CustomButtonProps) {
  return (
    <Button
      className={cn(
        variant === "custom" && "bg-gradient-to-r from-blue-500 to-purple-500",
        className
      )}
      {...props}
    />
  )
}
```

## Best Practices

### 1. Component Organization
- Group related components in feature-specific directories
- Keep reusable UI components in `components/ui`
- Place layout components in `components/layout`
- Store complex forms in `components/forms`

### 2. Styling Guidelines
- Use the `cn` utility for class name composition
- Leverage CSS variables for theming
- Maintain consistent spacing using Tailwind classes
- Implement responsive designs systematically

### 3. Form Handling
```typescript
// components/forms/signup-form.tsx
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"

const formSchema = z.object({
  username: z.string().min(2).max(50),
  email: z.string().email(),
  password: z.string().min(8),
})

export function SignupForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "",
      email: "",
      password: "",
    },
  })

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)}>
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        {/* Add other form fields */}
      </form>
    </Form>
  )
}
```

### 4. Dark Mode Implementation
```typescript
// components/theme-provider.tsx
import { ThemeProvider as NextThemesProvider } from "next-themes"

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  return (
    <NextThemesProvider
      attribute="class"
      defaultTheme="system"
      enableSystem
      disableTransitionOnChange
    >
      {children}
    </NextThemesProvider>
  )
}
```

## Advanced Features

### 1. Custom Hooks
```typescript
// hooks/use-theme-toggle.ts
import { useTheme } from "next-themes"

export function useThemeToggle() {
  const { theme, setTheme } = useTheme()

  const toggleTheme = () => {
    setTheme(theme === "dark" ? "light" : "dark")
  }

  return { theme, toggleTheme }
}
```

### 2. Component Composition
```typescript
// components/ui/card-with-form.tsx
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export function CardWithForm({ 
  title,
  description,
  children,
  footer
}: {
  title: string
  description?: string
  children: React.ReactNode
  footer?: React.ReactNode
}) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        {description && <CardDescription>{description}</CardDescription>}
      </CardHeader>
      <CardContent>{children}</CardContent>
      {footer && <CardFooter>{footer}</CardFooter>}
    </Card>
  )
}
```

## Performance Optimization

### 1. Component Loading
- Use dynamic imports for large components
- Implement loading states with shadcn's Skeleton component
- Optimize images using Next.js Image component

### 2. State Management
- Use React Query for server state
- Implement context for theme and authentication
- Leverage local storage for persistent preferences

## Accessibility

### 1. Core Principles
- Maintain ARIA labels and roles
- Ensure keyboard navigation
- Provide sufficient color contrast
- Support screen readers

### 2. Implementation
```typescript
// components/ui/accessible-button.tsx
import { Button } from "./button"

export function AccessibleButton({
  label,
  description,
  ...props
}: {
  label: string
  description?: string
} & React.ComponentProps<typeof Button>) {
  return (
    <Button
      aria-label={label}
      aria-description={description}
      {...props}
    />
  )
}
```

## Testing

### 1. Component Testing
```typescript
// __tests__/button.test.tsx
import { render, screen } from "@testing-library/react"
import { Button } from "@/components/ui/button"

describe("Button", () => {
  it("renders correctly", () => {
    render(<Button>Click me</Button>)
    expect(screen.getByRole("button")).toBeInTheDocument()
  })
})
```

Remember:
- Keep components modular and reusable
- Maintain consistent styling patterns
- Document component APIs clearly
- Test thoroughly, especially interactive elements
- Stay updated with shadcn UI releases
- Consider accessibility in all implementations 