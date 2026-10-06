# Python File Analyzer

## Objective
This tool analyzes a file and displays useful information about it.

## Features
- Checks whether the file exists
- Displays file size
- Calculates SHA-256 hash
- Detects file type
- Displays last modified time
- Handles invalid file path
- Provides a help option

## Requirements
- Python 3.x
- No external libraries are required

## How to Run

Run the following command:

    python tool.py <file_path>

Example:

    python tool.py sample.txt

For help:

    python tool.py --help

## Example Output

    ===== FILE ANALYZER =====
    File: sample.txt
    Size: 25 bytes
    SHA-256: [SHA-256 hash]
    Type: text/plain
    Modified: 2026-09-27 15:00:00

## Error Handling

If the file does not exist, the tool displays:

    Error: File does not exist.

## Future Improvements
- Add more file metadata
- Compare file hashes
- Add batch file analysis
- Export results to a report

## Author
IqaSec Academy Internship - Phase 1