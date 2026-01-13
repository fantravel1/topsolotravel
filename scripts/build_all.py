#!/usr/bin/env python3
"""
Master build script for TopSoloTravel.
Fetches data from APIs and generates all content.
"""

import os
import sys
from pathlib import Path

# Add scripts directory to path
SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

def main():
    """Run all build steps."""
    print("=" * 60)
    print("TopSoloTravel Content Build")
    print("=" * 60)

    # Step 1: Fetch country data
    print("\n[1/4] Fetching country data...")
    try:
        from fetch_countries import main as fetch_countries
        fetch_countries()
    except Exception as e:
        print(f"Error fetching countries: {e}")

    # Step 2: Process city data
    print("\n[2/4] Processing city data...")
    try:
        from fetch_cities import main as fetch_cities
        fetch_cities()
    except Exception as e:
        print(f"Error processing cities: {e}")

    # Step 3: Create image placeholders
    print("\n[3/4] Setting up image system...")
    try:
        from fetch_images import create_placeholder_images
        create_placeholder_images()
    except Exception as e:
        print(f"Error setting up images: {e}")

    # Step 4: Generate content
    print("\n[4/4] Generating Hugo content...")
    try:
        from generate_content import generate_all_content
        generate_all_content()
    except Exception as e:
        print(f"Error generating content: {e}")

    print("\n" + "=" * 60)
    print("Build complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Run 'hugo server' to preview locally")
    print("2. Run 'hugo --minify' to build for production")
    print("3. Deploy to GitHub Pages")


if __name__ == "__main__":
    main()
