# We have a python dictionary object which we want to convert into json string
# This is also called as serialization or encoding
# Also dump it to file
# In JSON format, False is written in lowercase like false
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

# Dump python dictionary object to a file
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)
