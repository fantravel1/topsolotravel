#!/usr/bin/env python3
"""
Fetch country data from RestCountries API
https://restcountries.com - Free, unlimited, no API key required
"""

import json
import urllib.request
import urllib.error
import time
from pathlib import Path
from typing import Optional

# Configuration
DATA_DIR = Path(__file__).parent.parent / "data"
RESTCOUNTRIES_API = "https://restcountries.com/v3.1/all"

# Region mapping for our site structure
REGION_MAPPING = {
    "Africa": "africa",
    "Americas": "americas",
    "Antarctic": "antarctica",
    "Asia": "asia",
    "Europe": "europe",
    "Oceania": "oceania",
}

# Solo travel safety ratings (curated data)
SAFETY_RATINGS = {
    # Very Safe
    "japan": "safe", "iceland": "safe", "switzerland": "safe", "singapore": "safe",
    "norway": "safe", "denmark": "safe", "finland": "safe", "new zealand": "safe",
    "portugal": "safe", "austria": "safe", "ireland": "safe", "netherlands": "safe",
    "canada": "safe", "australia": "safe", "slovenia": "safe", "czechia": "safe",
    "taiwan": "safe", "south korea": "safe", "united arab emirates": "safe",
    "qatar": "safe", "oman": "safe", "bahrain": "safe", "estonia": "safe",
    "croatia": "safe", "poland": "safe", "slovakia": "safe", "hungary": "safe",
    "spain": "safe", "germany": "safe", "belgium": "safe", "luxembourg": "safe",
    "sweden": "safe", "malta": "safe", "cyprus": "safe", "monaco": "safe",
    "liechtenstein": "safe", "san marino": "safe", "andorra": "safe",

    # Caution
    "thailand": "caution", "vietnam": "caution", "indonesia": "caution",
    "malaysia": "caution", "philippines": "caution", "india": "caution",
    "sri lanka": "caution", "nepal": "caution", "cambodia": "caution",
    "laos": "caution", "myanmar": "caution", "china": "caution",
    "mexico": "caution", "brazil": "caution", "argentina": "caution",
    "chile": "caution", "peru": "caution", "ecuador": "caution",
    "costa rica": "caution", "panama": "caution", "guatemala": "caution",
    "morocco": "caution", "egypt": "caution", "jordan": "caution",
    "turkey": "caution", "greece": "caution", "italy": "caution",
    "france": "caution", "united kingdom": "caution", "united states": "caution",
    "south africa": "caution", "tanzania": "caution", "kenya": "caution",
    "rwanda": "caution", "botswana": "caution", "namibia": "caution",
    "ghana": "caution", "senegal": "caution", "ethiopia": "caution",

    # Warning
    "colombia": "warning", "bolivia": "caution", "honduras": "warning",
    "el salvador": "warning", "nicaragua": "warning", "jamaica": "warning",
    "dominican republic": "caution", "haiti": "danger", "venezuela": "danger",
    "pakistan": "warning", "bangladesh": "caution", "nigeria": "warning",
    "russia": "warning", "ukraine": "danger", "belarus": "warning",
    "iran": "warning", "iraq": "danger", "syria": "danger",
    "afghanistan": "danger", "yemen": "danger", "somalia": "danger",
    "libya": "danger", "sudan": "danger", "south sudan": "danger",
}

