import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

personJSON = json.dumps(person, indent=4, sort_keys=True)  # results in JSON String
# print(personJSON)

# Convert from JSONString to Python Dictionary
# Decode json data
person = json.loads(personJSON)
print(person)

# Read JSON from a file and create a Python Dictionary
with open("person.json", "r") as file:
    person = json.load(file)
    print(person)
