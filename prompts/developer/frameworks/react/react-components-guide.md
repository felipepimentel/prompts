---
category: Developer
description: A comprehensive guide for developing reusable and maintainable React
  components using modern patterns and best practices
model: GPT-4
path: developer/frameworks/react/react-components-guide
prompt_type: Instruction-based prompting
tags:
- react
- typescript
- components
- frontend
- development
title: React Components Development Guide
version: '1.0'
---

# React Components Development Guide

## Core Principles
- Component architecture
- Reusability patterns
- Type safety
- Performance optimization
- Testing strategies

## Project Setup

### Directory Structure
```
src/
├── components/
│   ├── common/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   └── Button.module.css
│   │   └── Input/
│   │       ├── Input.tsx
│   │       ├── Input.test.tsx
│   │       └── Input.module.css
│   ├── layout/
│   │   ├── Header/
│   │   └── Footer/
│   └── features/
│       ├── Auth/
│       └── Dashboard/
├── hooks/
│   ├── useForm.ts
│   └── useAuth.ts
├── utils/
│   ├── validation.ts
│   └── formatting.ts
└── types/
    └── index.ts
```

### Component Template
```typescript
// src/components/common/Button/Button.tsx
import { forwardRef } from 'react'
import styles from './Button.module.css'

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline'
  size?: 'small' | 'medium' | 'large'
  isLoading?: boolean
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      variant = 'primary',
      size = 'medium',
      isLoading = false,
      children,
      className,
      disabled,
      ...props
    },
    ref
  ) => {
    return (
      <button
        ref={ref}
        className={[
          styles.button,
          styles[variant],
          styles[size],
          className
        ].filter(Boolean).join(' ')}
        disabled={disabled || isLoading}
        {...props}
      >
        {isLoading ? (
          <span className={styles.loader} />
        ) : children}
      </button>
    )
  }
)

Button.displayName = 'Button'
```

## Component Patterns

### Compound Components
```typescript
// src/components/common/Select/Select.tsx
import {
  createContext,
  useContext,
  useState,
  type ReactNode
} from 'react'

interface SelectContextType {
  value: string
  onChange: (value: string) => void
  isOpen: boolean
  setIsOpen: (isOpen: boolean) => void
}

const SelectContext = createContext<SelectContextType | null>(null)

interface SelectProps {
  value: string
  onChange: (value: string) => void
  children: ReactNode
}

export function Select({ value, onChange, children }: SelectProps) {
  const [isOpen, setIsOpen] = useState(false)
  
  return (
    <SelectContext.Provider
      value={{ value, onChange, isOpen, setIsOpen }}
    >
      <div className="select">{children}</div>
    </SelectContext.Provider>
  )
}

interface TriggerProps {
  children: ReactNode
}

Select.Trigger = function Trigger({ children }: TriggerProps) {
  const context = useContext(SelectContext)
  if (!context) throw new Error('Must be used within Select')
  
  return (
    <button
      onClick={() => context.setIsOpen(!context.isOpen)}
      className="select-trigger"
    >
      {children}
    </button>
  )
}

interface OptionProps {
  value: string
  children: ReactNode
}

Select.Option = function Option({ value, children }: OptionProps) {
  const context = useContext(SelectContext)
  if (!context) throw new Error('Must be used within Select')
  
  return (
    <div
      onClick={() => {
        context.onChange(value)
        context.setIsOpen(false)
      }}
      className="select-option"
    >
      {children}
    </div>
  )
}
```

### Render Props
```typescript
// src/components/common/List/List.tsx
import { type ReactNode } from 'react'

interface Item {
  id: string
  [key: string]: any
}

interface ListProps<T extends Item> {
  items: T[]
  renderItem: (item: T) => ReactNode
  keyExtractor?: (item: T) => string
}

export function List<T extends Item>({
  items,
  renderItem,
  keyExtractor = (item) => item.id
}: ListProps<T>) {
  return (
    <div className="list">
      {items.map((item) => (
        <div key={keyExtractor(item)} className="list-item">
          {renderItem(item)}
        </div>
      ))}
    </div>
  )
}
```

## Custom Hooks

