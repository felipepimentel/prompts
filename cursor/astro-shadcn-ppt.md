# Astro Project Setup

## Purpose
Create an Astro project and build the frontend.

## Description
Create a content-focused website using Astro.

## Prerequisites
- Requirement: Bun must be installed.

## Tech Stack

### Bun
- Description: A fast JavaScript runtime that allows for quick setup of development environments.

### Astro
- Description: A modern framework for building content-focused websites.

### TypeScript
- Description: A programming language that enables type-safe JavaScript development.

### Tailwind
- Description: A utility-first CSS framework that supports efficient design building.

### shadcn/ui
- Description: A high-quality, reusable React component library that allows for rapid construction of sophisticated UIs.

---

## Steps

### Step 1: Create an Astro project
Set up an Astro project.

Command:
```bash
bunx create-astro@latest ./ --template minimal --install --git --yes
```

---

### Step 2: Add Tailwind CSS
Add Tailwind CSS to the project.

Command:
```bash
npx astro add tailwind --yes --yes --yes
```

---

### Step 3: Add React
Add React to the project.

Command:
```bash
bunx --bun astro add react --yes --yes --yes
```

---

### Step 4: Create `styles/globals.css`
Create `src/styles/globals.css` and add the following content.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

### Step 5: Import the `globals.css` file
Add the following to `src/pages/index.astro` to import the CSS.

```javascript
import "../styles/globals.css";
```

---

### Step 6: Add settings to `astro.config.mjs`
Add the following settings to `astro.config.mjs`.

```javascript
export default defineConfig({
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
  ],
});
```

---

### Step 7: Edit the `tsconfig.json` file
Add the following settings to `tsconfig.json`.

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
  }
}
```

---

### Step 8: Initialize shadcn
Initialize shadcn.

Command:
```bash
bunx --bun shadcn@latest init --defaults
```

---

### Step 9: Install the Button component
Install the Button component from shadcn/ui.

Command:
```bash
bunx --bun shadcn add button
```

---

### Step 10: Add the Button component
Edit `src/pages/index.astro` as follows.

```html
---
import { Button } from "@/components/ui/button";
---
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <h1 class="text-3xl font-bold underline">Hello world!</h1>
    <Button variant="destructive">Hello World</Button>
  </body>
</html>
```

---

### Step 11: Verify shadcn/ui is reflected
Start the development server and verify the changes are reflected.

Command:
```bash
bun run dev
```
