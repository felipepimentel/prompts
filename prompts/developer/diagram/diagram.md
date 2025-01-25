---
category: Developer
description: A comprehensive guide for creating clear and effective technical diagrams,
  covering various types of diagrams, tools, and best practices for technical documentation.
model: GPT-4
path: developer/guidelines/technical-diagram-guide
prompt_type: Instruction-based prompting
tags:
- documentation
- diagrams
- architecture
- visualization
- communication
title: Technical Diagram Creation Guide
version: '1.0'
---

# Technical Diagram Creation Guide

## Core Principles
1. Clarity - Ensure diagrams are easy to understand
2. Consistency - Maintain uniform style and notation
3. Purpose - Focus on conveying specific information
4. Accessibility - Make diagrams readable for all audiences

## Diagram Types

### 1. Architecture Diagrams
```mermaid
graph TD
    A[Frontend] --> B[API Gateway]
    B --> C[Auth Service]
    B --> D[User Service]
    B --> E[Data Service]
    C --> F[(Auth DB)]
    D --> G[(User DB)]
    E --> H[(Data DB)]
```

### 2. Sequence Diagrams
```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant A as API
    participant D as Database

    U->>F: Submit Form
    F->>A: POST /api/data
    A->>D: Insert Data
    D-->>A: Success
    A-->>F: 201 Created
    F-->>U: Show Success
```

### 3. Class Diagrams
```mermaid
classDiagram
    class User {
        +String id
        +String name
        +String email
        +validate()
        +save()
    }
    class Order {
        +String id
        +User user
        +Array items
        +Date createdAt
        +calculateTotal()
    }
    User "1" --> "*" Order
```

### 4. Entity Relationship Diagrams
```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER {
        string id
        string name
        string email
    }
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER {
        string id
        string user_id
        date created_at
    }
    ORDER_ITEM {
        string id
        string order_id
        string product_id
        int quantity
    }
```

## Tools and Setup

### 1. Mermaid.js Configuration
```javascript
// mermaid.config.js
export default {
  theme: 'default',
  themeVariables: {
    primaryColor: '#326CE5',
    primaryTextColor: '#fff',
    primaryBorderColor: '#285AB4',
    lineColor: '#666',
    secondaryColor: '#7F7F7F',
    tertiaryColor: '#fff',
  },
  flowchart: {
    curve: 'basis',
    padding: 15,
  },
  sequence: {
    mirrorActors: false,
    bottomMarginAdj: 10,
    messageAlign: 'center',
  },
}
```

### 2. PlantUML Setup
```plantuml
@startuml
!theme plain
skinparam backgroundColor transparent
skinparam useBetaStyle true
skinparam handwritten false
skinparam defaultFontName "Arial"
skinparam defaultFontSize 12
skinparam roundCorner 8
skinparam dpi 300
skinparam arrowColor #666666
skinparam arrowThickness 1.5
@enduml
```

## Diagram Patterns

### 1. System Architecture
```mermaid
graph TB
    subgraph Client
        A[Web App]
        B[Mobile App]
    end
    
    subgraph Gateway
        C[API Gateway]
        D[Load Balancer]
    end
    
    subgraph Services
        E[Auth]
        F[Users]
        G[Products]
    end
    
    subgraph Data
        H[(Main DB)]
        I[(Cache)]
        J[(Search)]
    end
    
    A --> C
    B --> C
    C --> D
    D --> E
    D --> F
    D --> G
    E --> H
    F --> H
    G --> H
    E --> I
    F --> I
    G --> J
```

### 2. Component Interaction
```mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant Q as Queue
    participant W as Worker
    participant D as Database

    C->>A: Request
    A->>Q: Enqueue Job
    A-->>C: Accepted
    Q->>W: Process Job
    W->>D: Update Data
    W-->>Q: Complete
    Q-->>A: Notify
    A-->>C: Complete
```

## Documentation Integration

### 1. Markdown Integration
```markdown
# System Overview

## Architecture
![System Architecture](./diagrams/architecture.svg)

The system consists of the following components:

1. Frontend Applications
   - Web Application
   - Mobile Application

2. Backend Services
   - API Gateway
   - Authentication Service
   - User Service
   - Data Service

## Sequence Flow
```mermaid
sequenceDiagram
    User->>Frontend: Action
    Frontend->>Backend: Request
    Backend->>Database: Query
    Database-->>Backend: Result
    Backend-->>Frontend: Response
    Frontend-->>User: Update
```
```

### 2. API Documentation
```yaml
openapi: 3.0.0
info:
  title: API Documentation
  version: 1.0.0
paths:
  /users:
    get:
      summary: Get users
      description: |
        ```mermaid
        sequenceDiagram
            Client->>API: GET /users
            API->>DB: Query users
            DB-->>API: User data
            API-->>Client: User list
        ```
      responses:
        '200':
          description: Success
```

## Best Practices

### 1. Design
- Use consistent shapes and colors
- Maintain clear hierarchy
- Include legend when necessary
- Keep diagrams focused and simple
- Use appropriate level of detail

### 2. Layout
- Organize elements logically
- Use whitespace effectively
- Align elements properly
- Follow left-to-right/top-to-bottom flow
- Group related elements

### 3. Content
- Use clear labels
- Include necessary context
- Avoid technical jargon
- Provide descriptions
- Version control diagrams

### 4. Maintenance
- Keep diagrams up to date
- Document diagram sources
- Use automated generation
- Review periodically
- Track changes

## Tools and Resources

### 1. Recommended Tools
- Mermaid.js for code-based diagrams
- PlantUML for UML diagrams
- Draw.io for complex diagrams
- Lucidchart for team collaboration
- Figma for design-focused diagrams

### 2. Integration Tools
- VS Code extensions
- Documentation generators
- CI/CD pipeline tools
- Version control systems
- Collaboration platforms

## Resources
1. [Mermaid.js Documentation](https://mermaid-js.github.io/mermaid/)
2. [PlantUML Guide](https://plantuml.com/guide)
3. [C4 Model](https://c4model.com/)
4. [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/)
5. [Google Cloud Icons](https://cloud.google.com/icons)