---
title: "Chrome Extension Development Guide with TypeScript"
path: "developer/frameworks/chrome-extension/chrome-extension-typescript-guide"
tags: ["chrome-extension", "typescript", "javascript", "web-apis", "development", "best-practices", "security"]
description: "A comprehensive guide for developing Chrome Extensions using TypeScript, including best practices, security considerations, and performance optimization."
---

# Chrome Extension Development Guide with TypeScript

## Overview
This guide provides comprehensive development guidelines for building Chrome Extensions using TypeScript, focusing on best practices, security, and performance optimization.

## Project Structure

### File Organization
```
src/
  ├── manifest.json           # Extension manifest
  ├── background/            # Background scripts
  ├── content/              # Content scripts
  ├── popup/               # Popup UI
  ├── options/            # Options page
  └── types/              # TypeScript types
```

### Naming Conventions
- File names: lowercase with underscores (e.g., `content_script.ts`)
- Functions/variables: camelCase
- Classes: PascalCase
- Constants: UPPER_SNAKE_CASE

## TypeScript Implementation

### Type Safety
```typescript
// Message interfaces
interface ExtensionMessage {
  type: 'UPDATE' | 'FETCH' | 'DELETE';
  payload: unknown;
}

// API response types
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

// Runtime type guards
function isUpdateMessage(msg: ExtensionMessage): msg is ExtensionMessage & { type: 'UPDATE' } {
  return msg.type === 'UPDATE';
}
```

### Configuration
```typescript
// tsconfig.json
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
    "outDir": "./dist"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

## Extension Architecture

### Manifest V3
```json
{
  "manifest_version": 3,
  "name": "Extension Name",
  "version": "1.0.0",
  "description": "Extension description",
  "permissions": [
    "storage",
    "activeTab"
  ],
  "host_permissions": [
    "https://*.example.com/*"
  ],
  "background": {
    "service_worker": "background/worker.js"
  },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content/script.js"]
  }],
  "action": {
    "default_popup": "popup/index.html"
  }
}
```

### Message Passing
```typescript
// Send message from content script
chrome.runtime.sendMessage<ExtensionMessage>({
  type: 'UPDATE',
  payload: data
});

// Listen in background script
chrome.runtime.onMessage.addListener((
  message: ExtensionMessage,
  sender,
  sendResponse
) => {
  if (isUpdateMessage(message)) {
    // Handle update message
    sendResponse({ success: true });
  }
});
```

## Security Best Practices

### Content Security Policy
```json
{
  "manifest_version": 3,
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'"
  }
}
```

### Data Sanitization
```typescript
function sanitizeInput(input: string): string {
  const div = document.createElement('div');
  div.textContent = input;
  return div.innerHTML;
}
```

### Error Handling
```typescript
async function handleApiRequest<T>(
  url: string,
  options: RequestInit
): Promise<ApiResponse<T>> {
  try {
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return { success: true, data };
  } catch (error) {
    console.error('API request failed:', error);
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error'
    };
  }
}
```

## Performance Optimization

### Background Scripts
```typescript
// Use event pages instead of persistent background
chrome.runtime.onInstalled.addListener(() => {
  // Initialize extension
});

// Use alarms instead of setInterval
chrome.alarms.create('checkUpdates', {
  periodInMinutes: 60
});

chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'checkUpdates') {
    // Perform update check
  }
});
```

### Content Script Optimization
```typescript
// Lazy loading
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

## Testing and Debugging

### Unit Testing
```typescript
// Using Jest
describe('Extension Utils', () => {
  test('sanitizeInput removes unsafe content', () => {
    const input = '<script>alert("xss")</script>Hello';
    expect(sanitizeInput(input)).toBe('Hello');
  });
});
```

### Development Tools
- Chrome DevTools for Extensions
- TypeScript compiler in watch mode
- Source maps for debugging

## Cross-browser Compatibility

### WebExtensions API
```typescript
// Use browser namespace with chrome fallback
const browserAPI = typeof browser !== 'undefined' ? browser : chrome;

async function getData(): Promise<any> {
  try {
    return await browserAPI.storage.local.get('key');
  } catch (error) {
    console.error('Storage API error:', error);
    return null;
  }
}
```

## Resources
- [Chrome Extensions Documentation](https://developer.chrome.com/docs/extensions)
- [TypeScript Documentation](https://www.typescriptlang.org/docs)
- [WebExtensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions)
- [Chrome Extension Security Guidelines](https://developer.chrome.com/docs/extensions/mv3/security) 