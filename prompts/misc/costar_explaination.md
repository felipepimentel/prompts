# CO-STAR Prompt Engineering Framework

## Context
You are a prompt engineering specialist explaining the CO-STAR framework. Your task is to provide a comprehensive understanding of this methodology, from basic concepts to advanced applications, using a structured and progressive approach.

## Framework Overview

### 1. Core Components
```yaml
costar_elements:
  context:
    definition: "Background information and scenario setting"
    purpose: "Enable accurate understanding and response"
    examples: [
      "You are a data scientist analyzing customer behavior",
      "You are reviewing code for security vulnerabilities"
    ]
    
  objective:
    definition: "Clear goal or desired outcome"
    purpose: "Direct focus and guide response"
    examples: [
      "Identify patterns in customer purchase history",
      "Find potential SQL injection vulnerabilities"
    ]
    
  style:
    definition: "Writing format and presentation method"
    purpose: "Ensure consistent communication"
    examples: [
      "Technical analysis with statistical metrics",
      "Security report with severity ratings"
    ]
    
  tone:
    definition: "Emotional resonance and attitude"
    purpose: "Maintain appropriate sentiment"
    examples: [
      "Professional and analytical",
      "Urgent and focused on risk mitigation"
    ]
    
  audience:
    definition: "Target recipients of the response"
    purpose: "Tailor content appropriately"
    examples: [
      "Marketing team with basic data literacy",
      "Senior security engineers"
    ]
    
  response:
    definition: "Output format and structure"
    purpose: "Ensure usable and consistent results"
    examples: [
      "Structured report with visualizations",
      "Prioritized list of vulnerabilities"
    ]
```

### 2. Implementation Levels
```yaml
complexity_stages:
  basic:
    concepts: [
      "Single-task prompts",
      "Direct question-answer format"
    ]
    applications: [
      "Simple data analysis requests",
      "Basic code review tasks"
    ]
    
  intermediate:
    techniques: [
      "Multi-step reasoning",
      "Context-aware responses"
    ]
    integrations: [
      "Chain-of-thought prompting",
      "Tool-augmented analysis"
    ]
    
  advanced:
    strategies: [
      "System-level prompt design",
      "Dynamic context adaptation"
    ]
    optimizations: [
      "Response calibration",
      "Error handling patterns"
    ]
```

### 3. Integration Patterns
```yaml
implementation_patterns:
  context_layers:
    primary: "Core task context"
    secondary: [
      "Domain-specific knowledge",
      "Technical constraints"
    ]
    tertiary: [
      "Edge cases",
      "Error scenarios"
    ]
    
  objective_hierarchy:
    main_goals: [
      "Primary task completion",
      "Quality assurance"
    ]
    sub_objectives: [
      "Intermediate validations",
      "Progress tracking"
    ]
    
  style_matrix:
    formats: [
      "Technical documentation",
      "Executive summary"
    ]
    techniques: [
      "Progressive disclosure",
      "Layered complexity"
    ]
```

## Application Methods

### 1. Basic Implementation
- Component understanding
  - Clear context definition
  - Simple objective statement
  - Consistent style choice
- Simple integration
  - Direct prompts
  - Single-step responses
- Direct application
  - Clear instructions
  - Explicit outputs
- Basic examples
  - Common use cases
  - Standard patterns
- Core principles
  - Clarity first
  - Consistency focus

### 2. Intermediate Usage
- Component interaction
  - Context-objective alignment
  - Style-audience matching
- Pattern recognition
  - Common scenarios
  - Reusable templates
- Customization
  - Domain adaptation
  - Format flexibility
- Complex scenarios
  - Multi-step tasks
  - Conditional flows
- Error handling
  - Input validation
  - Fallback options

### 3. Advanced Application
- System integration
  - Framework embedding
  - Tool orchestration
- Pipeline optimization
  - Response tuning
  - Performance enhancement
- Performance tuning
  - Context optimization
  - Response calibration
- Edge cases
  - Error recovery
  - Exception handling
- Advanced patterns
  - Dynamic adaptation
  - Context switching

## Output Formats

### 1. Simple Format
```yaml
basic_prompt:
  context: "Data analysis task for marketing team"
  objective: "Identify customer segments"
  style: "Clear and analytical"
  tone: "Professional and objective"
  audience: "Marketing strategists"
  response: "Segmentation report with visualizations"
```

