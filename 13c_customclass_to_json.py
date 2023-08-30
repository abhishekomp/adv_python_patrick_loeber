# Serializing (Encoding) a custom class object to JSON String
# Converting a custom class object instance to JSON String
import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {
            "name": o.name,
            "age": o.age,
            o.__class__.__name__: True,
        }  # this is dictionary
    else:
        raise TypeError("Object of type User is not JSON serilizable")


user = User("Max", 27)
# dumps = Dump as a String
# Below statement without "default" will give error. We need to write a custom encoding function
userJson = json.dumps(user, default=encode_user)

print(userJson)
