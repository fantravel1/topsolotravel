# TopSoloTravel.com — Static Site Architecture

## Overview

Build **50,000+ static HTML pages** using Hugo + GitHub Pages, powered entirely by free data sources. Programmatic SEO targeting long-tail solo travel keywords across destinations, venues, safety guides, and practical travel information.

---

## GitHub Pages Constraints

- **1 GB max repository size** — HTML files are tiny, this supports 100,000+ pages easily
- **100 GB bandwidth/month** — sufficient for ~2-3M pageviews/month
- **No file count limit** — can have unlimited HTML files
- **Build via GitHub Actions** — bypasses 10 builds/hour limit

---

## Page Taxonomy — 50,000+ Pages

### 1. DESTINATION PAGES (~15,000 pages)

#### Country Pages (200 pages)
```
/destinations/japan/
/destinations/thailand/
/destinations/portugal/
```
**Data source:** RestCountries API + Wikidata + Wikivoyage

**Content:**
- Country overview for solo travelers
- Safety summary
- Visa requirements
- Best cities for solo travel
- Budget breakdown
- Cultural tips

#### City Pages (5,000 pages)
```
/destinations/japan/tokyo/
/destinations/thailand/bangkok/
/destinations/portugal/lisbon/
```
**Data source:** GeoNames (11M+ places) + OpenStreetMap + Wikivoyage

**Content:**
- Solo travel guide
- Neighborhoods for solo travelers
- Getting around alone
- Where to stay
- Where to eat solo
- Things to do alone
- Safety notes
- Cost breakdown

#### Neighborhood Pages (10,000 pages)
```
/destinations/japan/tokyo/shibuya/
/destinations/japan/tokyo/shinjuku/
/destinations/thailand/bangkok/khao-san/
```
**Data source:** OpenStreetMap administrative boundaries + Wikidata

**Content:**
- Neighborhood vibe for solo travelers
- Best solo-friendly spots
- Safety assessment
- Walkability
- Nearby attractions

---

### 2. VENUE PAGES (~20,000 pages)

#### Restaurants for Solo Diners (8,000 pages)
```
/eat/tokyo/solo-dining-guide/
/eat/paris/best-restaurants-bar-seating/
/eat/new-york/solo-friendly-restaurants/
```
**Data source:** OpenStreetMap (`amenity=restaurant`) + Wikidata

**Content:**
- Restaurants with bar seating
- Counter dining options
- Solo-friendly atmosphere
- Price range
- Cuisine type
- Hours

#### Cafes for Solo Travelers (4,000 pages)
```
/cafes/tokyo/work-friendly-cafes/
/cafes/lisbon/laptop-friendly-cafes/
/cafes/bali/digital-nomad-cafes/
```
**Data source:** OpenStreetMap (`amenity=cafe`) + wifi tags

**Content:**
- WiFi availability
- Power outlets
- Solo-friendly seating
- Laptop policy
- Hours
- Noise level

#### Bars for Solo Travelers (4,000 pages)
```
/nightlife/tokyo/solo-friendly-bars/
/nightlife/barcelona/bars-to-meet-people/
```
**Data source:** OpenStreetMap (`amenity=bar`, `amenity=pub`)

**Content:**
- Bar seating availability
- Atmosphere (social vs quiet)
- Safety notes
- Best nights to visit
- Solo traveler tips

#### Hotels & Hostels (4,000 pages)
```
/stay/tokyo/best-hostels-solo-travelers/
/stay/paris/hotels-no-single-supplement/
/stay/bali/social-hostels/
```
**Data source:** OpenStreetMap (`tourism=hotel`, `tourism=hostel`) + Wikivoyage

**Content:**
- Solo traveler suitability
- Social atmosphere rating
- Common areas
- Location safety
- Price range
- Booking tips

---

### 3. SAFETY PAGES (~5,000 pages)

#### Country Safety Guides (200 pages)
```
/safety/japan/
/safety/colombia/
/safety/thailand/
```
**Data source:** US State Dept API + UK FCDO API + Canadian advisories

