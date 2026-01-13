#!/usr/bin/env python3
"""
Fetch city data for solo travel destinations.
Uses curated data with coordinates for major cities.
GeoNames API can be integrated for additional data (requires free registration).
"""

import json
from pathlib import Path
from typing import Optional

DATA_DIR = Path(__file__).parent.parent / "data"

# Curated list of top solo travel cities with essential data
# Population data from various sources, coordinates from GeoNames
TOP_CITIES = [
    # Japan
    {"name": "Tokyo", "country": "Japan", "country_slug": "japan", "region": "Asia",
     "lat": 35.6762, "lng": 139.6503, "population": 13960000,
     "safety": "safe", "budget": "80-150", "highlights": ["temples", "food", "technology"],
     "best_time": "Mar-May, Oct-Nov", "airport": "NRT/HND"},
    {"name": "Kyoto", "country": "Japan", "country_slug": "japan", "region": "Asia",
     "lat": 35.0116, "lng": 135.7681, "population": 1475000,
     "safety": "safe", "budget": "70-130", "highlights": ["temples", "geisha", "gardens"],
     "best_time": "Mar-May, Oct-Nov", "airport": "KIX"},
    {"name": "Osaka", "country": "Japan", "country_slug": "japan", "region": "Asia",
     "lat": 34.6937, "lng": 135.5023, "population": 2750000,
     "safety": "safe", "budget": "65-120", "highlights": ["street food", "nightlife", "castle"],
     "best_time": "Mar-May, Oct-Nov", "airport": "KIX"},

    # Thailand
    {"name": "Bangkok", "country": "Thailand", "country_slug": "thailand", "region": "Asia",
     "lat": 13.7563, "lng": 100.5018, "population": 10539000,
     "safety": "caution", "budget": "35-70", "highlights": ["temples", "street food", "nightlife"],
     "best_time": "Nov-Feb", "airport": "BKK"},
    {"name": "Chiang Mai", "country": "Thailand", "country_slug": "thailand", "region": "Asia",
     "lat": 18.7883, "lng": 98.9853, "population": 131000,
     "safety": "safe", "budget": "30-60", "highlights": ["temples", "cooking classes", "digital nomads"],
     "best_time": "Nov-Feb", "airport": "CNX"},
    {"name": "Phuket", "country": "Thailand", "country_slug": "thailand", "region": "Asia",
     "lat": 7.9519, "lng": 98.3381, "population": 416582,
     "safety": "caution", "budget": "40-80", "highlights": ["beaches", "islands", "diving"],
     "best_time": "Nov-Apr", "airport": "HKT"},

    # Portugal
    {"name": "Lisbon", "country": "Portugal", "country_slug": "portugal", "region": "Europe",
     "lat": 38.7223, "lng": -9.1393, "population": 544851,
     "safety": "safe", "budget": "55-100", "highlights": ["tram 28", "pasteis de nata", "alfama"],
     "best_time": "Apr-Oct", "airport": "LIS"},
    {"name": "Porto", "country": "Portugal", "country_slug": "portugal", "region": "Europe",
     "lat": 41.1579, "lng": -8.6291, "population": 237591,
     "safety": "safe", "budget": "50-90", "highlights": ["port wine", "bridges", "ribeira"],
     "best_time": "May-Sep", "airport": "OPO"},
    {"name": "Lagos", "country": "Portugal", "country_slug": "portugal", "region": "Europe",
     "lat": 37.1028, "lng": -8.6732, "population": 31049,
     "safety": "safe", "budget": "45-85", "highlights": ["beaches", "cliffs", "surfing"],
     "best_time": "May-Oct", "airport": "FAO"},

    # Spain
    {"name": "Barcelona", "country": "Spain", "country_slug": "spain", "region": "Europe",
     "lat": 41.3851, "lng": 2.1734, "population": 1620343,
     "safety": "caution", "budget": "65-120", "highlights": ["gaudi", "beaches", "tapas"],
     "best_time": "Apr-Jun, Sep-Oct", "airport": "BCN"},
    {"name": "Madrid", "country": "Spain", "country_slug": "spain", "region": "Europe",
     "lat": 40.4168, "lng": -3.7038, "population": 3223334,
     "safety": "safe", "budget": "60-110", "highlights": ["museums", "nightlife", "tapas"],
     "best_time": "Apr-Jun, Sep-Oct", "airport": "MAD"},
    {"name": "Seville", "country": "Spain", "country_slug": "spain", "region": "Europe",
     "lat": 37.3891, "lng": -5.9845, "population": 688592,
     "safety": "safe", "budget": "50-90", "highlights": ["flamenco", "alcazar", "tapas"],
     "best_time": "Mar-May, Sep-Nov", "airport": "SVQ"},

    # Italy
    {"name": "Rome", "country": "Italy", "country_slug": "italy", "region": "Europe",
     "lat": 41.9028, "lng": 12.4964, "population": 2873000,
     "safety": "caution", "budget": "70-130", "highlights": ["colosseum", "vatican", "pasta"],
     "best_time": "Apr-Jun, Sep-Oct", "airport": "FCO"},
    {"name": "Florence", "country": "Italy", "country_slug": "italy", "region": "Europe",
     "lat": 43.7696, "lng": 11.2558, "population": 382258,
     "safety": "safe", "budget": "65-120", "highlights": ["art", "duomo", "tuscany"],
     "best_time": "Apr-Jun, Sep-Oct", "airport": "FLR"},
    {"name": "Venice", "country": "Italy", "country_slug": "italy", "region": "Europe",
     "lat": 45.4408, "lng": 12.3155, "population": 261905,
     "safety": "safe", "budget": "80-150", "highlights": ["canals", "architecture", "islands"],
     "best_time": "Apr-Jun, Sep-Oct", "airport": "VCE"},

    # France
    {"name": "Paris", "country": "France", "country_slug": "france", "region": "Europe",
     "lat": 48.8566, "lng": 2.3522, "population": 2161000,
     "safety": "caution", "budget": "90-160", "highlights": ["eiffel tower", "louvre", "cafes"],
     "best_time": "Apr-Jun, Sep-Oct", "airport": "CDG"},
    {"name": "Nice", "country": "France", "country_slug": "france", "region": "Europe",
     "lat": 43.7102, "lng": 7.2620, "population": 342522,
     "safety": "safe", "budget": "80-140", "highlights": ["beaches", "old town", "riviera"],
     "best_time": "May-Sep", "airport": "NCE"},
    {"name": "Lyon", "country": "France", "country_slug": "france", "region": "Europe",
     "lat": 45.7640, "lng": 4.8357, "population": 513275,
     "safety": "safe", "budget": "70-120", "highlights": ["gastronomy", "old town", "traboules"],
     "best_time": "Apr-Oct", "airport": "LYS"},

    # Germany
    {"name": "Berlin", "country": "Germany", "country_slug": "germany", "region": "Europe",
     "lat": 52.5200, "lng": 13.4050, "population": 3645000,
     "safety": "safe", "budget": "60-110", "highlights": ["history", "nightlife", "art"],
     "best_time": "May-Sep", "airport": "BER"},
    {"name": "Munich", "country": "Germany", "country_slug": "germany", "region": "Europe",
     "lat": 48.1351, "lng": 11.5820, "population": 1472000,
     "safety": "safe", "budget": "70-130", "highlights": ["beer gardens", "oktoberfest", "alps"],
     "best_time": "May-Sep", "airport": "MUC"},

    # United Kingdom
    {"name": "London", "country": "United Kingdom", "country_slug": "united-kingdom", "region": "Europe",
     "lat": 51.5074, "lng": -0.1278, "population": 8982000,
     "safety": "caution", "budget": "100-180", "highlights": ["museums", "history", "pubs"],
     "best_time": "May-Sep", "airport": "LHR"},
    {"name": "Edinburgh", "country": "United Kingdom", "country_slug": "united-kingdom", "region": "Europe",
     "lat": 55.9533, "lng": -3.1883, "population": 482005,
     "safety": "safe", "budget": "80-140", "highlights": ["castle", "festivals", "whisky"],
     "best_time": "May-Sep", "airport": "EDI"},

    # Vietnam
    {"name": "Hanoi", "country": "Vietnam", "country_slug": "vietnam", "region": "Asia",
     "lat": 21.0278, "lng": 105.8342, "population": 8054000,
     "safety": "caution", "budget": "25-50", "highlights": ["old quarter", "street food", "culture"],
     "best_time": "Oct-Apr", "airport": "HAN"},
    {"name": "Ho Chi Minh City", "country": "Vietnam", "country_slug": "vietnam", "region": "Asia",
     "lat": 10.8231, "lng": 106.6297, "population": 8993000,
     "safety": "caution", "budget": "25-50", "highlights": ["cu chi tunnels", "street food", "nightlife"],
     "best_time": "Dec-Apr", "airport": "SGN"},
    {"name": "Hoi An", "country": "Vietnam", "country_slug": "vietnam", "region": "Asia",
     "lat": 15.8801, "lng": 108.3380, "population": 120000,
     "safety": "safe", "budget": "25-45", "highlights": ["ancient town", "tailors", "lanterns"],
     "best_time": "Feb-May", "airport": "DAD"},

    # Indonesia
    {"name": "Bali", "country": "Indonesia", "country_slug": "indonesia", "region": "Asia",
     "lat": -8.4095, "lng": 115.1889, "population": 4225000,
     "safety": "caution", "budget": "35-70", "highlights": ["temples", "beaches", "yoga"],
     "best_time": "Apr-Oct", "airport": "DPS"},
    {"name": "Jakarta", "country": "Indonesia", "country_slug": "indonesia", "region": "Asia",
     "lat": -6.2088, "lng": 106.8456, "population": 10562000,
     "safety": "caution", "budget": "35-65", "highlights": ["museums", "food", "history"],
     "best_time": "Jun-Sep", "airport": "CGK"},

    # Australia
    {"name": "Sydney", "country": "Australia", "country_slug": "australia", "region": "Oceania",
     "lat": -33.8688, "lng": 151.2093, "population": 5312000,
     "safety": "safe", "budget": "100-170", "highlights": ["opera house", "beaches", "harbour"],
     "best_time": "Sep-Nov, Mar-May", "airport": "SYD"},
    {"name": "Melbourne", "country": "Australia", "country_slug": "australia", "region": "Oceania",
     "lat": -37.8136, "lng": 144.9631, "population": 5078000,
     "safety": "safe", "budget": "90-160", "highlights": ["coffee", "laneways", "culture"],
     "best_time": "Mar-May, Sep-Nov", "airport": "MEL"},

    # New Zealand
    {"name": "Auckland", "country": "New Zealand", "country_slug": "new-zealand", "region": "Oceania",
     "lat": -36.8509, "lng": 174.7645, "population": 1657000,
     "safety": "safe", "budget": "90-150", "highlights": ["harbour", "islands", "wine"],
     "best_time": "Dec-Mar", "airport": "AKL"},
    {"name": "Queenstown", "country": "New Zealand", "country_slug": "new-zealand", "region": "Oceania",
     "lat": -45.0312, "lng": 168.6626, "population": 15850,
     "safety": "safe", "budget": "100-180", "highlights": ["adventure sports", "scenery", "skiing"],
     "best_time": "Dec-Mar (summer), Jun-Aug (ski)", "airport": "ZQN"},

    # USA
    {"name": "New York City", "country": "United States", "country_slug": "united-states", "region": "Americas",
     "lat": 40.7128, "lng": -74.0060, "population": 8336817,
     "safety": "caution", "budget": "120-220", "highlights": ["broadway", "museums", "food"],
     "best_time": "Apr-Jun, Sep-Nov", "airport": "JFK"},
    {"name": "Los Angeles", "country": "United States", "country_slug": "united-states", "region": "Americas",
     "lat": 34.0522, "lng": -118.2437, "population": 3979576,
     "safety": "caution", "budget": "100-180", "highlights": ["beaches", "hollywood", "food"],
     "best_time": "Mar-May, Sep-Nov", "airport": "LAX"},
    {"name": "San Francisco", "country": "United States", "country_slug": "united-states", "region": "Americas",
     "lat": 37.7749, "lng": -122.4194, "population": 883305,
     "safety": "caution", "budget": "120-200", "highlights": ["golden gate", "tech", "food"],
     "best_time": "Sep-Nov", "airport": "SFO"},

    # Mexico
    {"name": "Mexico City", "country": "Mexico", "country_slug": "mexico", "region": "Americas",
     "lat": 19.4326, "lng": -99.1332, "population": 21782000,
     "safety": "caution", "budget": "45-85", "highlights": ["museums", "food", "history"],
     "best_time": "Mar-May", "airport": "MEX"},
    {"name": "Oaxaca", "country": "Mexico", "country_slug": "mexico", "region": "Americas",
     "lat": 17.0732, "lng": -96.7266, "population": 300050,
     "safety": "safe", "budget": "35-70", "highlights": ["food", "crafts", "mezcal"],
     "best_time": "Oct-May", "airport": "OAX"},

    # Peru
    {"name": "Lima", "country": "Peru", "country_slug": "peru", "region": "Americas",
     "lat": -12.0464, "lng": -77.0428, "population": 10719000,
     "safety": "caution", "budget": "40-80", "highlights": ["ceviche", "history", "miraflores"],
     "best_time": "Dec-Apr", "airport": "LIM"},
    {"name": "Cusco", "country": "Peru", "country_slug": "peru", "region": "Americas",
     "lat": -13.5319, "lng": -71.9675, "population": 428450,
     "safety": "caution", "budget": "35-70", "highlights": ["machu picchu", "inca history", "altitude"],
     "best_time": "May-Sep", "airport": "CUZ"},

    # Colombia
    {"name": "Medellin", "country": "Colombia", "country_slug": "colombia", "region": "Americas",
     "lat": 6.2476, "lng": -75.5658, "population": 2529403,
     "safety": "caution", "budget": "35-70", "highlights": ["transformation", "weather", "nomads"],
     "best_time": "Dec-Mar", "airport": "MDE"},
    {"name": "Cartagena", "country": "Colombia", "country_slug": "colombia", "region": "Americas",
     "lat": 10.3910, "lng": -75.4794, "population": 1028736,
     "safety": "caution", "budget": "45-90", "highlights": ["old town", "beaches", "nightlife"],
     "best_time": "Dec-Apr", "airport": "CTG"},

    # Iceland
    {"name": "Reykjavik", "country": "Iceland", "country_slug": "iceland", "region": "Europe",
     "lat": 64.1466, "lng": -21.9426, "population": 131136,
     "safety": "safe", "budget": "140-220", "highlights": ["northern lights", "hot springs", "nature"],
     "best_time": "Jun-Aug (summer), Sep-Mar (lights)", "airport": "KEF"},

    # Greece
    {"name": "Athens", "country": "Greece", "country_slug": "greece", "region": "Europe",
     "lat": 37.9838, "lng": 23.7275, "population": 664046,
     "safety": "safe", "budget": "55-100", "highlights": ["acropolis", "history", "islands"],
     "best_time": "Apr-Jun, Sep-Oct", "airport": "ATH"},
    {"name": "Santorini", "country": "Greece", "country_slug": "greece", "region": "Europe",
     "lat": 36.3932, "lng": 25.4615, "population": 15550,
     "safety": "safe", "budget": "80-160", "highlights": ["sunsets", "views", "wine"],
     "best_time": "Apr-Oct", "airport": "JTR"},

    # Netherlands
    {"name": "Amsterdam", "country": "Netherlands", "country_slug": "netherlands", "region": "Europe",
     "lat": 52.3676, "lng": 4.9041, "population": 872680,
     "safety": "caution", "budget": "90-150", "highlights": ["canals", "museums", "bikes"],
     "best_time": "Apr-Sep", "airport": "AMS"},

    # Czech Republic
    {"name": "Prague", "country": "Czech Republic", "country_slug": "czech-republic", "region": "Europe",
     "lat": 50.0755, "lng": 14.4378, "population": 1309000,
     "safety": "safe", "budget": "50-90", "highlights": ["old town", "beer", "architecture"],
     "best_time": "Apr-Jun, Sep-Oct", "airport": "PRG"},

    # Croatia
    {"name": "Dubrovnik", "country": "Croatia", "country_slug": "croatia", "region": "Europe",
     "lat": 42.6507, "lng": 18.0944, "population": 42615,
     "safety": "safe", "budget": "70-130", "highlights": ["old town", "game of thrones", "beaches"],
     "best_time": "May-Jun, Sep-Oct", "airport": "DBV"},
    {"name": "Split", "country": "Croatia", "country_slug": "croatia", "region": "Europe",
     "lat": 43.5081, "lng": 16.4402, "population": 178102,
     "safety": "safe", "budget": "60-110", "highlights": ["palace", "islands", "beaches"],
     "best_time": "May-Sep", "airport": "SPU"},

    # Turkey
    {"name": "Istanbul", "country": "Turkey", "country_slug": "turkey", "region": "Europe",
     "lat": 41.0082, "lng": 28.9784, "population": 15460000,
     "safety": "caution", "budget": "40-80", "highlights": ["hagia sophia", "bazaars", "bosphorus"],
     "best_time": "Apr-May, Sep-Nov", "airport": "IST"},

    # Morocco
    {"name": "Marrakech", "country": "Morocco", "country_slug": "morocco", "region": "Africa",
     "lat": 31.6295, "lng": -7.9811, "population": 928850,
     "safety": "caution", "budget": "40-80", "highlights": ["medina", "souks", "riads"],
     "best_time": "Mar-May, Sep-Nov", "airport": "RAK"},

    # South Africa
    {"name": "Cape Town", "country": "South Africa", "country_slug": "south-africa", "region": "Africa",
     "lat": -33.9249, "lng": 18.4241, "population": 433688,
     "safety": "caution", "budget": "50-100", "highlights": ["table mountain", "wine", "beaches"],
     "best_time": "Nov-Mar", "airport": "CPT"},

    # Singapore
    {"name": "Singapore", "country": "Singapore", "country_slug": "singapore", "region": "Asia",
     "lat": 1.3521, "lng": 103.8198, "population": 5686000,
     "safety": "safe", "budget": "80-150", "highlights": ["food", "gardens", "clean"],
     "best_time": "Year-round", "airport": "SIN"},

    # Malaysia
    {"name": "Kuala Lumpur", "country": "Malaysia", "country_slug": "malaysia", "region": "Asia",
     "lat": 3.1390, "lng": 101.6869, "population": 1808000,
     "safety": "safe", "budget": "35-70", "highlights": ["towers", "food", "shopping"],
     "best_time": "May-Jul, Dec-Feb", "airport": "KUL"},

    # India
    {"name": "Delhi", "country": "India", "country_slug": "india", "region": "Asia",
     "lat": 28.7041, "lng": 77.1025, "population": 16787941,
     "safety": "caution", "budget": "25-55", "highlights": ["monuments", "food", "history"],
     "best_time": "Oct-Mar", "airport": "DEL"},
    {"name": "Mumbai", "country": "India", "country_slug": "india", "region": "Asia",
     "lat": 19.0760, "lng": 72.8777, "population": 12442373,
     "safety": "caution", "budget": "30-60", "highlights": ["gateway", "bollywood", "street food"],
     "best_time": "Nov-Feb", "airport": "BOM"},
    {"name": "Jaipur", "country": "India", "country_slug": "india", "region": "Asia",
     "lat": 26.9124, "lng": 75.7873, "population": 3073350,
     "safety": "caution", "budget": "25-50", "highlights": ["pink city", "palaces", "shopping"],
     "best_time": "Oct-Mar", "airport": "JAI"},

    # South Korea
    {"name": "Seoul", "country": "South Korea", "country_slug": "south-korea", "region": "Asia",
     "lat": 37.5665, "lng": 126.9780, "population": 9776000,
     "safety": "safe", "budget": "60-110", "highlights": ["k-culture", "food", "technology"],
     "best_time": "Apr-Jun, Sep-Nov", "airport": "ICN"},
    {"name": "Busan", "country": "South Korea", "country_slug": "south-korea", "region": "Asia",
     "lat": 35.1796, "lng": 129.0756, "population": 3429000,
     "safety": "safe", "budget": "55-100", "highlights": ["beaches", "seafood", "temples"],
     "best_time": "Apr-Jun, Sep-Nov", "airport": "PUS"},

    # Taiwan
    {"name": "Taipei", "country": "Taiwan", "country_slug": "taiwan", "region": "Asia",
     "lat": 25.0330, "lng": 121.5654, "population": 2646000,
     "safety": "safe", "budget": "50-90", "highlights": ["night markets", "temples", "food"],
     "best_time": "Oct-Apr", "airport": "TPE"},
]


