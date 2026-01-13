#!/usr/bin/env python3
"""
Image fetcher for TopSoloTravel
Uses free, copyright-free image sources:
- Unsplash Source (deprecated but still works for placeholders)
- Pexels API (requires API key)
- Picsum (Lorem Picsum - completely free)
- Direct Unsplash URLs with proper attribution
"""

import os
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# Configuration
IMAGES_DIR = Path(__file__).parent.parent / "static" / "images"
DATA_DIR = Path(__file__).parent.parent / "data"

# Unsplash collection IDs for travel photos (public collections)
TRAVEL_COLLECTIONS = {
    "travel": "travel",
    "nature": "nature",
    "city": "city",
    "beach": "beach",
    "mountain": "mountains",
    "food": "food",
    "architecture": "architecture",
}

# Country-specific search terms for better images
COUNTRY_SEARCH_TERMS = {
    "japan": "japan temple tokyo",
    "thailand": "thailand temple bangkok",
    "portugal": "lisbon portugal",
    "spain": "spain barcelona",
    "italy": "italy rome venice",
    "france": "paris france eiffel",
    "germany": "germany berlin",
    "united kingdom": "london uk",
    "united states": "new york usa",
    "australia": "sydney australia",
    "new zealand": "new zealand landscape",
    "canada": "canada mountains",
    "brazil": "brazil rio",
    "mexico": "mexico city",
    "india": "india taj mahal",
    "china": "china great wall",
    "south korea": "seoul korea",
    "vietnam": "vietnam hanoi",
    "indonesia": "bali indonesia",
    "singapore": "singapore",
    "malaysia": "kuala lumpur malaysia",
    "philippines": "philippines beach",
    "greece": "greece santorini",
    "turkey": "istanbul turkey",
    "egypt": "egypt pyramids",
    "morocco": "morocco marrakech",
    "south africa": "cape town south africa",
    "kenya": "kenya safari",
    "tanzania": "tanzania serengeti",
    "peru": "peru machu picchu",
    "argentina": "buenos aires argentina",
    "chile": "chile patagonia",
    "colombia": "colombia cartagena",
    "costa rica": "costa rica rainforest",
    "iceland": "iceland northern lights",
    "norway": "norway fjords",
    "sweden": "stockholm sweden",
    "netherlands": "amsterdam netherlands",
    "switzerland": "switzerland alps",
    "austria": "vienna austria",
    "czech republic": "prague czech",
    "poland": "krakow poland",
    "croatia": "croatia dubrovnik",
    "ireland": "ireland dublin",
    "scotland": "scotland highlands",
}

def get_unsplash_url(query: str, width: int = 1200, height: int = 800) -> str:
    """Generate Unsplash Source URL for a search query."""
    # Using Unsplash Source API (free, no key required)
    query_formatted = query.replace(" ", ",")
    return f"https://source.unsplash.com/{width}x{height}/?{query_formatted}"

def get_picsum_url(width: int = 1200, height: int = 800, seed: str = None) -> str:
    """Generate Lorem Picsum URL (completely free)."""
    if seed:
        return f"https://picsum.photos/seed/{seed}/{width}/{height}"
    return f"https://picsum.photos/{width}/{height}"

def get_image_url_for_destination(name: str, type: str = "country") -> dict:
    """Get image URL for a destination."""
    name_lower = name.lower()

    # Get search term
    search_term = COUNTRY_SEARCH_TERMS.get(name_lower, f"{name} travel landscape")

    return {
        "hero": get_unsplash_url(search_term, 1920, 1080),
        "card": get_unsplash_url(search_term, 800, 600),
        "thumb": get_unsplash_url(search_term, 400, 300),
        "search_term": search_term,
        "attribution": "Photo from Unsplash"
    }

def generate_image_data(countries: list) -> dict:
    """Generate image URLs for all countries."""
    image_data = {}

    for country in countries:
        name = country.get("name", {}).get("common", country.get("name", ""))
        if isinstance(name, dict):
            name = name.get("common", "unknown")

        image_data[name.lower().replace(" ", "-")] = get_image_url_for_destination(name)

    return image_data

def create_placeholder_images():
    """Create placeholder image configuration."""
    # Create directories
    for subdir in ["destinations", "cities", "safety", "eat", "stay", "hero"]:
        (IMAGES_DIR / subdir).mkdir(parents=True, exist_ok=True)

    # Create a JSON file with image URLs for Hugo to use
    image_config = {
        "default_hero": get_picsum_url(1920, 1080, "hero"),
        "default_destination": get_picsum_url(1200, 800, "travel"),
        "default_city": get_picsum_url(1200, 800, "city"),
        "default_safety": get_picsum_url(1200, 800, "safety"),
        "categories": {
            "destinations": get_unsplash_url("travel landscape", 1200, 800),
            "safety": get_unsplash_url("travel safety", 1200, 800),
            "eat": get_unsplash_url("restaurant food dining", 1200, 800),
            "stay": get_unsplash_url("hotel hostel accommodation", 1200, 800),
            "nightlife": get_unsplash_url("bar nightlife", 1200, 800),
            "cafes": get_unsplash_url("cafe coffee", 1200, 800),
        }
    }

    # Save configuration
    config_path = DATA_DIR / "images.json"
    with open(config_path, "w") as f:
        json.dump(image_config, f, indent=2)

    print(f"Created image configuration at {config_path}")
    return image_config

if __name__ == "__main__":
    create_placeholder_images()
    print("Image placeholder system created!")
