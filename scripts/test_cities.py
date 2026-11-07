import json

with open("scripts/cities.json", encoding="utf-8") as f:
    cities = json.load(f)

print(type(cities), len(cities))
for city in cities:
    print(city["ville"], city["latitude"], city["longitude"])