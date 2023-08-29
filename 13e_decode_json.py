import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)

from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


# 3rd way of encoding Custom object
userJson = UserEncoder().encode(user)
print(userJson)


def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict["name"], age=dict["age"])
    return dict


# Converting Json to normal Python oject
# this will give a dictionary object
# user = json.loads(userJson)
user = json.loads(userJson, object_hook=decode_user)
print(type(user))
print(user.name)