# Budget estimates (USD per day)
BUDGET_ESTIMATES = {
    # Very cheap ($20-40/day)
    "vietnam": {"budget": "20-30", "midrange": "40-60", "luxury": "100+"},
    "cambodia": {"budget": "20-30", "midrange": "40-60", "luxury": "80+"},
    "laos": {"budget": "20-30", "midrange": "35-50", "luxury": "70+"},
    "nepal": {"budget": "20-30", "midrange": "40-60", "luxury": "100+"},
    "india": {"budget": "20-35", "midrange": "40-70", "luxury": "120+"},
    "indonesia": {"budget": "25-35", "midrange": "50-80", "luxury": "150+"},
    "philippines": {"budget": "25-40", "midrange": "50-80", "luxury": "120+"},
    "bolivia": {"budget": "25-35", "midrange": "45-70", "luxury": "100+"},
    "guatemala": {"budget": "30-40", "midrange": "50-80", "luxury": "120+"},
    "egypt": {"budget": "25-40", "midrange": "50-80", "luxury": "150+"},
    "morocco": {"budget": "30-45", "midrange": "60-90", "luxury": "150+"},

    # Cheap ($30-60/day)
    "thailand": {"budget": "30-45", "midrange": "60-100", "luxury": "200+"},
    "malaysia": {"budget": "35-50", "midrange": "60-100", "luxury": "180+"},
    "mexico": {"budget": "35-50", "midrange": "70-120", "luxury": "200+"},
    "peru": {"budget": "35-50", "midrange": "70-110", "luxury": "180+"},
    "colombia": {"budget": "35-50", "midrange": "60-100", "luxury": "150+"},
    "ecuador": {"budget": "35-50", "midrange": "60-90", "luxury": "140+"},
    "costa rica": {"budget": "45-60", "midrange": "80-130", "luxury": "200+"},
    "turkey": {"budget": "35-50", "midrange": "70-120", "luxury": "200+"},
    "greece": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"},
    "portugal": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"},

    # Moderate ($60-100/day)
    "spain": {"budget": "60-80", "midrange": "100-160", "luxury": "300+"},
    "italy": {"budget": "70-90", "midrange": "120-180", "luxury": "350+"},
    "france": {"budget": "80-100", "midrange": "140-200", "luxury": "400+"},
    "germany": {"budget": "70-90", "midrange": "110-170", "luxury": "300+"},
    "japan": {"budget": "70-100", "midrange": "120-180", "luxury": "350+"},
    "south korea": {"budget": "60-80", "midrange": "100-150", "luxury": "280+"},
    "taiwan": {"budget": "50-70", "midrange": "80-130", "luxury": "220+"},
    "united kingdom": {"budget": "80-110", "midrange": "150-220", "luxury": "400+"},
    "ireland": {"budget": "70-100", "midrange": "130-190", "luxury": "350+"},
    "netherlands": {"budget": "80-100", "midrange": "130-190", "luxury": "350+"},
    "belgium": {"budget": "70-90", "midrange": "120-180", "luxury": "320+"},
    "austria": {"budget": "70-90", "midrange": "120-180", "luxury": "320+"},
    "czech republic": {"budget": "50-70", "midrange": "90-140", "luxury": "250+"},
    "poland": {"budget": "40-60", "midrange": "70-120", "luxury": "200+"},
    "hungary": {"budget": "45-65", "midrange": "80-130", "luxury": "220+"},
    "croatia": {"budget": "55-75", "midrange": "100-150", "luxury": "280+"},

    # Expensive ($100-150/day)
    "united states": {"budget": "90-120", "midrange": "160-250", "luxury": "450+"},
    "canada": {"budget": "80-110", "midrange": "140-220", "luxury": "400+"},
    "australia": {"budget": "90-120", "midrange": "150-230", "luxury": "400+"},
    "new zealand": {"budget": "85-115", "midrange": "150-220", "luxury": "380+"},
    "singapore": {"budget": "80-110", "midrange": "140-220", "luxury": "400+"},
    "israel": {"budget": "90-120", "midrange": "160-240", "luxury": "420+"},
    "united arab emirates": {"budget": "100-140", "midrange": "180-280", "luxury": "500+"},

    # Very Expensive ($150+/day)
    "switzerland": {"budget": "120-160", "midrange": "200-300", "luxury": "550+"},
    "norway": {"budget": "110-150", "midrange": "180-280", "luxury": "500+"},
    "sweden": {"budget": "100-140", "midrange": "170-260", "luxury": "450+"},
    "denmark": {"budget": "100-140", "midrange": "170-260", "luxury": "450+"},
    "finland": {"budget": "100-140", "midrange": "170-250", "luxury": "420+"},
    "iceland": {"budget": "130-170", "midrange": "220-320", "luxury": "550+"},
}

