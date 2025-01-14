---
title: "Astro with TypeScript Development Guide"
path: "developer/frameworks/astro/guides/astro-typescript-development-guide"
tags: ["astro", "typescript", "frontend", "development", "setup", "guide", "web-development", "best-practices"]
description: "A comprehensive guide for developing Astro applications with TypeScript, focusing on type safety, best practices, and optimal development workflows"
---

# Astro with TypeScript Development Guide

## Overview
This guide provides comprehensive development guidelines for building type-safe Astro applications using TypeScript, focusing on best practices, performance optimization, and maintainable code structure.

## Prerequisites
- Node.js (v18.14.1 or higher)
- TypeScript knowledge
- Code editor with TypeScript support (VS Code recommended)
- Basic understanding of Astro concepts

## Project Setup

### 1. Create New Project
```bash
npm create astro@latest my-astro-app -- --template basics --typescript strict
```

### 2. TypeScript Configuration
Create or update `tsconfig.json`:
```json
{
  "extends": "astro/tsconfig/strict",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    },
    "jsx": "preserve",
    "jsxImportSource": "react",
    "strict": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*.ts", "src/**/*.tsx", "src/**/*.astro"],
  "exclude": ["node_modules"]
}
```

## Project Structure
```
src/
  ├── components/     # Reusable components
  │   ├── ui/        # UI components
  │   └── layouts/   # Layout components
  ├── content/       # Content collections
  │   └── config.ts  # Content configuration
  ├── layouts/       # Page layouts
  ├── pages/         # File-based routing
  ├── types/         # TypeScript types/interfaces
  └── utils/         # Utility functions
```

## TypeScript Best Practices

### 1. Component Types
```typescript
// src/types/components.ts
export interface Props {
  title: string;
  description?: string;
  image?: {
    src: string;
    alt: string;
  };
}

// src/components/Card.astro
---
import type { Props } from '../types/components';

const { title, description, image } = Astro.props;
---

<article class="card">
  {image && <img src={image.src} alt={image.alt} />}
  <h2>{title}</h2>
  {description && <p>{description}</p>}
</article>
```

### 2. Content Collections
```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  schema: z.object({
    title: z.string(),
    publishDate: z.date(),
    author: z.string(),
    tags: z.array(z.string()),
    image: z.object({
      src: z.string(),
      alt: z.string()
    }).optional()
  })
});

export const collections = { blog };
```

### 3. API Integration
```typescript
// src/types/api.ts
export interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

// src/utils/api.ts
export async function fetchData<T>(url: string): Promise<ApiResponse<T>> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return await response.json();
}
```

## Performance Optimization

### 1. Type-Safe Image Handling
```typescript
// src/components/OptimizedImage.astro
---
import { Image } from '@astrojs/image/components';
import type { ImageMetadata } from 'astro';

interface Props {
  src: ImageMetadata;
  alt: string;
  width?: number;
  height?: number;
}

const { src, alt, width, height } = Astro.props;
---

<Image 
  src={src}
  alt={alt}
  width={width}
  height={height}
  format="webp"
  loading="lazy"
/>
```

### 2. Dynamic Imports
```typescript
// src/pages/[slug].astro
---
import type { GetStaticPaths } from 'astro';
import { getCollection } from 'astro:content';

export const getStaticPaths = (async () => {
  const posts = await getCollection('blog');
  return posts.map(post => ({
    params: { slug: post.slug },
    props: { post },
  }));
}) satisfies GetStaticPaths;

const { post } = Astro.props;
const { Content } = await post.render();
---

<article>
  <Content />
</article>
```

## Development Workflow

### 1. Type Checking
```bash
# Run type checking
npm run astro check

# Watch mode for development
npm run astro check --watch
```

### 2. ESLint Configuration
```javascript
// .eslintrc.cjs
module.exports = {
  extends: [
    'plugin:@typescript-eslint/recommended',
    'plugin:astro/recommended',
  ],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  root: true,
  overrides: [
    {
      files: ['*.astro'],
      parser: 'astro-eslint-parser',
      parserOptions: {
        parser: '@typescript-eslint/parser',
        extraFileExtensions: ['.astro'],
      },
    },
  ],
};
```

## Error Handling

### 1. Type-Safe Error Boundaries
```typescript
// src/components/ErrorBoundary.tsx
import type { Component } from 'solid-js';
import { ErrorBoundary as SolidErrorBoundary } from 'solid-js';

interface ErrorBoundaryProps {
  fallback: Component;
  children: any;
}

export const ErrorBoundary: Component<ErrorBoundaryProps> = (props) => {
  return (
    <SolidErrorBoundary fallback={props.fallback}>
      {props.children}
    </SolidErrorBoundary>
  );
};
```

## Testing

### 1. Component Testing
```typescript
// src/components/__tests__/Card.test.ts
import { describe, it, expect } from 'vitest';
import { render } from '@testing-library/astro';
import Card from '../Card.astro';

describe('Card', () => {
  it('renders with required props', async () => {
    const { getByText } = await render(Card, {
      title: 'Test Card',
    });
    
    expect(getByText('Test Card')).toBeDefined();
  });
});
```

## Deployment Considerations

### 1. Environment Variables
```typescript
// src/env.d.ts
/// <reference types="astro/client" />

interface ImportMetaEnv {
  readonly PUBLIC_API_URL: string;
  readonly DATABASE_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

## Resources
- [Astro TypeScript Documentation](https://docs.astro.build/en/guides/typescript/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Astro Content Collections](https://docs.astro.build/en/guides/content-collections/)
- [Testing in Astro](https://docs.astro.build/en/guides/testing/) 