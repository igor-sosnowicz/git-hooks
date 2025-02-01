#!/bin/bash

SCRIPT_NAME=$(basename "$0")
SCRIPT_DIR="hooks/$SCRIPT_NAME"

# Check if the directory exists
if [[ -d "$SCRIPT_DIR" ]]; then
    # Loop through all script files in the directory
    for script in "$SCRIPT_DIR"/*; do
        # Check if the file is executable
        if [[ -x "$script" ]]; then
            script_name=$(basename "$script")
            echo "Running script: $script_name"
            "$script"  # Execute the script
        else
            echo "Skipping non-executable script: $script"
        fi
    done
else
    echo "Skipping $SCRIPT_DIR: directory not found."
fi
