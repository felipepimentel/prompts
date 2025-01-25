#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
from pathlib import Path
import frontmatter
from typing import List, Dict, Optional

REQUIRED_FIELDS = {
    'title': str,
    'description': str,
    'tags': list,
    'model': str,
    'category': str,
    'version': str
}

class PromptValidator:
    def __init__(self):
        self.errors: Dict[str, List[str]] = {}
        self.warnings: Dict[str, List[str]] = {}
        self.valid_count = 0
        self.invalid_count = 0

    def validate_field_type(self, field: str, value: any, expected_type: type) -> bool:
        """Validate if a field has the correct type."""
        if field == 'tags' and expected_type == list:
            return isinstance(value, list) and all(isinstance(tag, str) for tag in value)
        return isinstance(value, expected_type)

    def validate_prompt_file(self, file_path: str) -> bool:
        """Validate a single prompt file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            file_errors = []
            file_warnings = []
            
            # Verificar campos obrigatórios
            for field, expected_type in REQUIRED_FIELDS.items():
                if field not in post.metadata:
                    file_errors.append(f"Campo obrigatório '{field}' não encontrado")
                elif not self.validate_field_type(field, post.metadata[field], expected_type):
                    file_errors.append(f"Campo '{field}' tem tipo inválido. Esperado: {expected_type.__name__}")

            # Verificar conteúdo
            if not post.content or not post.content.strip():
                file_errors.append("Conteúdo do prompt está vazio")
            
            # Verificações adicionais
            if 'tags' in post.metadata and len(post.metadata['tags']) == 0:
                file_warnings.append("Lista de tags está vazia")
            
            if 'description' in post.metadata and len(post.metadata['description']) < 10:
                file_warnings.append("Descrição muito curta (menos de 10 caracteres)")

            # Armazenar resultados
            if file_errors:
                self.errors[file_path] = file_errors
                self.invalid_count += 1
            else:
                self.valid_count += 1
            
            if file_warnings:
                self.warnings[file_path] = file_warnings

            return len(file_errors) == 0

        except Exception as e:
            self.errors[file_path] = [f"Erro ao processar arquivo: {str(e)}"]
            self.invalid_count += 1
            return False

    def find_and_validate_prompts(self) -> bool:
        """Find and validate all prompt files."""
        prompts_dir = Path('prompts')
        if not prompts_dir.exists():
            print(f"❌ Erro: Diretório {prompts_dir} não encontrado")
            return False

        files = glob.glob(str(prompts_dir / '**/*.md'), recursive=True)
        if not files:
            print("❌ Erro: Nenhum arquivo de prompt encontrado")
            return False

        print(f"\n🔍 Validando {len(files)} arquivos de prompt...\n")
        
        all_valid = True
        for file_path in files:
            is_valid = self.validate_prompt_file(file_path)
            all_valid = all_valid and is_valid

        return all_valid

    def print_report(self):
        """Print validation report."""
        print("\n📊 Relatório de Validação")
        print("=" * 50)
        print(f"Total de prompts: {self.valid_count + self.invalid_count}")
        print(f"✅ Prompts válidos: {self.valid_count}")
        print(f"❌ Prompts inválidos: {self.invalid_count}")
        
        if self.errors:
            print("\n❌ Erros encontrados:")
            print("-" * 50)
            for file_path, errors in self.errors.items():
                print(f"\n📄 {os.path.relpath(file_path)}")
                for error in errors:
                    print(f"  • {error}")
        
        if self.warnings:
            print("\n⚠️  Avisos:")
            print("-" * 50)
            for file_path, warnings in self.warnings.items():
                print(f"\n📄 {os.path.relpath(file_path)}")
                for warning in warnings:
                    print(f"  • {warning}")

def main():
    """Main function to run the validation."""
    try:
        validator = PromptValidator()
        all_valid = validator.find_and_validate_prompts()
        validator.print_report()
        
        if not all_valid:
            print("\n❌ Validação falhou! Corrija os erros acima.")
            sys.exit(1)
        else:
            print("\n✅ Todos os prompts são válidos!")
            if validator.warnings:
                print("⚠️  Há alguns avisos que podem ser revisados.")
            sys.exit(0)
    
    except Exception as e:
        print(f"\n❌ Erro durante a validação: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main() 