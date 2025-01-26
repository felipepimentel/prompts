#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
import frontmatter
from typing import List, Dict, Any, Optional
import json
from dataclasses import dataclass
from enum import Enum
import yaml
import asyncio
from concurrent.futures import ThreadPoolExecutor
from benchmark_analysis import PromptAnalyzer, VisualizationGenerator
import re
import unicodedata

class ModelType(Enum):
    """Available LLM models for testing."""
    # OpenAI Models
    GPT4_TURBO = "gpt-4-1106-preview"
    GPT4 = "gpt-4"
    GPT35_TURBO = "gpt-3.5-turbo-1106"
    
    # Anthropic Models
    CLAUDE3_OPUS = "claude-3-opus-20240229"
    CLAUDE3_SONNET = "claude-3-sonnet-20240229"
    CLAUDE3_HAIKU = "claude-3-haiku-20240229"
    
    # Google Models
    GEMINI_ULTRA = "gemini-1.0-ultra"
    GEMINI_PRO = "gemini-1.0-pro"
    
    # Open Source Models
    LLAMA2_70B = "llama-2-70b-chat"
    MIXTRAL = "mixtral-8x7b"

class PromptComplexity(Enum):
    """Types of prompt complexity metrics."""
    LEXICAL = "lexical"
    STRUCTURAL = "structural"
    SEMANTIC = "semantic"
    COGNITIVE = "cognitive"

class SecurityRisk(Enum):
    """Types of security risks in prompts."""
    INJECTION = "injection"
    SENSITIVE_DATA = "sensitive_data"
    JAILBREAK = "jailbreak"
    UNSAFE_EXECUTION = "unsafe_execution"

@dataclass
class ComplexityMetrics:
    """Metrics for measuring prompt complexity."""
    lexical_diversity: float
    avg_word_length: float
    nested_depth: int
    conditional_count: int
    variable_count: int

@dataclass
class SecurityMetrics:
    """Metrics for security analysis."""
    risk_level: float
    identified_risks: List[SecurityRisk]
    sensitive_patterns: List[str]

class EvaluationCriteria(Enum):
    STRUCTURE = "structure"
    CLARITY = "clarity"
    COMPLETENESS = "completeness"
    CONSISTENCY = "consistency"
    PERFORMANCE = "performance"
    MODEL_PERFORMANCE = "model_performance"
    SEMANTIC_SIMILARITY = "semantic_similarity"
    TOKEN_EFFICIENCY = "token_efficiency"
    COMPLEXITY = "complexity"
    SECURITY = "security"
    I18N = "i18n"

@dataclass
class ModelTestResult:
    model: ModelType
    response: str
    execution_time: float
    token_count: int
    error_rate: float

@dataclass
class BenchmarkResult:
    score: float
    feedback: List[str]
    suggestions: List[str]
    model_results: Optional[List[ModelTestResult]] = None
    semantic_scores: Optional[Dict[str, float]] = None
    token_metrics: Optional[Dict[str, float]] = None
    complexity_metrics: Optional[ComplexityMetrics] = None
    security_metrics: Optional[SecurityMetrics] = None

