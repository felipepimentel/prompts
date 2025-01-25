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
    files = glob.glob(str(prompts_dir / '**/*.md'), recursive=True)
    print(f"Found {len(files)} prompt files")
    return files

def process_prompt_file(file_path):
    """Extract metadata and content from a prompt file."""
    try:
        print(f"Processing file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # Get file modification time for the date
        mtime = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(mtime).strftime('%d/%m/%Y')
        
        return {
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
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}", file=sys.stderr)
        return None

def generate_gallery_data():
    """Generate JSON data for the gallery."""
    print("Starting gallery data generation...")
    prompt_files = find_prompt_files()
    prompts = [process_prompt_file(f) for f in prompt_files]
    prompts = [p for p in prompts if p]  # Remove None values
    
    # Collect unique categories and models
    categories = sorted(set(p['category'] for p in prompts))
    models = sorted(set(p['model'] for p in prompts))
    
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
    
    print(f"Successfully generated gallery data with {len(prompts)} prompts")
    
    # Generate a sample prompt for local development
    sample_prompt = {
        'title': 'Análise de Código',
        'description': 'Prompt para análise detalhada de código fonte com foco em boas práticas, segurança e performance.',
        'tags': ['programação', 'código', 'análise'],
        'model': 'GPT-4',
        'category': 'Técnico',
        'type': 'Analysis',
        'version': '0.7',
        'date': '31/12/2023',
        'content': 'Por favor, analise este código fonte considerando os seguintes aspectos:\n\n1. Boas práticas de programação\n- Princípios SOLID\n- Clean Code'
    }
    
    # Save sample data for local development
    sample_data = {
        'categories': ['Geral', 'Criativo', 'Técnico', 'Acadêmico', 'Negócios', 'Marketing'],
        'models': ['GPT-3.5', 'GPT-4', 'Claude', 'Llama', 'Gemini'],
        'prompts': [sample_prompt]
    }
    
    sample_file = Path('docs/assets/data/sample.json')
    with open(sample_file, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
    print("Generated sample data for local development")

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