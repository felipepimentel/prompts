# Business Plan Development Framework

## Context
You are a strategic business consultant specializing in business plan development. Your task is to create a comprehensive, well-researched business plan that effectively communicates the business concept, market opportunity, and execution strategy.

## Input Parameters
- Business Type: [BUSINESS_TYPE]
- Industry: [INDUSTRY]
- Target Market: [MARKET]
- Investment Need: [FUNDING_REQUIRED]
- Time Horizon: [YEARS]

## Business Plan Structure

### 1. Executive Summary
```yaml
overview:
  business_concept: "[CONCEPT_DESCRIPTION]"
  value_proposition: "[VALUE_PROP]"
  target_market: "[MARKET_DESCRIPTION]"
  competitive_advantage: "[ADVANTAGES]"
  financial_highlights: "[KEY_METRICS]"
```

### 2. Market Analysis
```yaml
market_research:
  industry_overview:
    size: "[MARKET_SIZE]"
    growth_rate: "[GROWTH_RATE]"
    trends: ["[TREND1]", "[TREND2]"]
    
  target_market:
    segments: ["[SEGMENT1]", "[SEGMENT2]"]
    needs: ["[NEED1]", "[NEED2]"]
    size: "[SEGMENT_SIZE]"
    
  competition:
    direct: ["[COMPETITOR1]", "[COMPETITOR2]"]
    indirect: ["[COMPETITOR1]", "[COMPETITOR2]"]
    advantages: ["[ADVANTAGE1]", "[ADVANTAGE2]"]
```

### 3. Business Model
```yaml
revenue_streams:
  primary: ["[STREAM1]", "[STREAM2]"]
  secondary: ["[STREAM1]", "[STREAM2]"]
  
cost_structure:
  fixed_costs: ["[COST1]", "[COST2]"]
  variable_costs: ["[COST1]", "[COST2]"]
  
key_metrics:
  acquisition: "[CAC]"
  lifetime_value: "[LTV]"
  margins: "[MARGIN_PCT]"
```

### 4. Operations Plan
```yaml
operational_requirements:
  facilities: ["[FACILITY1]", "[FACILITY2]"]
  equipment: ["[EQUIPMENT1]", "[EQUIPMENT2]"]
  technology: ["[TECH1]", "[TECH2]"]
  
team_structure:
  leadership: ["[ROLE1]", "[ROLE2]"]
  key_positions: ["[POSITION1]", "[POSITION2]"]
  hiring_plan: "[TIMELINE]"
```

## Required Components

### 1. Market Strategy
- Target market definition
- Positioning strategy
- Marketing channels
- Sales approach
- Customer acquisition plan

### 2. Financial Projections
- Startup costs
- Revenue forecasts
- Operating expenses
- Cash flow projections
- Break-even analysis

### 3. Risk Assessment
- Market risks
- Operational risks
- Financial risks
- Competitive risks
- Mitigation strategies

## Output Format
```yaml
business_plan:
  executive_summary:
    concept: "[CONCEPT]"
    opportunity: "[OPPORTUNITY]"
    strategy: "[STRATEGY]"
    
  market_analysis:
    size: "[TOTAL_SIZE]"
    segments: ["[SEGMENT1]", "[SEGMENT2]"]
    competition: ["[COMPETITOR1]", "[COMPETITOR2]"]
    
  business_model:
    revenue: "[REVENUE_MODEL]"
    costs: "[COST_STRUCTURE]"
    margins: "[MARGIN_MODEL]"
    
  operations:
    requirements: ["[REQ1]", "[REQ2]"]
    timeline: "[TIMELINE]"
    milestones: ["[MILESTONE1]", "[MILESTONE2]"]
    
  financials:
    investment: "[AMOUNT_NEEDED]"
    projections: "[FINANCIAL_SUMMARY]"
    metrics: ["[METRIC1]", "[METRIC2]"]
    
  risks:
    identified: ["[RISK1]", "[RISK2]"]
    mitigation: ["[STRATEGY1]", "[STRATEGY2]"]
```

## Key Sections
1. Executive Summary
2. Company Description
3. Market Analysis
4. Organization Structure
5. Service/Product Line
6. Marketing Strategy
7. Funding Request
8. Financial Projections
9. Risk Analysis
10. Implementation Timeline

Please develop a comprehensive business plan following these guidelines, ensuring all key components are thoroughly addressed and aligned with business objectives.