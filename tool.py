import os
import sys
import hashlib
import mimetypes
from datetime import datetime


def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def analyze_file(file_path):
    """Analyze a file and display its basic information."""

    # Check whether the file exists
    if not os.path.isfile(file_path):
        print("Error: File does not exist.")
        return

    # Get file information
    file_size = os.path.getsize(file_path)
    file_hash = calculate_sha256(file_path)

    # Detect file type
    file_type = mimetypes.guess_type(file_path)[0] or "Unknown"

    # Get last modified time
    modified_time = datetime.fromtimestamp(
        os.path.getmtime(file_path)
    ).strftime("%Y-%m-%d %H:%M:%S")

    # Display file information
    print("\n===== FILE ANALYZER =====")
    print(f"File: {file_path}")
    print(f"Size: {file_size} bytes")
    print(f"SHA-256: {file_hash}")
    print(f"Type: {file_type}")
    print(f"Modified: {modified_time}")


def show_help():
    """Display help information."""

    print("\n===== FILE ANALYZER HELP =====")
    print("Purpose: Analyze a file and display basic information.")
    print("\nUsage:")
    print("  python tool.py <file_path>")

    print("\nExample:")
    print("  python tool.py sample.txt")


def main():
    """Main function of the program."""

    # Show help option
    if len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help"]:
        show_help()
        return

    # Check command-line argument
    if len(sys.argv) != 2:
        print("Error: Please provide a file path.")
        print("Usage: python tool.py <file_path>")
        print("Use --help for more information.")
        return

    # Analyze the selected file
    analyze_file(sys.argv[1])


if __name__ == "__main__":
    main()