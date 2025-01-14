#!/bin/bash

# Root directory path
directory="$(pwd)/./prompts"

# Output file path
output_file="directory_structure.md"

# Function to generate the directory structure
generate_structure() {
  local dir_path="$1"
  local indent="$2"
  local rel_path="$3"

  # Loop through sorted directory entries
  find "$dir_path" -maxdepth 1 -mindepth 1 -printf "%f\n" | sort | while read -r entry; do
    local entry_path="$dir_path/$entry"
    local entry_rel_path="${rel_path:+$rel_path/}$entry"
    
    if [ -d "$entry_path" ]; then
      # Recursively process subdirectory
      generate_structure "$entry_path" "" "$entry_rel_path"
    else
      # File - add path with checkbox
      echo "- [ ] ${entry_rel_path}" >> "$output_file"
    fi
  done
}

# Create empty output file
> "$output_file"

# Generate the directory structure
generate_structure "$directory" "" ""

echo "✓ Directory structure saved to '$output_file'"
