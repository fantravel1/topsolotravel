#!/usr/bin/env python3
"""
Generate Hugo content from data files.
Creates markdown files for countries, cities, and safety pages.
"""

import json
import os
import random
from pathlib import Path
from datetime import datetime
from typing import Optional

# Configuration
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
CONTENT_DIR = BASE_DIR / "content"

# Templates for content generation
COUNTRY_TEMPLATE = '''---
title: "{name}"
description: "Complete solo travel guide to {name}. Safety tips, best cities, budget breakdown, visa info, and essential tips for traveling alone in {name}."
region: "{region}"
subregion: "{subregion}"
featured: {featured}
safetyLevel: "{safety_level}"
heroImage: "https://source.unsplash.com/1600x900/?{image_query}"

quickFacts:
  capital: "{capital}"
  currency: "{currency}"
  language: "{language}"
  timezone: "{timezone}"
  population: "{population_formatted}"
  bestTime: "{best_time}"
  budget: "${budget_range}/day"
  visaFree: "{visa_info}"
  safety: "{safety_text}"

travelAdvisory:
  level: "info"
  advisoryLevel: 1
  message: "Exercise normal precautions in {name}."
  source: "Travel Advisory"
  date: "{current_year}"

safety:
  overview: "{name} is {safety_desc} for solo travelers. {safety_overview}"
  soloFemale: "Solo female travelers {female_safety} in {name}. Standard precautions are advised in tourist areas."
  tips:
    - "Keep valuables secure, especially in crowded areas"
    - "Stay aware of your surroundings, particularly at night"
    - "Use official transportation services"
    - "Share your itinerary with someone back home"
    - "Carry a copy of your passport separately from the original"
  avoid:
    - "Unlicensed taxis and transportation"
    - "Displaying expensive jewelry or electronics"
    - "Walking alone in unfamiliar areas late at night"

topCities:
{top_cities_yaml}

budget:
  overview: "{name} offers {budget_desc} options for solo travelers. Budget-conscious travelers can manage on ${budget_low}/day, while mid-range travelers typically spend ${budget_mid}/day."
  accommodation:
    budget: "${accommodation_budget}"
    midRange: "${accommodation_mid}"
    luxury: "${accommodation_luxury}"
  food:
    budget: "${food_budget}"
    midRange: "${food_mid}"
    luxury: "${food_luxury}"
  transport:
    budget: "${transport_budget}"
    midRange: "${transport_mid}"
    luxury: "${transport_luxury}"
  total:
    budget: "${budget_low}"
    midRange: "${budget_mid}"
    luxury: "${budget_high}"

visa:
  overview: "Visa requirements for {name} vary by nationality. Many passport holders enjoy visa-free or visa-on-arrival access."
  usPassport: "US passport holders should check current visa requirements before traveling."
  ukPassport: "UK passport holders should verify entry requirements."
  euPassport: "EU citizens should check Schengen area agreements if applicable."

culture:
  tips:
    - "Learn a few basic phrases in the local language"
    - "Respect local customs and dress codes"
    - "Be mindful of photography restrictions at religious sites"
    - "Tipping customs vary - research before your trip"
  etiquette:
    - "Greet locals appropriately based on local customs"
    - "Ask permission before photographing people"
    - "Dress modestly when visiting religious sites"

transport:
  overview: "Getting around {name} is {transport_ease}. {transport_desc}"
  options:
    - name: "Public Transit"
      description: "Available in major cities with varying quality and coverage."
    - name: "Taxis/Ride-sharing"
      description: "Widely available; use official services or trusted apps."
    - name: "Domestic Flights"
      description: "Useful for covering large distances efficiently."

faqs:
  - question: "Is {name} safe for solo travelers?"
    answer: "{name} is {safety_desc} for solo travelers. {faq_safety}"
  - question: "How much money do I need per day in {name}?"
    answer: "Budget travelers can get by on ${budget_low}/day, mid-range travelers typically spend ${budget_mid}/day, and luxury travelers should budget ${budget_high}+/day."
  - question: "What's the best time to visit {name}?"
    answer: "The best time to visit {name} is {best_time}. Weather and crowds vary by season."
  - question: "Do I need a visa for {name}?"
    answer: "Visa requirements depend on your nationality. Many countries offer visa-free or visa-on-arrival access. Always verify current requirements before travel."
  - question: "Is {name} good for first-time solo travelers?"
    answer: "{first_time_answer}"
---

{name} offers {appeal} for solo travelers. From {attractions} to {experiences}, there's something for every independent explorer.

## Why {name} is {great_word} for Solo Travelers

**{highlight_1_title}**: {highlight_1_desc}

**{highlight_2_title}**: {highlight_2_desc}

**{highlight_3_title}**: {highlight_3_desc}

## Best Experiences for Solo Travelers

- **Explore Local Markets**: Discover authentic local life and cuisine
- **Walking Tours**: Many cities offer free or affordable walking tours
- **Cultural Sites**: Museums, temples, and historical landmarks
- **Local Cuisine**: Try street food and local restaurants
- **Nature & Outdoors**: Parks, hiking trails, and scenic viewpoints

## Getting Around

{transport_tips}

## Solo Travel Tips for {name}

1. **Stay Connected**: Get a local SIM card or ensure your international plan works
2. **Join Group Tours**: A great way to meet other travelers
3. **Use Trusted Apps**: Download maps, translation, and transportation apps
4. **Book Ahead**: Especially during peak season
5. **Trust Your Instincts**: If something feels off, remove yourself from the situation
'''

