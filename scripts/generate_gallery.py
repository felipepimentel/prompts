#!/usr/bin/env python3
import os
import yaml
import re
from pathlib import Path
from collections import Counter

def read_prompt_file(file_path):
    """Read and parse a prompt file."""
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
    gallery_content = []
    all_categories = set()
    prompt_cards = []
    
    # Process all prompt files first to collect categories
    for prompt_file in prompts_dir.rglob('*.md'):
        if prompt_file.name == 'overview.md':
            continue
            
        front_matter, content = read_prompt_file(prompt_file)
        
        if not front_matter:
            continue
            
        title = front_matter.get('title', prompt_file.stem.replace('-', ' ').title())
        description = front_matter.get('description', '')
        tags = front_matter.get('tags', [])
        emoji = front_matter.get('emoji', '📝')
        template = front_matter.get('template', content)
        
        all_categories.update(tags)
        prompt_cards.append((title, description, template, tags, emoji))
    
    # Header with dynamic categories
    gallery_content.append(f'''# Prompt Gallery

<div class="gallery-header">
  <div class="search-container">
    <input type="text" class="prompt-search" placeholder="🔍 Search prompts...">
  </div>
  
  <div class="category-filters">
    {generate_category_filters(all_categories)}
  </div>
</div>

<div class="prompt-gallery">''')
    
    # Add all prompt cards
    for card_data in sorted(prompt_cards, key=lambda x: x[0]):  # Sort by title
        gallery_content.append(generate_prompt_card(*card_data))
    
    # Footer
    gallery_content.append('''</div>

<div class="pagination">
  <button class="page-btn" data-page="prev" disabled>← Previous</button>
  <span class="page-info">Page <span class="current-page">1</span> of <span class="total-pages">1</span></span>
  <button class="page-btn" data-page="next">Next →</button>
</div>

<script>
// Initialize pagination
const itemsPerPage = 9;
const promptCards = document.querySelectorAll('.prompt-card');
const totalPages = Math.ceil(promptCards.length / itemsPerPage);
let currentPage = 1;

function showPage(page) {
  const start = (page - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  
  Array.from(promptCards).forEach((card, index) => {
    if (card.style.display !== 'none') {
      const shouldShow = index >= start && index < end;
      card.style.display = shouldShow ? 'flex' : 'none';
    }
  });
  
  document.querySelector('.current-page').textContent = page;
  document.querySelector('.total-pages').textContent = totalPages;
  
  // Update button states
  document.querySelector('[data-page="prev"]').disabled = page === 1;
  document.querySelector('[data-page="next"]').disabled = page === totalPages;
}

document.querySelectorAll('.page-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    if (btn.dataset.page === 'prev' && currentPage > 1) {
      currentPage--;
    } else if (btn.dataset.page === 'next' && currentPage < totalPages) {
      currentPage++;
    }
    showPage(currentPage);
  });
});

// Initialize first page
showPage(1);
</script>''')
    
    # Write the gallery file
    with open('docs/index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(gallery_content))

if __name__ == '__main__':
    generate_gallery() 