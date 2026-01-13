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

ITINERARY_TEMPLATE = '''---
title: "{duration} in {name}"
description: "Perfect {duration} solo travel itinerary for {name}. Day-by-day guide with activities, accommodation tips, and budget breakdown."
country: "{country_slug}"
countryName: "{name}"
duration: "{duration}"
days: {days}
heroImage: "https://source.unsplash.com/1600x900/?{image_query}"

quickInfo:
  duration: "{duration}"
  budget: "${budget_total}"
  bestFor: "{best_for}"
  difficulty: "{difficulty}"

highlights:
{highlights_yaml}

budget:
  accommodation: "${accommodation}"
  food: "${food}"
  transport: "${transport}"
  activities: "${activities}"
  total: "${budget_total}"

faqs:
  - question: "Is {duration} enough time in {name}?"
    answer: "{time_answer}"
  - question: "What's the best season for this itinerary?"
    answer: "The ideal time to visit {name} is {best_time}. However, this itinerary works year-round with minor adjustments."
---

## {duration} Solo Travel Itinerary for {name}

{intro}

## Day-by-Day Breakdown

{daily_breakdown}

## Budget Breakdown

This itinerary is designed for {budget_style} travelers. Total estimated cost: ${budget_total}.

## Solo Travel Tips for This Itinerary

1. **Book accommodations in advance** during peak season
2. **Join group tours** for activities to meet other travelers
3. **Stay flexible** - the best experiences often come from spontaneous detours
4. **Connect locally** - use apps and hostels to meet fellow solo travelers
5. **Document your journey** - you'll want to remember these experiences

## What to Pack

- Comfortable walking shoes
- Layers for varying weather
- Universal power adapter
- Portable charger
- Copies of important documents
'''

BUDGET_GUIDE_TEMPLATE = '''---
title: "{name} on a Budget"
description: "Complete budget travel guide to {name} for solo travelers. Money-saving tips, cheap accommodation, affordable food, and free activities."
country: "{country_slug}"
countryName: "{name}"
heroImage: "https://source.unsplash.com/1600x900/?{image_query}"

budgetOverview:
  dailyBudget: "${daily_budget}"
  cheapestMonth: "{cheapest_month}"
  currency: "{currency}"
  costLevel: "{cost_level}"

accommodation:
  hostelDorm: "${hostel}"
  budgetHotel: "${budget_hotel}"
  airbnb: "${airbnb}"
  tips:
    - "Book hostels with kitchens to save on food"
    - "Consider Couchsurfing for free stays and local connections"
    - "Stay outside city centers for lower prices"

food:
  streetFood: "${street_food}"
  localRestaurant: "${local_restaurant}"
  grocery: "${grocery}"
  tips:
    - "Eat where locals eat for authentic and affordable meals"
    - "Markets offer fresh produce at low prices"
    - "Lunch specials are often cheaper than dinner"

transport:
  publicTransit: "${transit}"
  intercityBus: "${bus}"
  tips:
    - "Get transit passes for multi-day savings"
    - "Walk when possible - it's free and you see more"
    - "Night buses save on accommodation costs"

freeActivities:
{free_activities_yaml}

faqs:
  - question: "How much money do I need per day in {name}?"
    answer: "Budget travelers can manage on ${daily_budget}/day including basic accommodation, local food, and public transport."
  - question: "Is {name} expensive for tourists?"
    answer: "{expense_answer}"
---

## Budget Solo Travel in {name}

{intro}

## Daily Budget Breakdown

Living on ${daily_budget}/day in {name} is {feasibility}. Here's how to make it work:

### Accommodation (${hostel}-${budget_hotel}/night)
{accommodation_text}

### Food (${street_food}-${local_restaurant}/day)
{food_text}

### Transportation (${transit}/day)
{transport_text}

## Money-Saving Tips

1. **Travel in shoulder season** - Lower prices and fewer crowds
2. **Cook some meals** - Hostel kitchens save significant money
3. **Free walking tours** - Tip-based tours in most cities
4. **Student/youth discounts** - Bring valid ID for discounts
5. **Happy hour specials** - Enjoy nightlife affordably

## Free Things to Do

{free_activities_text}

## Budget Accommodation Tips

{budget_accommodation_tips}

## Eating Cheap in {name}

{eating_cheap_text}
'''

