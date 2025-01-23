---
description: Comprehensive guide for creating clear and effective technical diagrams,
  focusing on best practices, tools, and common patterns
path: developer/guidelines/technical-diagram-guide.md
prompt_type: Instruction-based prompting
tags:
- diagrams
- documentation
- architecture
- visualization
- planning
title: Technical Diagram Guide
---

# Technical Diagram Guide

## Overview
This guide provides a structured approach to creating technical diagrams that effectively communicate system architecture, workflows, and technical concepts.

## Diagram Types

### 1. Architecture Diagrams
```mermaid
graph TD
    A[Client] -->|HTTP| B[Load Balancer]
    B -->|Route| C[Web Server 1]
    B -->|Route| D[Web Server 2]
    C -->|Query| E[Database]
    D -->|Query| E
    C -->|Cache| F[Redis]
    D -->|Cache| F
```

### 2. Sequence Diagrams
```mermaid
sequenceDiagram
    participant U as User
    participant C as Client
    participant S as Server
    participant D as Database

    U->>C: Submit Form
    C->>S: POST /api/data
    S->>D: Insert Record
    D-->>S: Success
    S-->>C: 201 Created
    C-->>U: Show Success
```

### 3. Class Diagrams
```mermaid
classDiagram
    class User {
        +String id
        +String email
        +String password
        +validate()
        +authenticate()
    }
    class Profile {
        +String userId
        +String name
        +String avatar
        +update()
    }
    User "1" --> "1" Profile
```

### 4. Entity Relationship Diagrams
```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER {
        string id
        string email
        string name
    }
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER {
        string id
        string userId
        date created_at
    }
    ORDER_ITEM {
        string id
        string orderId
        string productId
        int quantity
    }
```

## Tools and Formats

### 1. Mermaid.js
```javascript
// Example configuration
const config = {
  theme: 'default',
  themeVariables: {
    primaryColor: '#ff0000',
    primaryTextColor: '#fff',
    primaryBorderColor: '#ff0000',
    lineColor: '#f00',
    secondaryColor: '#006100',
    tertiaryColor: '#fff'
  }
}
```

### 2. PlantUML
```plantuml
@startuml
package "Frontend" {
  [Web App]
  [Mobile App]
}

package "Backend" {
  [API Gateway]
  [Auth Service]
  [User Service]
  [Data Service]
}

database "Database" {
  [PostgreSQL]
  [Redis]
}

[Web App] --> [API Gateway]
[Mobile App] --> [API Gateway]
[API Gateway] --> [Auth Service]
[API Gateway] --> [User Service]
[API Gateway] --> [Data Service]
[Auth Service] --> [PostgreSQL]
[User Service] --> [PostgreSQL]
[Data Service] --> [PostgreSQL]
[Data Service] --> [Redis]
@enduml
```

### 3. Draw.io
```xml
<mxfile>
  <diagram id="example" name="Example">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="2" value="Component" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="120" y="120" width="120" height="60" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Best Practices

### 1. Layout Guidelines
```mermaid
graph LR
    A[Start] --> B[Process 1]
    B --> C[Process 2]
    C --> D[End]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
```

### 2. Color Usage
```mermaid
graph TD
    A[Critical Path] -->|High Priority| B[Main Process]
    B -->|Medium Priority| C[Sub Process]
    B -->|Low Priority| D[Optional Process]

    style A fill:#ff6b6b,stroke:#333,stroke-width:2px
    style B fill:#4ecdc4,stroke:#333,stroke-width:2px
    style C fill:#45b7d1,stroke:#333,stroke-width:2px
    style D fill:#96ceb4,stroke:#333,stroke-width:2px
```

## Common Patterns

### 1. Microservices Architecture
```mermaid
graph TD
    A[API Gateway] --> B[Auth Service]
    A --> C[User Service]
    A --> D[Product Service]
    A --> E[Order Service]
    
    B --> F[(Auth DB)]
    C --> G[(User DB)]
    D --> H[(Product DB)]
    E --> I[(Order DB)]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
```

### 2. Event-Driven Architecture
```mermaid
graph LR
    A[Producer] -->|Event| B[Event Bus]
    B -->|Subscribe| C[Consumer 1]
    B -->|Subscribe| D[Consumer 2]
    B -->|Subscribe| E[Consumer 3]
    
    style A fill:#f96,stroke:#333,stroke-width:2px
    style B fill:#69c,stroke:#333,stroke-width:2px
    style C fill:#9c6,stroke:#333,stroke-width:2px
    style D fill:#9c6,stroke:#333,stroke-width:2px
    style E fill:#9c6,stroke:#333,stroke-width:2px
```

## Documentation Integration

### 1. README Format
```markdown
# System Architecture

## Overview
[Brief description of the system]

## Components
[Component diagram showing main parts]

## Workflows
[Sequence diagrams for key processes]

## Data Model
[Entity relationship diagram]

## Deployment
[Deployment architecture diagram]
```

### 2. API Documentation
```mermaid
graph TD
    A[API Endpoint] --> B{Authentication}
    B -->|Valid| C[Process Request]
    B -->|Invalid| D[Return Error]
    C --> E[Database Operation]
    E -->|Success| F[Return Response]
    E -->|Error| G[Handle Error]
```

## Best Practices

1. Diagram Organization
   - Use clear hierarchy
   - Group related components
   - Show important relationships
   - Maintain consistent style

2. Visual Design
   - Use appropriate colors
   - Keep consistent spacing
   - Add clear labels
   - Include legend when needed

3. Documentation
   - Link to source code
   - Explain key decisions
   - Document changes
   - Version control diagrams

4. Maintenance
   - Update regularly
   - Review for accuracy
   - Archive old versions
   - Track changes

Remember to:
1. Keep diagrams simple
2. Focus on clarity
3. Use consistent notation
4. Include necessary context
5. Update documentation 