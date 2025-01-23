#!/bin/bash

# Install required Python packages
pip install pyyaml

# Make the Python script executable
chmod +x scripts/add_prompt_type.py

# Run the classification script
python3 scripts/add_prompt_type.py

# Git add all changes
git add prompts/**/*.md

echo "Classification complete! Please review the changes before committing." 