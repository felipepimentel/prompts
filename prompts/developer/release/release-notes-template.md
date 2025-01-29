---
title: "Release Notes Template"
path: "developer/release/release-notes-template"
tags: ["release-management", "documentation", "changelog", "version-control"]
description: "A structured template for creating clear and comprehensive release notes that effectively communicate changes to users"
prompt_type: "Documentation Framework"
---

<purpose>
To provide a framework for creating professional release notes that effectively communicate changes, improvements, and migration steps to users.
</purpose>

<context>
Use this template when preparing release notes for a new version of your software to ensure all important changes are properly documented.
</context>

<instructions>
Provide the following release information:

1. Release Overview
   - Version Details
     * Version number
     * Release date
     * Release type
     * Compatibility info

   - Release Summary
     * Major highlights
     * Target audience
     * Release scope
     * Overall impact

2. Feature Changes
   - New Features
     * Feature descriptions
     * Use cases
     * Configuration
     * Examples

   - Improvements
     * Enhanced features
     * Performance gains
     * User experience
     * Documentation

3. Technical Changes
   - Breaking Changes
     * Incompatibilities
     * Migration steps
     * Required updates
     * Configuration changes

   - Bug Fixes
     * Fixed issues
     * Security patches
     * Known issues
     * Workarounds

4. Additional Information
   - Installation
     * Requirements
     * Update steps
     * Verification
     * Rollback process

   - Support Details
     * Documentation
     * Support channels
     * Contributors
     * Future plans

</instructions>

<variables>
- version_number: Release version
- release_type: Major/minor/patch
- release_date: Release date
- target_platforms: Supported platforms
</variables>

<examples>
Example 1:
Input: Web application framework release
Output:
```markdown
# Release Notes - v2.1.0

## Overview
We're excited to announce the release of version 2.1.0 of our web framework! This release focuses on performance improvements and developer experience enhancements.

### Release Information
- **Version:** 2.1.0
- **Release Date:** March 15, 2024
- **Type:** Minor Release
- **Compatibility:** Requires Node.js 16.x or higher

## What's New

### 🚀 New Features
- **Hot Module Reloading**
  - Added support for instant component updates during development
  - No browser refresh needed for most changes
  - Preserves component state during updates

- **Build Optimization**
  - Introduced tree-shaking for smaller bundle sizes
  - Improved code splitting algorithm
  - Added support for module federation

### 🔧 Improvements
- **Performance**
  - 30% faster build times
  - Reduced memory usage during development
  - Optimized chunk generation

- **Developer Experience**
  - Enhanced error messages with helpful suggestions
  - Added TypeScript 5.0 support
  - Improved debugging tools integration

## Technical Details

### Breaking Changes
1. **Configuration Updates**
   ```javascript
   // Old configuration
   module.exports = {
     optimize: true
   };
   
   // New configuration
   module.exports = {
     optimization: {
       level: 'advanced'
     }
   };
   ```

2. **API Changes**
   - Deprecated: `app.legacy()` method
   - New: Use `app.compatibility()` instead

### Migration Steps
1. Update your configuration file
2. Replace deprecated API calls
3. Update minimum Node.js version if needed

### Bug Fixes
- Fixed memory leak in development server
- Resolved CORS issues with WebSocket connections
- Fixed TypeScript definition conflicts

## Additional Information

### Installation
```bash
npm install framework@2.1.0
```

### Documentation
- Full documentation: [docs.framework.dev](https://docs.framework.dev)
- Migration guide: [docs.framework.dev/migrate](https://docs.framework.dev/migrate)

### Contributors
A huge thank you to our contributors:
- @developer1 - Hot Module Reloading
- @developer2 - Build optimizations
- @developer3 - Bug fixes

## What's Next
Stay tuned for v2.2.0, which will focus on:
- Enhanced SSR capabilities
- Built-in image optimization
- New routing features
```

Example 2:
Input: Mobile app release
Output:
```markdown
# MyApp v3.0.0 Release Notes

## 🎉 Major Release Highlights
We're thrilled to present version 3.0.0 of MyApp, featuring a complete UI redesign and powerful new features!

### Release Details
- **Version:** 3.0.0
- **Release Date:** April 1, 2024
- **Platforms:** iOS 15+ / Android 11+
- **App Size:** 45MB (iOS) / 40MB (Android)

## ✨ New Features

### Modern UI Redesign
- Fresh, modern interface with improved accessibility
- Dark mode support
- Customizable themes
- Responsive layouts for all device sizes

### Enhanced Performance
- 50% faster app startup
- Reduced battery usage
- Optimized image loading
- Smoother animations

### New Capabilities
- Offline mode support
- Cross-device sync
- Biometric authentication
- Widget support

## 🔨 Technical Updates

### Breaking Changes
1. **Minimum OS Requirements**
   - iOS: Now requires iOS 15 or later
   - Android: Now requires Android 11 or later

2. **Data Storage**
   - New data format for better performance
   - Automatic migration of existing data

### Migration Notes
- App will automatically migrate user data
- Backup recommended before updating
- Cannot downgrade after update

### Fixed Issues
- Resolved crash on large file uploads
- Fixed notification delays
- Corrected timezone handling
- Improved error reporting

## 📱 Installation

### iOS Users
Update through the App Store

### Android Users
Update through the Google Play Store

## 📖 Additional Information

### Documentation
- User Guide: [myapp.com/guide](https://myapp.com/guide)
- FAQ: [myapp.com/faq](https://myapp.com/faq)

### Support
- Email: support@myapp.com
- Twitter: @MyAppSupport

### Acknowledgments
Special thanks to our beta testers and the following contributors:
- Design Team: @designer1, @designer2
- Development Team: @dev1, @dev2
- QA Team: @qa1, @qa2

## 🔮 Coming Soon
- Cloud backup feature
- Advanced search capabilities
- Integration with more services
```
</examples>

<notes>
- Be clear and concise
- Highlight important changes
- Include all breaking changes
- Provide migration steps
- Thank contributors
- Link to documentation
- Use consistent formatting
- Include version numbers
</notes> 