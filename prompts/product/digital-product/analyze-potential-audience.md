# Digital Product Audience Analysis Framework

## Context
You are an experienced market research analyst specializing in digital product audience analysis. Your task is to conduct a comprehensive analysis of potential target audiences, providing actionable insights for product development and marketing strategies.

## Input Parameters
- Product Type: [PRODUCT_CATEGORY]
- Industry Vertical: [INDUSTRY]
- Geographic Scope: [REGIONS]
- Price Point: [PRICE_RANGE]
- Competition Level: [LOW|MEDIUM|HIGH]

## Analysis Framework

### 1. Market Segmentation
```yaml
segments:
  - name: "[SEGMENT_NAME]"
    size: "[MARKET_SIZE]"
    growth_rate: "[GROWTH_PERCENTAGE]"
    characteristics:
      demographics: ["[DEMO1]", "[DEMO2]"]
      behaviors: ["[BEHAVIOR1]", "[BEHAVIOR2]"]
      needs: ["[NEED1]", "[NEED2]"]
```

### 2. User Behavior Analysis
```yaml
behaviors:
  digital_presence:
    platforms: ["[PLATFORM1]", "[PLATFORM2]"]
    usage_patterns: ["[PATTERN1]", "[PATTERN2]"]
    
  purchasing:
    channels: ["[CHANNEL1]", "[CHANNEL2]"]
    decision_factors: ["[FACTOR1]", "[FACTOR2]"]
    price_sensitivity: "[SENSITIVITY_LEVEL]"
    
  engagement:
    preferred_content: ["[CONTENT1]", "[CONTENT2]"]
    interaction_style: "[STYLE]"
    brand_affinity: "[AFFINITY_LEVEL]"
```

### 3. Market Opportunity Assessment
```yaml
opportunities:
  segment_potential:
    revenue: "[REVENUE_ESTIMATE]"
    growth: "[GROWTH_RATE]"
    barriers: ["[BARRIER1]", "[BARRIER2]"]
    
  competitive_landscape:
    direct_competitors: ["[COMPETITOR1]", "[COMPETITOR2]"]
    indirect_competitors: ["[COMPETITOR3]", "[COMPETITOR4]"]
    market_gaps: ["[GAP1]", "[GAP2]"]
```

## Research Methods

### 1. Quantitative Analysis
- Market size calculations
- Demographics data
- Usage statistics
- Revenue projections
- Growth trends

### 2. Qualitative Research
- User interviews
- Focus groups
- Behavioral observation
- Social listening
- Sentiment analysis

### 3. Competitive Analysis
- Feature comparison
- Pricing analysis
- Market positioning
- User satisfaction
- Market share

## Insight Categories

### 1. User Needs
```yaml
needs:
  functional: ["[NEED1]", "[NEED2]"]
  emotional: ["[NEED3]", "[NEED4]"]
  social: ["[NEED5]", "[NEED6]"]
  aspirational: ["[NEED7]", "[NEED8]"]
```

### 2. Market Trends
```yaml
trends:
  technology: ["[TREND1]", "[TREND2]"]
  consumer_behavior: ["[TREND3]", "[TREND4]"]
  industry_specific: ["[TREND5]", "[TREND6]"]
```

## Output Format
```yaml
audience_analysis:
  executive_summary:
    key_findings: ["[FINDING1]", "[FINDING2]"]
    recommendations: ["[REC1]", "[REC2]"]
    
  market_segments:
    primary:
      description: "[PRIMARY_SEGMENT]"
      size: "[SEGMENT_SIZE]"
      opportunity: "[OPPORTUNITY_SIZE]"
      
    secondary:
      description: "[SECONDARY_SEGMENT]"
      size: "[SEGMENT_SIZE]"
      opportunity: "[OPPORTUNITY_SIZE]"
      
  targeting_strategy:
    channels: ["[CHANNEL1]", "[CHANNEL2]"]
    messaging: ["[MESSAGE1]", "[MESSAGE2]"]
    positioning: "[POSITION_STATEMENT]"
    
  action_plan:
    short_term: ["[ACTION1]", "[ACTION2]"]
    medium_term: ["[ACTION3]", "[ACTION4]"]
    long_term: ["[ACTION5]", "[ACTION6]"]
```

Please conduct a thorough audience analysis following these guidelines, ensuring both depth of insights and actionability of recommendations.