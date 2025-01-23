---
description: A comprehensive guide for developing Chrome extensions using TypeScript,
  focusing on best practices, performance optimization, and modern development patterns
path: developer/frameworks/chrome-extension/guides/chrome-extension-typescript-development-guide
prompt_type: Instruction-based prompting
tags:
- chrome-extension
- typescript
- javascript
- web-development
- browser-extension
- development
- guide
title: Chrome Extension Development with TypeScript Guide
---

# Chrome Extension Development with TypeScript Guide

## Overview
This guide provides detailed instructions and best practices for developing Chrome extensions using TypeScript, ensuring type safety, maintainability, and optimal performance.

## Prerequisites
- Node.js (v18 or higher)
- TypeScript knowledge
- Chrome browser
- Code editor (VS Code recommended)
- Basic understanding of browser extensions

## Project Setup

### 1. Initialize Project
```bash
mkdir my-chrome-extension
cd my-chrome-extension
npm init -y
npm install --save-dev typescript @types/chrome webpack webpack-cli ts-loader
```

### 2. TypeScript Configuration
Create `tsconfig.json`:
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ES2020",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": false,
    "outDir": "./dist",
    "rootDir": "./src",
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

### 3. Webpack Configuration
Create `webpack.config.js`:
```javascript
const path = require('path');

module.exports = {
  mode: 'production',
  entry: {
    background: './src/background/index.ts',
    content: './src/content/index.ts',
    popup: './src/popup/index.ts'
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js'],
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  }
};
```

## Project Structure
```
src/
  ├── background/        # Background scripts
  │   └── index.ts
  ├── content/          # Content scripts
  │   └── index.ts
  ├── popup/           # Popup UI
  │   ├── components/
  │   └── index.ts
  ├── types/          # TypeScript types
  │   └── index.ts
  └── utils/         # Shared utilities
      └── index.ts
```

## Type Definitions

### 1. Message Types
```typescript
// src/types/messages.ts
export type MessageType = 'UPDATE' | 'FETCH' | 'DELETE';

export interface ExtensionMessage<T = unknown> {
  type: MessageType;
  payload: T;
}

export interface MessageResponse<T = unknown> {
  success: boolean;
  data?: T;
  error?: string;
}
```

### 2. API Types
```typescript
// src/types/api.ts
export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

export interface RequestOptions extends RequestInit {
  timeout?: number;
}
```

## Core Features Implementation

### 1. Background Script
```typescript
// src/background/index.ts
import { ExtensionMessage, MessageResponse } from '@/types/messages';

chrome.runtime.onInstalled.addListener(() => {
  // Initialize extension settings
  chrome.storage.sync.set({ 
    enabled: true,
    settings: {
      theme: 'light',
      notifications: true
    }
  });
});

// Message handling
chrome.runtime.onMessage.addListener(
  (
    message: ExtensionMessage,
    sender,
    sendResponse: (response: MessageResponse) => void
  ) => {
    try {
      switch (message.type) {
        case 'UPDATE':
          handleUpdate(message.payload, sendResponse);
          break;
        case 'FETCH':
          handleFetch(message.payload, sendResponse);
          break;
        default:
          throw new Error(`Unknown message type: ${message.type}`);
      }
    } catch (error) {
      sendResponse({
        success: false,
        error: error instanceof Error ? error.message : 'Unknown error'
      });
    }
    return true; // Keep message channel open for async response
  }
);
```

### 2. Content Script
```typescript
// src/content/index.ts
import { ExtensionMessage, MessageResponse } from '@/types/messages';

class ContentScript {
  private observer: MutationObserver;

  constructor() {
    this.observer = new MutationObserver(this.handleDOMChanges.bind(this));
    this.initialize();
  }

  private async initialize(): Promise<void> {
    // Initialize content script
    await this.injectStyles();
    this.setupObserver();
    this.addEventListeners();
  }

  private setupObserver(): void {
    this.observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  private handleDOMChanges(mutations: MutationRecord[]): void {
    // Handle DOM changes
    for (const mutation of mutations) {
      // Process mutations
    }
  }

  private addEventListeners(): void {
    document.addEventListener('click', this.handleClick.bind(this));
  }

  private async handleClick(event: MouseEvent): Promise<void> {
    // Handle click events
  }

  private async injectStyles(): Promise<void> {
    const style = document.createElement('style');
    style.textContent = await this.loadStyles();
    document.head.appendChild(style);
  }

  private async loadStyles(): Promise<string> {
    // Load and return styles
    return '';
  }
}

new ContentScript();
```