### 2. Detailed Format
```yaml
detailed_prompt:
  context:
    background: "Quarterly customer analysis project"
    constraints: [
      "Focus on high-value customers",
      "Consider recent purchases only"
    ]
    requirements: [
      "Statistical significance",
      "Actionable insights"
    ]
    
  objective:
    primary_goal: "Identify customer segments"
    success_criteria: [
      "Clear segment definitions",
      "Measurable characteristics"
    ]
    
  style_and_tone:
    writing_style: "Technical with business context"
    emotional_tone: "Professional and objective"
    formatting: "Structured report with sections"
    
  audience:
    primary: "Marketing strategy team"
    characteristics: [
      "Basic data literacy",
      "Business focus"
    ]
    needs: [
      "Actionable insights",
      "Clear recommendations"
    ]
    
  response:
    format: "Detailed report"
    structure: "Executive summary with detailed sections"
    requirements: [
      "Visual representations",
      "Statistical validation"
    ]
```

## Framework Principles
1. Clarity: Clear and unambiguous communication
2. Consistency: Uniform approach across prompts
3. Completeness: All necessary components included
4. Coherence: Logical flow and connection
5. Context-Awareness: Situation-appropriate responses
6. Audience-Focus: Tailored to recipient needs
7. Goal-Orientation: Clear objective alignment
8. Format-Compliance: Structured output adherence
9. Scalability: Adaptable to complexity
10. Maintainability: Easy to update and modify

## Best Practices
1. Clear Context: Provide comprehensive background
2. Specific Objectives: Define measurable goals
3. Consistent Style: Maintain uniform approach
4. Appropriate Tone: Match audience expectations
5. Defined Audience: Understand recipient needs
6. Structured Response: Follow format guidelines
7. Regular Review: Assess and update prompts
8. Continuous Improvement: Refine based on feedback
9. Documentation: Maintain clear records
10. Version Control: Track prompt evolution

## Implementation Guide

### 1. Getting Started
1. Define your use case clearly
2. Identify core requirements
3. Select appropriate complexity level
4. Choose relevant patterns
5. Create initial templates

### 2. Development Process
1. Start with basic implementation
2. Test with simple scenarios
3. Gradually add complexity
4. Validate responses
5. Refine based on feedback

### 3. Advanced Integration
1. Implement system-level patterns
2. Develop error handling
3. Optimize performance
4. Document extensively
5. Maintain version control

## Practical Examples

### 1. Code Review Assistant
```yaml
basic_implementation:
  context: "You are a senior software engineer reviewing Python code"
  objective: "Identify potential performance issues and suggest improvements"
  style: "Technical and constructive"
  tone: "Professional and educational"
  audience: "Junior developers"
  response: "Structured code review with examples"

advanced_implementation:
  context:
    background: "Code review for high-traffic microservice"
    constraints: [
      "Must maintain backward compatibility",
      "Performance critical system"
    ]
    domain: "Python backend services"
    
  objective:
    primary: "Optimize code performance"
    secondary: [
      "Maintain code readability",
      "Ensure scalability"
    ]
    
  style_and_tone:
    format: "Detailed technical review"
    approach: "Educational and collaborative"
    examples: "Include before/after code snippets"
    
  response:
    structure: [
      "Performance analysis",
      "Optimization suggestions",
      "Implementation examples",
      "Risk assessment"
    ]
    priorities: [
      "Critical performance issues",
      "Scalability concerns",
      "Code maintainability"
    ]
```

### 2. Data Analysis Guide
```yaml
basic_implementation:
  context: "You are a data analyst explaining findings to stakeholders"
  objective: "Present key insights from customer behavior analysis"
  style: "Clear and business-focused"
  tone: "Professional and accessible"
  audience: "Marketing team"
  response: "Visual report with key findings"

advanced_implementation:
  context:
    background: "Quarterly customer retention analysis"
    scope: [
      "Past 12 months data",
      "Focus on high-value segments"
    ]
    stakeholders: [
      "Marketing team",
      "Product managers",
      "Executive leadership"
    ]
    
  objective:
    primary: "Identify churn risk factors"
    secondary: [
      "Segment customer behaviors",
      "Recommend retention strategies"
    ]
    
  style_and_tone:
    format: "Multi-level report"
    sections: [
      "Executive summary",
      "Detailed analysis",
      "Technical appendix"
    ]
    visualization: "Progressive complexity"
    
  response:
    deliverables: [
      "Dashboard overview",
      "Detailed findings report",
      "Action recommendations"
    ]
    metrics: [
      "Churn rate trends",
      "Segment performance",
      "Revenue impact"
    ]
```

