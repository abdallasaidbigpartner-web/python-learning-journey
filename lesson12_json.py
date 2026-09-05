"""
Lesson 12: Working with JSON

Demonstrates converting Python dictionaries to/from JSON, both via
files (json.dump/json.load) and via strings (json.dumps/json.loads)
- the standard format for APIs and config data.
"""

import json

profile = {
    "name": "Abdalla",
    "age": 20,
    "skills": ["Python", "Git", "SQL"]
}

with open("profile.json", "w") as file:
    json.dump(profile, file)

with open("profile.json", "r") as file:
    loaded_profile = json.load(file)

print(loaded_profile["name"])
print(loaded_profile["skills"])

json_string = json.dumps(profile)
print(json_string)

parsed_back = json.loads(json_string)
print(parsed_back["age"])