CITY_TEMPLATE = '''---
title: "{name}"
description: "Complete solo travel guide to {name}, {country}. Best neighborhoods, solo dining, accommodation, and things to do alone in {name}."
country: "{country}"
countrySlug: "{country_slug}"
region: "{region}"
featured: true
safetyLevel: "{safety_level}"
heroImage: "https://source.unsplash.com/1600x900/?{image_query}"

quickFacts:
  country: "{country}"
  population: "{population_formatted}"
  timezone: "{timezone}"
  bestTime: "{best_time}"
  budget: "${budget}/day"
  safety: "{safety_text}"
  airport: "{airport}"

highlights:
{highlights_yaml}

neighborhoods:
  - name: "City Center"
    description: "Central location with easy access to main attractions, restaurants, and nightlife."
    safety: "safe"
  - name: "Historic District"
    description: "Cultural heart with museums, landmarks, and traditional architecture."
    safety: "safe"

accommodation:
  - name: "Central Hostel"
    type: "Hostel"
    description: "Social atmosphere perfect for meeting other travelers."
    priceFrom: "${hostel_price}"
    soloFriendly: true
  - name: "Boutique Hotel"
    type: "Hotel"
    description: "Comfortable private rooms in central location."
    priceFrom: "${hotel_price}"
    noSingleSupplement: true

dining:
  tips:
    - "Counter seating is perfect for solo diners"
    - "Lunch specials offer great value"
    - "Food markets are social and affordable"

faqs:
  - question: "Is {name} safe for solo travelers?"
    answer: "{name} is {safety_desc} for solo travelers. The city has good infrastructure and tourist-friendly areas."
  - question: "How many days should I spend in {name}?"
    answer: "Most solo travelers spend 3-5 days in {name} to see the main attractions and explore neighborhoods."
  - question: "What's the best area to stay for solo travelers?"
    answer: "The city center and historic districts are ideal for solo travelers due to walkability and safety."
---

{name} is {city_appeal} for solo travelers visiting {country}. {intro_text}

## Why Solo Travelers Love {name}

{name} offers a perfect blend of {blend} that makes it ideal for independent exploration.

## Best Neighborhoods for Solo Travelers

The city center provides easy access to attractions and services. Historic areas offer cultural immersion and walkable streets.

## Getting Around {name}

{transport_info}

## Solo Dining in {name}

{dining_info}

## Top Things to Do Solo in {name}

1. **Walking Tours**: Join a free walking tour to meet other travelers
2. **Museums & Galleries**: Perfect solo activities with no time pressure
3. **Local Markets**: Great for people-watching and sampling food
4. **Parks & Gardens**: Peaceful spots for reading or relaxing
5. **Day Trips**: Many organized tours available for solo travelers
'''