### 3. API Documentation Generator
```yaml
basic_implementation:
  context: "You are a technical writer creating API documentation"
  objective: "Document REST API endpoints and usage"
  style: "Clear and technical"
  tone: "Precise and helpful"
  audience: "External developers"
  response: "Structured API documentation"

advanced_implementation:
  context:
    background: "Public REST API documentation"
    api_type: "RESTful microservices"
    security: "OAuth2 authentication"
    version: "v2.0"
    
  objective:
    primary: "Create comprehensive API documentation"
    requirements: [
      "Endpoint descriptions",
      "Authentication flows",
      "Request/response examples",
      "Error handling"
    ]
    
  style_and_tone:
    format: "OpenAPI specification"
    sections: [
      "Overview",
      "Authentication",
      "Endpoints",
      "Examples"
    ]
    code_samples: [
      "curl",
      "Python",
      "JavaScript"
    ]
    
  response:
    structure: [
      "API reference",
      "Integration guide",
      "Troubleshooting"
    ]
    examples: [
      "Basic usage",
      "Advanced scenarios",
      "Error handling"
    ]
```

## Common Patterns and Anti-patterns

### Effective Patterns
1. Progressive Disclosure
   - Start with basic concepts
   - Add complexity gradually
   - Provide detailed examples when needed

2. Context Layering
   - Core context first
   - Domain-specific details
   - Implementation constraints
   - Edge cases and exceptions

3. Response Structuring
   - Clear hierarchy
   - Consistent formatting
   - Progressive detail levels
   - Linked references

### Anti-patterns to Avoid
1. Context Overload
   - Too much background information
   - Irrelevant details
   - Conflicting constraints

2. Ambiguous Objectives
   - Unclear goals
   - Mixed priorities
   - Undefined success criteria

3. Mismatched Style
   - Technical jargon for non-technical audience
   - Oversimplified explanations for experts
   - Inconsistent terminology

## Framework Evolution

### 1. Continuous Improvement
- Regular effectiveness assessment
- User feedback integration
- Pattern refinement
- Template updates

### 2. Adaptation Strategies
- Domain-specific customization
- Tool integration
- Workflow optimization
- Performance tuning

### 3. Quality Assurance
- Response validation
- Consistency checking
- User acceptance testing
- Performance monitoring

## Advanced Integration Patterns

### 1. Chain-of-Thought Integration
```yaml
chain_pattern:
  structure:
    initial_prompt:
      context: "Complex problem decomposition"
      objective: "Break down problem into steps"
    
    intermediate_steps:
      - step: "Problem analysis"
        prompt_type: "Analytical"
        output: "Key components identified"
      
      - step: "Solution planning"
        prompt_type: "Strategic"
        output: "Action plan created"
      
      - step: "Implementation"
        prompt_type: "Technical"
        output: "Detailed solution"
    
    final_synthesis:
      prompt_type: "Integration"
      output: "Complete solution with rationale"
```

### 2. Multi-Modal Response Pattern
```yaml
multimodal_pattern:
  components:
    text_output:
      format: "Structured explanation"
      level: "Adaptive complexity"
      
    visual_elements:
      diagrams: "Process flows"
      charts: "Data visualization"
      code_blocks: "Implementation examples"
      
    interactive_components:
      checkpoints: "Understanding validation"
      exercises: "Practical application"
      feedback: "Response refinement"
```

### 3. Context Inheritance Pattern
```yaml
inheritance_pattern:
  base_context:
    domain: "Core technical knowledge"
    constraints: "Fundamental limitations"
    requirements: "Basic expectations"
    
  specialized_contexts:
    - type: "Security focus"
      inherits: "base_context"
      adds: ["Security requirements", "Threat models"]
      
    - type: "Performance focus"
      inherits: "base_context"
      adds: ["Performance metrics", "Optimization goals"]
      
    - type: "Maintenance focus"
      inherits: "base_context"
      adds: ["Maintainability criteria", "Documentation standards"]
```

## Troubleshooting Guide

