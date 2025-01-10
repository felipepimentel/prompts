# Developer Prompts

A collection of prompts designed to assist with software development tasks.

## Code Review Prompt

### Context
Use this prompt when you need to review code for best practices, potential issues, and improvements.

### Variables
- {language}: Programming language of the code
- {code_snippet}: The code to be reviewed
- {review_focus}: Specific aspects to focus on (e.g., "security", "performance", "readability")

### Prompt Template
```
Act as an experienced {language} developer conducting a thorough code review. Review the following code with special attention to {review_focus}:

{code_snippet}

Please provide:
1. Potential issues and bugs
2. Best practices violations
3. Performance considerations
4. Suggested improvements
5. Security concerns (if applicable)
```

### Example Usage
```
Act as an experienced Python developer conducting a thorough code review. Review the following code with special attention to security and performance:

def process_user_data(user_input):
    query = "SELECT * FROM users WHERE id = " + user_input
    db.execute(query)
    return True

Please provide:
1. Potential issues and bugs
2. Best practices violations
3. Performance considerations
4. Suggested improvements
5. Security concerns (if applicable)
```

### Best Practices
- Always specify the programming language
- Be clear about review focus areas
- Include context about the code's purpose
- Request specific types of feedback

## Strategic Linting

### Context
Use this prompt to define comprehensive linting directives for your project.

### Variables
- {project_type}: Type of project (e.g., "frontend", "backend", "full-stack")
- {language}: Primary programming language
- {focus_areas}: Key areas of concern (e.g., "security", "performance", "maintainability")

### Prompt Template
```
Define linting directives for a {project_type} project using {language} with focus on {focus_areas}.

Provide directives in the following categories:

1. Code Quality
ENFORCE:
  - style=<standard>
  - types=<strictness>
  - docs=<requirement>
  - tests=<coverage>

2. Security
CHECK:
  - input=<validation>
  - auth=<level>
  - data=<protection>
  - api=<security>

3. Performance
OPTIMIZE:
  - complexity=<limit>
  - memory=<efficiency>
  - async=<handling>
  - cache=<strategy>

4. Environment-Specific Rules
ENV: development
  - <dev_rules>
ENV: production
  - <prod_rules>

Include implementation details for:
1. Tool configuration
2. CI/CD integration
3. Team adoption guidelines
4. Exception handling
```

### Example Usage
```
Define linting directives for a "frontend" project using "TypeScript" with focus on "security, performance, accessibility".

Provide directives in the following categories:

1. Code Quality
ENFORCE:
  - style=airbnb
  - types=strict
  - docs=required
  - tests=coverage:80

2. Security
CHECK:
  - input=sanitize
  - auth=validate
  - data=encrypt
  - api=secure

3. Performance
OPTIMIZE:
  - complexity=O(n)
  - memory=efficient
  - async=promise
  - cache=browser

4. Environment-Specific Rules
ENV: development
  - debug=verbose
  - checks=all
ENV: production
  - optimize=bundle
  - security=max

Include implementation details for:
1. Tool configuration
2. CI/CD integration
3. Team adoption guidelines
4. Exception handling
```

### Best Practices
- Define clear standards
- Include all environments
- Consider team workflow
- Document exceptions

## Documentation Generator

### Context
Use this prompt to generate comprehensive documentation for code.

### Variables
- {language}: Programming language
- {code}: Code to document
- {doc_style}: Documentation style (e.g., JSDoc, Google Style, NumPy)

### Prompt Template
```
Generate {doc_style} style documentation for the following {language} code. Include:
- Function/class purpose
- Parameters and return values
- Usage examples
- Important notes/warnings

Code:
{code}
```

### Example Usage
```
Generate Google Style documentation for the following Python code. Include:
- Function/class purpose
- Parameters and return values
- Usage examples
- Important notes/warnings

Code:
def calculate_discount(price, percentage, max_discount=100):
    discount = price * (percentage / 100)
    return min(discount, max_discount)
```

### Best Practices
- Specify documentation style guide
- Include example usage scenarios
- Request parameter descriptions
- Ask for edge cases and limitations

## Architecture Planning

### Context
Use this prompt when planning software architecture or system design.

### Variables
- {project_type}: Type of project (e.g., web app, mobile app, API)
- {requirements}: Key requirements and constraints
- {scale}: Expected scale and performance needs

### Prompt Template
```
Design a software architecture for a {project_type} with the following requirements:

Requirements:
{requirements}

Scale Considerations:
{scale}

Please provide:
1. High-level architecture diagram (in text/ASCII)
2. Key components and their responsibilities
3. Data flow between components
4. Technology stack recommendations
5. Potential challenges and solutions
```

### Best Practices
- Be specific about requirements
- Include scale considerations
- Request specific deliverables
- Ask for trade-off analysis

## More Prompts

Check out our [Contributing Guide](../contributing.md) to add more developer prompts to this collection. 