SAFETY_TEMPLATE = '''---
title: "{name}"
description: "{name} safety guide for solo travelers. Travel advisories, emergency contacts, scam alerts, and safety tips."
isCountry: {is_country}
safetyLevel: "{safety_level}"
heroImage: "https://source.unsplash.com/1600x900/?{image_query}"

travelAdvisory:
  level: "{advisory_level}"
  advisoryLevel: {advisory_number}
  message: "{advisory_message}"
  source: "Travel Advisory"
  date: "{current_year}"

safetyRatings:
  - category: "Overall Safety"
    level: "{safety_level}"
    rating: "{safety_text}"
  - category: "Solo Female"
    level: "{female_level}"
    rating: "{female_rating}"
  - category: "Night Safety"
    level: "{night_level}"
    rating: "{night_rating}"
  - category: "Transport"
    level: "{transport_level}"
    rating: "{transport_rating}"

soloSafety:
  overview: "{safety_overview}"
  dosList:
    - "Stay aware of your surroundings"
    - "Keep valuables secure and out of sight"
    - "Use official transportation services"
    - "Share your itinerary with someone back home"
    - "Trust your instincts"
  dontsList:
    - "Flash expensive items in public"
    - "Accept drinks from strangers"
    - "Walk alone in unfamiliar areas at night"
    - "Leave belongings unattended"

femaleSafety:
  overview: "{female_overview}"
  tips:
    - "Dress appropriately for local customs"
    - "Be cautious with alcohol consumption"
    - "Use women-only transportation options where available"
    - "Stay in well-reviewed accommodations"
  dresscode: "Research local dress customs, especially for religious sites."

scams:
  - name: "Taxi Overcharging"
    description: "Unlicensed or metered taxi drivers may overcharge tourists."
    avoidance: "Use ride-sharing apps or agree on fare before departure."
  - name: "Distraction Theft"
    description: "Groups may create distractions while accomplices steal."
    avoidance: "Keep belongings secure and be wary of unsolicited attention."

emergency:
  police: "Local emergency number"
  ambulance: "Local emergency number"
  fire: "Local emergency number"
  touristPolice: "Check locally"

health:
  overview: "Standard travel health precautions apply. Ensure routine vaccinations are up to date."
  vaccinations:
    - "Routine vaccinations (MMR, tetanus, etc.)"
    - "Hepatitis A and B recommended"
    - "Check CDC or WHO recommendations"

faqs:
  - question: "Is {name} safe for solo travelers?"
    answer: "{name} is {safety_desc} for solo travelers. {faq_answer}"
  - question: "Is {name} safe for solo female travelers?"
    answer: "{female_faq_answer}"
  - question: "What are the main safety concerns in {name}?"
    answer: "Common concerns include petty theft in tourist areas and transportation scams. Standard precautions minimize risk."
---

## Is {name} Safe for Solo Travelers?

{safety_intro}

## Safety Overview

{safety_overview_long}

## Solo Female Traveler Safety

{female_safety_long}

## Emergency Contacts

Keep local emergency numbers saved in your phone. Your embassy can assist with serious issues.

## Health & Medical

{health_info}

## Transportation Safety

{transport_safety}

## Final Safety Tips

1. Register with your embassy
2. Purchase travel insurance
3. Keep digital copies of important documents
4. Stay connected with family/friends
5. Trust your instincts
'''


