# Linting for Composer Agents: The Simple Guide 🎨

Imagine you're teaching a robot to paint a picture. You want to give it clear rules about what colors to use, how to hold the brush, and where to paint. That's exactly what linting directives do for composer agents!

## The Basics 🌟

Think of linting directives like a recipe card:

```yaml
TELL_ROBOT:
  what: "paint a tree"
  how: "carefully"
  rules: "stay inside the lines"
```

## Three Magic Words 🎭

1. **ENFORCE** - "You MUST do this!"

   ```yaml
   ENFORCE: {
       naming: "clean", # Like saying "always label your toys"
       structure: "neat", # Like "keep your room organized"
     }
   ```

2. **CHECK** - "Please make sure this is right"

   ```yaml
   CHECK: {
       spelling: "correct", # Like "double-check your homework"
       formatting: "readable", # Like "write neatly"
     }
   ```

3. **OPTIMIZE** - "Try to make this better"
   ```yaml
   OPTIMIZE: {
       speed: "fast", # Like "clean your room quickly"
       memory: "efficient", # Like "don't waste space"
     }
   ```

## Real Examples Made Simple 🎈

### When Writing React Components

```typescript
// Tell the robot: "Keep things tidy!"
// @lint-directive: ENFORCE neat-code
const Button = ({ text }) => {
  // Put hooks at the top, like putting your shoes on before your coat
  const [isClicked, setClicked] = useState(false);

  // Name things clearly, like labeling your lunchbox
  const handleClick = () => setClicked(true);

  return <button onClick={handleClick}>{text}</button>;
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