SOLO_FEMALE_TEMPLATE = '''---
title: "Solo Female Travel in {name}"
description: "Complete solo female travel guide to {name}. Safety tips, best areas, cultural advice, and practical information for women traveling alone."
country: "{country_slug}"
countryName: "{name}"
heroImage: "https://source.unsplash.com/1600x900/?{image_query}"

safetyRating: "{safety_rating}"
overallRating: "{overall_rating}"

safetyFactors:
  streetHarassment: "{harassment_level}"
  nightSafety: "{night_safety}"
  soloFriendly: "{solo_friendly}"
  dresscode: "{dresscode}"

bestAreas:
{best_areas_yaml}

tips:
  cultural:
    - "{cultural_tip_1}"
    - "{cultural_tip_2}"
    - "{cultural_tip_3}"
  safety:
    - "Share your itinerary with someone back home"
    - "Trust your instincts - if something feels wrong, leave"
    - "Keep emergency numbers saved in your phone"
  practical:
    - "{practical_tip_1}"
    - "{practical_tip_2}"
    - "{practical_tip_3}"

faqs:
  - question: "Is {name} safe for solo female travelers?"
    answer: "{safety_answer}"
  - question: "What should women wear in {name}?"
    answer: "{dress_answer}"
  - question: "Can women go out alone at night in {name}?"
    answer: "{night_answer}"
---

## Solo Female Travel Guide to {name}

{intro}

## Is {name} Safe for Women Traveling Alone?

{safety_overview}

## Cultural Considerations

{cultural_section}

## Best Areas for Solo Female Travelers

{best_areas_text}

## What to Wear

{dress_section}

## Night Safety

{night_section}

## Meeting Other Travelers

{social_section}

## Top Tips from Female Travelers

1. {top_tip_1}
2. {top_tip_2}
3. {top_tip_3}
4. {top_tip_4}
5. {top_tip_5}

## Emergency Resources

- Tourist police: Check locally
- Embassy: Register before travel
- Local women's organizations: Research before arrival
'''

