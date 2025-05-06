import json

EXPECTED_KEYS = {"name", "code", "visited", "cities"}
CITY_KEYS = {"name", "latitude", "longitude", "visited"}


def validate_wandertrack_json(filepath: str) -> bool:
    try:
        with open(filepath, encoding='utf-8') as f:
            countries = json.load(f)

        if not isinstance(countries, list):
            raise TypeError("❌ Root element should be a list of countries")

        for i, country in enumerate(countries):
            if not isinstance(country, dict):
                raise TypeError(f"❌ Country at index {i} is not a dictionary")

            missing_country_keys = EXPECTED_KEYS - country.keys()
            if missing_country_keys:
                raise KeyError(f"❌ Country '{country.get('name', f'index {i}')}' is missing keys: {missing_country_keys}")

            if not isinstance(country["cities"], list):
                raise TypeError(f"❌ 'cities' field for country '{country['name']}' must be a list")

            for j, city in enumerate(country["cities"]):
                if not isinstance(city, dict):
                    raise TypeError(f"❌ City at index {j} in country '{country['name']}' is not a dictionary")

                missing_city_keys = CITY_KEYS - city.keys()
                if missing_city_keys:
                    raise KeyError(
                        f"❌ City '{city.get('name', f'index {j}')}' in country '{country['name']}' "
                        f"is missing keys: {missing_city_keys}"
                    )

        print("✅ wandertrack.json is valid.")
        return True

    except Exception as e:
        print(str(e))
        return False