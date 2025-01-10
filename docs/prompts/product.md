# Product Prompts

A collection of prompts designed to assist with product development and management tasks.

## User Story Generator

### Context
Use this prompt to create well-structured user stories for product features.

### Variables
- {user_type}: Type of user (e.g., "admin", "customer", "content creator")
- {feature}: The feature or functionality being described
- {benefit}: The value or benefit to the user

### Prompt Template
```
Create detailed user stories for a {user_type} who needs to {feature}.

Include:
1. User story in standard format (As a..., I want..., So that...)
2. Acceptance criteria
3. Technical considerations
4. Edge cases
5. Dependencies
6. Estimated complexity (T-shirt size)

Consider both happy path and error scenarios.
```

### Example Usage
```
Create detailed user stories for a "content creator" who needs to "schedule social media posts across multiple platforms".

Include:
1. User story in standard format (As a..., I want..., So that...)
2. Acceptance criteria
3. Technical considerations
4. Edge cases
5. Dependencies
6. Estimated complexity (T-shirt size)

Consider both happy path and error scenarios.
```

### Best Practices
- Be specific about user type
- Focus on user value
- Include clear acceptance criteria
- Consider edge cases

## Feature Prioritization

### Context
Use this prompt to help prioritize features and create product roadmaps.

### Variables
- {features_list}: List of features to prioritize
- {business_goals}: Key business objectives
- {constraints}: Resource or time constraints
- {metrics}: Success metrics

### Prompt Template
```
Help prioritize the following features considering our business goals and constraints:

Features:
{features_list}

Business Goals:
{business_goals}

Constraints:
{constraints}

Success Metrics:
{metrics}

Please provide:
1. Prioritized feature list with reasoning
2. Impact vs effort analysis
3. Suggested timeline
4. Risk assessment
5. Dependencies between features
```

### Best Practices
- List all features clearly
- Define business goals
- Specify constraints
- Include success metrics

## Product Requirements Document

### Context
Use this prompt to generate comprehensive PRDs for new features.

### Variables
- {feature_name}: Name of the feature
- {target_users}: Primary user segments
- {problem_statement}: Problem being solved
- {success_criteria}: Definition of success

### Prompt Template
```
Create a detailed PRD for {feature_name} targeting {target_users}.

Include:
1. Problem Statement
   - Current situation
   - User pain points
   - Market opportunity

2. Proposed Solution
   - Feature overview
   - User flows
   - Technical requirements
   - UI/UX considerations

3. Success Metrics
   - KPIs
   - Success criteria
   - Measurement approach

4. Implementation Details
   - Dependencies
   - Timeline
   - Resource requirements
   - Risks and mitigation

5. Future Considerations
   - Scalability
   - Maintenance
   - Potential improvements
```

### Best Practices
- Be specific about the problem
- Include clear success metrics
- Consider implementation details
- Think about future scalability

## More Prompts

Check out our [Contributing Guide](../contributing.md) to add more product prompts to this collection. 