### Form Management
```typescript
// src/hooks/useForm.ts
import { useState, useCallback } from 'react'

interface FormState {
  [key: string]: any
}

interface ValidationRules {
  [key: string]: (value: any) => string | undefined
}

interface UseFormOptions {
  initialValues: FormState
  validationRules?: ValidationRules
  onSubmit: (values: FormState) => void | Promise<void>
}

export function useForm({
  initialValues,
  validationRules = {},
  onSubmit
}: UseFormOptions) {
  const [values, setValues] = useState(initialValues)
  const [errors, setErrors] = useState<FormState>({})
  const [isSubmitting, setIsSubmitting] = useState(false)
  
  const validateField = useCallback(
    (name: string, value: any) => {
      const validate = validationRules[name]
      if (!validate) return undefined
      return validate(value)
    },
    [validationRules]
  )
  
  const handleChange = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      const { name, value } = event.target
      setValues((prev) => ({ ...prev, [name]: value }))
      
      const error = validateField(name, value)
      setErrors((prev) => ({
        ...prev,
        [name]: error
      }))
    },
    [validateField]
  )
  
  const handleSubmit = useCallback(
    async (event: React.FormEvent) => {
      event.preventDefault()
      
      const newErrors: FormState = {}
      Object.keys(values).forEach((key) => {
        const error = validateField(key, values[key])
        if (error) newErrors[key] = error
      })
      
      if (Object.keys(newErrors).length > 0) {
        setErrors(newErrors)
        return
      }
      
      setIsSubmitting(true)
      try {
        await onSubmit(values)
      } finally {
        setIsSubmitting(false)
      }
    },
    [values, validateField, onSubmit]
  )
  
  return {
    values,
    errors,
    isSubmitting,
    handleChange,
    handleSubmit
  }
}
```

### Data Fetching
```typescript
// src/hooks/useQuery.ts
import { useState, useEffect } from 'react'

interface QueryOptions<T> {
  queryFn: () => Promise<T>
  initialData?: T
  onSuccess?: (data: T) => void
  onError?: (error: Error) => void
}

export function useQuery<T>({
  queryFn,
  initialData,
  onSuccess,
  onError
}: QueryOptions<T>) {
  const [data, setData] = useState<T | undefined>(initialData)
  const [error, setError] = useState<Error | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  
  useEffect(() => {
    let isMounted = true
    
    async function fetchData() {
      try {
        const result = await queryFn()
        if (isMounted) {
          setData(result)
          onSuccess?.(result)
        }
      } catch (err) {
        if (isMounted) {
          const error = err instanceof Error ? err : new Error(String(err))
          setError(error)
          onError?.(error)
        }
      } finally {
        if (isMounted) {
          setIsLoading(false)
        }
      }
    }
    
    fetchData()
    
    return () => {
      isMounted = false
    }
  }, [queryFn, onSuccess, onError])
  
  return { data, error, isLoading }
}
```

## Testing

### Component Testing
```typescript
// src/components/common/Button/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react'
import { Button } from './Button'

describe('Button', () => {
  it('renders children correctly', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })
  
  it('handles click events', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>Click me</Button>)
    
    fireEvent.click(screen.getByText('Click me'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })
  
  it('shows loading state', () => {
    render(<Button isLoading>Click me</Button>)
    expect(screen.queryByText('Click me')).not.toBeInTheDocument()
    expect(screen.getByRole('button')).toBeDisabled()
  })
  
  it('applies variant classes correctly', () => {
    const { container } = render(
      <Button variant="secondary">Click me</Button>
    )
    expect(container.firstChild).toHaveClass('secondary')
  })
})
```

### Hook Testing
```typescript
// src/hooks/useForm.test.ts
import { renderHook, act } from '@testing-library/react'
import { useForm } from './useForm'

describe('useForm', () => {
  const initialValues = { email: '', password: '' }
  const validationRules = {
    email: (value: string) =>
      !value.includes('@') ? 'Invalid email' : undefined,
    password: (value: string) =>
      value.length < 6 ? 'Password too short' : undefined
  }
  
  it('initializes with initial values', () => {
    const { result } = renderHook(() =>
      useForm({
        initialValues,
        validationRules,
        onSubmit: jest.fn()
      })
    )
    
    expect(result.current.values).toEqual(initialValues)
  })
  
  it('updates values on change', () => {
    const { result } = renderHook(() =>
      useForm({
        initialValues,
        validationRules,
        onSubmit: jest.fn()
      })
    )
    
    act(() => {
      result.current.handleChange({
        target: { name: 'email', value: 'test@example.com' }
      } as React.ChangeEvent<HTMLInputElement>)
    })
    
    expect(result.current.values.email).toBe('test@example.com')
  })
  
  it('validates fields on change', () => {
    const { result } = renderHook(() =>
      useForm({
        initialValues,
        validationRules,
        onSubmit: jest.fn()
      })
    )
    
    act(() => {
      result.current.handleChange({
        target: { name: 'email', value: 'invalid' }
      } as React.ChangeEvent<HTMLInputElement>)
    })
    
    expect(result.current.errors.email).toBe('Invalid email')
  })
})
```

## Best Practices

### Component Design
1. Single responsibility
2. Prop type safety
3. Controlled components
4. Error boundaries
5. Accessibility

### Performance
- Memoization
- Code splitting
- Lazy loading
- Virtual lists
- Bundle optimization

### Testing
1. Component testing
2. Hook testing
3. Integration tests
4. Snapshot tests
5. E2E testing

### Development
- Type safety
- Documentation
- Error handling
- State management
- Code organization

## Resources
- React documentation
- TypeScript guides
- Testing library docs
- Performance guides
- Accessibility guidelines