### 1. Common Issues and Solutions
```yaml
troubleshooting_patterns:
  context_misalignment:
    symptoms: [
      "Inconsistent responses",
      "Missing key information",
      "Irrelevant details"
    ]
    solutions: [
      "Review context completeness",
      "Validate context relevance",
      "Add missing constraints"
    ]
    
  objective_drift:
    symptoms: [
      "Off-topic responses",
      "Incomplete solutions",
      "Scope creep"
    ]
    solutions: [
      "Refine objective clarity",
      "Add success criteria",
      "Implement checkpoints"
    ]
    
  style_inconsistency:
    symptoms: [
      "Varying tone",
      "Inconsistent formatting",
      "Mixed terminology"
    ]
    solutions: [
      "Create style guide",
      "Implement templates",
      "Add style validation"
    ]
```

### 2. Quality Assurance Checklist
1. Context Validation
   - [ ] All required background information included
   - [ ] Constraints clearly defined
   - [ ] Dependencies identified
   - [ ] Edge cases considered

2. Objective Clarity
   - [ ] Goals explicitly stated
   - [ ] Success criteria defined
   - [ ] Metrics identified
   - [ ] Priorities established

3. Style Consistency
   - [ ] Tone appropriate for audience
   - [ ] Formatting consistent
   - [ ] Terminology standardized
   - [ ] Examples relevant

4. Response Quality
   - [ ] Meets all requirements
   - [ ] Follows specified format
   - [ ] Includes necessary detail
   - [ ] Maintains clarity

### 3. Performance Optimization
```yaml
optimization_strategies:
  response_tuning:
    metrics: [
      "Accuracy",
      "Completeness",
      "Consistency",
      "Efficiency"
    ]
    methods: [
      "Template refinement",
      "Context optimization",
      "Pattern analysis"
    ]
    
  error_reduction:
    prevention: [
      "Input validation",
      "Context verification",
      "Format checking"
    ]
    handling: [
      "Graceful degradation",
      "Alternative paths",
      "Recovery procedures"
    ]
    
  efficiency_improvement:
    techniques: [
      "Context pruning",
      "Template optimization",
      "Response caching"
    ]
    monitoring: [
      "Performance metrics",
      "Quality indicators",
      "Usage patterns"
    ]
```

## Implementation Workflows

### 1. Development Lifecycle
```yaml
lifecycle_stages:
  planning:
    activities: [
      "Requirements gathering",
      "Use case analysis",
      "Pattern selection"
    ]
    outputs: [
      "Requirements document",
      "Implementation plan",
      "Success criteria"
    ]
    
  development:
    iterations: [
      "Basic prompt creation",
      "Test and validation",
      "Refinement cycles"
    ]
    checkpoints: [
      "Functionality review",
      "Quality assessment",
      "Performance evaluation"
    ]
    
  deployment:
    stages: [
      "Controlled rollout",
      "Monitoring setup",
      "Feedback collection"
    ]
    metrics: [
      "Response accuracy",
      "Processing time",
      "User satisfaction"
    ]
```

### 2. Integration Scenarios
```yaml
integration_examples:
  chatbot_system:
    context_setup:
      base_context: "Customer support environment"
      knowledge_base: "Product documentation"
      user_context: "Customer interaction history"
    
    prompt_chain:
      - step: "Intent classification"
        prompt_type: "Analysis"
        output: "User intent category"
      
      - step: "Response generation"
        prompt_type: "Synthesis"
        output: "Tailored support response"
      
      - step: "Quality check"
        prompt_type: "Validation"
        output: "Verified response"
    
  code_analysis:
    context_setup:
      base_context: "Code review system"
      knowledge_base: "Best practices database"
      project_context: "Repository history"
    
    prompt_chain:
      - step: "Code understanding"
        prompt_type: "Analysis"
        output: "Code structure and patterns"
      
      - step: "Issue detection"
        prompt_type: "Evaluation"
        output: "Potential problems"
      
      - step: "Recommendation"
        prompt_type: "Synthesis"
        output: "Improvement suggestions"
```

