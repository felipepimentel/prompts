#!/usr/bin/env python3
import os
import yaml
import re
from pathlib import Path
from collections import Counter

def read_prompt_file(file_path):
    """Read and parse a prompt file."""
    print(f"Reading file: {file_path}")  # Debug log
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract front matter
    if content.startswith('---'):
        parts = content.split('---', 2)[1:]
        if len(parts) >= 2:
            front_matter = yaml.safe_load(parts[0])
            content = parts[1].strip()
        else:
            front_matter = {}
            content = content.strip()
    else:
        front_matter = {}
        content = content.strip()
    
    return front_matter, content

def generate_prompt_card(title, description, template, tags, emoji='📝'):
    """Generate HTML for a prompt card."""
    card_id = re.sub(r'[^a-z0-9]', '-', title.lower())
    
    return f'''
  <div class="prompt-card" data-prompt-id="{card_id}" data-categories="{','.join(tags)}">
    <div class="prompt-header">
      <h3 class="prompt-title">{emoji} {title}</h3>
    </div>

    <div class="prompt-tags">
      {' '.join(f'<span class="prompt-tag">{tag}</span>' for tag in tags)}
    </div>

    <div class="prompt-content">
      <div class="prompt-description">
        {description}
      </div>
      
      <div class="prompt-template">
        <pre id="{card_id}-template">{template}</pre>
      </div>
    </div>

    <div class="prompt-actions">
      <button class="action-btn copy-btn" data-clipboard-target="#{card_id}-template">
        <span class="btn-icon">📋</span>
        <span class="btn-text">Copy</span>
      </button>
    </div>
  </div>'''

def generate_category_filters(categories):
    """Generate HTML for category filter buttons."""
    buttons = ['<button class="filter-btn active" data-category="all">All Prompts</button>']
    for category in sorted(categories):
        buttons.append(f'<button class="filter-btn" data-category="{category.lower()}">{category}</button>')
    return '\n    '.join(buttons)

def generate_gallery():
    """Generate the complete gallery page."""
    prompts_dir = Path('docs/prompts')
    print(f"Scanning directory: {prompts_dir}")  # Debug log
    
    gallery_content = []
    all_categories = set()
    prompt_cards = []
    
    # Process all prompt files first to collect categories
    for prompt_file in prompts_dir.rglob('*.md'):
        if prompt_file.name == 'overview.md':
            continue
            
        front_matter, content = read_prompt_file(prompt_file)
        print(f"Processing {prompt_file}: {front_matter.get('title', 'No title')}")  # Debug log
        
        if not front_matter:
            continue
            
        title = front_matter.get('title', prompt_file.stem.replace('-', ' ').title())
        description = front_matter.get('description', '')
        tags = front_matter.get('tags', [])
        emoji = front_matter.get('emoji', '📝')
        template = front_matter.get('template', content)
        
        all_categories.update(tags)
        prompt_cards.append((title, description, template, tags, emoji))
    
    print(f"Total prompts found: {len(prompt_cards)}")  # Debug log
    print(f"Categories found: {all_categories}")  # Debug log
    
    # Header with search only
    gallery_content.append(f'''# Prompt Gallery

<div class="gallery-header">
  <div class="search-container">
    <input type="text" class="prompt-search" placeholder="🔍 Search prompts...">
  </div>
</div>

<div class="prompt-gallery">''')
    
    # Add all prompt cards
    for card_data in sorted(prompt_cards, key=lambda x: x[0]):  # Sort by title
        gallery_content.append(generate_prompt_card(*card_data))
    
    # Footer with pagination
    gallery_content.append('''</div>

<div class="pagination">
  <button class="page-btn" data-page="prev" disabled>← Previous</button>
  <span class="page-info">Page <span class="current-page">1</span> of <span class="total-pages">1</span></span>
  <button class="page-btn" data-page="next">Next →</button>
</div>''')
    
    # Write the gallery file
    output_file = 'docs/index.md'
    print(f"Writing gallery to: {output_file}")  # Debug log
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(gallery_content))
    print("Gallery generation complete")  # Debug log

if __name__ == '__main__':
    generate_gallery() 