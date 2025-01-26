---
category: Developer
description: A comprehensive guide for developing modern frontend applications using
  Next.js, focusing on best practices, state management, and performance optimization.
model: GPT-4
path: developer/frameworks/nextjs/nextjs-frontend-guide
prompt_type: Instruction-based prompting
tags:
- nextjs
- react
- typescript
- zustand
- shadcn-ui
- tailwind
- frontend
- development
title: Next.js Frontend Development Guide
version: '1.0'
---

# Next.js Frontend Development Guide

## Overview
This guide provides comprehensive development guidelines for building modern frontend applications using Next.js, React, TypeScript, and related technologies, focusing on best practices and performance optimization.

## Core Technologies

### Primary Stack
- Next.js App Router
- React Server Components
- TypeScript
- Zustand (State Management)
- Shadcn UI / Radix UI
- Tailwind CSS

## Project Structure

### Directory Organization
```
src/
  ├── app/              # Next.js App Router
  │   ├── (auth)/     # Auth-related routes
  │   ├── (shop)/    # Shop-related routes
  │   └── api/      # API routes
  ├── components/  # React components
  │   ├── ui/    # UI components
  │   └── forms/ # Form components
  ├── lib/      # Utility functions
  ├── stores/  # Zustand stores
  └── types/  # TypeScript types
```

## Code Style

### TypeScript Best Practices
```typescript
// ✅ Good: Clear interfaces and type definitions
interface User {
  id: string;
  name: string;
  email: string;
  preferences: UserPreferences;
}

// ✅ Good: Map instead of enum
const UserRole = {
  ADMIN: 'admin',
  USER: 'user',
  GUEST: 'guest',
} as const;

type UserRoleType = typeof UserRole[keyof typeof UserRole];

// ❌ Bad: Avoid enums
enum UserRoleEnum {
  ADMIN = 'admin',
  USER = 'user',
  GUEST = 'guest',
}
```

### Component Structure
```typescript
// components/ProductCard.tsx
import { type FC } from 'react';
import { cn } from '@/lib/utils';
import { Card } from '@/components/ui/card';

interface ProductCardProps {
  title: string;
  price: number;
  image: string;
  onAddToCart: () => void;
  className?: string;
}

export const ProductCard: FC<ProductCardProps> = ({
  title,
  price,
  image,
  onAddToCart,
  className,
}) => {
  return (
    <Card className={cn('overflow-hidden', className)}>
      <div className="relative aspect-square">
        <Image
          src={image}
          alt={title}
          fill
          className="object-cover"
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        />
      </div>
      <div className="p-4">
        <h3 className="text-lg font-semibold">{title}</h3>
        <p className="text-gray-600">${price.toFixed(2)}</p>
        <Button onClick={onAddToCart}>Add to Cart</Button>
      </div>
    </Card>
  );
};
```

## State Management

### Zustand Store
```typescript
// stores/cart.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface CartItem {
  id: string;
  quantity: number;
}

interface CartStore {
  items: CartItem[];
  addItem: (id: string) => void;
  removeItem: (id: string) => void;
  clearCart: () => void;
}

export const useCartStore = create<CartStore>()(
  persist(
    (set) => ({
      items: [],
      addItem: (id) =>
        set((state) => ({
          items: state.items.some((item) => item.id === id)
            ? state.items.map((item) =>
                item.id === id
                  ? { ...item, quantity: item.quantity + 1 }
                  : item
              )
            : [...state.items, { id, quantity: 1 }],
        })),
      removeItem: (id) =>
        set((state) => ({
          items: state.items.filter((item) => item.id !== id),
        })),
      clearCart: () => set({ items: [] }),
    }),
    {
      name: 'cart-storage',
    }
  )
);
```

## Server Components

### Data Fetching
```typescript
// app/products/page.tsx
import { ProductCard } from '@/components/ProductCard';
import { getProducts } from '@/lib/api';

export default async function ProductsPage() {
  const products = await getProducts();
  
  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6">Products</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {products.map((product) => (
          <ProductCard
            key={product.id}
            {...product}
          />
        ))}
      </div>
    </div>
  );
}
```

## Client Components

### Interactive Features
```typescript
'use client';

import { useState, useEffect } from 'react';
import { useTheme } from 'next-themes';
import { Button } from '@/components/ui/button';

export function ThemeToggle() {
  const [mounted, setMounted] = useState(false);
  const { theme, setTheme } = useTheme();

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return (
    <Button
      variant="ghost"
      size="sm"
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
    >
      {theme === 'dark' ? '🌞' : '🌙'}
    </Button>
  );
}
```

## Error Handling

### Error Boundaries
```typescript
// app/error.tsx
'use client';

import { Button } from '@/components/ui/button';

interface ErrorBoundaryProps {
  error: Error;
  reset: () => void;
}

export default function Error({ error, reset }: ErrorBoundaryProps) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[400px]">
      <h2 className="text-2xl font-bold mb-4">Something went wrong!</h2>
      <p className="text-gray-600 mb-4">{error.message}</p>
      <Button onClick={reset}>Try again</Button>
    </div>
  );
}
```

## Performance Optimization

### Image Optimization
```typescript
// components/OptimizedImage.tsx
import Image from 'next/image';
import { cn } from '@/lib/utils';

interface OptimizedImageProps {
  src: string;
  alt: string;
  width?: number;
  height?: number;
  priority?: boolean;
  className?: string;
}

export function OptimizedImage({
  src,
  alt,
  width,
  height,
  priority = false,
  className,
}: OptimizedImageProps) {
  return (
    <div className={cn('relative', className)}>
      <Image
        src={src}
        alt={alt}
        width={width}
        height={height}
        priority={priority}
        className="object-cover"
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      />
    </div>
  );
}
```

### Dynamic Imports
```typescript
// components/HeavyComponent.tsx
import dynamic from 'next/dynamic';
import { Spinner } from '@/components/ui/spinner';

const HeavyChart = dynamic(
  () => import('@/components/charts/HeavyChart'),
  {
    loading: () => <Spinner />,
    ssr: false,
  }
);
```

## Testing

### Component Testing
```typescript
// __tests__/ProductCard.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { ProductCard } from '@/components/ProductCard';

describe('ProductCard', () => {
  const mockProduct = {
    title: 'Test Product',
    price: 99.99,
    image: '/test.jpg',
  };

  it('renders product information correctly', () => {
    render(<ProductCard {...mockProduct} onAddToCart={() => {}} />);
    
    expect(screen.getByText(mockProduct.title)).toBeInTheDocument();
    expect(screen.getByText('$99.99')).toBeInTheDocument();
  });

  it('calls onAddToCart when button is clicked', () => {
    const handleAddToCart = jest.fn();
    render(<ProductCard {...mockProduct} onAddToCart={handleAddToCart} />);
    
    fireEvent.click(screen.getByText('Add to Cart'));
    expect(handleAddToCart).toHaveBeenCalledTimes(1);
  });
});
```

## Resources
- [Next.js Documentation](https://nextjs.org/docs)
- [React Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)
- [Zustand Documentation](https://github.com/pmndrs/zustand)
- [Shadcn UI Documentation](https://ui.shadcn.com)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)