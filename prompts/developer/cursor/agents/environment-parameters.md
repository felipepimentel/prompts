# Cursor Environment Configuration Guide

## Overview
This document outlines the standardized approach for managing Cursor workspace environments through environment variables and configuration files. It provides a systematic method for handling workspace settings, themes, and project-specific configurations.

## Environment Variables

### Core Configuration
```env
# Workspace Identification
CURSOR_WORKSPACE_NAME="project-name"
CURSOR_WORKSPACE_TYPE="development|staging|production"

# Editor Settings
CURSOR_THEME="default-dark"
CURSOR_FONT_FAMILY="JetBrains Mono"
CURSOR_FONT_SIZE="14"

# Project Configuration
CURSOR_PROJECT_ROOT="${workspaceFolder}"
CURSOR_PROJECT_TYPE="node|python|go|etc"
```

### Advanced Settings
```env
# Performance Optimization
CURSOR_MEMORY_LIMIT="4096"
CURSOR_CPU_LIMIT="2"

# Feature Flags
CURSOR_ENABLE_COPILOT=true
CURSOR_ENABLE_FORMATTING=true
```

## Workspace Configuration

### Base Structure
```json
{
  "workspace": {
    "name": "${CURSOR_WORKSPACE_NAME}",
    "type": "${CURSOR_WORKSPACE_TYPE}",
    "settings": {
      "editor": {
        "theme": "${CURSOR_THEME}",
        "font": {
          "family": "${CURSOR_FONT_FAMILY}",
          "size": "${CURSOR_FONT_SIZE}"
        }
      },
      "project": {
        "root": "${CURSOR_PROJECT_ROOT}",
        "type": "${CURSOR_PROJECT_TYPE}"
      }
    }
  }
}
```

## Implementation Guide

### 1. Environment Setup
1. Create `.env` file in project root
2. Copy base configuration from above
3. Customize values for your project

### 2. Workspace Integration
```typescript
// config/workspace.ts
import { loadEnv } from './utils';

export const initWorkspace = async () => {
  const env = await loadEnv();
  return {
    name: env.CURSOR_WORKSPACE_NAME,
    type: env.CURSOR_WORKSPACE_TYPE,
    // ... additional configuration
  };
};
```

## Supported Themes

You can use any installed VSCode theme. Popular options include:

- "Default Dark+"
- "GitHub Dark"
- "One Dark Pro"
- "Dracula"
- "Night Owl"
- "Material Theme"

## Tips

1. Keep `.env` in your `.gitignore` to allow team members to use their preferred themes
2. Create an `.env.example` with default theme settings
3. Use the task runner for easy theme switching
4. Combine with other workspace settings for a complete development environment

## Contributing

Feel free to contribute improvements or report issues on GitHub!