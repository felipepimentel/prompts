---
category: Developer
description: A comprehensive guide for creating well-structured, maintainable, and
  reusable components across different frameworks
model: GPT-4
path: developer/instructions/new-component.md
prompt_type: Instruction-based prompting
tags:
- components
- development
- best-practices
- architecture
- design-patterns
title: Component Development Guidelines
version: '1.0'
---

# Component Development Guidelines

## 1. Component Architecture
### 1.1 Core Principles
- Single Responsibility
- Reusability
- Maintainability
- Testability
- Documentation
- Type Safety

### 1.2 File Structure
```
components/
├── ComponentName/
│   ├── index.ts
│   ├── ComponentName.tsx
│   ├── ComponentName.styles.ts
│   ├── ComponentName.test.tsx
│   ├── ComponentName.stories.tsx
│   └── types.ts
```

## 2. Component Design
### 2.1 Interface Definition
```typescript
interface ComponentProps {
  // Required props
  id: string;
  label: string;
  
  // Optional props with defaults
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
  
  // Event handlers
  onChange?: (value: string) => void;
  onBlur?: () => void;
  
  // Children and styling
  className?: string;
  style?: React.CSSProperties;
  children?: React.ReactNode;
}
```

### 2.2 Implementation Pattern
```typescript
import React from 'react';
import { useStyles } from './ComponentName.styles';
import { ComponentProps } from './types';

export const ComponentName: React.FC<ComponentProps> = ({
  id,
  label,
  variant = 'primary',
  disabled = false,
  onChange,
  onBlur,
  className,
  style,
  children,
}) => {
  const styles = useStyles();
  
  // Component logic here
  
  return (
    <div className={styles.root}>
      {/* Component JSX */}
    </div>
  );
};
```

## 3. State Management
### 3.1 Local State
- Use hooks appropriately
- Manage state updates
- Handle side effects
- Implement cleanup
- Cache results

### 3.2 External State
- Redux/Context usage
- Props management
- State synchronization
- Event handling
- Data flow

## 4. Styling Approach
### 4.1 CSS-in-JS
```typescript
export const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    padding: theme.spacing(2),
  },
  primary: {
    color: theme.palette.primary.main,
  },
  secondary: {
    color: theme.palette.secondary.main,
  },
}));
```

### 4.2 Style Guidelines
- Theme consistency
- Responsive design
- Accessibility
- Dark mode support
- CSS variables
- Style isolation

## 5. Testing Strategy
### 5.1 Unit Tests
```typescript
describe('ComponentName', () => {
  it('renders correctly', () => {
    render(<ComponentName id="test" label="Test" />);
    expect(screen.getByText('Test')).toBeInTheDocument();
  });
  
  it('handles events properly', () => {
    const onChange = jest.fn();
    render(<ComponentName id="test" label="Test" onChange={onChange} />);
    // Test implementation
  });
});
```

### 5.2 Test Coverage
- Render testing
- Event handling
- State changes
- Edge cases
- Error states
- Accessibility

## 6. Documentation
### 6.1 Component Documentation
```typescript
/**
 * ComponentName - Description of the component's purpose
 *
 * @component
 * @example
 * ```tsx
 * <ComponentName
 *   id="example"
 *   label="Example Label"
 *   onChange={(value) => console.log(value)}
 * />
 * ```
 */
```

### 6.2 Storybook Integration
```typescript
export default {
  title: 'Components/ComponentName',
  component: ComponentName,
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary'],
    },
  },
} as ComponentMeta<typeof ComponentName>;

const Template: ComponentStory<typeof ComponentName> = (args) => (
  <ComponentName {...args} />
);

export const Primary = Template.bind({});
Primary.args = {
  id: 'story',
  label: 'Story Example',
};
```

## 7. Performance Optimization
### 7.1 Rendering Optimization
- Memoization
- Lazy loading
- Code splitting
- Virtual rendering
- Tree shaking

### 7.2 Resource Management
- Asset optimization
- Bundle size
- Memory usage
- Network requests
- Cache strategy

## 8. Accessibility
### 8.1 ARIA Implementation
- Semantic HTML
- ARIA labels
- Keyboard navigation
- Focus management
- Screen readers

### 8.2 Compliance
- WCAG guidelines
- Color contrast
- Error states
- Loading states
- Interactive elements

## Best Practices
1. Follow component composition patterns
2. Implement proper type checking
3. Write comprehensive tests
4. Document thoroughly
5. Optimize performance
6. Ensure accessibility
7. Maintain consistency

Remember: Component development requires careful attention to architecture, reusability, and maintainability. Always consider the component's role in the larger application context.