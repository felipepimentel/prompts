---
title: "Code Review Expert Guide"
path: "developer/guidelines/code-review"
tags: ["code-review", "best-practices", "quality-assurance"]
description: "A comprehensive guide for conducting thorough code reviews, focusing on code quality, standards, and best practices"
prompt_type: "Expert Role-Playing"
---

<purpose>
To provide a structured approach for conducting thorough and effective code reviews, ensuring code quality and maintainability.
</purpose>

<context>
Use this prompt when reviewing pull requests or code changes to ensure comprehensive analysis and constructive feedback.
</context>

<instructions>
Please review the following pull request or code changes:
[Paste the PR diff or provide a summary of changes]

Analyze the code for:
1. Potential issues or improvements in the code implementation
2. Adherence to project's coding standards and best practices
3. Test coverage and additional testing needs
4. Documentation completeness and clarity
5. Security vulnerabilities and performance concerns

For each identified point:
- Provide a clear explanation of the issue or observation
- Suggest specific improvements or solutions
- Reference relevant best practices or standards when applicable
</instructions>

<variables>
- code_changes: The pull request diff or summary of changes to review
- project_standards: Specific coding standards or guidelines for the project
- context_info: Additional context about the changes (optional)
</variables>

<examples>
Example 1:
Input: PR implementing a new authentication system
Output: Review focusing on security best practices, error handling, and authentication flow

Example 2:
Input: PR refactoring database queries
Output: Review emphasizing query optimization, connection handling, and transaction management
</examples>

<notes>
- Focus on constructive feedback that helps improve code quality
- Consider both technical correctness and maintainability
- Balance between detailed analysis and timely review
- Maintain a professional and collaborative tone
</notes>