---
category: Developer
description: A comprehensive guide for using styled-components in React applications,
  covering advanced patterns, theming, and best practices
model: GPT-4
path: developer/frameworks/react/styled-components-guide
prompt_type: Instruction-based prompting
tags:
- react
- styled-components
- css-in-js
- styling
- frontend
title: React Styled Components Guide
version: '1.0'
---

# React Styled Components Guide

## Core Principles
- Component-based styling
- Dynamic styling
- Theme management
- Performance optimization
- Reusability patterns

## Setup and Configuration

### Installation
```bash
# Using npm
npm install styled-components
npm install -D @types/styled-components

# Using yarn
yarn add styled-components
yarn add -D @types/styled-components
```

### TypeScript Configuration
```typescript
// src/types/styled.d.ts
import 'styled-components'

declare module 'styled-components' {
  export interface DefaultTheme {
    colors: {
      primary: string
      secondary: string
      background: string
      text: string
      error: string
    }
    spacing: {
      xs: string
      sm: string
      md: string
      lg: string
      xl: string
    }
    breakpoints: {
      mobile: string
      tablet: string
      desktop: string
    }
    typography: {
      fontFamily: string
      fontSize: {
        small: string
        medium: string
        large: string
        xlarge: string
      }
      fontWeight: {
        regular: number
        medium: number
        bold: number
      }
    }
  }
}
```

## Theme Setup

### Theme Definition
```typescript
// src/styles/theme.ts
import { DefaultTheme } from 'styled-components'

export const theme: DefaultTheme = {
  colors: {
    primary: '#0070f3',
    secondary: '#7928ca',
    background: '#ffffff',
    text: '#000000',
    error: '#ff0000'
  },
  spacing: {
    xs: '0.25rem',
    sm: '0.5rem',
    md: '1rem',
    lg: '1.5rem',
    xl: '2rem'
  },
  breakpoints: {
    mobile: '320px',
    tablet: '768px',
    desktop: '1024px'
  },
  typography: {
    fontFamily: 'system-ui, sans-serif',
    fontSize: {
      small: '0.875rem',
      medium: '1rem',
      large: '1.25rem',
      xlarge: '1.5rem'
    },
    fontWeight: {
      regular: 400,
      medium: 500,
      bold: 700
    }
  }
}
```

### Theme Provider Setup
```typescript
// src/providers/ThemeProvider.tsx
import { ThemeProvider as StyledThemeProvider } from 'styled-components'
import { theme } from '../styles/theme'

interface ThemeProviderProps {
  children: React.ReactNode
}

export function ThemeProvider({ children }: ThemeProviderProps) {
  return (
    <StyledThemeProvider theme={theme}>
      {children}
    </StyledThemeProvider>
  )
}
```

## Component Patterns

### Basic Styling
```typescript
// src/components/Button/Button.tsx
import styled, { css } from 'styled-components'

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'outline'
  size?: 'small' | 'medium' | 'large'
  fullWidth?: boolean
}

export const Button = styled.button<ButtonProps>`
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  font-weight: ${({ theme }) => theme.typography.fontWeight.medium};
  transition: all 0.2s ease-in-out;
  
  ${({ fullWidth }) =>
    fullWidth &&
    css`
      width: 100%;
    `}
  
  ${({ size, theme }) => {
    switch (size) {
      case 'small':
        return css`
          padding: ${theme.spacing.xs} ${theme.spacing.sm};
          font-size: ${theme.typography.fontSize.small};
        `
      case 'large':
        return css`
          padding: ${theme.spacing.md} ${theme.spacing.lg};
          font-size: ${theme.typography.fontSize.large};
        `
      default:
        return css`
          padding: ${theme.spacing.sm} ${theme.spacing.md};
          font-size: ${theme.typography.fontSize.medium};
        `
    }
  }}
  
  ${({ variant, theme }) => {
    switch (variant) {
      case 'secondary':
        return css`
          background: ${theme.colors.secondary};
          color: white;
          
          &:hover {
            background: ${theme.colors.secondary}dd;
          }
        `
      case 'outline':
        return css`
          background: transparent;
          border: 2px solid ${theme.colors.primary};
          color: ${theme.colors.primary};
          
          &:hover {
            background: ${theme.colors.primary}11;
          }
        `
      default:
        return css`
          background: ${theme.colors.primary};
          color: white;
          
          &:hover {
            background: ${theme.colors.primary}dd;
          }
        `
    }
  }}
  
  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
`
```

### Composition Patterns
```typescript
// src/components/Card/Card.tsx
import styled from 'styled-components'

const CardContainer = styled.div`
  background: ${({ theme }) => theme.colors.background};
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: ${({ theme }) => theme.spacing.md};
`

const CardHeader = styled.div`
  margin-bottom: ${({ theme }) => theme.spacing.md};