class PromptBenchmark:
    def __init__(self, config_file: Optional[str] = None):
        self.results: Dict[str, Dict[EvaluationCriteria, BenchmarkResult]] = {}
        self.config = self._load_config(config_file)
        self.analyzer = PromptAnalyzer()
        self.visualization = VisualizationGenerator()
        
    def _load_config(self, config_file: Optional[str]) -> Dict[str, Any]:
        if not config_file:
            return {
                "models": ["gpt-3.5-turbo"],
                "test_cases": [],
                "evaluation_criteria": {
                    "response_length": (50, 1000),
                    "max_tokens": 500,
                    "temperature": 0.7
                }
            }
        
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    
    async def evaluate_model_performance(self, content: str, metadata: Dict[str, Any]) -> BenchmarkResult:
        score = 0.0
        feedback = []
        suggestions = []
        model_results = []
        
        # Simulate model testing - replace with actual API calls
        for model_name in self.config["models"]:
            try:
                # Simulated model call
                import time
                import random
                
                start_time = time.time()
                time.sleep(0.5)  # Simulate API call
                
                model_result = ModelTestResult(
                    model=ModelType(model_name),
                    response="Simulated response",
                    execution_time=time.time() - start_time,
                    token_count=random.randint(100, 500),
                    error_rate=random.random()
                )
                
                model_results.append(model_result)
                score += (1 - model_result.error_rate) * 0.5
                
                if model_result.error_rate < 0.2:
                    feedback.append(f"✓ Good performance on {model_name}")
                else:
                    suggestions.append(f"Optimize prompt for better performance on {model_name}")
                    
            except Exception as e:
                suggestions.append(f"Error testing with {model_name}: {str(e)}")
        
        return BenchmarkResult(score / len(self.config["models"]), feedback, suggestions, model_results)
    
    def evaluate_structure(self, content: str, metadata: Dict[str, Any]) -> BenchmarkResult:
        score = 0.0
        feedback = []
        suggestions = []
        
        # Check for clear sections
        if "---" in content:
            score += 0.2
            feedback.append("✓ Has proper frontmatter separation")
        else:
            suggestions.append("Add proper frontmatter separation using '---'")
            
        # Check for required metadata
        required_fields = ['title', 'description', 'tags', 'model', 'category', 'version']
        present_fields = [field for field in required_fields if field in metadata]
        score += 0.4 * (len(present_fields) / len(required_fields))
        
        if len(present_fields) == len(required_fields):
            feedback.append("✓ Contains all required metadata fields")
        else:
            missing = set(required_fields) - set(present_fields)
            suggestions.append(f"Add missing metadata fields: {', '.join(missing)}")
            
        # Check content structure
        sections = content.split('\n\n')
        if len(sections) > 1:
            score += 0.2
            feedback.append("✓ Has clear section separation")
        else:
            suggestions.append("Add clear section separation with blank lines")
            
        # Check for examples
        if "example" in content.lower() or "```" in content:
            score += 0.2
            feedback.append("✓ Contains examples or code blocks")
        else:
            suggestions.append("Consider adding examples or code blocks")
            
        return BenchmarkResult(score, feedback, suggestions)
    
    def evaluate_clarity(self, content: str) -> BenchmarkResult:
        score = 0.0
        feedback = []
        suggestions = []
        
        # Check for clear instructions
        if any(keyword in content.lower() for keyword in ["you are", "your task", "your role"]):
            score += 0.3
            feedback.append("✓ Clear role/task definition")
        else:
            suggestions.append("Add clear role or task definition")
            
        # Check for formatting guidelines
        if "<format>" in content or "format:" in content.lower():
            score += 0.3
            feedback.append("✓ Contains format specifications")
        else:
            suggestions.append("Add output format specifications")
            
        # Check for success criteria
        if any(keyword in content.lower() for keyword in ["success", "criteria", "expected", "requirements"]):
            score += 0.4
            feedback.append("✓ Includes success criteria")
        else:
            suggestions.append("Add clear success criteria or requirements")
            
        return BenchmarkResult(score, feedback, suggestions)
    
    async def evaluate_semantic_similarity(self, content: str, all_prompts: List[str]) -> BenchmarkResult:
        """Evaluate semantic similarity with other prompts."""
        score = 0.0
        feedback = []
        suggestions = []
        semantic_scores = {}
        
        for other_prompt in all_prompts:
            if other_prompt != content:
                similarity = self.analyzer.compute_semantic_similarity(content, other_prompt)
                semantic_scores[other_prompt] = similarity
                
                if similarity > 0.8:
                    feedback.append(f"✓ High similarity ({similarity:.2f}) with another prompt")
                    suggestions.append("Consider consolidating similar prompts")
                
        if semantic_scores:
            score = sum(semantic_scores.values()) / len(semantic_scores)
            
        return BenchmarkResult(score, feedback, suggestions, semantic_scores=semantic_scores)
    
    def evaluate_token_efficiency(self, content: str, model_results: List[ModelTestResult]) -> BenchmarkResult:
        """Evaluate token efficiency metrics."""
        score = 0.0
        feedback = []
        suggestions = []
        
        # Analyze token efficiency for each model result
        token_metrics = {}
        for result in model_results:
            metrics = self.analyzer.analyze_token_efficiency(content, result.token_count)
            token_metrics[result.model.value] = metrics
            
            if metrics["token_ratio"] > 2.0:
                suggestions.append(f"High token ratio for {result.model.value}. Consider optimizing prompt length.")
            elif metrics["token_ratio"] < 0.5:
                suggestions.append(f"Low token ratio for {result.model.value}. Prompt might be too verbose.")
                
            score += 1.0 - abs(1.0 - metrics["token_ratio"])
            
        score = score / len(model_results) if model_results else 0.0
        
        return BenchmarkResult(score, feedback, suggestions, token_metrics=token_metrics)
    
    def evaluate_complexity(self, content: str) -> BenchmarkResult:
        """Analyzes prompt complexity across multiple dimensions."""
        score = 0.0
        feedback = []
        suggestions = []
        
        # Lexical analysis
        words = content.lower().split()
        unique_words = len(set(words))
        total_words = len(words)
        lexical_diversity = unique_words / total_words if total_words > 0 else 0
        avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
        
        # Structural analysis
        nested_depth = 0
        max_depth = 0
        for char in content:
            if char in '{[(<':
                nested_depth += 1
                max_depth = max(max_depth, nested_depth)
            elif char in '}])>':
                nested_depth = max(0, nested_depth - 1)
                
        # Count conditionals and variables
        conditional_count = sum(1 for keyword in ['if', 'when', 'unless', 'else'] 
                              if keyword in content.lower().split())
        variable_count = content.count('{{') + content.count('{%')
        
        metrics = ComplexityMetrics(
            lexical_diversity=lexical_diversity,
            avg_word_length=avg_word_length,
            nested_depth=max_depth,
            conditional_count=conditional_count,
            variable_count=variable_count
        )
        
        # Score calculation and feedback
        if lexical_diversity > 0.7:
            score += 0.2
            feedback.append("✓ Good lexical diversity")
        else:
            suggestions.append("Consider using more diverse vocabulary")
            
        if max_depth <= 3:
            score += 0.2
            feedback.append("✓ Appropriate nesting depth")
        else:
            suggestions.append(f"High nesting depth ({max_depth} levels) may confuse models")
            
        if conditional_count <= 5:
            score += 0.2
            feedback.append("✓ Reasonable number of conditionals")
        else:
            suggestions.append("High number of conditionals may increase complexity")
            
        if variable_count <= 10:
            score += 0.2
            feedback.append("✓ Manageable number of variables")
        else:
            suggestions.append("Consider reducing the number of variables")
            
        return BenchmarkResult(score, feedback, suggestions, complexity_metrics=metrics)
    
    def evaluate_security(self, content: str) -> BenchmarkResult:
        """Analyzes potential security risks in the prompt."""
        score = 1.0
        feedback = []
        suggestions = []
        identified_risks = []
        sensitive_patterns = []
        
        # Security patterns to check
        risk_patterns = {
            SecurityRisk.INJECTION: [
                r'system\s*prompt',
                r'ignore\s*(previous|above)',
                r'bypass',
                r'override'
            ],
            SecurityRisk.SENSITIVE_DATA: [
                r'api[_-]?key',
                r'password',
                r'secret',
                r'token',
                r'credential'
            ],
            SecurityRisk.JAILBREAK: [
                r'ignore\s*ethics',
                r'ignore\s*rules',
                r'unlimited\s*power',
                r'no\s*restrictions'
            ],
            SecurityRisk.UNSAFE_EXECUTION: [
                r'execute\s*command',
                r'run\s*shell',
                r'system\s*call',
                r'eval'
            ]
        }
        
        content_lower = content.lower()
        
        # Check each risk category
        for risk_type, patterns in risk_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content_lower):
                    score -= 0.2
                    identified_risks.append(risk_type)
                    sensitive_patterns.append(pattern)
                    suggestions.append(f"Security risk ({risk_type.value}): Found pattern '{pattern}'")
        
        if score > 0.8:
            feedback.append("✓ No major security risks detected")
        else:
            feedback.append("⚠ Security risks detected - review suggestions")
            
        metrics = SecurityMetrics(
            risk_level=1.0 - score,
            identified_risks=list(set(identified_risks)),
            sensitive_patterns=list(set(sensitive_patterns))
        )
        
        return BenchmarkResult(max(0.0, score), feedback, suggestions, security_metrics=metrics)
    
    def evaluate_i18n(self, content: str) -> BenchmarkResult:
        """Analyzes internationalization aspects of the prompt."""
        score = 0.0
        feedback = []
        suggestions = []
        
        # Character set analysis
        has_non_ascii = any(ord(c) > 127 for c in content)
        unicode_categories = set(unicodedata.category(c) for c in content)
        
        # Regional format detection
        region_patterns = {
            'date_format': r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b',
            'time_format': r'\b(\d{1,2}:\d{2})\b',
            'currency': r'[\$€£¥]',
            'phone': r'\+\d{1,3}[-\s]?\d{1,14}',
            'timezone': r'\b[A-Z]{3,4}[-+]\d{1,2}(:?\d{2})?\b'
        }
        
        found_patterns = {
            key: bool(re.search(pattern, content))
            for key, pattern in region_patterns.items()
        }
        
        # Scoring and feedback
        if has_non_ascii:
            score += 0.2
            feedback.append("✓ Supports non-ASCII characters")
        else:
            suggestions.append("Consider adding support for non-ASCII characters")
            
        if 'Lo' in unicode_categories:  # Other Letters (e.g., CJK)
            score += 0.2
            feedback.append("✓ Supports CJK characters")
            
        if any(found_patterns.values()):
            suggestions.append("Contains region-specific formats - consider using ISO standards:")
            for format_type, found in found_patterns.items():
                if found:
                    suggestions.append(f"- Replace {format_type} with ISO format")
        else:
            score += 0.3
            feedback.append("✓ No region-specific formats detected")
            
        # Variable interpolation check
        if '{{' in content and '}}' in content:
            score += 0.3
            feedback.append("✓ Uses variable interpolation")
        else:
            suggestions.append("Consider using variables for localizable content")
            
        return BenchmarkResult(score, feedback, suggestions)

    async def benchmark_prompt(self, file_path: str, all_prompts: Optional[List[str]] = None) -> Dict[EvaluationCriteria, BenchmarkResult]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                
            results = {}
            
            # Basic evaluations
            results[EvaluationCriteria.STRUCTURE] = self.evaluate_structure(post.content, post.metadata)
            results[EvaluationCriteria.CLARITY] = self.evaluate_clarity(post.content)
            
            # Advanced evaluations
            results[EvaluationCriteria.COMPLEXITY] = self.evaluate_complexity(post.content)
            results[EvaluationCriteria.SECURITY] = self.evaluate_security(post.content)
            results[EvaluationCriteria.I18N] = self.evaluate_i18n(post.content)
            
            # Model performance evaluation
            model_results = await self.evaluate_model_performance(post.content, post.metadata)
            results[EvaluationCriteria.MODEL_PERFORMANCE] = model_results
            
            # Semantic analysis
            if all_prompts:
                semantic_results = await self.evaluate_semantic_similarity(post.content, all_prompts)
                results[EvaluationCriteria.SEMANTIC_SIMILARITY] = semantic_results
            
            # Token efficiency
            if model_results.model_results:
                token_results = self.evaluate_token_efficiency(post.content, model_results.model_results)
                results[EvaluationCriteria.TOKEN_EFFICIENCY] = token_results
            
            self.results[file_path] = results
            return results
            
        except Exception as e:
            print(f"Error benchmarking {file_path}: {str(e)}")
            return {}
    
    def generate_report(self, output_file: Optional[str] = None, html_report: Optional[str] = None) -> None:
        """Generate both JSON and HTML reports."""
        report = {
            "summary": {
                "total_prompts": len(self.results),
                "average_scores": {},
                "model_performance": {},
                "semantic_analysis": {
                    "avg_similarity": 0.0,
                    "similar_prompt_pairs": []
                },
                "token_efficiency": {
                    "avg_ratio": 0.0,
                    "efficiency_by_model": {}
                }
            },
            "detailed_results": {}
        }
        
        # Calculate averages and collect metrics
        for criteria in EvaluationCriteria:
            scores = [results[criteria].score for results in self.results.values() if criteria in results]
            if scores:
                report["summary"]["average_scores"][criteria.value] = sum(scores) / len(scores)
                
                # Collect model-specific metrics
                if criteria == EvaluationCriteria.MODEL_PERFORMANCE:
                    self._collect_model_metrics(report)
                
                # Collect semantic similarity metrics
                elif criteria == EvaluationCriteria.SEMANTIC_SIMILARITY:
                    self._collect_semantic_metrics(report)
                
                # Collect token efficiency metrics
                elif criteria == EvaluationCriteria.TOKEN_EFFICIENCY:
                    self._collect_token_metrics(report)
        
        # Generate detailed results
        self._generate_detailed_results(report)
        
        # Save JSON report
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
        else:
            print(json.dumps(report, indent=2))
        
        # Generate HTML report with visualizations
        if html_report:
            self.visualization.generate_html_report(report, html_report)

async def main():
    if len(sys.argv) < 2:
        print("Usage: benchmark_prompts.py <prompt_file_or_directory> [output_file] [config_file] [html_report]")
        sys.exit(1)
        
    target = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    config_file = sys.argv[3] if len(sys.argv) > 3 else None
    html_report = sys.argv[4] if len(sys.argv) > 4 else None
    
    benchmark = PromptBenchmark(config_file)
    
    # Collect all prompts for semantic similarity analysis
    all_prompts = []
    if os.path.isdir(target):
        for prompt_file in Path(target).glob("**/*.md"):
            if "prompts" in str(prompt_file):
                with open(prompt_file, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    all_prompts.append(post.content)
    
    # Run benchmarks
    if os.path.isfile(target):
        await benchmark.benchmark_prompt(target, all_prompts if len(all_prompts) > 1 else None)
    else:
        tasks = []
        for prompt_file in Path(target).glob("**/*.md"):
            if "prompts" in str(prompt_file):
                tasks.append(benchmark.benchmark_prompt(str(prompt_file), all_prompts))
        await asyncio.gather(*tasks)
    
    # Generate reports
    benchmark.generate_report(output_file, html_report)

if __name__ == '__main__':
    asyncio.run(main()) 