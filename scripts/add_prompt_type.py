#!/usr/bin/env python3
import os
import re
import yaml
from typing import Dict, Optional

PROMPT_TYPES = {
    "zero-shot": "Zero-shot prompting",
    "few-shot": "Few-shot prompting",
    "chain-of-thought": "Chain-of-thought prompting",
    "instruction": "Instruction-based prompting",
    "role": "Role-based prompting",
    "context": "Contextual prompting",
    "meta": "Meta prompting",
    "self-consistency": "Self-consistency prompting",
    "generated-knowledge": "Generated knowledge prompting",
    "dynamic": "Dynamic prompt optimization",
    "automatic": "Automatic prompt engineering",
    "multi-prompt": "Multi-prompt fusion",
    "prompt-chaining": "Prompt chaining",
    "directional": "Directional stimulus prompting",
    "graph": "Graph prompting",
    "hybrid": "Hybrid prompting",
    "constraint": "Constraint-based prompting",
    "scenario": "Scenario-based prompting",
    "template": "Template-based prompting",
    "iterative": "Iterative prompting"
}

def detect_prompt_type(content: str, tags: list) -> str:
    """Detect the most likely prompt type based on content and tags."""
    # Add logic to detect prompt type based on content patterns and tags
    if any("meta" in tag.lower() for tag in tags):
        return PROMPT_TYPES["meta"]
    if "<step" in content or "step by step" in content.lower():
        return PROMPT_TYPES["chain-of-thought"]
    if "<role" in content or "you are a" in content.lower():
        return PROMPT_TYPES["role"]
    if "<example" in content and "example" in content.lower():
        return PROMPT_TYPES["few-shot"]
    # Add more detection rules
    return PROMPT_TYPES["instruction"]  # default

def update_frontmatter(file_path: str) -> None:
    """Update frontmatter of a markdown file to include prompt_type."""
    with open(file_path, 'r') as f:
        content = f.read()

    # Find frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not frontmatter_match:
        return

    # Parse frontmatter
    frontmatter = yaml.safe_load(frontmatter_match.group(1))
    if not isinstance(frontmatter, dict):
        frontmatter = {}

    # Skip if prompt_type already exists
    if 'prompt_type' in frontmatter:
        return

    # Detect prompt type
    prompt_type = detect_prompt_type(content, frontmatter.get('tags', []))
    frontmatter['prompt_type'] = prompt_type

    # Write back
    new_content = f"---\n{yaml.dump(frontmatter, allow_unicode=True)}---\n{frontmatter_match.group(2)}"
    with open(file_path, 'w') as f:
        f.write(new_content)

def main():
    """Process all markdown files in the prompts directory."""
    prompts_dir = "prompts"
    for root, _, files in os.walk(prompts_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                update_frontmatter(file_path)

if __name__ == "__main__":
    main() 