#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
import frontmatter
from typing import List, Dict, Optional, Set
import argparse
import fnmatch

class PromptSearcher:
    def __init__(self):
        self.prompts_dir = Path('prompts')
        if not self.prompts_dir.exists():
            print(f"Error: Directory {self.prompts_dir} does not exist")
            sys.exit(1)

    def find_prompt_files(self) -> List[Path]:
        """Find all prompt markdown files."""
        return list(self.prompts_dir.glob('**/*.md'))

    def matches_filename(self, filename: str, pattern: Optional[str]) -> bool:
        """Check if filename matches the search pattern."""
        if not pattern:
            return True
        return fnmatch.fnmatch(filename.lower(), f'*{pattern.lower()}*')

    def matches_tags(self, file_tags: List[str], search_tags: Optional[List[str]]) -> bool:
        """Check if file has all the specified tags."""
        if not search_tags:
            return True
        if not file_tags:
            return False
        return all(tag.lower() in [t.lower() for t in file_tags] for tag in search_tags)

    def matches_prompt_type(self, file_type: str, search_type: Optional[str]) -> bool:
        """Check if file matches the prompt type."""
        if not search_type:
            return True
        if not file_type:
            return False
        return search_type.lower() in file_type.lower()

    def matches_model(self, file_model: str, search_model: Optional[str]) -> bool:
        """Check if file matches the model."""
        if not search_model:
            return True
        if not file_model:
            return False
        return search_model.lower() in file_model.lower()

    def search_prompts(self, 
                      filename: Optional[str] = None,
                      tags: Optional[List[str]] = None,
                      prompt_type: Optional[str] = None,
                      model: Optional[str] = None) -> List[Dict]:
        """
        Search prompts with the given filters.
        Returns list of matching prompts with their metadata and paths.
        """
        results = []
        
        for file_path in self.find_prompt_files():
            try:
                # Check filename first (fastest check)
                if not self.matches_filename(file_path.name, filename):
                    continue

                # Read and check metadata
                with open(file_path, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                
                metadata = post.metadata if post.metadata else {}
                
                # Apply all filters
                if not self.matches_tags(metadata.get('tags', []), tags):
                    continue
                    
                if not self.matches_prompt_type(metadata.get('prompt_type', ''), prompt_type):
                    continue
                    
                if not self.matches_model(metadata.get('model', ''), model):
                    continue

                # If all filters pass, add to results
                result = {
                    'path': str(file_path.relative_to(self.prompts_dir)),
                    'title': metadata.get('title', file_path.stem),
                    'description': metadata.get('description', ''),
                    'tags': metadata.get('tags', []),
                    'prompt_type': metadata.get('prompt_type', ''),
                    'model': metadata.get('model', '')
                }
                results.append(result)

            except Exception as e:
                print(f"Error processing {file_path}: {e}", file=sys.stderr)
                continue

        return results

def main():
    parser = argparse.ArgumentParser(description='Search prompts with various filters')
    parser.add_argument('-n', '--name', help='Search by filename pattern')
    parser.add_argument('-t', '--tags', help='Search by tags (comma-separated)', type=lambda s: [t.strip() for t in s.split(',')])
    parser.add_argument('-p', '--prompt-type', help='Search by prompt type')
    parser.add_argument('-m', '--model', help='Search by model')
    parser.add_argument('-j', '--json', action='store_true', help='Output in JSON format')
    
    args = parser.parse_args()
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    searcher = PromptSearcher()
    results = searcher.search_prompts(
        filename=args.name,
        tags=args.tags,
        prompt_type=args.prompt_type,
        model=args.model
    )
    
    # Print results
    if args.json:
        import json
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(f"\nFound {len(results)} matching prompts:\n")
        for result in results:
            print(f"📄 {result['path']}")
            print(f"   Title: {result['title']}")
            print(f"   Type: {result['prompt_type']}")
            print(f"   Model: {result['model']}")
            print(f"   Tags: {', '.join(result['tags'])}")
            print()

if __name__ == '__main__':
    main() 