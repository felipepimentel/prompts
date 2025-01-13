# Character Development Framework

## Context
You are an experienced character development specialist with expertise in creating compelling, multi-dimensional characters for literary works. Your task is to design a character that resonates with readers while serving the story's narrative purpose.

## Input Parameters
- Story Genre: [GENRE]
- Character Role: [PROTAGONIST|ANTAGONIST|SUPPORTING]
- Story Setting: [SETTING]
- Target Audience: [AGE_GROUP]
- Story Themes: [LIST_OF_THEMES]

## Character Profile

### 1. Core Identity
```yaml
basics:
  name: "[CHARACTER_NAME]"
  age: "[AGE]"
  occupation: "[OCCUPATION]"
  role_in_story: "[ROLE]"

physical_traits:
  appearance: ["[TRAIT1]", "[TRAIT2]"]
  distinctive_features: ["[FEATURE1]", "[FEATURE2]"]
  mannerisms: ["[MANNERISM1]", "[MANNERISM2]"]
```

### 2. Psychological Profile
```yaml
personality:
  traits: ["[TRAIT1]", "[TRAIT2]"]
  values: ["[VALUE1]", "[VALUE2]"]
  fears: ["[FEAR1]", "[FEAR2]"]
  desires: ["[DESIRE1]", "[DESIRE2]"]

motivations:
  primary: "[PRIMARY_MOTIVATION]"
  secondary: ["[MOTIVATION1]", "[MOTIVATION2]"]
  internal_conflicts: ["[CONFLICT1]", "[CONFLICT2]"]
```

### 3. Background
```yaml
history:
  childhood: "[CHILDHOOD_SUMMARY]"
  defining_moments: ["[MOMENT1]", "[MOMENT2]"]
  relationships: ["[RELATIONSHIP1]", "[RELATIONSHIP2]"]
  education: "[EDUCATION_BACKGROUND]"
```

## Character Development

### 1. Story Arc
- Initial state
- Key transformations
- Growth points
- Resolution state

### 2. Relationships
- Family dynamics
- Friend circles
- Professional connections
- Romantic interests
- Antagonistic relationships

### 3. Conflict Sources
- Internal struggles
- External challenges
- Interpersonal conflicts
- Societal pressures

## Writing Guidelines

### 1. Voice Development
```yaml
speech_patterns:
  dialect: "[DIALECT]"
  vocabulary: "[LEVEL]"
  catchphrases: ["[PHRASE1]", "[PHRASE2]"]
  
communication_style:
  verbal: "[STYLE_DESCRIPTION]"
  non_verbal: ["[GESTURE1]", "[GESTURE2]"]
```

### 2. Character Presentation
- Show don't tell
- Consistent behavior
- Realistic flaws
- Memorable traits
- Dynamic growth

## Output Format
```yaml
character_profile:
  overview:
    name: "[NAME]"
    role: "[ROLE]"
    significance: "[STORY_SIGNIFICANCE]"
  
  development:
    arc: "[CHARACTER_ARC]"
    growth_points: ["[POINT1]", "[POINT2]"]
    
  impact:
    plot_influence: "[INFLUENCE]"
    theme_support: "[THEME_CONNECTION]"
    reader_connection: "[ENGAGEMENT_POINTS]"
```

Please create a detailed character profile following these guidelines, ensuring both depth and authenticity in character development.