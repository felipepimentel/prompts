---
title: "React with TypeScript and shadcn/ui Development Guide"
path: "developer/frameworks/react/react-typescript-shadcn-guide"
tags: ["react", "typescript", "shadcn-ui", "next.js", "tailwind", "frontend", "development"]
description: "A comprehensive guide for developing React applications using TypeScript, shadcn/ui, and modern best practices."
---

# React with TypeScript and shadcn/ui Development Guide

## Overview
This guide provides comprehensive development guidelines for building modern React applications using TypeScript, shadcn/ui, and Next.js App Router, focusing on best practices and performance optimization.

## Project Setup

### Dependencies
```json
{
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "tailwindcss": "^3.3.0",
    "@radix-ui/react-icons": "^1.3.0",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.0.0"
  }
}
```

### Project Structure
```
src/
  ├── app/              # Next.js App Router pages
  ├── components/       # React components
  │   ├── ui/          # shadcn/ui components
  │   └── custom/      # Custom components
  ├── lib/             # Utility functions
  ├── hooks/           # Custom React hooks
  ├── types/           # TypeScript types
  └── styles/          # Global styles
```

## TypeScript Best Practices

### Type Definitions
```typescript
// ✅ Good: Clear interface definitions
interface User {
  id: string;
  name: string;
  email: string;
  preferences: UserPreferences;
}

interface UserPreferences {
  theme: 'light' | 'dark' | 'system';
  notifications: boolean;
  language: string;
}

// ❌ Bad: Loose typing
interface Data {
  [key: string]: any;
}
```

### Component Props
```typescript
// ✅ Good: Strongly typed props
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'destructive' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  children: React.ReactNode;
}

const Button = ({
  variant = 'default',
  size = 'md',
  isLoading = false,
  children,
  ...props
}: ButtonProps) => {
  return (
    <button
      className={cn(
        buttonVariants({ variant, size }),
        isLoading && 'opacity-50 cursor-not-allowed'
      )}
      disabled={isLoading}
      {...props}
    >
      {isLoading ? <Spinner className="mr-2" /> : null}
      {children}
    </button>
  );
};
```

## React Components

### Functional Components
```typescript
// ✅ Good: Well-structured functional component
import { useState, useEffect } from 'react';
import { User } from '@/types';

interface UserProfileProps {
  userId: string;
  onUpdate: (user: User) => void;
}

export function UserProfile({ userId, onUpdate }: UserProfileProps) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    async function fetchUser() {
      try {
        setIsLoading(true);
        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) throw new Error('Failed to fetch user');
        const data = await response.json();
        setUser(data);
      } catch (err) {
        setError(err instanceof Error ? err : new Error('Unknown error'));
      } finally {
        setIsLoading(false);
      }
    }

    fetchUser();
  }, [userId]);

  if (isLoading) return <Spinner />;
  if (error) return <ErrorMessage message={error.message} />;
  if (!user) return null;

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">{user.name}</h1>
      <p className="text-gray-600">{user.email}</p>
      {/* Additional profile content */}
    </div>
  );
}
```

## shadcn/ui Integration

### Component Customization
```typescript
// components/ui/custom-dialog.tsx
import * as React from 'react';
import * as DialogPrimitive from '@radix-ui/react-dialog';
import { cn } from '@/lib/utils';

const Dialog = DialogPrimitive.Root;
const DialogTrigger = DialogPrimitive.Trigger;

const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPrimitive.Portal>
    <DialogPrimitive.Overlay
      className="fixed inset-0 bg-black/50 backdrop-blur-sm"
    />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] translate-x-[-50%] translate-y-[-50%]",
        "w-full max-w-lg p-6 bg-white rounded-lg shadow-xl",
        "dark:bg-gray-900",
        className
      )}
      {...props}
    >
      {children}
    </DialogPrimitive.Content>
  </DialogPrimitive.Portal>
));
DialogContent.displayName = "DialogContent";

export { Dialog, DialogTrigger, DialogContent };
```

## Performance Optimization

### Code Splitting
```typescript
// ✅ Good: Lazy loading components
const HeavyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <HeavyComponent />
    </Suspense>
  );
}
```

### Memoization
```typescript
// ✅ Good: Proper use of useMemo and useCallback
function ExpensiveList({ items, onItemSelect }: ExpensiveListProps) {
  const sortedItems = useMemo(() => {
    return [...items].sort((a, b) => b.priority - a.priority);
  }, [items]);

  const handleSelect = useCallback((id: string) => {
    onItemSelect(id);
  }, [onItemSelect]);

  return (
    <ul>
      {sortedItems.map(item => (
        <ListItem
          key={item.id}
          item={item}
          onSelect={handleSelect}
        />
      ))}
    </ul>
  );
}
```

## State Management

### React Query Integration
```typescript
// ✅ Good: Efficient data fetching with React Query
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function UserDashboard() {
  const queryClient = useQueryClient();
  
  const { data: user, isLoading } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  const updateUser = useMutation({
    mutationFn: (newData: Partial<User>) => updateUserData(userId, newData),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['user', userId] });
    },
  });

  if (isLoading) return <Spinner />;

  return (
    <div>
      <UserProfile
        user={user}
        onUpdate={data => updateUser.mutate(data)}
      />
    </div>
  );
}
```

## Testing

### Component Testing
```typescript
// ✅ Good: Comprehensive component tests
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders children correctly', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('handles click events', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('displays loading state', () => {
    render(<Button isLoading>Submit</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
    expect(screen.getByTestId('spinner')).toBeInTheDocument();
  });
});
```

## Accessibility

### ARIA Attributes
```typescript
// ✅ Good: Accessible components
function Accordion({ items }: AccordionProps) {
  const [openItem, setOpenItem] = useState<string | null>(null);

  return (
    <div role="region" aria-label="Accordion">
      {items.map(item => (
        <div key={item.id}>
          <button
            id={`accordion-header-${item.id}`}
            aria-expanded={openItem === item.id}
            aria-controls={`accordion-panel-${item.id}`}
            onClick={() => setOpenItem(item.id)}
          >
            {item.title}
          </button>
          <div
            id={`accordion-panel-${item.id}`}
            role="region"
            aria-labelledby={`accordion-header-${item.id}`}
            hidden={openItem !== item.id}
          >
            {item.content}
          </div>
        </div>
      ))}
    </div>
  );
}
```

## Resources
- [React Documentation](https://react.dev)
- [TypeScript Documentation](https://www.typescriptlang.org/docs)
- [shadcn/ui Documentation](https://ui.shadcn.com)
- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs) 