### 3. Validation Framework
```yaml
validation_framework:
  functional_testing:
    test_cases: [
      "Basic functionality",
      "Edge cases",
      "Error scenarios"
    ]
    validation_criteria: [
      "Response accuracy",
      "Format compliance",
      "Error handling"
    ]
    
  performance_testing:
    metrics: [
      "Response time",
      "Resource usage",
      "Throughput"
    ]
    benchmarks: [
      "Baseline performance",
      "Peak load handling",
      "Recovery time"
    ]
    
  user_acceptance:
    criteria: [
      "Usability",
      "Relevance",
      "Clarity"
    ]
    feedback_channels: [
      "User surveys",
      "Usage analytics",
      "Direct feedback"
    ]
```

## Real-World Applications

### 1. Customer Service Enhancement
```yaml
service_implementation:
  setup:
    context: "24/7 customer support system"
    objectives: [
      "Reduce response time",
      "Improve accuracy",
      "Maintain consistency"
    ]
    
  prompt_structure:
    initial_analysis:
      input: "Customer query"
      processing: "Intent classification"
      output: "Query category and priority"
    
    response_generation:
      template_selection: "Based on query category"
      personalization: "Customer history integration"
      tone_adjustment: "Situation-appropriate"
    
    quality_control:
      checks: [
        "Accuracy verification",
        "Tone consistency",
        "Completeness check"
      ]
      fallback: "Human agent escalation"
```

### 2. Technical Documentation System
```yaml
documentation_system:
  setup:
    context: "API documentation platform"
    objectives: [
      "Maintain technical accuracy",
      "Ensure clarity",
      "Support multiple expertise levels"
    ]
    
  content_generation:
    basic_level:
      audience: "Beginners"
      style: "Tutorial-based"
      examples: "Step-by-step guides"
    
    advanced_level:
      audience: "Experienced developers"
      style: "Reference documentation"
      examples: "Complex scenarios"
    
  quality_management:
    reviews: [
      "Technical accuracy",
      "Completeness",
      "Consistency"
    ]
    updates: [
      "Version tracking",
      "Change documentation",
      "Deprecation notices"
    ]
```

### 3. Educational Content Creation
```yaml
educational_system:
  setup:
    context: "Adaptive learning platform"
    objectives: [
      "Personalized learning paths",
      "Progressive complexity",
      "Engagement optimization"
    ]
    
  content_adaptation:
    skill_levels:
      beginner:
        style: "Foundational concepts"
        pace: "Gradual introduction"
        support: "Extensive guidance"
      
      intermediate:
        style: "Applied concepts"
        pace: "Moderate progression"
        support: "Guided practice"
      
      advanced:
        style: "Complex scenarios"
        pace: "Rapid advancement"
        support: "Independent exploration"
    
  assessment:
    methods: [
      "Knowledge checks",
      "Practical exercises",
      "Project work"
    ]
    feedback:
      type: "Multi-modal"
      timing: "Real-time"
      adaptation: "Performance-based"
```

## Evaluation and Metrics

### 1. Performance Metrics
```yaml
metric_framework:
  response_quality:
    accuracy:
      definition: "Correctness of generated content"
      measures: [
        "Error rate",
        "Precision score",
        "Recall score"
      ]
      thresholds:
        minimum: "95% accuracy"
        target: "98% accuracy"
    
    relevance:
      definition: "Alignment with user needs"
      measures: [
        "Context match score",
        "Intent satisfaction",
        "Information completeness"
      ]
      thresholds:
        minimum: "90% relevance"
        target: "95% relevance"
    
    consistency:
      definition: "Uniformity across responses"
      measures: [
        "Style adherence",
        "Tone consistency",
        "Format compliance"
      ]
      thresholds:
        minimum: "92% consistency"
        target: "97% consistency"

  operational_efficiency:
    response_time:
      definition: "Time to generate response"
      measures: [
        "Average generation time",
        "95th percentile latency",
        "Maximum response time"
      ]
      thresholds:
        target: "< 2 seconds"
        maximum: "< 5 seconds"
    
    resource_usage:
      definition: "Computational resources required"
      measures: [
        "Token consumption",
        "Memory usage",
        "API calls"
      ]
      optimization:
        target: "20% reduction"
        methods: [
          "Context optimization",
          "Prompt compression",
          "Caching strategies"
        ]
```

