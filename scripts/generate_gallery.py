#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import frontmatter
import glob
from pathlib import Path
import html
from datetime import datetime

def find_prompt_files():
    """Find all prompt markdown files in the prompts directory."""
    print("Starting to find prompt files...")
    prompts_dir = Path('prompts')
    if not prompts_dir.exists():
        print(f"Error: Directory {prompts_dir} does not exist")
        sys.exit(1)
    
    print(f"Searching in {prompts_dir.absolute()}")
    files = glob.glob(str(prompts_dir / '**/*.md'), recursive=True)
    print(f"Found {len(files)} prompt files")
    for file in files:
        print(f"Found file: {file}")
    return files

def process_prompt_file(file_path):
    """Extract metadata and content from a prompt file."""
    try:
        print(f"\nProcessing file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"File content length: {len(content)} bytes")
            if not content.strip():
                print(f"Warning: Empty file {file_path}")
                return None
            
            if not content.startswith('---'):
                print(f"Warning: File {file_path} does not have frontmatter")
                return None
                
            post = frontmatter.loads(content)
            if not post.metadata:
                print(f"Warning: No metadata found in {file_path}")
                return None
        
        # Get file modification time for the date
        mtime = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(mtime).strftime('%d/%m/%Y')
        
        # Validate required fields
        required_fields = ['title', 'description', 'category', 'model']
        missing_fields = [field for field in required_fields if not post.get(field)]
        if missing_fields:
            print(f"Warning: Missing required fields in {file_path}: {missing_fields}")
            return None
        
        prompt_data = {
            'title': str(post.get('title', 'Untitled')),
            'description': str(post.get('description', '')),
            'tags': post.get('tags', []),
            'model': str(post.get('model', 'GPT-4')),
            'category': str(post.get('category', 'Geral')),
            'type': str(post.get('type', 'General')),
            'version': str(post.get('version', '1.0')),
            'date': date,
            'content': post.content.strip()
        }
        
        print(f"Successfully processed {file_path}")
        return prompt_data
        
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}", file=sys.stderr)
        return None

def generate_gallery_data():
    """Generate JSON data for the gallery."""
    print("\nStarting gallery data generation...")
    prompt_files = find_prompt_files()
    
    if not prompt_files:
        print("No prompt files found!")
        return
    
    prompts = []
    for file in prompt_files:
        result = process_prompt_file(file)
        if result:
            prompts.append(result)
    
    print(f"\nSuccessfully processed {len(prompts)} out of {len(prompt_files)} files")
    
    if not prompts:
        print("Warning: No valid prompts found!")
        return
    
    # Collect unique categories and models
    categories = sorted(set(p['category'] for p in prompts))
    models = sorted(set(p['model'] for p in prompts))
    
    print(f"\nFound categories: {categories}")
    print(f"Found models: {models}")
    
    gallery_data = {
        'categories': categories,
        'models': models,
        'prompts': prompts
    }
    
    # Save to JSON file
    output_file = Path('docs/assets/data/gallery.json')
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(gallery_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nSuccessfully generated gallery data with {len(prompts)} prompts")
    print(f"Output file: {output_file.absolute()}")

def main():
    """Main function to generate the gallery data."""
    try:
        print("Starting gallery data generation process...")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Python version: {sys.version}")
        generate_gallery_data()
        print("Gallery data generation completed successfully!")
    except Exception as e:
        print(f"Error during gallery data generation: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main() 