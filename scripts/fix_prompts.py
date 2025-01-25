#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
from pathlib import Path
import frontmatter
import re
from typing import Dict, Any, Optional

def extract_title_from_content(content: str) -> Optional[str]:
    """Extract title from the first heading in content."""
    if not content:
        return None
    
    # Try to find first markdown heading
    heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if heading_match:
        return heading_match.group(1).strip()
    
    # Try to find first line
    lines = content.strip().split('\n')
    if lines:
        return lines[0].strip()
    
    return None

def extract_tags_from_path(file_path: str) -> list:
    """Extract meaningful tags from file path."""
    parts = file_path.lower().replace('\\', '/').split('/')
    # Remove 'prompts' and file name
    parts = [p for p in parts[1:-1] if p not in ['prompts']]
    return parts

def infer_category_from_path(file_path: str) -> str:
    """Infer category from file path."""
    parts = file_path.lower().replace('\\', '/').split('/')
    if len(parts) > 1:
        main_category = parts[1].title()
        return main_category
    return "Geral"

def fix_version_type(version: Any) -> str:
    """Convert version to string format."""
    if isinstance(version, (int, float)):
        return str(version)
    if isinstance(version, str):
        return version
    return "1.0"

def fix_prompt_file(file_path: str) -> bool:
    """Fix a single prompt file format."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to load existing frontmatter
        post = frontmatter.loads(content)
        metadata = post.metadata if post.metadata else {}
        
        # Fix or add required fields
        if 'title' not in metadata or not metadata['title']:
            title = extract_title_from_content(post.content)
            metadata['title'] = title or os.path.basename(file_path).replace('.md', '').replace('-', ' ').title()
        
        if 'description' not in metadata or not metadata['description']:
            # Use first non-empty line after title as description
            lines = [l.strip() for l in post.content.split('\n') if l.strip()]
            desc_line = next((l for l in lines if not l.startswith('#')), '')
            metadata['description'] = desc_line[:100] if desc_line else f"Prompt para {metadata['title']}"
        
        if 'tags' not in metadata or not metadata['tags']:
            metadata['tags'] = extract_tags_from_path(file_path)
        
        if 'model' not in metadata or not metadata['model']:
            metadata['model'] = "GPT-4"  # Default model
        
        if 'category' not in metadata or not metadata['category']:
            metadata['category'] = infer_category_from_path(file_path)
        
        if 'version' not in metadata:
            metadata['version'] = "1.0"
        else:
            metadata['version'] = fix_version_type(metadata['version'])
        
        # Create new frontmatter post
        new_post = frontmatter.Post(post.content, **metadata)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(new_post))
        
        return True

    except Exception as e:
        print(f"Erro ao processar {file_path}: {str(e)}")
        return False

def main():
    """Main function to fix all prompts."""
    try:
        prompts_dir = Path('prompts')
        if not prompts_dir.exists():
            print(f"❌ Erro: Diretório {prompts_dir} não encontrado")
            sys.exit(1)

        files = glob.glob(str(prompts_dir / '**/*.md'), recursive=True)
        if not files:
            print("❌ Erro: Nenhum arquivo de prompt encontrado")
            sys.exit(1)

        print(f"\n🔧 Corrigindo {len(files)} arquivos de prompt...\n")
        
        success_count = 0
        error_count = 0
        
        for file_path in files:
            print(f"Processando: {os.path.relpath(file_path)}")
            if fix_prompt_file(file_path):
                success_count += 1
            else:
                error_count += 1
        
        print("\n📊 Relatório de Correção")
        print("=" * 50)
        print(f"Total de prompts: {len(files)}")
        print(f"✅ Corrigidos com sucesso: {success_count}")
        print(f"❌ Erros: {error_count}")
        
        if error_count > 0:
            sys.exit(1)
        
        print("\n✅ Todos os prompts foram processados!")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n❌ Erro durante o processo: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main() 