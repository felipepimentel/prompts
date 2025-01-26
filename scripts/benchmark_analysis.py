#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from typing import Dict, List, Any
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
from datetime import datetime
import jinja2

class PromptAnalyzer:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings_cache = {}
        
    def compute_semantic_similarity(self, prompt1: str, prompt2: str) -> float:
        """Compute semantic similarity between two prompts."""
        if prompt1 not in self.embeddings_cache:
            self.embeddings_cache[prompt1] = self.model.encode([prompt1])[0]
        if prompt2 not in self.embeddings_cache:
            self.embeddings_cache[prompt2] = self.model.encode([prompt2])[0]
            
        similarity = cosine_similarity(
            [self.embeddings_cache[prompt1]], 
            [self.embeddings_cache[prompt2]]
        )[0][0]
        
        return float(similarity)
    
    def analyze_token_efficiency(self, prompt: str, response_tokens: int) -> Dict[str, float]:
        """Analyze token efficiency metrics."""
        prompt_tokens = len(prompt.split())
        return {
            "token_ratio": response_tokens / prompt_tokens if prompt_tokens > 0 else 0,
            "prompt_tokens": prompt_tokens,
            "response_tokens": response_tokens,
            "total_tokens": prompt_tokens + response_tokens
        }

class VisualizationGenerator:
    def __init__(self, output_dir: str = "benchmark_reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Load HTML template
        template_path = Path(__file__).parent / "templates" / "report_template.html"
        if not template_path.exists():
            self._create_default_template()
        
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_path.parent)
        )
        
    def _create_default_template(self):
        template_dir = Path(__file__).parent / "templates"
        template_dir.mkdir(exist_ok=True)
        
        template_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Prompt Benchmark Report</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .chart { margin: 20px 0; }
        .metric { 
            background: #f5f5f5; 
            padding: 10px; 
            margin: 10px 0; 
            border-radius: 5px; 
        }
        .trend { margin: 20px 0; }
    </style>
</head>
<body>
    <h1>Prompt Benchmark Report</h1>
    <div class="timestamp">Generated on: {{ timestamp }}</div>
    
    <h2>Summary</h2>
    <div class="metrics">
        {% for metric in summary_metrics %}
        <div class="metric">
            <h3>{{ metric.name }}</h3>
            <p>{{ metric.value }}</p>
        </div>
        {% endfor %}
    </div>
    
    <h2>Performance Charts</h2>
    {% for chart in charts %}
    <div class="chart">
        <h3>{{ chart.title }}</h3>
        {{ chart.div | safe }}
    </div>
    {% endfor %}
    
    <h2>Trends</h2>
    {% for trend in trends %}
    <div class="trend">
        <h3>{{ trend.title }}</h3>
        {{ trend.div | safe }}
    </div>
    {% endfor %}
    
    <h2>Detailed Results</h2>
    {{ detailed_results | safe }}
</body>
</html>
        """
        
        with open(template_dir / "report_template.html", "w") as f:
            f.write(template_content)
    
    def generate_performance_charts(self, results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate performance visualization charts."""
        charts = []
        
        # Model Performance Comparison
        if "model_performance" in results["summary"]:
            model_data = results["summary"]["model_performance"]
            
            # Execution Time Chart
            exec_times = {model: metrics["avg_execution_time"] 
                         for model, metrics in model_data.items()}
            fig = go.Figure(data=[
                go.Bar(name=model, x=["Execution Time"], y=[time])
                for model, time in exec_times.items()
            ])
            fig.update_layout(title="Average Execution Time by Model")
            charts.append({
                "title": "Execution Time Comparison",
                "div": fig.to_html(full_html=False)
            })
            
            # Error Rate Chart
            error_rates = {model: metrics["avg_error_rate"]
                          for model, metrics in model_data.items()}
            fig = go.Figure(data=[
                go.Bar(name=model, x=["Error Rate"], y=[rate])
                for model, rate in error_rates.items()
            ])
            fig.update_layout(title="Error Rate by Model")
            charts.append({
                "title": "Error Rate Comparison",
                "div": fig.to_html(full_html=False)
            })
        
        # Score Distribution
        scores = []
        for file_results in results["detailed_results"].values():
            for criteria_results in file_results.values():
                scores.append(criteria_results["score"])
        
        fig = go.Figure(data=[go.Histogram(x=scores)])
        fig.update_layout(title="Score Distribution")
        charts.append({
            "title": "Score Distribution",
            "div": fig.to_html(full_html=False)
        })
        
        return charts
    
    def generate_trend_charts(self, results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate trend analysis charts."""
        trends = []
        
        # Create a timeline of scores
        timeline_data = []
        for file_path, file_results in results["detailed_results"].items():
            for criteria, criteria_results in file_results.items():
                timeline_data.append({
                    "file": file_path,
                    "criteria": criteria,
                    "score": criteria_results["score"]
                })
        
        df = pd.DataFrame(timeline_data)
        
        # Score trends by criteria
        fig = px.line(df, x=df.index, y="score", color="criteria",
                     title="Score Trends by Criteria")
        trends.append({
            "title": "Score Trends",
            "div": fig.to_html(full_html=False)
        })
        
        return trends
    
    def generate_html_report(self, results: Dict[str, Any], output_file: str) -> None:
        """Generate an HTML report with interactive visualizations."""
        template = self.env.get_template("report_template.html")
        
        # Generate charts
        charts = self.generate_performance_charts(results)
        trends = self.generate_trend_charts(results)
        
        # Prepare summary metrics
        summary_metrics = [
            {"name": "Total Prompts", "value": results["summary"]["total_prompts"]},
            {"name": "Average Scores", "value": {
                k: f"{v:.2f}" for k, v in results["summary"]["average_scores"].items()
            }}
        ]
        
        # Generate HTML
        html_content = template.render(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            summary_metrics=summary_metrics,
            charts=charts,
            trends=trends,
            detailed_results=f"<pre>{json.dumps(results['detailed_results'], indent=2)}</pre>"
        )
        
        # Save report
        report_path = self.output_dir / output_file
        with open(report_path, "w") as f:
            f.write(html_content)
        
        print(f"Report generated: {report_path}") 