# Best time to visit
BEST_TIMES = {
    "japan": "Mar-May, Oct-Nov",
    "thailand": "Nov-Feb",
    "vietnam": "Feb-Apr, Aug-Oct",
    "indonesia": "Apr-Oct",
    "malaysia": "Year-round",
    "philippines": "Dec-May",
    "india": "Oct-Mar",
    "nepal": "Oct-Nov, Mar-May",
    "sri lanka": "Dec-Mar (west), Apr-Sep (east)",
    "cambodia": "Nov-Apr",
    "laos": "Nov-Feb",
    "china": "Apr-May, Sep-Oct",
    "south korea": "Apr-Jun, Sep-Nov",
    "taiwan": "Oct-Apr",
    "singapore": "Year-round",
    "portugal": "Apr-Oct",
    "spain": "Apr-Jun, Sep-Oct",
    "italy": "Apr-Jun, Sep-Oct",
    "france": "Apr-Jun, Sep-Oct",
    "germany": "May-Sep",
    "united kingdom": "May-Sep",
    "ireland": "May-Sep",
    "netherlands": "Apr-Sep",
    "belgium": "May-Sep",
    "switzerland": "Jun-Sep (summer), Dec-Mar (ski)",
    "austria": "Jun-Sep, Dec-Mar",
    "greece": "Apr-Jun, Sep-Oct",
    "croatia": "May-Sep",
    "turkey": "Apr-May, Sep-Nov",
    "czech republic": "May-Sep",
    "poland": "May-Sep",
    "hungary": "Apr-Jun, Sep-Oct",
    "iceland": "Jun-Aug",
    "norway": "Jun-Aug (summer), Dec-Mar (northern lights)",
    "sweden": "May-Sep",
    "denmark": "May-Sep",
    "finland": "Jun-Aug (summer), Dec-Mar (winter)",
    "united states": "Varies by region",
    "canada": "Jun-Sep (summer), Dec-Mar (ski)",
    "mexico": "Dec-Apr",
    "costa rica": "Dec-Apr",
    "peru": "May-Sep",
    "colombia": "Dec-Mar, Jul-Aug",
    "brazil": "Apr-Oct",
    "argentina": "Oct-Apr",
    "chile": "Nov-Mar",
    "australia": "Sep-Nov, Mar-May",
    "new zealand": "Dec-Mar",
    "morocco": "Mar-May, Sep-Nov",
    "egypt": "Oct-Apr",
    "south africa": "May-Sep",
    "kenya": "Jul-Oct",
    "tanzania": "Jun-Oct",
}