### 3. Popup UI
```typescript
// src/popup/index.ts
import { ExtensionMessage, MessageResponse } from '@/types/messages';

class PopupUI {
  private form: HTMLFormElement;

  constructor() {
    this.form = document.querySelector('form')!;
    this.initialize();
  }

  private initialize(): void {
    this.loadSettings();
    this.addEventListeners();
  }

  private async loadSettings(): Promise<void> {
    const settings = await chrome.storage.sync.get('settings');
    this.updateUI(settings);
  }

  private updateUI(settings: any): void {
    // Update UI with settings
  }

  private addEventListeners(): void {
    this.form.addEventListener('submit', this.handleSubmit.bind(this));
  }

  private async handleSubmit(event: Event): Promise<void> {
    event.preventDefault();
    // Handle form submission
  }
}

new PopupUI();
```

## Utility Functions

### 1. API Utilities
```typescript
// src/utils/api.ts
import { ApiResponse, RequestOptions } from '@/types/api';

export async function fetchWithTimeout<T>(
  url: string,
  options: RequestOptions = {}
): Promise<ApiResponse<T>> {
  const { timeout = 5000, ...fetchOptions } = options;

  try {
    const controller = new AbortController();
    const id = setTimeout(() => controller.abort(), timeout);

    const response = await fetch(url, {
      ...fetchOptions,
      signal: controller.signal
    });
    clearTimeout(id);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return { success: true, data };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error'
    };
  }
}
```

### 2. Storage Utilities
```typescript
// src/utils/storage.ts
export async function getStorageItem<T>(key: string): Promise<T | undefined> {
  try {
    const result = await chrome.storage.sync.get(key);
    return result[key];
  } catch (error) {
    console.error(`Error getting storage item ${key}:`, error);
    return undefined;
  }
}

export async function setStorageItem<T>(
  key: string,
  value: T
): Promise<void> {
  try {
    await chrome.storage.sync.set({ [key]: value });
  } catch (error) {
    console.error(`Error setting storage item ${key}:`, error);
  }
}
```

## Performance Optimization

### 1. Event Page Pattern
```typescript
// src/background/index.ts
// Use event pages instead of persistent background
chrome.runtime.onInstalled.addListener(() => {
  // Initialize only necessary data
});

// Use alarms for periodic tasks
chrome.alarms.create('checkUpdates', {
  periodInMinutes: 60
});

chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'checkUpdates') {
    // Perform update check
  }
});
```

### 2. Content Script Optimization
```typescript
// src/content/index.ts
// Lazy loading resources
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Load resource
      observer.unobserve(entry.target);
    }
  });
});

// Efficient DOM manipulation
const fragment = document.createDocumentFragment();
elements.forEach(el => fragment.appendChild(el));
container.appendChild(fragment);
```

## Testing

### 1. Unit Testing
```typescript
// src/utils/__tests__/api.test.ts
import { fetchWithTimeout } from '../api';

describe('API Utils', () => {
  test('fetchWithTimeout handles timeout', async () => {
    const result = await fetchWithTimeout('http://example.com', {
      timeout: 1
    });
    expect(result.success).toBe(false);
    expect(result.error).toContain('timeout');
  });
});
```

### 2. E2E Testing
```typescript
// e2e/extension.test.ts
describe('Extension E2E', () => {
  beforeAll(async () => {
    await browser.runtime.loadExtension('./dist');
  });

  test('extension activates on target pages', async () => {
    await browser.url('http://example.com');
    const element = await browser.$('.extension-element');
    expect(await element.isDisplayed()).toBe(true);
  });
});
```

## Security Considerations

### 1. Content Security Policy
```json
// manifest.json
{
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'",
    "sandbox": "sandbox allow-scripts allow-forms allow-popups allow-modals"
  }
}
```

### 2. Data Sanitization
```typescript
// src/utils/security.ts
export function sanitizeHTML(input: string): string {
  const div = document.createElement('div');
  div.textContent = input;
  return div.innerHTML;
}

export function validateURL(url: string): boolean {
  try {
    new URL(url);
    return true;
  } catch {
    return false;
  }
}
```

## Resources
- [Chrome Extension Documentation](https://developer.chrome.com/docs/extensions/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Chrome Extension Manifest V3](https://developer.chrome.com/docs/extensions/mv3/intro/)
- [Web Extensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions) 