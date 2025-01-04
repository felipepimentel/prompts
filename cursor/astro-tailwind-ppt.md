# Astro Project Setup

## Purpose
Create an Astro project and build the frontend.

## Description
Create a content-focused website using Astro.

## Prerequisites
- Requirement: Bun must be installed.

## Tech Stack

### Bun
- Description: A fast JavaScript runtime that allows for quick setup of the development environment.

### Astro
- Description: A modern framework for building content-focused websites.

### TypeScript
- Description: A programming language that enables type-safe JavaScript development.

### Tailwind
- Description: A utility-first CSS framework that aids in efficient design construction.

---

## Steps

### Step 1: Create an Astro Project
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

### Step 3: Apply Tailwind CSS to Code
Modify the `index.astro` code to ensure Tailwind CSS styles are applied.

Changes:
Change the following:
```html
<h1>Astro</h1>
```
To:
```html
<h1 class="text-3xl font-bold underline">Hello world!</h1>
```

---

### Step 4: Verify Tailwind CSS is Applied
Start the development server and verify that the changes are reflected.

Command:
```bash
bun run dev
```