`

const CardTitle = styled.h3`
  font-size: ${({ theme }) => theme.typography.fontSize.large};
  font-weight: ${({ theme }) => theme.typography.fontWeight.bold};
  margin: 0;
`

const CardContent = styled.div`
  color: ${({ theme }) => theme.colors.text};
`

interface CardProps {
  title: string
  children: React.ReactNode
}

export function Card({ title, children }: CardProps) {
  return (
    <CardContainer>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent>{children}</CardContent>
    </CardContainer>
  )
}
```

### Responsive Design
```typescript
// src/styles/mixins.ts
import { css, FlattenSimpleInterpolation } from 'styled-components'

export const media = {
  mobile: (styles: FlattenSimpleInterpolation) => css`
    @media (min-width: ${({ theme }) => theme.breakpoints.mobile}) {
      ${styles}
    }
  `,
  tablet: (styles: FlattenSimpleInterpolation) => css`
    @media (min-width: ${({ theme }) => theme.breakpoints.tablet}) {
      ${styles}
    }
  `,
  desktop: (styles: FlattenSimpleInterpolation) => css`
    @media (min-width: ${({ theme }) => theme.breakpoints.desktop}) {
      ${styles}
    }
  `
}

// Usage example
const ResponsiveContainer = styled.div`
  padding: ${({ theme }) => theme.spacing.sm};
  
  ${media.tablet(css`
    padding: ${({ theme }) => theme.spacing.md};
  `)}
  
  ${media.desktop(css`
    padding: ${({ theme }) => theme.spacing.lg};
    max-width: 1200px;
    margin: 0 auto;
  `)}
`
```

## Advanced Patterns

### Global Styles
```typescript
// src/styles/GlobalStyles.ts
import { createGlobalStyle } from 'styled-components'

export const GlobalStyles = createGlobalStyle`
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  
  html,
  body {
    font-family: ${({ theme }) => theme.typography.fontFamily};
    font-size: ${({ theme }) => theme.typography.fontSize.medium};
    color: ${({ theme }) => theme.colors.text};
    background: ${({ theme }) => theme.colors.background};
  }
  
  a {
    color: ${({ theme }) => theme.colors.primary};
    text-decoration: none;
    
    &:hover {
      text-decoration: underline;
    }
  }
`
```

### Animation Utilities
```typescript
// src/styles/animations.ts
import { keyframes, css } from 'styled-components'

export const fadeIn = keyframes`
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
`

export const slideIn = keyframes`
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
`

export const animate = {
  fadeIn: css`
    animation: ${fadeIn} 0.3s ease-in-out;
  `,
  slideIn: css`
    animation: ${slideIn} 0.4s ease-out;
  `
}
```

## Performance Optimization

### Dynamic Styles
```typescript
// src/components/DynamicComponent.tsx
import styled from 'styled-components'

// Bad: Creates new class for each color value
const BadComponent = styled.div`
  color: ${props => props.color};
`

// Good: Uses CSS custom properties
const GoodComponent = styled.div`
  color: var(--color);
  
  ${({ color }) => color && `--color: ${color};`}
`
```

### Component Memoization
```typescript
// src/components/MemoizedComponent.tsx
import { memo } from 'react'
import styled from 'styled-components'

const StyledComponent = styled.div`
  /* styles */
`

interface Props {
  title: string
  onClick: () => void
}

export const MemoizedComponent = memo(
  function MemoizedComponent({ title, onClick }: Props) {
    return (
      <StyledComponent onClick={onClick}>
        {title}
      </StyledComponent>
    )
  }
)
```

## Testing

### Component Testing
```typescript
// src/components/Button/Button.test.tsx
import { render } from '@testing-library/react'
import { ThemeProvider } from 'styled-components'
import { theme } from '../../styles/theme'
import { Button } from './Button'

const renderWithTheme = (component: React.ReactNode) => {
  return render(
    <ThemeProvider theme={theme}>{component}</ThemeProvider>
  )
}

describe('Button', () => {
  it('applies correct styles for variant', () => {
    const { container } = renderWithTheme(
      <Button variant="primary">Click me</Button>
    )
    
    expect(container.firstChild).toHaveStyleRule(
      'background',
      theme.colors.primary
    )
  })
  
  it('applies full width styles when specified', () => {
    const { container } = renderWithTheme(
      <Button fullWidth>Click me</Button>
    )
    
    expect(container.firstChild).toHaveStyleRule(
      'width',
      '100%'
    )
  })
})
```

## Best Practices

### Component Design
1. Consistent naming
2. Prop validation
3. Theme usage
4. Responsive design
5. Accessibility

### Performance
- Memoization
- CSS variables
- Bundle optimization
- Dynamic styles
- SSR support

### Development
1. Type safety
2. Documentation
3. Testing
4. Code organization
5. Theme consistency

### Maintenance
- Component library
- Style guide
- Documentation
- Version control
- Code reviews

## Resources
- Styled Components docs
- React documentation
- TypeScript guides
- Testing guides
- Performance tips