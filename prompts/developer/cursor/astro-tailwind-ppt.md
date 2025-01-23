---
description: A comprehensive guide for setting up and optimizing an Astro project
  with Tailwind CSS integration using Bun as the package manager
path: developer/frameworks/astro/guides/astro-tailwind-setup-guide
prompt_type: Instruction-based prompting
tags:
- astro
- tailwind
- typescript
- frontend
- setup
- guide
- css
- bun
- web-development
title: Astro with Tailwind CSS Setup Guide
---

# Astro with Tailwind CSS Setup Guide

## Overview
This guide provides step-by-step instructions for setting up an Astro project with Tailwind CSS integration, focusing on best practices and modern development workflows.

## Prerequisites
- Bun installed (latest version recommended)
- Basic knowledge of TypeScript and Tailwind CSS
- Code editor (VS Code recommended)

## Tech Stack Benefits
- **Bun**: Ultra-fast JavaScript runtime and package manager
- **Astro**: Optimized for content-focused websites with partial hydration
- **TypeScript**: Enhanced developer experience with type safety
- **Tailwind**: Utility-first CSS framework for rapid UI development

## Setup Steps

### 1. Project Initialization
```bash
bunx create-astro@latest ./ --template minimal --install --git --yes
```

### 2. Tailwind CSS Integration
```bash
npx astro add tailwind --yes
```

### 3. Configure Tailwind
Create `src/styles/globals.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 4. Update Astro Config
Modify `astro.config.mjs`:
```javascript
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [
    tailwind({
      // Disable injecting a basic `base.css` import
      applyBaseStyles: false,
    }),
  ],
});
```

### 5. Create Base Layout
Create `src/layouts/BaseLayout.astro`:
```astro
---
import '../styles/globals.css';

interface Props {
  title: string;
  description?: string;
}

const { title, description = 'Astro site with Tailwind CSS' } = Astro.props;
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content={description} />
    <title>{title}</title>
  </head>
  <body class="min-h-screen bg-white dark:bg-gray-900">
    <slot />
  </body>
</html>
```

### 6. Update Index Page
Modify `src/pages/index.astro`:
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Welcome">
  <main class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-gray-900 dark:text-white">
      Welcome to Astro + Tailwind CSS
    </h1>
    <p class="mt-4 text-lg text-gray-600 dark:text-gray-300">
      Start building your content-focused website
    </p>
  </main>
</BaseLayout>
```

## Best Practices

### Performance Optimization
- Use `client:load` sparingly
- Implement proper code splitting
- Optimize images using Astro's image integration
- Minimize unused Tailwind classes

### Development Workflow
- Follow component-driven development
- Implement proper TypeScript types
- Use Git for version control
- Document component usage

### Code Organization
```
src/
  ├── components/    # Reusable components
  ├── layouts/       # Page layouts
  ├── pages/         # Astro pages
  └── styles/        # Global styles
```

## Verification
Start the development server:
```bash
bun run dev
```

Visit `http://localhost:4321` to verify the setup.

## Common Issues & Solutions

### Styles Not Applying
- Verify globals.css is imported
- Check Tailwind configuration
- Clear build cache

### Build Performance
- Enable build caching
- Optimize dependencies
- Use proper content configuration

### Type Support
- Ensure proper TypeScript configuration
- Use Astro's built-in types
- Keep dependencies updated 