ACTIVITY_TEMPLATE = '''---
title: "{activity} in {name}"
description: "Complete guide to {activity} in {name} for solo travelers. Best spots, tours, costs, and tips for {activity_lower} alone."
country: "{country_slug}"
countryName: "{name}"
activity: "{activity}"
heroImage: "https://source.unsplash.com/1600x900/?{image_query}"

activityInfo:
  difficulty: "{difficulty}"
  cost: "${cost}"
  bestSeason: "{best_season}"
  soloFriendly: "{solo_friendly}"

topSpots:
{spots_yaml}

tours:
  groupTour: "${group_tour}"
  privateTour: "${private_tour}"
  selfGuided: "{self_guided}"

gear:
{gear_yaml}

faqs:
  - question: "Can I do {activity_lower} solo in {name}?"
    answer: "{solo_answer}"
  - question: "What's the best time for {activity_lower} in {name}?"
    answer: "The ideal season for {activity_lower} in {name} is {best_season}."
  - question: "How much does {activity_lower} cost in {name}?"
    answer: "Expect to spend ${cost} for a typical {activity_lower} experience including equipment and guides."
---

## {activity} in {name} for Solo Travelers

{intro}

## Best Spots for {activity}

{spots_text}

## Solo {activity} Tips

{solo_tips}

## Tours vs Self-Guided

{tours_text}

## What to Bring

{gear_text}

## Safety Considerations

{safety_text}

## Meeting Other {activity} Enthusiasts

{social_text}

## Budget Breakdown

- Group tours: ${group_tour}
- Equipment rental: ${rental}
- Solo/self-guided: {self_guided_cost}

## Best Season

{season_text}
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


def generate_city_safety_content(city: dict) -> str:
    """Generate safety page content for a city."""
    name = city["name"]
    country = city["country"]
    safety_level = city.get("safety_level", "caution")

    # Determine advisory level
    advisory_map = {
        "safe": ("info", 1),
        "caution": ("info", 2),
        "warning": ("warning", 3),
        "danger": ("danger", 4)
    }
    advisory_level, advisory_number = advisory_map.get(safety_level, ("info", 2))

    content = SAFETY_TEMPLATE.format(
        name=f"{name}, {country}",
        is_country="false",
        safety_level=safety_level,
        image_query=f"{name.lower().replace(' ', '+')}+{country.lower().replace(' ', '+')}+safety",
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
        safety_overview=f"{name} is {get_safety_desc(safety_level)} for solo travelers visiting {country}.",
        female_overview=f"Solo female travelers {('generally feel comfortable' if safety_level in ['safe', 'caution'] else 'should take extra precautions')} in {name}.",
        safety_desc=get_safety_desc(safety_level),
        faq_answer="Most travelers have positive experiences with standard precautions in this city.",
        female_faq_answer=f"Solo female travelers {('generally have positive experiences' if safety_level in ['safe', 'caution'] else 'should research and plan carefully')} in {name}.",
        safety_intro=f"{name} is {get_safety_desc(safety_level)} for solo travelers visiting this popular destination in {country}.",
        safety_overview_long=f"As a major destination in {country}, {name} presents {('few safety concerns' if safety_level == 'safe' else 'manageable safety considerations')} for prepared travelers. Tourist areas are generally well-patrolled.",
        female_safety_long=f"Women traveling alone in {name} {('generally report feeling safe' if safety_level in ['safe', 'caution'] else 'should exercise heightened awareness')}, especially in tourist areas and during daylight hours.",
        health_info="Healthcare facilities are available in the city. Ensure travel insurance covers medical expenses.",
        transport_safety="Use official transportation services. Metro, buses, and ride-sharing apps are generally safe options."
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


# Activity definitions for each region
REGION_ACTIVITIES = {
    "Asia": ["Hiking", "Temples", "Street Food Tours", "Meditation Retreats", "Cooking Classes"],
    "Europe": ["Hiking", "Museums", "Food Tours", "Wine Tasting", "Architecture Tours"],
    "Americas": ["Hiking", "Beach Activities", "Wildlife Tours", "Adventure Sports", "Food Tours"],
    "Africa": ["Safari", "Hiking", "Cultural Tours", "Wildlife Photography", "Desert Tours"],
    "Oceania": ["Hiking", "Diving", "Beach Activities", "Wildlife Tours", "Adventure Sports"],
}

DEFAULT_ACTIVITIES = ["Hiking", "Food Tours", "Cultural Tours", "Photography", "Walking Tours"]


def generate_itinerary_content(country: dict, duration: str, days: int) -> str:
    """Generate itinerary page content for a country."""
    name = country["name"]
    slug = country["slug"]
    region = country.get("region", "")

    # Budget calculations
    budget = country.get("budget_per_day", {"budget": "50-80"})
    if isinstance(budget, dict):
        daily = int(budget.get("budget", "50-80").split("-")[0])
    else:
        daily = 50

    budget_total = daily * days

    # Generate highlights
    highlights = [
        f"Explore the capital and major cities",
        f"Experience local cuisine and culture",
        f"Visit iconic landmarks and attractions",
        f"Connect with fellow travelers"
    ]
    highlights_yaml = "\n".join([f'  - "{h}"' for h in highlights])

    # Generate daily breakdown
    daily_breakdown = ""
    for d in range(1, days + 1):
        if d == 1:
            daily_breakdown += f"### Day {d}: Arrival & Orientation\nArrive, settle into your accommodation, and explore your immediate neighborhood. Get your bearings and recover from travel.\n\n"
        elif d == days:
            daily_breakdown += f"### Day {d}: Final Explorations & Departure\nLast-minute shopping, revisit favorite spots, and prepare for departure.\n\n"
        elif d <= days // 3:
            daily_breakdown += f"### Day {d}: City Exploration\nDeep dive into the main city - museums, landmarks, and local neighborhoods.\n\n"
        elif d <= (days * 2) // 3:
            daily_breakdown += f"### Day {d}: Day Trip or New City\nVenture outside the main city or travel to your next destination.\n\n"
        else:
            daily_breakdown += f"### Day {d}: Cultural Immersion\nCooking class, local market visit, or cultural experience.\n\n"

    content = ITINERARY_TEMPLATE.format(
        name=name,
        country_slug=slug,
        duration=duration,
        days=days,
        image_query=f"{name.lower().replace(' ', '+')}+travel+itinerary",
        budget_total=budget_total,
        best_for="First-time visitors" if days <= 7 else "In-depth explorers",
        difficulty="Easy" if days <= 7 else "Moderate",
        highlights_yaml=highlights_yaml,
        accommodation=int(budget_total * 0.35),
        food=int(budget_total * 0.25),
        transport=int(budget_total * 0.20),
        activities=int(budget_total * 0.20),
        time_answer=f"{'Yes, ' + duration + ' gives you a solid introduction to ' + name + '.' if days <= 7 else duration + ' allows for an in-depth exploration of ' + name + '.'}",
        best_time=country.get("best_time_to_visit", "Year-round"),
        intro=f"This {duration} itinerary covers the highlights of {name}, perfect for solo travelers looking to maximize their experience.",
        daily_breakdown=daily_breakdown,
        budget_style="budget to mid-range"
    )

    return content


def generate_budget_guide_content(country: dict) -> str:
    """Generate budget travel guide content for a country."""
    name = country["name"]
    slug = country["slug"]

    # Budget calculations
    budget = country.get("budget_per_day", {"budget": "50-80"})
    if isinstance(budget, dict):
        daily = int(budget.get("budget", "50-80").split("-")[0])
    else:
        daily = 50

    # Determine cost level
    if daily < 30:
        cost_level = "Very Budget-Friendly"
        feasibility = "very achievable"
    elif daily < 50:
        cost_level = "Budget-Friendly"
        feasibility = "comfortable"
    elif daily < 80:
        cost_level = "Moderate"
        feasibility = "manageable with planning"
    else:
        cost_level = "Higher Cost"
        feasibility = "challenging but possible"

    # Free activities
    free_activities = [
        "Walking tours of historic areas",
        "Public parks and gardens",
        "Free museum days",
        "Local markets (window shopping)",
        "Beach or nature areas"
    ]
    free_activities_yaml = "\n".join([f'  - "{a}"' for a in free_activities])

    content = BUDGET_GUIDE_TEMPLATE.format(
        name=name,
        country_slug=slug,
        image_query=f"{name.lower().replace(' ', '+')}+budget+travel",
        daily_budget=daily,
        cheapest_month="Shoulder season months",
        currency=country.get("currency", "Local currency"),
        cost_level=cost_level,
        hostel=int(daily * 0.25),
        budget_hotel=int(daily * 0.45),
        airbnb=int(daily * 0.35),
        street_food=int(daily * 0.10),
        local_restaurant=int(daily * 0.20),
        grocery=int(daily * 0.08),
        transit=int(daily * 0.10),
        bus=int(daily * 0.15),
        free_activities_yaml=free_activities_yaml,
        expense_answer=f"{name} is {cost_level.lower()} for tourists. Budget travelers can manage on ${daily}/day with careful planning.",
        intro=f"Traveling {name} on a budget is {feasibility}. This guide shows you how to maximize experiences while minimizing costs.",
        feasibility=feasibility,
        accommodation_text=f"Hostels offer the best value, with dorm beds starting around ${int(daily * 0.25)}. Budget hotels run ${int(daily * 0.45)}+ for private rooms.",
        food_text=f"Street food and local eateries offer meals for ${int(daily * 0.10)}-{int(daily * 0.15)}. Cooking in hostel kitchens saves more.",
        transport_text=f"Public transit averages ${int(daily * 0.10)}/day. Walking is free and the best way to explore.",
        free_activities_text="Many cities offer free walking tours, public parks, and free museum days. Nature areas and beaches are typically free.",
        budget_accommodation_tips="Book hostels with kitchens to save on food costs. Look for weekly discounts for longer stays.",
        eating_cheap_text="Follow the locals - street vendors and small family restaurants offer the best value and authenticity."
    )

    return content


def generate_solo_female_content(country: dict) -> str:
    """Generate solo female travel guide content for a country."""
    name = country["name"]
    slug = country["slug"]
    safety_level = country.get("safety_level", "caution")

    # Determine ratings based on safety level
    if safety_level == "safe":
        safety_rating = "High"
        overall_rating = "Excellent"
        harassment_level = "Low"
        night_safety = "Generally Safe"
        solo_friendly = "Very Friendly"
    elif safety_level == "caution":
        safety_rating = "Moderate-High"
        overall_rating = "Good"
        harassment_level = "Low-Moderate"
        night_safety = "Use Caution"
        solo_friendly = "Friendly"
    else:
        safety_rating = "Moderate"
        overall_rating = "Requires Preparation"
        harassment_level = "Moderate"
        night_safety = "Caution Advised"
        solo_friendly = "With Research"

    best_areas = [
        {"name": "Tourist Districts", "safety": "High", "notes": "Well-patrolled, many travelers"},
        {"name": "City Centers", "safety": "High", "notes": "Busy during day, use caution at night"},
        {"name": "Upscale Neighborhoods", "safety": "High", "notes": "Safer but pricier accommodation"}
    ]
    best_areas_yaml = ""
    for area in best_areas:
        best_areas_yaml += f'''  - name: "{area['name']}"
    safety: "{area['safety']}"
    notes: "{area['notes']}"
