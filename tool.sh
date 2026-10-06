#!/bin/bash

# Bash File Analyzer
# This tool analyzes a file and displays basic information.

show_help() {
    echo "===== BASH FILE ANALYZER ====="
    echo "Purpose: Analyze a file and display basic information."
    echo ""
    echo "Usage:"
    echo "  ./tool.sh <file_path>"
    echo ""
    echo "Example:"
    echo "  ./tool.sh sample.txt"
}

analyze_file() {
    file_path="$1"

    # Check whether the file exists
    if [ ! -f "$file_path" ]; then
        echo "Error: File does not exist."
        return 1
    fi

    # Get file size
    file_size=$(wc -c < "$file_path")

    # Calculate SHA-256 hash
    file_hash=$(sha256sum "$file_path" | awk '{print $1}')

    # Detect file type
    file_type=$(file -b "$file_path")

    # Get last modified time
    modified_time=$(stat -c "%y" "$file_path")

    echo ""
    echo "===== FILE ANALYZER ====="
    echo "File: $file_path"
    echo "Size: $file_size bytes"
    echo "SHA-256: $file_hash"
    echo "Type: $file_type"
    echo "Modified: $modified_time"
}

if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    show_help
    exit 0
fi

if [ "$#" -ne 1 ]; then
    echo "Error: Please provide a file path."
    echo "Usage: ./tool.sh <file_path>"
    echo "Use --help for more information."
    exit 1
fi

analyze_file "$1"