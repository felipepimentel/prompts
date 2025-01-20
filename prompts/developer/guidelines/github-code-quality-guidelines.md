---
title: "GitHub Code Quality Guidelines"
path: "developer/guidelines/github-code-quality-guidelines"
tags: ["github", "code-quality", "best-practices", "development", "guidelines"]
description: "A comprehensive set of guidelines for maintaining high code quality in GitHub repositories, focusing on verification, clarity, and preservation of existing functionality."
---

# GitHub Code Quality Guidelines

## Overview
This document outlines essential guidelines for maintaining high code quality in GitHub repositories. These guidelines focus on verification, clarity, and preservation of existing functionality while making changes.

## Core Guidelines

### 1. Information Verification
- Always verify information before presenting it
- Avoid making assumptions or speculations without clear evidence
- Base decisions on concrete data and documentation

### 2. Change Management
- Make changes file by file to ensure proper review
- Provide all edits in a single, coherent chunk per file
- Avoid suggesting changes to files when no modifications are needed

### 3. Code Preservation
- Preserve existing code structures and functionalities
- Don't remove unrelated code or features
- Maintain the integrity of the codebase

### 4. Documentation Practices
- Provide links to real files, not placeholders
- Focus on current implementation details when relevant
- Maintain clear and concise documentation

### 5. Review Process
- Review changes systematically
- Verify implementations within the provided context
- Focus on substantive changes rather than formatting

## Best Practices

### Code Changes
```yaml
do:
  - Make changes file by file
  - Provide complete edits in single chunks
  - Preserve existing functionality
  - Verify information before changes
  - Focus on requested changes only

avoid:
  - Multiple-step instructions for same file
  - Whitespace-only changes
  - Unnecessary updates
  - Speculative changes
  - Removing unrelated code
```

### Documentation
```yaml
do:
  - Link to real files
  - Provide clear implementation details
  - Focus on current context
  - Document substantive changes
  - Maintain clear references

avoid:
  - Using placeholder file names
  - Unnecessary summaries
  - Redundant confirmations
  - Implementation checks for visible context
  - Discussion of unrelated changes
```

## Implementation Guidelines

### 1. Change Verification
- Verify all information before implementation
- Check current file contents and implementations
- Ensure changes align with requirements

### 2. Code Modification
- Make targeted, specific changes
- Preserve existing code structure
- Avoid unnecessary modifications

### 3. Documentation Standards
- Provide clear, accurate file references
- Document only necessary changes
- Maintain focus on current implementation

## Quality Checklist

1. Information Verification
   - [ ] All information is verified
   - [ ] No assumptions made
   - [ ] Clear evidence supports changes

2. Change Management
   - [ ] Changes are file-specific
   - [ ] Edits are consolidated
   - [ ] No unnecessary modifications

3. Code Preservation
   - [ ] Existing functionality preserved
   - [ ] No unrelated code removed
   - [ ] Code structure maintained

4. Documentation
   - [ ] Real file references used
   - [ ] Clear implementation details
   - [ ] Focused on current context

## Resources
- [GitHub Documentation](https://docs.github.com)
- [Code Review Guidelines](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)
- [Best Practices for Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/best-practices-for-pull-requests) 