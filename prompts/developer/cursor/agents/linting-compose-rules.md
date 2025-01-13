# Composer Agent Linting Guidelines

## Overview
This document provides structured guidelines for implementing linting directives in composer agents. It focuses on maintainable, clear, and effective code quality enforcement.

## Core Concepts

### Directive Types

1. **ENFORCE**
   - Mandatory rules that must be followed
   - Used for critical code quality requirements
   - Example:
   ```yaml
   ENFORCE:
     naming:
       convention: "consistent"
       pattern: "descriptive"
     structure:
       organization: "modular"
       hierarchy: "clear"
   ```

2. **CHECK**
   - Validation rules for code quality
   - Used for runtime verification
   - Example:
   ```yaml
   CHECK:
     validation:
       input: "sanitized"
       types: "verified"
     formatting:
       style: "standard"
       readability: "high"
   ```

3. **OPTIMIZE**
   - Performance improvement directives
   - Used for efficiency enhancements
   - Example:
   ```yaml
   OPTIMIZE:
     performance:
       execution: "efficient"
       memory: "minimal"
     response:
       time: "optimized"
       resources: "managed"
   ```

## Implementation Guidelines

### React Component Example
```typescript
// @lint-directive: ENFORCE component-structure
const Button: React.FC<ButtonProps> = ({ text, onClick }) => {
  const [state, setState] = useState<ButtonState>(initialState);

  const handleInteraction = useCallback(() => {
    setState(newState);
    onClick?.();
  }, [onClick]);

  return <button onClick={handleInteraction}>{text}</button>;
};
```

### When Handling Data

```python
# Tell the robot: "Be careful with the data!"
# @lint-directive: CHECK data-safety
def process_user_info(data):
    # Always check if you have everything you need
    if not data:
        return "Oops, no data!"

    # Keep things clean and safe
    clean_data = remove_bad_stuff(data)
    return clean_data
```

## Simple Rules to Remember 🌈

1. **Be Clear**

   - Use simple names
   - Write what you mean
   - Keep things organized

2. **Be Safe**

   - Check for mistakes
   - Handle errors nicely
   - Keep secrets safe

3. **Be Smart**
   - Make things fast
   - Don't waste space
   - Keep it simple

## Quick Tips 💡

- Start with `ENFORCE` for important rules
- Use `CHECK` for things that might go wrong
- Add `OPTIMIZE` when everything works but could be better

## Examples by Task 🎯

### Making a Website

```yaml
ENFORCE: {
    components: "neat", # Keep your toys organized
    naming: "clear", # Label everything clearly
    safety: "important", # Don't run with scissors
  }
```

### Working with Data

```yaml
CHECK: {
    input: "clean", # Wash your hands before eating
    storage: "safe", # Put things away properly
    output: "correct", # Double-check your work
  }
```

### Making Things Fast

```yaml
OPTIMIZE: {
    loading: "quick", # Pack your bag the night before
    response: "instant", # Answer quickly when called
    memory: "light", # Don't carry too much stuff
  }
```

## When Things Go Wrong 🚨

1. If the agent isn't following rules:

   - Check if your instructions are clear
   - Make sure you're using the right magic word
   - Try breaking big rules into smaller ones

2. If things are too slow:
   - Start with the most important rules
   - Add optimization rules later
   - Keep it simple at first

## Remember! 🌟

- Start simple
- Be clear
- Stay consistent
- Check your work
- Make it better over time

Just like teaching a friend to play a game, be patient and clear with your composer agents, and they'll learn to follow your linting rules perfectly! 🎮