---
category: Developer
description: A comprehensive guide for setting up an Astro project with Tailwind CSS
  integration, focusing on efficient design construction.
model: GPT-4
path: developer/frameworks/astro/astro-tailwind-setup-guide
prompt_type: Instruction-based prompting
tags:
- astro
- tailwind
- typescript
- frontend
- setup
- guide
- css
title: Astro with Tailwind CSS Setup Guide
version: '1.0'
---

# Astro with Tailwind CSS Setup Guide

## Advanced Configuration

### Custom Tailwind Configuration
Create a `tailwind.config.mjs` file with extended configuration:

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      // Add your custom theme extensions here
      colors: {
        primary: {
          50: '#f8fafc',
          // ... add more shades
        }
      }
    }
  },
  plugins: []
}
```

### Dark Mode Support
Add dark mode support to your project:

1. Enable dark mode in `tailwind.config.mjs`:
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  // ... rest of config
}
```

2. Add dark mode toggle functionality:
```typescript
// src/components/ThemeToggle.astro
---
---
<button id="themeToggle">
  <svg width="20" height="20" fill="currentColor" class="dark:hidden">
    <!-- Sun icon -->
  </svg>
  <svg width="20" height="20" fill="currentColor" class="hidden dark:block">
    <!-- Moon icon -->
  </svg>
</button>

<script>
  const theme = (() => {
    if (typeof localStorage !== 'undefined' && localStorage.getItem('theme')) {
      return localStorage.getItem('theme');
    }
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    return 'light';
  })();
      
  if (theme === 'light') {
    document.documentElement.classList.remove('dark');
  } else {
    document.documentElement.classList.add('dark');
  }

  window.localStorage.setItem('theme', theme);
</script>
```

## Best Practices

### 1. CSS Organization
- Use Tailwind's layer directives for custom styles
- Maintain consistent class ordering
- Utilize @apply for repeated patterns

### 2. Performance Optimization
- Enable JIT mode
- Purge unused styles
- Minimize custom CSS

### 3. Responsive Design
- Use mobile-first approach
- Implement fluid typography
- Test across devices

## Troubleshooting

### Common Issues

#### 1. Styles Not Applying
- Check import order in `globals.css`
- Verify Tailwind directives
- Clear build cache

#### 2. Build Performance
- Use proper content configuration
- Enable build caching
- Optimize dependencies

#### 3. Integration Issues
- Check Astro configuration
- Verify plugin compatibility
- Update dependencies

## Development Workflow

### 1. Project Structure
```
src/
  ├── components/    # Reusable components
  ├── layouts/       # Page layouts
  ├── pages/         # Astro pages
  └── styles/        # Global styles and Tailwind config
```

### 2. Version Control
- Track configuration files
- Ignore build artifacts
- Document style decisions

### 3. Team Collaboration
- Maintain style guide
- Document custom utilities
- Share component patterns