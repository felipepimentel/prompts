#!/usr/bin/env python3

import os
import argparse
from pathlib import Path


def normalize_filename(filepath: Path) -> None:
    """
    Normalize a filename by converting hyphens to underscores.
    Following the prompts directory convention:
    - Directories use hyphens (example: content-creation)
    - Files use underscores (example: context_to_blog_converter.md)
    
    If the normalized filename already exists, it will skip the renaming.
    """
    # Skip directories - they should keep hyphens
    if filepath.is_dir():
        return

    if '-' not in filepath.name:
        return

    new_name = filepath.name.replace('-', '_')
    new_path = filepath.parent / new_name
    
    if new_path.exists():
        print(f"Skipping {filepath} - {new_path} already exists")
        return
        
    filepath.rename(new_path)
    print(f"Renamed: {filepath} -> {new_path}")


def normalize_directory(directory: Path, recursive: bool = True) -> None:
    """
    Normalize all filenames in the given directory following the prompts convention:
    - Directories: use hyphens (example: content-creation)
    - Files: use underscores (example: context_to_blog_converter.md)
    
    If recursive is True, it will also process subdirectories.
    """
    if recursive:
        for item in directory.rglob("*"):
            if item.is_file():  # Only normalize files, keep directory names with hyphens
                normalize_filename(item)
    else:
        for item in directory.iterdir():
            if item.is_file():  # Only normalize files, keep directory names with hyphens
                normalize_filename(item)


def main():
    parser = argparse.ArgumentParser(
        description="""
        Normalize filenames following the prompts directory convention:
        - Directories use hyphens (example: content-creation)
        - Files use underscores (example: context_to_blog_converter.md)
        """
    )
    parser.add_argument("directory", type=str, help="Directory to process")
    parser.add_argument("--no-recursive", action="store_true", help="Don't process subdirectories")
    
    args = parser.parse_args()
    directory = Path(args.directory)
    
    if not directory.exists() or not directory.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return
    
    normalize_directory(directory, recursive=not args.no_recursive)


if __name__ == "__main__":
    main() 