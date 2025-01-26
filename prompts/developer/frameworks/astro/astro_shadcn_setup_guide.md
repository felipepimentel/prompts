---
category: Developer
description: A comprehensive guide for setting up an Astro project with shadcn/ui
  components, including Tailwind CSS and React integration.
model: GPT-4
path: developer/frameworks/astro/astro-shadcn-setup-guide
prompt_type: Instruction-based prompting
tags:
- astro
- shadcn-ui
- tailwind
- react
- typescript
- frontend
- setup
- guide
title: Astro with shadcn/ui Setup Guide
version: '1.0'
---

# Astro with shadcn/ui Setup Guide

## Troubleshooting

### Common Issues

#### 1. Bun Installation Issues
- Ensure you have the latest version of Bun installed
- Try clearing Bun's cache: `bun pm cache rm`
- Check system requirements

#### 2. Tailwind CSS Not Working
- Verify `globals.css` is imported correctly
- Check `astro.config.mjs` configuration
- Clear the `.astro` cache directory

#### 3. shadcn/ui Component Issues
- Ensure React is properly configured
- Check component import paths
- Verify all dependencies are installed

### Error Messages and Solutions

#### ENOENT Error
```bash
Error: ENOENT: no such file or directory
```
Solution: Ensure you're in the correct directory and all paths are correct.

#### Type Errors
```typescript
Type ... is not assignable to type ...
```
Solution: Check your `tsconfig.json` and ensure all types are properly imported.

## Best Practices

### 1. Project Structure
```
src/
  ├── components/
  │   └── ui/        # shadcn/ui components
  ├── layouts/       # Astro layouts
  ├── pages/         # Astro pages
  └── styles/        # Global styles
```

### 2. Performance Optimization
- Use client:load sparingly
- Implement proper code splitting
- Optimize images and assets

### 3. Development Workflow
- Use Git for version control
- Follow component-driven development
- Implement proper testing strategies