'''

    content = SOLO_FEMALE_TEMPLATE.format(
        name=name,
        country_slug=slug,
        image_query=f"{name.lower().replace(' ', '+')}+solo+female+travel",
        safety_rating=safety_rating,
        overall_rating=overall_rating,
        harassment_level=harassment_level,
        night_safety=night_safety,
        solo_friendly=solo_friendly,
        dresscode="Varies by area - research local customs",
        best_areas_yaml=best_areas_yaml,
        cultural_tip_1="Research local customs before visiting religious sites",
        cultural_tip_2="Learn basic phrases in the local language",
        cultural_tip_3="Observe how local women dress and behave",
        practical_tip_1="Download offline maps and translation apps",
        practical_tip_2="Keep emergency contacts easily accessible",
        practical_tip_3="Book accommodations with good reviews from solo female travelers",
        safety_answer=f"{name} is {overall_rating.lower()} for solo female travelers. Most women report positive experiences with standard precautions.",
        dress_answer=f"Dress codes in {name} vary by region. Research specific areas you'll visit and pack versatile, modest options.",
        night_answer=f"Night safety in {name}: {night_safety}. Stick to well-lit, busy areas and use trusted transportation.",
        intro=f"Solo female travel in {name} is {overall_rating.lower()}. This guide covers everything women need to know for a safe, enjoyable trip.",
        safety_overview=f"Women traveling alone in {name} generally report {('very positive' if safety_level == 'safe' else 'positive')} experiences. Standard precautions ensure smooth travels.",
        cultural_section=f"Understanding local culture enhances your experience in {name}. Observe local women for cues on dress and behavior.",
        best_areas_text="Tourist districts and city centers offer the safest environments for solo female travelers, with good infrastructure and other travelers nearby.",
        dress_section=f"Pack versatile clothing appropriate for {name}'s climate and culture. Layers and modest options work well.",
        night_section=f"{night_safety}. Use reputable transportation apps, stay in well-lit areas, and trust your instincts.",
        social_section="Hostels, tours, and travel apps help connect with other solo travelers. Many women find travel companions along the way.",
        top_tip_1="Trust your instincts - they're your best safety tool",
        top_tip_2="Share your itinerary with someone back home",
        top_tip_3="Book first nights in advance for peace of mind",
        top_tip_4="Join women's travel groups for destination-specific advice",
        top_tip_5="Carry a doorstop or portable lock for extra security"
    )

    return content


def generate_activity_content(country: dict, activity: str) -> str:
    """Generate activity page content for a country."""
    name = country["name"]
    slug = country["slug"]
    region = country.get("region", "")

    # Activity-specific details
    activity_details = {
        "Hiking": {"difficulty": "Moderate", "cost": "20-100", "season": "Spring/Fall", "gear": ["Hiking boots", "Daypack", "Water bottle", "Sunscreen"]},
        "Temples": {"difficulty": "Easy", "cost": "5-20", "season": "Year-round", "gear": ["Modest clothing", "Comfortable shoes", "Camera"]},
        "Street Food Tours": {"difficulty": "Easy", "cost": "15-50", "season": "Year-round", "gear": ["Empty stomach", "Cash", "Camera"]},
        "Meditation Retreats": {"difficulty": "Easy", "cost": "50-200", "season": "Year-round", "gear": ["Comfortable clothes", "Open mind", "Journal"]},
        "Cooking Classes": {"difficulty": "Easy", "cost": "30-80", "season": "Year-round", "gear": ["Appetite", "Camera", "Notebook"]},
        "Museums": {"difficulty": "Easy", "cost": "10-25", "season": "Year-round", "gear": ["Comfortable shoes", "Camera", "Notebook"]},
        "Food Tours": {"difficulty": "Easy", "cost": "40-100", "season": "Year-round", "gear": ["Appetite", "Comfortable shoes", "Cash for extras"]},
        "Wine Tasting": {"difficulty": "Easy", "cost": "30-100", "season": "Harvest season", "gear": ["ID", "Designated transport", "Notebook"]},
        "Architecture Tours": {"difficulty": "Easy", "cost": "15-40", "season": "Year-round", "gear": ["Camera", "Comfortable shoes", "Guide book"]},
        "Beach Activities": {"difficulty": "Easy-Moderate", "cost": "20-80", "season": "Summer", "gear": ["Swimsuit", "Sunscreen", "Towel"]},
        "Wildlife Tours": {"difficulty": "Moderate", "cost": "50-200", "season": "Varies", "gear": ["Binoculars", "Camera", "Neutral clothing"]},
        "Adventure Sports": {"difficulty": "Challenging", "cost": "50-200", "season": "Varies", "gear": ["Athletic wear", "Insurance", "Camera"]},
        "Safari": {"difficulty": "Easy", "cost": "150-500", "season": "Dry season", "gear": ["Binoculars", "Camera", "Neutral clothing", "Hat"]},
        "Cultural Tours": {"difficulty": "Easy", "cost": "20-60", "season": "Year-round", "gear": ["Camera", "Comfortable shoes", "Respect"]},
        "Wildlife Photography": {"difficulty": "Moderate", "cost": "100-300", "season": "Varies", "gear": ["Camera with zoom", "Tripod", "Patience"]},
        "Desert Tours": {"difficulty": "Moderate", "cost": "80-250", "season": "Cooler months", "gear": ["Sun protection", "Layers", "Water"]},
        "Diving": {"difficulty": "Moderate-Challenging", "cost": "80-200", "season": "Varies", "gear": ["Certification", "Swimsuit", "Underwater camera"]},
        "Photography": {"difficulty": "Easy", "cost": "Free-50", "season": "Year-round", "gear": ["Camera", "Extra batteries", "Memory cards"]},
        "Walking Tours": {"difficulty": "Easy", "cost": "Free-30", "season": "Year-round", "gear": ["Comfortable shoes", "Water", "Camera"]},
    }

    details = activity_details.get(activity, {"difficulty": "Easy", "cost": "30-80", "season": "Year-round", "gear": ["Comfortable clothes", "Camera"]})

    # Parse cost
    cost_str = details["cost"]
    if "-" in str(cost_str):
        cost_low = cost_str.split("-")[0]
    else:
        cost_low = str(cost_str)

    # Format gear list
    gear_yaml = "\n".join([f'  - "{g}"' for g in details["gear"]])

    # Format spots
    spots = [
        {"name": "Popular destination 1", "rating": "Excellent", "notes": "Top-rated spot"},
        {"name": "Hidden gem 2", "rating": "Great", "notes": "Less crowded alternative"},
        {"name": "Local favorite 3", "rating": "Authentic", "notes": "Off the beaten path"}
    ]
    spots_yaml = ""
    for spot in spots:
        spots_yaml += f'''  - name: "{spot['name']}"
    rating: "{spot['rating']}"
    notes: "{spot['notes']}"
