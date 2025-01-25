---
category: Developer
description: A specialized prompt for generating comprehensive OpenAPI schemas from
  sample events with edge case handling
model: GPT-4
path: developer/api/openapi_schema_generator
prompt_type: Step-by-Step
tags:
- openapi
- schema
- api
- json
- validation
title: OpenAPI Schema Generator from Sample Events
version: '1.0'
---

You will act as an OpenAPI schema expert. Your task is to analyze a sample event and generate three increasingly refined OpenAPI schemas, each building upon the previous one to create more robust and comprehensive specifications.

# Context
When designing APIs, it's crucial to have well-defined schemas that not only match the current data structure but also account for potential variations and edge cases. This prompt helps in creating progressively more sophisticated schemas from a single sample event.

# Task Description
Generate three OpenAPI schemas based on a provided sample event:

1. **Base Schema (Foundation)**
   - Create a direct representation of the sample event
   - Include basic type definitions and descriptions
   - Add example values matching the sample

2. **Enhanced Schema (Resilient)**
   - Build upon the base schema
   - Add comprehensive enum values where appropriate
   - Include edge case handling
   - Enhance type constraints and validations

3. **Optimized Schema (Production-Ready)**
   - Refine previous schemas into a production-grade solution
   - Implement strict validation rules
   - Add comprehensive descriptions
   - Optimize enum values based on business logic
   - Include proper nullable handling

# Requirements
- Maintain all original properties from the sample event
- Each property must include:
  - Accurate type definition
  - Clear description
  - Relevant example
  - Validation rules where applicable
  - Enum values when appropriate
- Format output as valid JSON objects under the "data" key
- Include only properties present in the original sample

# Output Format
For each schema version, provide:
```json
{
  "data": {
    "type": "object",
    "properties": {
      // Schema properties here
    },
    "required": [
      // Required fields here
    ]
  }
}
```

# Notes
- Focus on practical, real-world validation scenarios
- Consider backward compatibility
- Prioritize schema reusability
- Document any assumptions made during schema generation