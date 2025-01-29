---
title: "Project Component Decomposition Guide"
path: "developer/architecture/component-decomposition"
tags: ["architecture", "project-planning", "system-design", "modularity"]
description: "A systematic approach to breaking down projects into manageable components while considering dependencies and implementation order"
prompt_type: "Design Framework"
---

<purpose>
To provide a structured methodology for decomposing complex projects into well-defined, manageable components while maintaining clear boundaries and interfaces.
</purpose>

<context>
Use this guide when starting a new project or restructuring an existing one to identify and organize its core components and their interactions.
</context>

<instructions>
Provide the project overview and requirements, then follow these steps:

1. Component Identification
   - Core Functionality
     * Primary features
     * Business requirements
     * Technical requirements
     * System boundaries

   - Component Categories
     * Frontend modules
     * Backend services
     * Data storage
     * External integrations

2. Component Analysis
   - For Each Component:
     * Component name
     * Primary responsibility
     * Key features
     * Technical scope
     * Dependencies

   - Implementation Considerations
     * Technical challenges
     * Resource requirements
     * Security concerns
     * Performance needs

3. Component Relationships
   - Interface Definitions
     * API contracts
     * Data flow
     * Event handling
     * State management

   - Integration Points
     * Service boundaries
     * Communication patterns
     * Shared resources
     * Cross-cutting concerns

4. Development Planning
   - Implementation Order
     * Critical path components
     * Dependency order
     * Risk mitigation
     * Quick wins

   - Development Strategy
     * Team allocation
     * Technical stack
     * Development phases
     * Milestone planning
</instructions>

<variables>
- project_overview: High-level project description
- requirements: Functional and non-functional requirements
- constraints: Technical and business constraints
- timeline: Project timeline and milestones
</variables>

<examples>
Example 1:
Input: E-commerce platform decomposition
Output:
```yaml
Components:
1. User Management:
   - Name: UserService
   - Functionality: Authentication, profiles, permissions
   - Challenges: Security, session management
   - Dependencies: None (core service)
   
2. Product Catalog:
   - Name: ProductService
   - Functionality: Product CRUD, search, categories
   - Challenges: Search performance, image handling
   - Dependencies: UserService (for seller info)

3. Order Processing:
   - Name: OrderService
   - Functionality: Cart, checkout, order management
   - Challenges: Transaction consistency
   - Dependencies: UserService, ProductService

Development Order:
1. UserService (foundation)
2. ProductService (core functionality)
3. OrderService (business operations)
```

Example 2:
Input: Content management system
Output:
```yaml
Components:
1. Content Engine:
   - Name: ContentCore
   - Functionality: Content CRUD, versioning
   - Challenges: Version control, content relationships
   - Dependencies: None

2. Media Manager:
   - Name: MediaService
   - Functionality: File upload, processing, delivery
   - Challenges: Large file handling, formats
   - Dependencies: ContentCore

3. Publishing System:
   - Name: PublishEngine
   - Functionality: Scheduling, distribution
   - Challenges: Consistency, caching
   - Dependencies: ContentCore, MediaService

Development Order:
1. ContentCore (foundation)
2. MediaService (asset handling)
3. PublishEngine (delivery system)
```
</examples>

<notes>
- Focus on clear boundaries
- Consider scalability
- Plan for maintainability
- Document dependencies
- Consider testing strategy
- Plan for monitoring
- Allow for future changes
</notes>