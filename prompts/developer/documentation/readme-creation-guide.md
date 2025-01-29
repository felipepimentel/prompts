---
title: "GitHub README Creation Guide"
path: "developer/documentation/readme-template"
tags: ["documentation", "github", "markdown", "project-setup"]
description: "A comprehensive guide for creating professional and informative README files for GitHub repositories"
prompt_type: "Documentation Framework"
---

<purpose>
To provide a structured approach for creating clear, comprehensive, and well-organized README files that effectively communicate project information.
</purpose>

<context>
Use this guide when creating or updating a README file for a GitHub repository to ensure all essential information is included and properly formatted.
</context>

<instructions>
Provide the following project information:

1. Project Overview
   - Basic Information
     * Project name
     * Brief description
     * Key features
     * Current status

   - Project Context
     * Purpose
     * Target audience
     * Use cases
     * Technologies used

2. Documentation Structure
   - Header Section
     * Project logo/banner
     * Project title
     * Short description
     * Status badges
     * Quick links

   - Installation Guide
     * Prerequisites
     * Dependencies
     * Step-by-step setup
     * Configuration

   - Usage Instructions
     * Basic usage
     * Examples
     * Configuration options
     * Common commands

3. Additional Information
   - Project Details
     * Features list
     * Architecture
     * API documentation
     * Screenshots/demos

   - Community Info
     * Contributing guide
     * Code of conduct
     * Issue templates
     * Pull request process

4. Maintenance Details
   - Project Status
     * Version information
     * Roadmap
     * Known issues
     * Future plans

   - Support Info
     * Documentation
     * Troubleshooting
     * Contact methods
     * Community links
</instructions>

<variables>
- project_name: Name of the project
- project_description: Brief project overview
- technologies: Technologies used
- license_type: Project license
</variables>

<examples>
Example 1:
Input: Node.js API project
Output:
```markdown
# Project Name

[![Build Status](https://travis-ci.org/username/project.svg?branch=master)](https://travis-ci.org/username/project)
[![npm version](https://badge.fury.io/js/project.svg)](https://badge.fury.io/js/project)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A fast and flexible API for processing data with Node.js.

## Features

- Fast data processing
- RESTful API endpoints
- Automatic documentation
- Extensive test coverage

## Installation

```bash
npm install project-name
```

## Quick Start

```javascript
const api = require('project-name');

api.process({
  data: 'example',
  options: { /* config */ }
});
```

## Documentation

For detailed documentation, visit [docs.project.com](https://docs.project.com)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Submit a pull request

## License

MIT © [Your Name]
```

Example 2:
Input: Python CLI tool
Output:
```markdown
# CLI Tool Name

![Python Version](https://img.shields.io/pypi/pyversions/tool-name.svg)
![PyPI version](https://badge.fury.io/py/tool-name.svg)

A command-line tool for automating common development tasks.

## Installation

```bash
pip install tool-name
```

## Usage

```bash
tool-name --action process --input file.txt
```

## Features

- File processing
- Batch operations
- Custom plugins
- Configuration profiles

## Configuration

Create a `config.yaml` file:

```yaml
settings:
  output_dir: ./output
  log_level: info
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

Apache 2.0 © [Your Name]
```
</examples>

<notes>
- Keep it concise but complete
- Use clear headings
- Include working examples
- Add relevant badges
- Keep documentation updated
- Use proper formatting
- Include contact information
</notes>