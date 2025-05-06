import csv
import json
import pycountry
from collections import defaultdict

INPUT_DATA_PATH = 'worldcities.csv'
OUTPUT_DATA_PATH = 'wandertrack.json'

custom_country_map = {
    "Korea, South": "KR",
    "Korea, North": "KP",
    "Russia": "RU",
    "Turkey": "TR",
    "Congo (Kinshasa)": "CD",  # Democratic Republic of the Congo
    "Congo (Brazzaville)": "CG",  # Republic of the Congo
    "Burma": "MM",  # Myanmar
    "Côte d’Ivoire": "CI",
    "Gambia, The": "GM",
    "Bahamas, The": "BS",
    "Macau": "MO",
    "Reunion": "RE",
    "Gaza Strip": "PS",
    "West Bank": "PS",
    "Brunei": "BN",
    "Kosovo": "XK",  # not ISO official but commonly used
    "Saint Martin": "MF",
    "Sint Maarten": "SX",
    "Saint Barthelemy": "BL",
    "Bonaire, Sint Eustatius, and Saba": "BQ",
    "Svalbard": "SJ",
    "Vatican City": "VA",
    "Saint Helena, Ascension, and Tristan da Cunha": "SH",
    "South Georgia and South Sandwich Islands": "GS",
    "South Georgia And South Sandwich Islands": "GS",
    "Pitcairn Islands": "PN",
    "U.S. Virgin Islands": "VI",
    "Falkland Islands (Islas Malvinas)": "FK"
}


def get_country_code(name):
    try:
        return custom_country_map.get(country_name) or pycountry.countries.lookup(country_name).alpha_2
    except LookupError:
        return ''  # If not found, leave empty

countries = defaultdict(list)

with open(INPUT_DATA_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country = row['country']
        city = {
            'name': row['city'],
            'latitude': float(row['lat']),
            'longitude': float(row['lng']),
            'population': float(row['population']) if row['population'] else 0
        }
        countries[country].append(city)

# Build structured data with ISO_A2
structured_data = []
for country_name, cities in countries.items():
    iso_code = get_country_code(country_name)
    if iso_code == '':
        print(f"[WARN] ISO code not found for: {country_name}")
    sorted_cities = sorted(cities, key=lambda x: x['population'], reverse=True)
    top_cities = sorted_cities[:10]
    structured_data.append({
        'name': country_name,
        'code': iso_code,
        'visited': False,
        'cities': [{'name': c['name'], 'visited': False, 'latitude': c['latitude'], 'longitude': c['longitude']} for c in top_cities]
    })

with open(OUTPUT_DATA_PATH, 'w', encoding='utf-8') as jsonfile:
    json.dump(structured_data, jsonfile, indent=2, ensure_ascii=False)

print(f"Generated {OUTPUT_DATA_PATH} with {len(structured_data)} countries.")
