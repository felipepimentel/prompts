#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import frontmatter
import glob
from pathlib import Path
import html

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
        
        # Get relative path without extension for URL
        url_path = str(Path(file_path)).replace('.md', '')
        if url_path.startswith('prompts/'):
            url_path = url_path[8:]  # Remove 'prompts/' prefix
            
        # Escape content for HTML and JavaScript
        content = post.content.strip()
        content = html.escape(content, quote=True)
        content = content.replace('\n', '\\n')
        
        # Ensure all values are strings
        return {
            'title': str(post.get('title', 'Untitled')),
            'description': html.escape(str(post.get('description', '')), quote=True),
            'tags': post.get('tags', []),
            'model': str(post.get('model', 'GPT-4')),
            'category': str(post.get('category', 'Misc')),
            'type': str(post.get('type', 'General')),
            'version': str(post.get('version', '1.0')),
            'url': url_path,
            'content': content
        }
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}", file=sys.stderr)
        return None

def generate_gallery_page():
    """Generate the gallery page HTML."""
    print("Starting gallery generation...")
    prompt_files = find_prompt_files()
    prompts = [process_prompt_file(f) for f in prompt_files]
    prompts = [p for p in prompts if p]  # Remove None values
    print(f"Successfully processed {len(prompts)} prompts")
    
    # Collect unique categories and models for filters
    categories = sorted(set(p['category'] for p in prompts))
    models = sorted(set(p['model'] for p in prompts))
    print(f"Found categories: {categories}")
    print(f"Found models: {models}")
    
    # Generate filter buttons
    filter_buttons = '''
        <div class="filter-section">
            <button class="filter-btn active" data-filter="all">All</button>
            {}
            {}
        </div>
    '''.format(
        '\n'.join(f'<button class="filter-btn" data-filter="category-{html.escape(cat.lower())}">{html.escape(cat)}</button>' for cat in categories),
        '\n'.join(f'<button class="filter-btn" data-filter="model-{html.escape(model.lower())}">{html.escape(model)}</button>' for model in models)
    )
    
    cards_html = []
    for prompt in prompts:
        tags_html = ''.join([
            f'<span class="prompt-tag">{html.escape(tag)}</span>'
            for tag in prompt['tags']
        ])
        
        # Add data attributes for filtering
        data_attrs = f'''data-category="{html.escape(prompt['category'].lower())}" 
                        data-model="{html.escape(prompt['model'].lower())}"
                        data-type="{html.escape(prompt['type'].lower())}"'''
        
        card_html = f'''
        <div class="prompt-card" {data_attrs}>
            <div class="prompt-header">
                <h3 class="prompt-title">{html.escape(prompt['title'])}</h3>
                <div class="prompt-tags">
                    {tags_html}
                </div>
                <p class="prompt-description">{prompt['description']}</p>
            </div>

            <div class="prompt-details">
                <div class="prompt-detail-item">
                    <span class="prompt-detail-label">Model:</span>
                    <span class="prompt-detail-value">{html.escape(prompt['model'])}</span>
                </div>
                <div class="prompt-detail-item">
                    <span class="prompt-detail-label">Category:</span>
                    <span class="prompt-detail-value">{html.escape(prompt['category'])}</span>
                </div>
                <div class="prompt-detail-item">
                    <span class="prompt-detail-label">Type:</span>
                    <span class="prompt-detail-value">{html.escape(prompt['type'])}</span>
                </div>
                <div class="prompt-detail-item">
                    <span class="prompt-detail-label">Version:</span>
                    <span class="prompt-detail-value">{html.escape(prompt['version'])}</span>
                </div>
            </div>

            <div class="prompt-content">
                <div class="prompt-text">{prompt['content']}</div>
                <button class="copy-button" title="Copy prompt">
                    <span class="material-icons">content_copy</span>
                </button>
            </div>
        </div>'''
        cards_html.append(card_html)
    
    template = '''---
title: Prompt Engineering Collection
description: A curated collection of high-quality prompts for various use cases, organized by category and optimized for different AI models.
---

<head>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>

<div class="gallery-header">
  <p>A curated collection of high-quality prompts for various use cases, organized by category and optimized for different AI models.</p>
  
  <div class="search-container">
    <input type="text" class="prompt-search" placeholder="Search prompts..." aria-label="Search prompts">
  </div>
</div>

{filters}

<div class="prompt-gallery">
{cards}
</div>'''.format(filters=filter_buttons, cards='\n'.join(cards_html))
    
    output_file = Path('docs/index.md')
    print(f"Writing output to {output_file}")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)
    print("Gallery generation completed successfully")

def main():
    """Main function to generate the gallery."""
    try:
        print("Starting gallery generation process...")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Python version: {sys.version}")
        generate_gallery_page()
        print("Gallery generation completed successfully!")
    except Exception as e:
        print(f"Error during gallery generation: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main() 