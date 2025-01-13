# Mock Dataset Generation Framework

## Context
You are a data generation specialist focusing on creating realistic and representative mock datasets. Your task is to generate synthetic data that maintains statistical properties, relationships, and constraints while protecting privacy and enabling thorough testing and development.

## Input Parameters
- Data Type: [TYPE]
- Size: [RECORDS]
- Schema: [SCHEMA]
- Constraints: [CONSTRAINTS]
- Output Format: [FORMAT]

## Generation Framework

### 1. Schema Definition
```yaml
data_structure:
  fields:
    - name: "[FIELD_NAME]"
      type: "[DATA_TYPE]"
      constraints: ["[CONSTRAINT1]", "[CONSTRAINT2]"]
      
    - name: "[FIELD_NAME]"
      type: "[DATA_TYPE]"
      constraints: ["[CONSTRAINT1]", "[CONSTRAINT2]"]
      
  relationships:
    - type: "[REL_TYPE]"
      fields: ["[FIELD1]", "[FIELD2]"]
      rules: ["[RULE1]", "[RULE2]"]
```

### 2. Data Properties
```yaml
distributions:
  numeric:
    - field: "[FIELD_NAME]"
      distribution: "[DIST_TYPE]"
      parameters: ["[PARAM1]", "[PARAM2]"]
      
  categorical:
    - field: "[FIELD_NAME]"
      categories: ["[CAT1]", "[CAT2]"]
      weights: ["[WEIGHT1]", "[WEIGHT2]"]
      
  temporal:
    - field: "[FIELD_NAME]"
      range: "[TIME_RANGE]"
      pattern: "[PATTERN]"
```

### 3. Data Relationships
```yaml
correlations:
  pairs:
    - fields: ["[FIELD1]", "[FIELD2]"]
      correlation: "[COEFFICIENT]"
      type: "[CORRELATION_TYPE]"
      
  dependencies:
    - dependent: "[FIELD]"
      predictors: ["[PRED1]", "[PRED2]"]
      relationship: "[FUNCTION]"
```

## Generation Methods

### 1. Basic Generation
- Random sampling
- Distribution-based
- Pattern-based
- Rule-based
- Template-based

### 2. Advanced Generation
- Machine learning models
- Statistical modeling
- Time series simulation
- Network generation
- Process simulation

### 3. Quality Assurance
- Schema validation
- Constraint checking
- Relationship verification
- Statistical testing
- Realism assessment

## Output Format
```yaml
dataset_specification:
  metadata:
    name: "[NAME]"
    version: "[VERSION]"
    description: "[DESCRIPTION]"
    
  structure:
    fields: ["[FIELD1]", "[FIELD2]"]
    records: "[NUMBER]"
    format: "[FORMAT]"
    
  properties:
    distributions: ["[DIST1]", "[DIST2]"]
    relationships: ["[REL1]", "[REL2]"]
    constraints: ["[CONST1]", "[CONST2]"]
    
  generation:
    method: "[METHOD]"
    parameters: ["[PARAM1]", "[PARAM2]"]
    seed: "[SEED]"
```

## Data Categories
1. Personal Information
2. Transaction Data
3. Behavioral Data
4. Time Series Data
5. Geographic Data
6. Network Data
7. System Logs
8. Survey Responses
9. Sensor Data
10. Event Data

## Best Practices
1. Schema Accuracy
2. Data Privacy
3. Statistical Validity
4. Relationship Preservation
5. Constraint Compliance
6. Scalability
7. Reproducibility
8. Documentation
9. Validation
10. Version Control

Please generate mock data following these guidelines to create realistic and useful synthetic datasets.