**Content:**
- Overall safety rating
- Current travel advisories
- Health requirements
- Scam warnings
- Emergency contacts
- Solo-specific risks

#### Solo Female Safety Guides (200 pages)
```
/safety/japan/solo-female/
/safety/india/solo-female/
/safety/morocco/solo-female/
```
**Data source:** Government advisories + Georgetown WPS Index (public reports)

**Content:**
- Female-specific safety tips
- Dress code considerations
- Areas to avoid
- Transportation safety
- Harassment prevention
- Emergency resources

#### City Safety Guides (2,000 pages)
```
/safety/tokyo/
/safety/mexico-city/
/safety/johannesburg/
```
**Data source:** US State Dept + UNODC crime statistics + OSM

**Content:**
- Neighborhood safety breakdown
- Safe areas for solo travelers
- Areas to avoid at night
- Transportation safety
- Scam alerts
- Emergency numbers

#### LGBTQ+ Safety Guides (200 pages)
```
/safety/japan/lgbtq/
/safety/uae/lgbtq/
/safety/netherlands/lgbtq/
```
**Data source:** Wikidata legal status + public legal databases

**Content:**
- Legal status
- Social acceptance
- Safe neighborhoods
- LGBTQ+ venues
- Pride events
- Safety tips

#### Health & Vaccination Guides (200 pages)
```
/health/thailand/
/health/kenya/
/health/brazil/
```
**Data source:** CDC travel health RSS + WHO APIs

**Content:**
- Required vaccinations
- Recommended vaccinations
- Health risks
- Medical facilities
- Travel insurance tips
- Medication rules

---

### 4. PRACTICAL GUIDES (~5,000 pages)

#### Visa Requirement Pages (2,000 pages)
```
/visas/us-passport/japan/
/visas/uk-passport/thailand/
/visas/indian-passport/schengen/
```
**Data source:** Passport Index Dataset (GitHub, MIT license)

**Content:**
- Visa required/free status
- Visa-free duration
- E-visa availability
- Application process
- Cost
- Processing time

#### Cost of Living Guides (500 pages)
```
/budget/tokyo/
/budget/bali/
/budget/lisbon/
```
**Data source:** World Bank data + Wikidata + Wikivoyage

**Content:**
- Daily budget breakdown
- Accommodation costs
- Food costs
- Transportation costs
- Activity costs
- Money-saving tips

#### Getting Around Guides (500 pages)
```
/transport/tokyo/
/transport/bangkok/
/transport/rome/
```
**Data source:** OpenStreetMap transit + GTFS feeds + Wikivoyage

**Content:**
- Public transit overview
- Airport connections
- Getting around solo
- Safety tips
- Apps to download
- Cost breakdown

#### Weather & Best Time to Visit (500 pages)
```
/weather/tokyo/
/weather/bali/
/weather/iceland/
```
**Data source:** Met Norway API (free, global) + historical averages

**Content:**
- Monthly weather breakdown
- Best months for solo travel
- Rainy season
- Peak vs shoulder season
- Packing tips
- Event calendar

#### Language & Communication (200 pages)
```
/language/japan/
/language/thailand/
/language/brazil/
```
**Data source:** RestCountries + Wikidata + Wikivoyage phrasebooks

**Content:**
- Official languages
- English proficiency
- Essential phrases
- Translation app tips
- SIM card/eSIM info
- WiFi availability

---

### 5. ACTIVITY PAGES (~3,000 pages)

#### Things to Do Solo (2,000 pages)
```
/activities/tokyo/solo/
/activities/paris/solo/
/activities/new-york/solo/
```
**Data source:** OpenStreetMap (`tourism=attraction`, `tourism=museum`) + Wikidata + Wikivoyage

**Content:**
- Top solo-friendly activities
- Free activities
- Walking tours
- Museums & galleries
- Day trips
- Meetup opportunities

#### National Parks & Nature (500 pages)
```
/nature/usa/yellowstone/
/nature/japan/fuji/
/nature/new-zealand/milford-sound/
```
**Data source:** Wikidata + OpenStreetMap + NPS API (US parks)

