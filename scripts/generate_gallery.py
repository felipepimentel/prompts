#!/usr/bin/env python3
import os
import frontmatter
import glob
from pathlib import Path
import html

def find_prompt_files():
    """Find all prompt markdown files in the prompts directory."""
    prompts_dir = Path('prompts')
    return glob.glob(str(prompts_dir / '**/*.md'), recursive=True)

def process_prompt_file(file_path):
    """Extract metadata and content from a prompt file."""
    try:
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
        
        return {
            'title': post.get('title', 'Untitled'),
            'description': html.escape(post.get('description', ''), quote=True),
            'tags': post.get('tags', []),
            'model': post.get('model', 'GPT-4'),
            'category': post.get('category', 'Misc'),
            'type': post.get('type', 'General'),
            'version': post.get('version', '1.0'),
            'url': url_path,
            'content': content
        }
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        return None

def generate_gallery_page():
    """Generate the gallery page HTML."""
    prompt_files = find_prompt_files()
    prompts = [process_prompt_file(f) for f in prompt_files]
    prompts = [p for p in prompts if p]  # Remove None values
    
    # Collect unique categories and models for filters
    categories = sorted(set(p['category'] for p in prompts))
    models = sorted(set(p['model'] for p in prompts))
    
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
    
    with open('docs/index.md', 'w', encoding='utf-8') as f:
        f.write(template)

def main():
    """Main function to generate the gallery."""
    print("Finding prompt files...")
    prompt_files = find_prompt_files()
    print(f"Found {len(prompt_files)} prompt files")
    
    print("Generating gallery...")
    generate_gallery_page()
    print("Gallery generated successfully!")

if __name__ == '__main__':
    main() 