'''

    content = ACTIVITY_TEMPLATE.format(
        activity=activity,
        activity_lower=activity.lower(),
        name=name,
        country_slug=slug,
        image_query=f"{name.lower().replace(' ', '+')}+{activity.lower().replace(' ', '+')}",
        difficulty=details["difficulty"],
        cost=cost_low,
        best_season=details["season"],
        solo_friendly="Yes",
        spots_yaml=spots_yaml,
        group_tour=int(int(cost_low) * 1.5) if cost_low.isdigit() else 50,
        private_tour=int(int(cost_low) * 3) if cost_low.isdigit() else 100,
        self_guided="Possible" if activity not in ["Safari", "Diving"] else "Not recommended",
        gear_yaml=gear_yaml,
        solo_answer=f"Absolutely! {activity} in {name} is very solo-friendly. Group tours make it easy to join others.",
        intro=f"{activity} in {name} offers incredible experiences for solo travelers. Whether joining a group or exploring independently, you'll find plenty of options.",
        spots_text=f"The best spots for {activity.lower()} in {name} range from popular tourist favorites to hidden local gems.",
        solo_tips=f"Join group tours to meet other travelers. Many {activity.lower()} experiences are designed for mixed groups, making solo participation easy.",
        tours_text=f"Group tours (${int(int(cost_low) * 1.5) if cost_low.isdigit() else 50}) offer convenience and social opportunities. Self-guided options work well for independent travelers.",
        gear_text="Pack light but prepared. Most gear can be rented locally if needed.",
        safety_text=f"Follow guide instructions and stay within designated areas. Travel insurance covering {activity.lower()} is recommended.",
        social_text=f"Tours and organized activities are great for meeting fellow {activity.lower()} enthusiasts. Hostels often organize group trips.",
        rental=int(int(cost_low) * 0.3) if cost_low.isdigit() else 15,
        self_guided_cost="Free to minimal" if activity not in ["Safari", "Diving"] else "Not recommended without guides",
        season_text=f"The ideal time for {activity.lower()} in {name} is {details['season']}."
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

    # Generate city pages and city safety pages
    city_count = 0
    city_safety_count = 0
    for city in cities:
        country_slug = city.get("country_slug", "")
        city_slug = city.get("slug", "")

        if not country_slug or not city_slug:
            continue

        # Generate city destination page
        content = generate_city_content(city)
        filepath = CONTENT_DIR / "destinations" / country_slug / city_slug / "_index.md"
        save_content(content, filepath)
        city_count += 1

        # Generate city safety page
        city_safety_content = generate_city_safety_content(city)
        city_safety_filepath = CONTENT_DIR / "safety" / country_slug / city_slug / "_index.md"
        save_content(city_safety_content, city_safety_filepath)
        city_safety_count += 1

    print(f"Generated {city_count} city pages")
    print(f"Generated {city_safety_count} city safety pages")

    total_safety = len(countries) + city_safety_count

    # Generate itinerary pages (1 week, 2 weeks, 3 weeks for each country)
    itinerary_count = 0
    itinerary_durations = [("1 Week", 7), ("2 Weeks", 14), ("3 Weeks", 21)]
    for country in countries:
        slug = country["slug"]
        if not slug or "/" in slug:
            continue

        for duration, days in itinerary_durations:
            content = generate_itinerary_content(country, duration, days)
            duration_slug = duration.lower().replace(" ", "-")
            filepath = CONTENT_DIR / "itineraries" / slug / duration_slug / "_index.md"
            save_content(content, filepath)
            itinerary_count += 1

    print(f"Generated {itinerary_count} itinerary pages")

    # Generate budget guides
    budget_count = 0
    for country in countries:
        slug = country["slug"]
        if not slug or "/" in slug:
            continue

        content = generate_budget_guide_content(country)
        filepath = CONTENT_DIR / "budget" / slug / "_index.md"
        save_content(content, filepath)
        budget_count += 1

    print(f"Generated {budget_count} budget guide pages")

    # Generate solo female travel guides
    female_count = 0
    for country in countries:
        slug = country["slug"]
        if not slug or "/" in slug:
            continue

        content = generate_solo_female_content(country)
        filepath = CONTENT_DIR / "solo-female" / slug / "_index.md"
        save_content(content, filepath)
        female_count += 1

    print(f"Generated {female_count} solo female travel pages")

    # Generate activity pages
    activity_count = 0
    for country in countries:
        slug = country["slug"]
        region = country.get("region", "")
        if not slug or "/" in slug:
            continue

        # Get activities for this region
        activities = REGION_ACTIVITIES.get(region, DEFAULT_ACTIVITIES)

        for activity in activities:
            content = generate_activity_content(country, activity)
            activity_slug = activity.lower().replace(" ", "-")
            filepath = CONTENT_DIR / "activities" / slug / activity_slug / "_index.md"
            save_content(content, filepath)
            activity_count += 1

    print(f"Generated {activity_count} activity pages")

    # Calculate totals
    base_pages = len(countries) + city_count
    guide_pages = total_safety + itinerary_count + budget_count + female_count + activity_count
    total_pages = base_pages + guide_pages

    print(f"\n{'='*50}")
    print("Content Generation Summary")
    print(f"{'='*50}")
    print(f"Country pages:       {len(countries)}")
    print(f"City pages:          {city_count}")
    print(f"Safety pages:        {total_safety}")
    print(f"Itinerary pages:     {itinerary_count}")
    print(f"Budget guides:       {budget_count}")
    print(f"Solo female guides:  {female_count}")
    print(f"Activity pages:      {activity_count}")
    print(f"{'='*50}")
    print(f"TOTAL PAGES:         {total_pages}")
    print(f"{'='*50}")


if __name__ == "__main__":
    generate_all_content()
