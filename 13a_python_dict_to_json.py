# We have a python dictionary which we want to convert into json string
# Also dump it to file
import json

# This is a Python Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

personJSON = json.dumps(person, indent=4, sort_keys=True)  # results in JSON String
print(personJSON)

# dump it into a file
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)
