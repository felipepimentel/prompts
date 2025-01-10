# Data Prompts

A collection of prompts designed to assist with data analysis, visualization, and insights generation.

## Data Analysis

### Context
Use this prompt to analyze data and extract meaningful insights.

### Variables
- {data_description}: Description of the data to be analyzed
- {analysis_goal}: Specific objective of the analysis
- {required_metrics}: Key metrics to calculate
- {output_format}: Desired format of the results

### Prompt Template
```
Analyze the following {data_description} to achieve {analysis_goal}.

Calculate and provide:
1. {required_metrics}
2. Key trends and patterns
3. Notable anomalies
4. Statistical significance
5. Actionable insights

Present the results in {output_format} format.

Additional considerations:
- Data quality issues
- Limitations of the analysis
- Confidence levels
- Recommendations for further analysis
```

### Example Usage
```
Analyze the following "monthly sales data for the past 2 years" to achieve "identification of seasonal patterns and growth trends".

Calculate and provide:
1. "Monthly growth rates, YoY comparisons, seasonal indices"
2. Key trends and patterns
3. Notable anomalies
4. Statistical significance
5. Actionable insights

Present the results in "bullet points with supporting charts description" format.

Additional considerations:
- Data quality issues
- Limitations of the analysis
- Confidence levels
- Recommendations for further analysis
```

### Best Practices
- Specify exact metrics needed
- Request confidence levels
- Consider data limitations
- Ask for actionable insights

## Data Visualization

### Context
Use this prompt to get recommendations for effective data visualization.

### Variables
- {data_type}: Type of data to visualize
- {audience}: Target audience for the visualization
- {purpose}: Goal of the visualization
- {constraints}: Any technical or design constraints

### Prompt Template
```
Recommend visualization approaches for {data_type} targeting {audience} with the purpose of {purpose}.

Consider:
1. Chart/graph types
2. Key elements to highlight
3. Color schemes and accessibility
4. Interactive features
5. Annotations and context

Technical constraints:
{constraints}

Provide:
1. Primary visualization recommendation
2. Alternative approaches
3. Implementation considerations
4. Best practices for chosen format
```

### Best Practices
- Define audience clearly
- Specify visualization purpose
- Consider accessibility
- Include technical constraints

## SQL Query Generation

### Context
Use this prompt to generate SQL queries for data analysis.

### Variables
- {objective}: Goal of the query
- {tables}: Available database tables and their schemas
- {conditions}: Specific conditions or filters
- {output}: Required output format

### Prompt Template
```
Generate a SQL query to {objective} using the following tables:

Tables Structure:
{tables}

Requirements:
1. Include these conditions: {conditions}
2. Output should be: {output}
3. Consider performance optimization
4. Include error handling

Please provide:
1. Complete SQL query
2. Explanation of each major component
3. Any assumptions made
4. Performance considerations
```

### Example Usage
```
Generate a SQL query to "find top 10 customers by revenue in the last quarter" using the following tables:

Tables Structure:
- customers (id, name, region)
- orders (id, customer_id, order_date, total_amount)
- order_items (order_id, product_id, quantity, price)

Requirements:
1. Include these conditions: "only completed orders, exclude cancelled orders"
2. Output should be: "customer name, total revenue, number of orders"
3. Consider performance optimization
4. Include error handling

Please provide:
1. Complete SQL query
2. Explanation of each major component
3. Any assumptions made
4. Performance considerations
```

### Best Practices
- Specify table relationships
- Include performance requirements
- Define output format clearly
- Request error handling

## More Prompts

Check out our [Contributing Guide](../contributing.md) to add more data analysis prompts to this collection. 