#!/usr/bin/env python3
"""
Find HTML files that don't have the new navigation
"""

from pathlib import Path

BASE_DIR = Path(r"C:\Users\dell\Documents\God digital marketing website 2")

def main():
    """Find files without has-dropdown class"""
    print("==> Finding files without new navigation...\n")

    failed_files = []

    # Find all HTML files
    html_files = list(BASE_DIR.rglob("*.html"))

    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Check if file has new navigation
            if 'has-dropdown' not in content:
                rel_path = file_path.relative_to(BASE_DIR)
                failed_files.append(str(rel_path))
                print(f"[MISSING NAV] {rel_path}")
        except Exception as e:
            rel_path = file_path.relative_to(BASE_DIR)
            print(f"[ERROR] {rel_path}: {str(e)}")

    print(f"\n{'='*60}")
    print(f"Total files missing navigation: {len(failed_files)}")
    print(f"{'='*60}")

    # Print list for easy copying
    if failed_files:
        print("\nFiles to fix:")
        for f in failed_files:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
