# Prompt Classification System

## Overview
Each prompt in this catalog is classified according to its primary technique type. This classification helps users quickly identify and select the most appropriate prompt for their needs.

## Classification in Frontmatter
Prompts include a `prompt_type` field in their frontmatter:

```yaml
---
title: "Example Prompt"
prompt_type: "Chain-of-thought prompting"
---
```

## Available Classifications

| Type | Description | Best For |
|------|-------------|----------|
| Zero-shot prompting | Direct instructions without examples | Simple, straightforward tasks |
| Few-shot prompting | Instructions with examples | Tasks requiring pattern recognition |
| Chain-of-thought prompting | Step-by-step reasoning | Complex problem solving |
| Instruction-based prompting | Clear, direct commands | Specific task execution |
| Role-based prompting | Character/role assumption | Specialized perspective tasks |
| Contextual prompting | Progressive context building | Complex, nuanced responses |
| Meta prompting | Prompt creation guidance | Prompt engineering |
| Self-consistency prompting | Multiple path reasoning | Verification-heavy tasks |
| Generated knowledge prompting | Context generation | Research and analysis |
| Dynamic prompt optimization | Real-time adjustments | Interactive workflows |
| Automatic prompt engineering | Programmatic generation | Large-scale applications |
| Multi-prompt fusion | Combined techniques | Complex, multi-faceted tasks |
| Prompt chaining | Sequential prompting | Multi-step workflows |
| Directional stimulus prompting | Subtle guidance | Style-specific content |
| Graph prompting | Relationship mapping | Network/hierarchy analysis |
| Hybrid prompting | Multiple technique combination | Complex use cases |
| Constraint-based prompting | Limited parameter space | Specific output format |
| Scenario-based prompting | Situational context | Real-world applications |
| Template-based prompting | Structured formats | Standardized outputs |
| Iterative prompting | Progressive refinement | Quality-critical tasks |

## Usage Guidelines
1. Choose the most specific classification that applies
2. When multiple techniques are used, select the primary/dominant one
3. Consider the main purpose of the prompt when classifying
4. Update classification if the prompt's approach changes significantly 