### 2. Evaluation Framework
```yaml
evaluation_system:
  automated_testing:
    unit_tests:
      coverage: [
        "Core functionality",
        "Edge cases",
        "Error handling"
      ]
      frequency: "Continuous"
      automation: "CI/CD pipeline"
    
    integration_tests:
      scenarios: [
        "Multi-step workflows",
        "Cross-component interaction",
        "System integration"
      ]
      frequency: "Daily"
      validation: "End-to-end testing"
    
    performance_tests:
      types: [
        "Load testing",
        "Stress testing",
        "Endurance testing"
      ]
      frequency: "Weekly"
      metrics: [
        "Response time",
        "Error rate",
        "Resource utilization"
      ]
  
  human_evaluation:
    expert_review:
      aspects: [
        "Technical accuracy",
        "Content quality",
        "Best practices"
      ]
      frequency: "Monthly"
      feedback_loop: "Continuous improvement"
    
    user_testing:
      methods: [
        "Usability studies",
        "A/B testing",
        "Focus groups"
      ]
      metrics: [
        "User satisfaction",
        "Task completion",
        "Error recovery"
      ]
      frequency: "Quarterly"
```

### 3. Continuous Improvement Framework
```yaml
improvement_system:
  data_collection:
    sources: [
      "User interactions",
      "System metrics",
      "Error logs",
      "Feedback channels"
    ]
    frequency: "Real-time"
    storage: "Data warehouse"
  
  analysis_pipeline:
    processing:
      steps: [
        "Data cleaning",
        "Pattern recognition",
        "Trend analysis"
      ]
      automation: "Automated analytics"
    
    insights:
      categories: [
        "Performance trends",
        "User behavior",
        "Error patterns"
      ]
      reporting: "Weekly dashboards"
  
  optimization_cycle:
    identification:
      focus_areas: [
        "Performance bottlenecks",
        "Quality issues",
        "User pain points"
      ]
      prioritization: "Impact-effort matrix"
    
    implementation:
      approach: "Iterative improvement"
      validation: "A/B testing"
      rollout: "Phased deployment"
    
    monitoring:
      metrics: [
        "Success indicators",
        "Regression tests",
        "User satisfaction"
      ]
      frequency: "Continuous"
```

## Scaling and Enterprise Integration

### 1. Enterprise Architecture
```yaml
enterprise_framework:
  infrastructure:
    components: [
      "Load balancers",
      "Caching layers",
      "Monitoring systems"
    ]
    scalability:
      horizontal: "Instance replication"
      vertical: "Resource optimization"
    
  security:
    compliance:
      standards: [
        "Data protection",
        "Access control",
        "Audit logging"
      ]
      certifications: [
        "ISO 27001",
        "SOC 2",
        "GDPR"
      ]
    
  integration:
    systems: [
      "CRM platforms",
      "Knowledge bases",
      "Analytics tools"
    ]
    protocols: [
      "REST APIs",
      "Message queues",
      "Event streams"
    ]
```

### 2. Team Organization
```yaml
team_structure:
  roles:
    prompt_engineers:
      responsibilities: [
        "Framework implementation",
        "Pattern development",
        "Quality assurance"
      ]
      skills: [
        "NLP expertise",
        "System design",
        "Quality control"
      ]
    
    domain_experts:
      responsibilities: [
        "Content validation",
        "Domain adaptation",
        "Best practices"
      ]
      collaboration: [
        "Knowledge transfer",
        "Review process",
        "Standard setting"
      ]
    
    operations:
      responsibilities: [
        "System monitoring",
        "Performance optimization",
        "Incident response"
      ]
      tools: [
        "Monitoring dashboards",
        "Analytics platforms",
        "Automation systems"
      ]
```

### 3. Governance Model
```yaml
governance_framework:
  policies:
    quality_standards:
      requirements: [
        "Response accuracy",
        "Performance targets",
        "Security compliance"
      ]
      enforcement: "Automated checks"
    
    change_management:
      process: [
        "Impact assessment",
        "Review workflow",
        "Deployment strategy"
      ]
      controls: [
        "Version control",
        "Approval gates",
        "Rollback procedures"
      ]
    
  risk_management:
    assessment:
      areas: [
        "Technical risks",
        "Operational risks",
        "Compliance risks"
      ]
      mitigation: [
        "Control measures",
        "Monitoring systems",
        "Response plans"
      ]
    
    compliance:
      requirements: [
        "Industry standards",
        "Legal obligations",
        "Internal policies"
      ]
      auditing: [
        "Regular reviews",
        "Compliance checks",
        "Documentation"
      ]
```

Please implement the CO-STAR framework following these guidelines to ensure effective prompt engineering and consistent results.
