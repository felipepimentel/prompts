#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
import frontmatter
from collections import defaultdict
from typing import Dict, Set, List
import json

def find_prompt_files() -> List[Path]:
    """Find all prompt markdown files in the prompts directory."""
    prompts_dir = Path('prompts')
    if not prompts_dir.exists():
        print(f"Error: Directory {prompts_dir} does not exist")
        sys.exit(1)
    
    return list(prompts_dir.glob('**/*.md'))

def get_directory_structure() -> List[str]:
    """Get all directories and subdirectories in prompts folder."""
    prompts_dir = Path('prompts')
    directories = []
    
    for path in prompts_dir.rglob('*'):
        if path.is_dir():
            rel_path = path.relative_to(prompts_dir)
            directories.append(str(rel_path))
    
    return sorted(directories)

def analyze_prompts() -> Dict:
    """Analyze all prompts and extract metadata."""
    files = find_prompt_files()
    
    # Initialize data structures
    models = set()
    prompt_types = set()
    tags = set()
    
    # Process each file
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                
                # Extract metadata if available
                if post.metadata:
                    if 'model' in post.metadata:
                        models.add(post.metadata['model'])
                    if 'prompt_type' in post.metadata:
                        prompt_types.add(post.metadata['prompt_type'])
                    if 'tags' in post.metadata and isinstance(post.metadata['tags'], list):
                        tags.update(post.metadata['tags'])
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    # Prepare final report
    report = {
        "directories": get_directory_structure(),
        "models": sorted(list(models)),
        "prompt_types": sorted(list(prompt_types)),
        "tags": sorted(list(tags))
    }
    
    return report

def save_report(report: Dict, output_file: str = "prompt_analysis.json"):
    """Save the analysis report to a file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Report saved to {output_file}")
    
    # Example: additional log entry in "analysis_log.txt"
    with open("analysis_log.txt", "a", encoding="utf-8") as logf:
        logf.write(
            f"[ANALYZE_PROMPTS] Generated report '{output_file}' with "
            f"{len(report.get('directories', []))} directories, "
            f"{len(report.get('models', []))} models, "
            f"{len(report.get('tags', []))} tags\n"
        )

def main():
    report = analyze_prompts()
    save_report(report)

if __name__ == '__main__':
    main() 