**Content:**
- Solo hiking safety
- Trail difficulty
- Best time to visit
- Getting there alone
- Accommodation options
- Safety tips

#### UNESCO World Heritage Sites (500 pages)
```
/unesco/japan/kyoto-temples/
/unesco/peru/machu-picchu/
/unesco/cambodia/angkor/
```
**Data source:** Wikidata (UNESCO property P757)

**Content:**
- Site overview
- Visiting solo
- Getting there
- Best time to visit
- Nearby accommodation
- Safety notes

---

### 6. COMPARISON & LIST PAGES (~2,000 pages)

#### Best Destinations Lists (500 pages)
```
/best/solo-travel-destinations-2025/
/best/solo-female-travel-destinations/
/best/cheapest-solo-travel-destinations/
/best/safest-countries-solo-travel/
```
**Data source:** Aggregated from other pages + editorial

#### City Comparisons (500 pages)
```
/compare/tokyo-vs-seoul-solo-travel/
/compare/lisbon-vs-barcelona-solo/
/compare/bali-vs-thailand-solo/
```
**Data source:** Aggregated data from city pages

#### Monthly Destination Guides (500 pages)
```
/when/best-solo-destinations-january/
/when/best-solo-destinations-february/
/when/where-to-go-solo-summer/
```
**Data source:** Weather data + event calendars

#### Budget Category Pages (500 pages)
```
/budget-travel/under-50-day/
/budget-travel/under-100-day/
/luxury-solo-travel/
```
**Data source:** Aggregated from city budget pages

---

## Free Data Sources Summary

| Data Type | Source | License | API/Download |
|-----------|--------|---------|--------------|
| POI (restaurants, bars, hotels) | OpenStreetMap Overpass | ODbL | API |
| City/country data | RestCountries | Free | API |
| Structured data | Wikidata | CC0 | SPARQL API |
| Travel content | Wikivoyage | CC BY-SA | API/dumps |
| Place names | GeoNames | CC BY | API (10K/day free) |
| US travel advisories | State Dept | Public domain | JSON API |
| UK travel advisories | FCDO | OGL | JSON API |
| Canadian advisories | Canada.gc | OGL-Canada | JSON API |
| Health advisories | CDC | Public domain | RSS |
| Visa requirements | Passport Index Dataset | MIT | GitHub CSV |
| Weather | Met Norway | CC | API |
| US parks | NPS | Public domain | API |
| Currency | Frankfurter | Free | API |
| Images | Unsplash/Pexels/Pixabay | Free commercial | API |

---

## URL Structure

```
topsolotravel.com/
├── destinations/
│   ├── {country}/
│   │   ├── index.html
│   │   └── {city}/
│   │       ├── index.html
│   │       └── {neighborhood}/
├── eat/
│   └── {city}/
├── stay/
│   └── {city}/
├── nightlife/
│   └── {city}/
├── cafes/
│   └── {city}/
├── safety/
│   ├── {country}/
│   │   ├── index.html
│   │   ├── solo-female/
│   │   └── lgbtq/
│   └── {city}/
├── visas/
│   └── {passport}/
│       └── {destination}/
├── budget/
│   └── {city}/
├── transport/
│   └── {city}/
├── weather/
│   └── {city}/
├── activities/
│   └── {city}/
├── nature/
│   └── {country}/
│       └── {park}/
├── unesco/
│   └── {country}/
│       └── {site}/
├── best/
│   └── {list-slug}/
├── compare/
│   └── {comparison-slug}/
└── when/
    └── {month-slug}/
```

---

## Hugo Build Process

### 1. Data Collection Scripts (Python)
```
/scripts/
├── fetch_countries.py      # RestCountries API
├── fetch_cities.py         # GeoNames API
├── fetch_venues.py         # OpenStreetMap Overpass
├── fetch_safety.py         # Government APIs
├── fetch_visas.py          # Parse Passport Index CSV
├── fetch_weather.py        # Met Norway API
└── fetch_wikivoyage.py     # Wikivoyage API
```