def fetch_countries() -> list:
    """Fetch all countries from RestCountries API."""
    print("Fetching country data from RestCountries API...")

    try:
        req = urllib.request.Request(
            RESTCOUNTRIES_API,
            headers={"User-Agent": "TopSoloTravel/1.0"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode())
            print(f"Fetched {len(data)} countries")
            return data
    except urllib.error.URLError as e:
        print(f"Error fetching countries: {e}")
        return []


def process_country(country: dict) -> dict:
    """Process raw country data into our format."""
    name = country.get("name", {}).get("common", "Unknown")
    name_lower = name.lower()

    # Get currency
    currencies = country.get("currencies", {})
    currency_info = ""
    if currencies:
        first_currency = list(currencies.values())[0]
        currency_code = list(currencies.keys())[0]
        currency_info = f"{first_currency.get('name', '')} ({currency_code})"

    # Get languages
    languages = country.get("languages", {})
    language_list = list(languages.values()) if languages else ["Unknown"]

    # Get capital
    capitals = country.get("capital", [])
    capital = capitals[0] if capitals else "N/A"

    # Map region
    region = country.get("region", "Unknown")
    subregion = country.get("subregion", "")

    # Get safety rating
    safety = SAFETY_RATINGS.get(name_lower, "caution")

    # Get budget estimates
    budget = BUDGET_ESTIMATES.get(name_lower, {
        "budget": "40-70",
        "midrange": "80-150",
        "luxury": "200+"
    })

    # Get best time to visit
    best_time = BEST_TIMES.get(name_lower, "Varies by region")

    # Get timezone
    timezones = country.get("timezones", ["UTC"])
    timezone = timezones[0] if timezones else "UTC"

    return {
        "name": name,
        "slug": name_lower.replace(" ", "-").replace("'", ""),
        "official_name": country.get("name", {}).get("official", name),
        "cca2": country.get("cca2", ""),
        "cca3": country.get("cca3", ""),
        "region": region,
        "subregion": subregion,
        "region_slug": REGION_MAPPING.get(region, "other"),
        "capital": capital,
        "population": country.get("population", 0),
        "area": country.get("area", 0),
        "currency": currency_info,
        "languages": language_list,
        "language": language_list[0] if language_list else "Unknown",
        "timezone": timezone,
        "timezones": timezones,
        "flag_emoji": country.get("flag", ""),
        "flag_svg": country.get("flags", {}).get("svg", ""),
        "flag_png": country.get("flags", {}).get("png", ""),
        "coat_of_arms": country.get("coatOfArms", {}).get("svg", ""),
        "maps_google": country.get("maps", {}).get("googleMaps", ""),
        "maps_osm": country.get("maps", {}).get("openStreetMaps", ""),
        "landlocked": country.get("landlocked", False),
        "borders": country.get("borders", []),
        "driving_side": country.get("car", {}).get("side", "right"),
        "calling_code": country.get("idd", {}).get("root", "") + "".join(country.get("idd", {}).get("suffixes", [])[:1]),

        # Solo travel data
        "safety_level": safety,
        "budget_per_day": budget,
        "best_time_to_visit": best_time,

        # Coordinates for maps
        "latlng": country.get("latlng", [0, 0]),
        "capital_latlng": country.get("capitalInfo", {}).get("latlng", [0, 0]),

        # UN membership
        "un_member": country.get("unMember", False),
        "independent": country.get("independent", True),

        # Featured flag (for homepage)
        "featured": name_lower in [
            "japan", "thailand", "portugal", "spain", "italy",
            "france", "germany", "australia", "new zealand", "canada",
            "united states", "mexico", "peru", "costa rica", "iceland",
            "norway", "greece", "croatia", "vietnam", "indonesia"
        ]
    }


def save_countries(countries: list):
    """Save processed country data."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Save all countries
    all_countries_path = DATA_DIR / "countries.json"
    with open(all_countries_path, "w", encoding="utf-8") as f:
        json.dump(countries, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(countries)} countries to {all_countries_path}")

    # Save individual country files
    countries_dir = DATA_DIR / "countries"
    countries_dir.mkdir(exist_ok=True)

    for country in countries:
        country_path = countries_dir / f"{country['slug']}.json"
        with open(country_path, "w", encoding="utf-8") as f:
            json.dump(country, f, indent=2, ensure_ascii=False)

    print(f"Saved individual country files to {countries_dir}")

    # Save by region
    regions = {}
    for country in countries:
        region = country["region_slug"]
        if region not in regions:
            regions[region] = []
        regions[region].append(country)

    for region, region_countries in regions.items():
        region_path = DATA_DIR / f"countries_by_region_{region}.json"
        with open(region_path, "w", encoding="utf-8") as f:
            json.dump(region_countries, f, indent=2, ensure_ascii=False)

    return countries


def main():
    """Main function to fetch and process country data."""
    raw_countries = fetch_countries()

    if not raw_countries:
        print("No countries fetched, using fallback data...")
        return []

    # Process all countries
    processed = []
    for country in raw_countries:
        try:
            processed_country = process_country(country)
            processed.append(processed_country)
        except Exception as e:
            print(f"Error processing country: {e}")
            continue

    # Sort by name
    processed.sort(key=lambda x: x["name"])

    # Save data
    save_countries(processed)

    print(f"\nProcessed {len(processed)} countries")
    print(f"Featured countries: {len([c for c in processed if c['featured']])}")

    return processed


if __name__ == "__main__":
    main()
