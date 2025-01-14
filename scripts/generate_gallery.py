#!/usr/bin/env python3
import os
import yaml
import re
from pathlib import Path
from collections import Counter

def read_prompt_file(file_path):
    """Read and parse a prompt file."""
    print(f"Reading file: {file_path}")  # Debug log
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
        # Extract front matter
        if content.startswith('---'):
            try:
                # Split on first two occurrences of ---
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = yaml.safe_load(parts[1])
                    content = parts[2].strip()
                else:
                    print(f"Warning: Invalid front matter format in {file_path}")
                    front_matter = {}
            except yaml.YAMLError as e:
                print(f"Warning: Failed to parse YAML in {file_path}: {e}")
                front_matter = {}
        else:
            front_matter = {}
        
        print(f"Front matter found: {front_matter}")  # Debug log
        return front_matter, content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return {}, ""

def generate_prompt_card(title, description, template, tags, emoji='📝'):
    """Generate HTML for a prompt card."""
    card_id = re.sub(r'[^a-z0-9]', '-', title.lower())
    
    # Format template for better display
    template_lines = template.strip().split('\n')
    formatted_template = '\n'.join(line.strip() for line in template_lines)
    
    return f'''
  <div class="prompt-card" data-prompt-id="{card_id}" data-categories="{','.join(tags)}">
    <div class="prompt-header">
      <h3 class="prompt-title">{emoji} {title}</h3>
      <div class="prompt-tags">
        {' '.join(f'<span class="prompt-tag">{tag}</span>' for tag in tags)}
      </div>
    </div>

    <div class="prompt-content">
      <div class="prompt-description">{description}</div>
      <div class="prompt-template">
        <pre id="{card_id}-template">{formatted_template}</pre>
      </div>
    </div>

    <div class="prompt-actions">
      <button class="action-btn copy-btn" data-clipboard-target="#{card_id}-template">
        <span class="btn-icon">📋</span>
        <span class="btn-text">Copy</span>
      </button>
    </div>
  </div>'''

def find_prompt_files(base_dir):
    """Find all prompt files recursively."""
    prompt_files = []
    base_path = Path(base_dir)
    
    print(f"Scanning directory: {base_path} (absolute: {base_path.absolute()})")
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md') and not file in ['overview.md', 'README.md']:
                file_path = Path(root) / file
                print(f"Found prompt file: {file_path}")
                prompt_files.append(file_path)
    
    return prompt_files

def generate_gallery():
    """Generate the complete gallery page."""
    prompts_dir = Path('prompts')
    gallery_content = []
    all_categories = set()
    prompt_cards = []
    
    # Process all prompt files first to collect categories
    prompt_files = find_prompt_files(prompts_dir)
    print(f"Found {len(prompt_files)} prompt files")
    
    for prompt_file in prompt_files:
        front_matter, content = read_prompt_file(prompt_file)
        print(f"Processing {prompt_file}: {front_matter.get('title', 'No title')}")
        
        if not front_matter:
            print(f"Warning: No front matter found in {prompt_file}")
            continue
            
        title = front_matter.get('title', prompt_file.stem.replace('-', ' ').title())
        description = front_matter.get('description', '')
        tags = front_matter.get('tags', [])
        emoji = front_matter.get('emoji', '📝')
        template = front_matter.get('template', content)
        
        # Skip if no title or template
        if not title or not template:
            print(f"Warning: Skipping {prompt_file} - missing title or template")
            continue
        
        all_categories.update(tags)
        prompt_cards.append((title, description, template, tags, emoji))
    
    print(f"Total prompts found: {len(prompt_cards)}")
    print(f"Categories found: {all_categories}")
    
    # Generate the gallery page
    gallery_content = ['''# Prompt Gallery

<div class="gallery-header">
  <div class="search-container">
    <input type="text" class="prompt-search" placeholder="🔍 Search prompts...">
  </div>
</div>

<div class="prompt-gallery">''']
    
    # Add all prompt cards
    for card_data in sorted(prompt_cards, key=lambda x: x[0]):
        gallery_content.append(generate_prompt_card(*card_data))
    
    # Add pagination
    gallery_content.append('''</div>

<div class="pagination">
  <button class="page-btn" data-page="prev" disabled>← Previous</button>
  <span class="page-info">Page <span class="current-page">1</span> of <span class="total-pages">1</span></span>
  <button class="page-btn" data-page="next">Next →</button>
</div>''')
    
    # Write the gallery file
    output_file = 'docs/index.md'
    print(f"Writing gallery to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(gallery_content))
    print("Gallery generation complete")

if __name__ == '__main__':
    generate_gallery() 