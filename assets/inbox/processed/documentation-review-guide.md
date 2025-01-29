---
title: "Documentation Review Guide"
path: "content-creation/writing/documentation-review"
tags: ["documentation", "technical-writing", "content-review", "best-practices"]
description: "A comprehensive guide for reviewing and improving technical documentation with focus on clarity, completeness, and user experience"
prompt_type: "Analysis Framework"
---

<purpose>
To provide a structured approach for reviewing technical documentation and suggesting improvements that enhance user understanding and satisfaction.
</purpose>

<context>
Use this guide when reviewing technical documentation, API references, user guides, or any other technical content that needs evaluation and improvement.
</context>

<instructions>
Review the provided documentation:
[Paste current documentation]

Analyze the following aspects:

1. Content Completeness
   - Missing sections or topics
   - Depth of coverage
   - Prerequisites and dependencies
   - Setup instructions
   - Troubleshooting guides
   - API references
   - Code examples

2. Technical Accuracy
   - Current best practices
   - Deprecated features or methods
   - Version compatibility
   - Platform-specific information
   - Security considerations
   - Performance implications

3. Structure and Organization
   - Logical flow
   - Information hierarchy
   - Navigation and cross-references
   - Search-friendliness
   - Progressive disclosure
   - Quick start guides

4. User Experience
   - Readability
   - Code sample quality
   - Visual aids and diagrams
   - Interactive examples
   - Mobile responsiveness
   - Accessibility

5. Maintenance Considerations
   - Version control
   - Update frequency
   - Contribution guidelines
   - Style guide compliance
   - Link validity
   - Asset management

Provide recommendations for:
- Content additions or expansions
- Outdated content removal
- Clarity improvements
- User experience enhancements
- Technical accuracy updates
</instructions>

<variables>
- current_docs: Documentation to review
- target_audience: Primary audience type
- doc_type: Type of documentation
- tech_stack: Related technologies
</variables>

<examples>
Example 1:
Input: API documentation review
Output:
```markdown
Recommendations:
1. Add authentication examples for all supported methods
2. Update deprecated endpoint references
3. Include rate limiting information
4. Add interactive API explorer
5. Expand error handling documentation
```

Example 2:
Input: Installation guide review
Output:
```markdown
Improvements needed:
1. Add system requirements section
2. Update package versions
3. Include troubleshooting guide
4. Add container deployment instructions
5. Improve security best practices
```
</examples>

<notes>
- Consider different user skill levels
- Focus on actionable improvements
- Maintain consistent terminology
- Verify technical accuracy
- Consider internationalization
- Check for broken links
- Ensure code samples are tested
</notes>