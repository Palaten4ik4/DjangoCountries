# countries/utils.py

import json

def load_countries_from_file(filename="country-by-languages.json"):
    with open(filename, "r") as file:
        return json.load(file)