def process_city(city: dict) -> dict:
    """Process city data into our format."""
    name_slug = city["name"].lower().replace(" ", "-").replace("'", "")

    return {
        "name": city["name"],
        "slug": name_slug,
        "country": city["country"],
        "country_slug": city["country_slug"],
        "region": city["region"],
        "lat": city["lat"],
        "lng": city["lng"],
        "population": city["population"],
        "safety_level": city["safety"],
        "budget_per_day": city["budget"],
        "highlights": city["highlights"],
        "best_time_to_visit": city["best_time"],
        "airport_code": city.get("airport", ""),
        "image_search": f"{city['name']} {city['country']} travel",
    }


def save_cities(cities: list):
    """Save city data."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Save all cities
    all_cities_path = DATA_DIR / "cities.json"
    with open(all_cities_path, "w", encoding="utf-8") as f:
        json.dump(cities, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(cities)} cities to {all_cities_path}")

    # Save individual city files
    cities_dir = DATA_DIR / "cities"
    cities_dir.mkdir(exist_ok=True)

    for city in cities:
        city_path = cities_dir / f"{city['slug']}.json"
        with open(city_path, "w", encoding="utf-8") as f:
            json.dump(city, f, indent=2, ensure_ascii=False)

    # Group by country
    by_country = {}
    for city in cities:
        country = city["country_slug"]
        if country not in by_country:
            by_country[country] = []
        by_country[country].append(city)

    for country, country_cities in by_country.items():
        country_path = DATA_DIR / "cities" / f"by_country_{country}.json"
        with open(country_path, "w", encoding="utf-8") as f:
            json.dump(country_cities, f, indent=2, ensure_ascii=False)

    return cities


def main():
    """Main function."""
    print("Processing city data...")

    # Process all cities
    processed = [process_city(city) for city in TOP_CITIES]

    # Sort by name
    processed.sort(key=lambda x: x["name"])

    # Save
    save_cities(processed)

    print(f"Processed {len(processed)} cities")
    return processed


if __name__ == "__main__":
    main()
