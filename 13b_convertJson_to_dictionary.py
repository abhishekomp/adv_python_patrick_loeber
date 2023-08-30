# Converting a JSONString (JSONObject) to Python Dictionary
# This is called de-serialization or decoding
import json

# Python Dictionary
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
# Decode json data (convert to python dictionary)
person = json.loads(personJSON)  # loads = load from a string
print(type(person))  # return an obect of type <class 'dict'>
print(person)

# Read JSON from a file and create a Python Dictionary
# Decode JSON data
with open("person.json", "r") as file:
    person = json.load(file)
    print(person)