def load_countries() -> list:
    """Load country data from JSON file."""
    countries_file = DATA_DIR / "countries.json"
    if countries_file.exists():
        with open(countries_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def load_cities() -> list:
    """Load city data from JSON file."""
    cities_file = DATA_DIR / "cities.json"
    if cities_file.exists():
        with open(cities_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def get_safety_text(level: str) -> str:
    """Convert safety level to descriptive text."""
    mapping = {
        "safe": "Very Safe",
        "caution": "Generally Safe",
        "warning": "Exercise Caution",
        "danger": "Avoid Non-Essential Travel"
    }
    return mapping.get(level, "Exercise Caution")


def get_safety_desc(level: str) -> str:
    """Get safety description."""
    mapping = {
        "safe": "generally very safe",
        "caution": "generally safe with normal precautions",
        "warning": "safe with increased caution",
        "danger": "challenging for travelers"
    }
    return mapping.get(level, "generally safe")


def format_population(pop: int) -> str:
    """Format population number."""
    if pop >= 1_000_000_000:
        return f"{pop / 1_000_000_000:.1f} billion"
    elif pop >= 1_000_000:
        return f"{pop / 1_000_000:.1f} million"
    elif pop >= 1_000:
        return f"{pop / 1_000:.0f}K"
    return str(pop)


def generate_country_content(country: dict, cities: list) -> str:
    """Generate markdown content for a country."""
    name = country["name"]
    slug = country["slug"]
    safety_level = country.get("safety_level", "caution")

    # Get budget info
    budget = country.get("budget_per_day", {"budget": "50-80", "midrange": "100-150", "luxury": "200+"})
    if isinstance(budget, dict):
        budget_parts = budget.get("budget", "50-80").split("-")
        budget_low = budget_parts[0] if budget_parts else "50"
        budget_mid_parts = budget.get("midrange", "100-150").split("-")
        budget_mid = budget_mid_parts[0] if budget_mid_parts else "100"
        budget_high_str = budget.get("luxury", "200+").replace("+", "")
        budget_high = budget_high_str if budget_high_str else "200"
    else:
        budget_low, budget_mid, budget_high = "50", "100", "200"

    # Get cities for this country
    country_cities = [c for c in cities if c.get("country_slug") == slug][:4]

    # Format top cities YAML
    top_cities_yaml = ""
    for city in country_cities:
        top_cities_yaml += f'''  - name: "{city['name']}"
    url: "/destinations/{slug}/{city['slug']}/"
    description: "Popular destination for solo travelers with great infrastructure."
    highlights: {json.dumps(city.get('highlights', ['culture', 'food', 'history']))}
'''

    if not top_cities_yaml:
        top_cities_yaml = f'''  - name: "{country.get('capital', 'Capital')}"
    url: "/destinations/{slug}/"
    description: "The capital city offers diverse experiences for solo travelers."
    highlights: ["culture", "food", "history"]
'''

    # Generate content
    content = COUNTRY_TEMPLATE.format(
        name=name,
        region=country.get("region", ""),
        subregion=country.get("subregion", ""),
        featured=str(country.get("featured", False)).lower(),
        safety_level=safety_level,
        image_query=f"{name.lower().replace(' ', '+')}+travel+landscape",
        capital=country.get("capital", "N/A"),
        currency=country.get("currency", "Local currency"),
        language=country.get("language", "Local language"),
        timezone=country.get("timezone", "Local time"),
        population_formatted=format_population(country.get("population", 0)),
        best_time=country.get("best_time_to_visit", "Varies by region"),
        budget_range=f"{budget_low}-{budget_mid}",
        visa_info="Check requirements",
        safety_text=get_safety_text(safety_level),
        current_year=datetime.now().year,
        safety_desc=get_safety_desc(safety_level),
        safety_overview="Standard travel precautions are recommended for all visitors.",
        female_safety="generally feel safe" if safety_level in ["safe", "caution"] else "should exercise extra caution",
        top_cities_yaml=top_cities_yaml,
        budget_desc="varied" if safety_level != "safe" else "excellent value",
        budget_low=budget_low,
        budget_mid=budget_mid,
        budget_high=budget_high,
        accommodation_budget=str(int(int(budget_low) * 0.4)),
        accommodation_mid=str(int(int(budget_mid) * 0.4)),
        accommodation_luxury=str(int(int(budget_high) * 0.5)),
        food_budget=str(int(int(budget_low) * 0.3)),
        food_mid=str(int(int(budget_mid) * 0.3)),
        food_luxury=str(int(int(budget_high) * 0.3)),
        transport_budget=str(int(int(budget_low) * 0.2)),
        transport_mid=str(int(int(budget_mid) * 0.2)),
        transport_luxury=str(int(int(budget_high) * 0.15)),
        transport_ease="manageable" if safety_level in ["safe", "caution"] else "requires planning",
        transport_desc="Major cities have public transportation. Taxis and ride-sharing are widely available.",
        faq_safety="Most visitors have positive experiences with standard precautions.",
        first_time_answer=f"{'Yes, ' + name + ' is excellent for first-time solo travelers due to good infrastructure and welcoming culture.' if safety_level in ['safe', 'caution'] else name + ' can be visited by experienced travelers who research and plan carefully.'}",
        appeal="incredible experiences" if safety_level == "safe" else "unique adventures",
        attractions="vibrant cities",
        experiences="rich cultural heritage",
        great_word="Great" if safety_level in ["safe", "caution"] else "Possible",
        highlight_1_title="Welcoming Culture",
        highlight_1_desc=f"Visitors to {name} often comment on the hospitality of locals.",
        highlight_2_title="Diverse Experiences",
        highlight_2_desc=f"From cities to countryside, {name} offers varied experiences.",
        highlight_3_title="Solo-Friendly Infrastructure",
        highlight_3_desc=f"{'Good tourist infrastructure makes solo travel straightforward.' if safety_level in ['safe', 'caution'] else 'Planning ahead helps ensure smooth travels.'}",
        transport_tips=f"Research transportation options before arrival. Major cities typically have public transit, taxis, and ride-sharing options."
    )

    return content


def generate_city_content(city: dict) -> str:
    """Generate markdown content for a city."""
    name = city["name"]
    country = city["country"]
    safety_level = city.get("safety_level", "caution")
    budget = city.get("budget_per_day", "50-100")

    # Parse budget
    budget_parts = budget.split("-")
    budget_low = budget_parts[0] if budget_parts else "50"

    # Format highlights
    highlights = city.get("highlights", ["culture", "food", "history"])
    highlights_yaml = "\n".join([f'  - "{h}"' for h in highlights])

    content = CITY_TEMPLATE.format(
        name=name,
        country=country,
        country_slug=city.get("country_slug", country.lower().replace(" ", "-")),
        region=city.get("region", ""),
        safety_level=safety_level,
        image_query=f"{name.lower().replace(' ', '+')}+{country.lower().replace(' ', '+')}+city",
        population_formatted=format_population(city.get("population", 0)),
        timezone=f"UTC{'+' if city.get('lng', 0) > 0 else ''}{int(city.get('lng', 0) / 15)}",
        best_time=city.get("best_time_to_visit", "Year-round"),
        budget=budget,
        safety_text=get_safety_text(safety_level),
        airport=city.get("airport_code", "Local airport"),
        highlights_yaml=highlights_yaml,
        hostel_price=str(int(int(budget_low) * 0.3)),
        hotel_price=str(int(int(budget_low) * 0.6)),
        safety_desc=get_safety_desc(safety_level),
        city_appeal="an excellent destination" if safety_level in ["safe", "caution"] else "an adventurous choice",
        intro_text=f"Whether you're exploring for a few days or settling in longer, {name} has plenty to offer independent travelers.",
        blend="culture, cuisine, and modern amenities",
        transport_info="Public transportation, taxis, and ride-sharing apps make getting around straightforward. Walking is often the best way to explore central areas.",
        dining_info="Solo dining is common and comfortable. Look for counter seating at restaurants, busy food markets, and casual cafes."
    )

    return content


def generate_safety_content(country: dict) -> str:
    """Generate safety page content for a country."""
    name = country["name"]
    safety_level = country.get("safety_level", "caution")

    # Determine advisory level
    advisory_map = {
        "safe": ("info", 1),
        "caution": ("info", 2),
        "warning": ("warning", 3),
        "danger": ("danger", 4)
    }
    advisory_level, advisory_number = advisory_map.get(safety_level, ("info", 2))

    content = SAFETY_TEMPLATE.format(
        name=name,
        is_country="true",
        safety_level=safety_level,
        image_query=f"{name.lower().replace(' ', '+')}+travel+safety",
        advisory_level=advisory_level,
        advisory_number=advisory_number,
        advisory_message=f"Exercise {'normal' if safety_level == 'safe' else 'increased'} precautions in {name}.",
        current_year=datetime.now().year,
        safety_text=get_safety_text(safety_level),
        female_level=safety_level,
        female_rating=get_safety_text(safety_level),
        night_level="caution" if safety_level == "safe" else safety_level,
        night_rating="Exercise Caution" if safety_level == "safe" else get_safety_text(safety_level),
        transport_level=safety_level,
        transport_rating=get_safety_text(safety_level),
        safety_overview=f"{name} is {get_safety_desc(safety_level)} for solo travelers.",
        female_overview=f"Solo female travelers {('generally feel comfortable' if safety_level in ['safe', 'caution'] else 'should take extra precautions')} in {name}.",
        safety_desc=get_safety_desc(safety_level),
        faq_answer="Most travelers have positive experiences with standard precautions.",
        female_faq_answer=f"Solo female travelers {('generally have positive experiences' if safety_level in ['safe', 'caution'] else 'should research and plan carefully')} in {name}.",
        safety_intro=f"{name} is {get_safety_desc(safety_level)} for solo travelers visiting the country.",
        safety_overview_long=f"Overall, {name} presents {('few safety concerns' if safety_level == 'safe' else 'manageable safety considerations')} for prepared travelers. Standard precautions help ensure a smooth trip.",
        female_safety_long=f"Women traveling alone in {name} {('generally report feeling safe' if safety_level in ['safe', 'caution'] else 'should exercise heightened awareness')}. Respecting local customs and dressing appropriately helps.",
        health_info="Consult your doctor before travel. Ensure routine vaccinations are current and consider destination-specific recommendations.",
        transport_safety="Use official transportation services. Ride-sharing apps offer transparency and safety. Avoid unlicensed vehicles."
    )

    return content


def save_content(content: str, filepath: Path):
    """Save content to file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def generate_all_content():
    """Generate all content files."""
    print("Loading data...")
    countries = load_countries()
    cities = load_cities()

    if not countries:
        print("No country data found. Run fetch_countries.py first.")
        return

    print(f"Generating content for {len(countries)} countries...")

    # Generate country pages
    for country in countries:
        slug = country["slug"]

        # Skip if country has problematic characters
        if not slug or "/" in slug:
            continue

        # Generate country index page
        content = generate_country_content(country, cities)
        filepath = CONTENT_DIR / "destinations" / slug / "_index.md"
        save_content(content, filepath)

        # Generate safety page
        safety_content = generate_safety_content(country)
        safety_filepath = CONTENT_DIR / "safety" / slug / "_index.md"
        save_content(safety_content, safety_filepath)

    print(f"Generated {len(countries)} country pages")
    print(f"Generated {len(countries)} safety pages")

    # Generate city pages
    city_count = 0
    for city in cities:
        country_slug = city.get("country_slug", "")
        city_slug = city.get("slug", "")

        if not country_slug or not city_slug:
            continue

        content = generate_city_content(city)
        filepath = CONTENT_DIR / "destinations" / country_slug / city_slug / "_index.md"
        save_content(content, filepath)
        city_count += 1

    print(f"Generated {city_count} city pages")

    print("\nContent generation complete!")
    print(f"Total pages: {len(countries) * 2 + city_count}")


if __name__ == "__main__":
    generate_all_content()
