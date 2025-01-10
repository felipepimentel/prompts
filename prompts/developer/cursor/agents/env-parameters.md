# Cursor Workspace .ENV Themes

A guide to managing Cursor/VSCode workspace themes and settings through environment variables.

## Overview

This guide shows how to configure your Cursor/VSCode workspace settings using `.env` files, allowing for:

- Dynamic theme management
- Project-specific configurations
- Shared workspace settings across team members

![Cursor Workspace Settings](https://i.imgur.com/vsB5ocq.png)

## Setup Instructions

### 1. Environment Configuration

Add these variables to your `.env` file:

```env
# Cursor Workspace Configuration
CURSOR_WORKSPACE="YourWorkspaceName"
CURSOR_PROJECT="Your Project Name"

# VSCode Theme Settings
VSCODE_COLOR_THEME="Default Dark+"
VSCODE_PREFERRED_DARK_THEME="Default Dark+"
```

### 2. Workspace Script

Create `scripts/update-vscode-theme.ps1`:

```powershell
# Load .env file
$envContent = Get-Content -Path ".env" -Raw
$envLines = $envContent -split "`n" | Where-Object { $_ -match '^\s*[^#]' }

# Parse settings
$settings = @{}
foreach ($line in $envLines) {
    if ($line -match 'VSCODE_COLOR_THEME=(.+)') {
        $settings['workbench.colorTheme'] = $matches[1].Trim('"')
    }
    if ($line -match 'VSCODE_PREFERRED_DARK_THEME=(.+)') {
        $settings['workbench.preferredDarkColorTheme'] = $matches[1].Trim('"')
    }
    if ($line -match 'CURSOR_WORKSPACE=(.+)') {
        $workspaceName = $matches[1].Trim('"')
    }
}

# Determine workspace file name
$workspaceFile = "$workspaceName.code-workspace"

# Create workspace if it doesn't exist
if (-not (Test-Path $workspaceFile)) {
    @{
        folders = @(@{ path = "." })
        settings = @{}
        extensions = @{
            recommendations = @()
        }
        tasks = @{}
    } | ConvertTo-Json -Depth 100 | Set-Content -Path $workspaceFile
}

# Read workspace file
$workspace = Get-Content -Path $workspaceFile -Raw | ConvertFrom-Json

# Update theme settings
$workspace.settings.'workbench.colorTheme' = $settings['workbench.colorTheme']
$workspace.settings.'workbench.preferredDarkColorTheme' = $settings['workbench.preferredDarkColorTheme']

# Save workspace file
$workspace | ConvertTo-Json -Depth 100 | Set-Content -Path $workspaceFile

Write-Host "VSCode theme settings updated from .env file for workspace: $workspaceFile"
```

### 3. Workspace Configuration

Your workspace file (e.g., `YourWorkspace.code-workspace`) will be automatically created/updated with:

```json
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "workbench.colorTheme": "Default Dark+",
    "workbench.preferredDarkColorTheme": "Default Dark+",
    "workbench.colorCustomizations": {
      "statusBar.background": "#1a1a1a",
      "statusBar.foreground": "#00ff00",
      "activityBar.background": "#1a1a1a",
      "activityBar.foreground": "#33FF66",
      "titleBar.activeBackground": "#1a1a1a",
      "titleBar.activeForeground": "#33FF66",
      "editorCursor.foreground": "#33FF66",
      "editorCursor.background": "#1a1a1a",
      "terminalCursor.foreground": "#33FF66",
      "terminalCursor.background": "#1a1a1a"
    }
  },
  "tasks": {
    "update-theme": {
      "label": "Update Theme from ENV",
      "type": "shell",
      "command": "${workspaceFolder}/scripts/update-vscode-theme.ps1",
      "problemMatcher": []
    }
  }
}
```

### 4. Usage

1. Update theme settings in `.env`
2. Run the update task:
   - From Command Palette: `Tasks: Run Task` > `Update Theme from ENV`
   - Or run `./scripts/update-vscode-theme.ps1` directly

![Theme Settings](https://i.imgur.com/bwOVM04.png)
![Task Runner](https://i.imgur.com/198ACe4.png)

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