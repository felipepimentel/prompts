---
description: A comprehensive guide for building modern web applications using Astro
  with JavaScript and Tailwind CSS, focusing on performance optimization and best
  practices.
path: developer/frameworks/astro/javascript-astro-tailwind-guide
prompt_type: Instruction-based prompting
tags:
- javascript
- astro
- tailwind
- web-development
- performance
- seo
title: JavaScript, Astro, and Tailwind CSS Development Guide
---

# JavaScript, Astro, and Tailwind CSS Development Guide

## Overview
This guide provides comprehensive development guidelines for building modern web applications using Astro, JavaScript, and Tailwind CSS, with a focus on performance optimization and best practices.

## Project Structure
```
src/
  ├── components/     # Reusable Astro components
  │   ├── ui/        # UI components
  │   └── layout/    # Layout components
  ├── layouts/       # Page layouts
  ├── pages/         # File-based routing
  │   └── [...slug]  # Dynamic routes
  └── styles/        # Global styles
public/             # Static assets
astro.config.mjs    # Astro configuration
tailwind.config.cjs # Tailwind configuration
```

## Component Development

### Astro Component Example
```astro
---
// Header.astro
interface Props {
  title: string;
  description?: string;
}

const { title, description } = Astro.props;
---

<header class="bg-white shadow-sm">
  <div class="max-w-7xl mx-auto px-4 py-6">
    <h1 class="text-3xl font-bold text-gray-900">
      {title}
    </h1>
    {description && (
      <p class="mt-2 text-gray-600">
        {description}
      </p>
    )}
  </div>
</header>
```

### Page Component Example
```astro
---
// src/pages/blog/[...slug].astro
import Layout from '../../layouts/BlogLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map(post => ({
    params: { slug: post.slug },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await post.render();
---

<Layout title={post.data.title}>
  <article class="prose lg:prose-xl mx-auto">
    <h1>{post.data.title}</h1>
    <Content />
  </article>
</Layout>
```

## Routing and Navigation

### Dynamic Routes
```astro
---
// src/pages/products/[category]/[id].astro
export async function getStaticPaths() {
  const products = await getProducts();
  return products.map(product => ({
    params: { 
      category: product.category,
      id: product.id 
    },
    props: { product },
  }));
}

const { product } = Astro.props;
---

<Layout title={product.name}>
  <div class="product-details">
    <h1 class="text-2xl font-bold">{product.name}</h1>
    <p class="text-gray-600">{product.description}</p>
  </div>
</Layout>
```

## Performance Optimization

### Partial Hydration
```astro
---
// Interactive component with selective hydration
import InteractiveCounter from '../components/InteractiveCounter';
---

<div class="page-content">
  <!-- Static content -->
  <h1>Welcome</h1>
  
  <!-- Hydrated only when visible -->
  <InteractiveCounter client:visible />
  
  <!-- Hydrated after main content -->
  <Comments client:idle />
  
  <!-- Hydrated immediately -->
  <SearchBar client:load />
</div>
```

### Image Optimization
```astro
---
import { Image } from '@astrojs/image/components';
---

<Image 
  src={import('../assets/hero.jpg')} 
  alt="Hero image"
  width={800}
  height={600}
  format="webp"
  loading="lazy"
  class="rounded-lg shadow-md"
/>
```

## Styling with Tailwind CSS

### Configuration
```javascript
// tailwind.config.cjs
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: '#3b82f6',
        secondary: '#64748b',
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '65ch',
            color: '#1f2937',
            a: {
              color: '#3b82f6',
              '&:hover': {
                color: '#2563eb',
              },
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
```

### Component Styling
```astro
---
// Card.astro
interface Props {
  title: string;
  content: string;
}

const { title, content } = Astro.props;
---

<div class="rounded-lg shadow-md bg-white overflow-hidden hover:shadow-lg transition">
  <div class="px-6 py-4">
    <h3 class="text-xl font-semibold text-gray-900 mb-2">
      {title}
    </h3>
    <p class="text-gray-600">
      {content}
    </p>
  </div>
  <div class="px-6 py-4 bg-gray-50">
    <slot name="footer" />
  </div>
</div>
```

## SEO and Meta Tags

### SEO Component
```astro
---
// components/SEO.astro
interface Props {
  title: string;
  description: string;
  image?: string;
  canonicalURL?: string;
}

const {
  title,
  description,
  image = '/default-og.png',
  canonicalURL = Astro.url,
} = Astro.props;
---

<head>
  <title>{title}</title>
  <meta name="description" content={description} />
  
  <!-- Open Graph -->
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:image" content={image} />
  <meta property="og:url" content={canonicalURL} />
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content={description} />
  <meta name="twitter:image" content={image} />
  
  <!-- Canonical URL -->
  <link rel="canonical" href={canonicalURL} />
</head>
```

## Data Management

### Content Collections
```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    author: z.string(),
    image: z.string().optional(),
    tags: z.array(z.string()),
  }),
});

export const collections = {
  blog,
};
```

## Testing and Accessibility

### Component Testing
```typescript
// Card.test.ts
import { describe, it, expect } from 'vitest';
import { render } from '@testing-library/astro';
import Card from '../components/Card.astro';

describe('Card', () => {
  it('renders title and content correctly', async () => {
    const { getByText } = await render(Card, {
      title: 'Test Title',
      content: 'Test Content',
    });
    
    expect(getByText('Test Title')).toBeDefined();
    expect(getByText('Test Content')).toBeDefined();
  });
});
```

## Resources
- [Astro Documentation](https://docs.astro.build)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [JavaScript MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Core Web Vitals](https://web.dev/vitals/)
- [Astro Performance Guide](https://docs.astro.build/en/guides/performance/) 