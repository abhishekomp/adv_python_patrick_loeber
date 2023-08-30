import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# def encode_user(o):
#     if isinstance(o, User):
#         return {"name": o.name, "age": o.age, o.__class__.__name__: True}
#     else:
#         raise TypeError("Object of type User is not JSON serilizable")


user = User("Max", 27)

from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {
                "name": o.name,
                "age": o.age,
                o.__class__.__name__: True,
            }  # this is a dictionary object
        return JSONEncoder.default(self, o)


# dumps = Dump as a String
# Below statement without default will give error. We need to write a custom encoding function
# userJson = json.dumps(user, default=encode_user)

# 2nd way of encoding Custom object to JSON String
# userJson = json.dumps(user, cls=UserEncoder)

# 3rd way of encoding Custom object
userJson = UserEncoder().encode(user)

print(userJson)

# dump it into a file Try this.
with open("user.json", "w") as f:
    json.dump(userJson, f, indent=4)