### 2. Data Storage
```
/data/
├── countries.json
├── cities.json
├── venues/
│   ├── tokyo-restaurants.json
│   ├── tokyo-bars.json
│   └── ...
├── safety/
├── visas/
└── weather/
```

### 3. Hugo Templates
```
/layouts/
├── destinations/
│   ├── country.html
│   ├── city.html
│   └── neighborhood.html
├── venues/
│   ├── restaurants.html
│   ├── bars.html
│   └── hotels.html
├── safety/
│   ├── country.html
│   ├── city.html
│   └── female.html
└── _default/
    ├── baseof.html
    └── list.html
```

### 4. Content Generation
```bash
# Generate markdown files from data
python scripts/generate_content.py

# Build static site
hugo --minify

# Output: 50,000+ HTML files in /public
```

### 5. GitHub Actions Workflow
```yaml
name: Build and Deploy
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * 0'  # Weekly rebuild

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v3
      - name: Fetch fresh data
        run: python scripts/fetch_all.py
      - name: Build
        run: hugo --minify
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

---

## Page Priority for Launch

### Phase 1: Foundation (5,000 pages)
- [ ] 200 country destination pages
- [ ] 500 top city destination pages
- [ ] 200 country safety pages
- [ ] 200 solo female safety pages
- [ ] 500 city safety pages
- [ ] Top 100 visa requirement combinations
- [ ] 50 "best of" list pages

### Phase 2: Venue Expansion (15,000 pages)
- [ ] Restaurant guides for top 500 cities
- [ ] Cafe guides for top 300 cities
- [ ] Bar guides for top 300 cities
- [ ] Hotel/hostel guides for top 500 cities

### Phase 3: Deep Content (30,000 pages)
- [ ] Neighborhood pages for top 200 cities
- [ ] All visa combinations (2,000+)
- [ ] Weather guides
- [ ] Transport guides
- [ ] Activity pages
- [ ] UNESCO/nature pages

### Phase 4: Comparison & Programmatic (50,000+ pages)
- [ ] City vs city comparisons
- [ ] Monthly destination guides
- [ ] Budget category pages
- [ ] Long-tail keyword pages

---

## SEO Implementation

### On-Page Elements (Hugo Templates)
```html
<!-- Title tag -->
<title>{{ .Title }} | Top Solo Travel</title>

<!-- Meta description -->
<meta name="description" content="{{ .Params.description }}">

<!-- Canonical -->
<link rel="canonical" href="{{ .Permalink }}">

<!-- Schema.org -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TravelGuide",
  "name": "{{ .Title }}",
  "description": "{{ .Params.description }}",
  "author": {
    "@type": "Organization",
    "name": "Top Solo Travel"
  }
}
</script>
```

### Internal Linking Strategy
- Every city links to its country
- Every country links to its cities
- Every venue page links to city guide
- Every safety page links to destination
- Contextual links in content
- Related destinations in sidebar

### Sitemap Generation
Hugo generates sitemap.xml automatically. Submit to:
- Google Search Console
- Bing Webmaster Tools

---

## Attribution Requirements

Footer must include:
```
Data: © OpenStreetMap contributors | Wikivoyage (CC BY-SA) | 
US State Department | UK FCDO | CDC | Met Norway | GeoNames
```

---

## Estimated Build Stats

| Metric | Estimate |
|--------|----------|
| Total HTML pages | 50,000+ |
| Average page size | 15-25 KB |
| Total repository size | 500-800 MB |
| Hugo build time | 30-60 seconds |
| GitHub Actions minutes | ~5 min/build |

---

## Next Steps

1. **Set up Hugo project structure**
2. **Create data fetching scripts**
3. **Build base templates**
4. **Generate Phase 1 content (5,000 pages)**
5. **Deploy to GitHub Pages**
6. **Submit sitemap to search engines**
7. **Monitor indexing in Search Console**
8. **Expand to Phase 2-4**
