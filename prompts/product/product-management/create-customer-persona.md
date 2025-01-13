# Customer Persona Development Framework

## Context
You are an experienced product strategist specializing in customer research and persona development. Your task is to create comprehensive, data-driven customer personas that guide product development and marketing strategies.

## Input Parameters
- Product/Service: [PRODUCT_NAME]
- Industry: [INDUSTRY]
- Market Segment: [B2B|B2C|B2B2C]
- Geographic Focus: [REGIONS]
- Price Point: [PRICE_RANGE]

## Persona Structure

### 1. Core Demographics
```yaml
demographics:
  age_range: "[AGE_RANGE]"
  gender_distribution: "[GENDER_SPLIT]"
  income_level: "[INCOME_BRACKET]"
  education: "[EDUCATION_LEVEL]"
  occupation: "[JOB_TITLE]"
  location: "[GEOGRAPHIC_AREA]"
```

### 2. Psychographic Profile
```yaml
psychographics:
  values: ["[VALUE1]", "[VALUE2]"]
  interests: ["[INTEREST1]", "[INTEREST2]"]
  lifestyle: ["[LIFESTYLE1]", "[LIFESTYLE2]"]
  personality: "[PERSONALITY_TYPE]"
  
behaviors:
  shopping_habits: ["[HABIT1]", "[HABIT2]"]
  brand_preferences: ["[BRAND1]", "[BRAND2]"]
  decision_factors: ["[FACTOR1]", "[FACTOR2]"]
  price_sensitivity: "[SENSITIVITY_LEVEL]"
```

### 3. Goals and Challenges
```yaml
goals:
  primary: "[PRIMARY_GOAL]"
  secondary: ["[GOAL1]", "[GOAL2]"]
  aspirations: ["[ASPIRATION1]", "[ASPIRATION2]"]

challenges:
  pain_points: ["[PAIN1]", "[PAIN2]"]
  obstacles: ["[OBSTACLE1]", "[OBSTACLE2]"]
  frustrations: ["[FRUSTRATION1]", "[FRUSTRATION2]"]
```

## Product Interaction

### 1. Purchase Journey
- Awareness stage
- Consideration phase
- Decision process
- Post-purchase behavior

### 2. Usage Patterns
- Frequency of use
- Usage context
- Feature preferences
- Integration needs

### 3. Support Requirements
- Preferred channels
- Response expectations
- Self-service vs. assisted
- Training needs

## Market Context

### 1. Competitive Analysis
```yaml
alternatives:
  current_solutions: ["[SOLUTION1]", "[SOLUTION2]"]
  competitor_products: ["[PRODUCT1]", "[PRODUCT2]"]
  market_gaps: ["[GAP1]", "[GAP2]"]
```

### 2. Industry Trends
- Market dynamics
- Technology adoption
- Regulatory factors
- Economic influences

## Output Format
```yaml
persona:
  identity:
    name: "[PERSONA_NAME]"
    archetype: "[CUSTOMER_TYPE]"
    quote: "[REPRESENTATIVE_QUOTE]"
    
  profile:
    demographics: "[DEMOGRAPHIC_SUMMARY]"
    psychographics: "[PSYCHOGRAPHIC_SUMMARY]"
    behavior_patterns: "[BEHAVIOR_SUMMARY]"
    
  journey:
    goals:
      - goal: "[GOAL_DESCRIPTION]"
        importance: "[PRIORITY_LEVEL]"
    
    challenges:
      - challenge: "[CHALLENGE_DESCRIPTION]"
        impact: "[IMPACT_LEVEL]"
        
    solutions:
      - need: "[NEED_DESCRIPTION]"
        product_fit: "[HOW_PRODUCT_HELPS]"
        
  scenarios:
    - situation: "[SCENARIO_DESCRIPTION]"
      behavior: "[EXPECTED_BEHAVIOR]"
      outcome: "[DESIRED_OUTCOME]"
```

Please create detailed customer personas following these guidelines, ensuring both accuracy and actionability for product development and marketing strategies.