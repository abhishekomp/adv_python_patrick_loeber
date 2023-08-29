# Dictionary is mutable.
# Creating a dictionary
mydict = {"name": "Max", "age": 28, "city": "Boston"}
print(mydict)

# Creating a dictionary
mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

name_val = mydict["name"]
print(name_val)

# KeyError: 'last_name'
# name_val = mydict["last_name"] #will throw exception because there is no key named "last_name"
print(name_val)

# Adding a new entry to a dictionary
mydict["email"] = "max@xyz.com"
print(mydict)

# Delete an entry from a dictionary
del mydict["name"]
print(mydict)

# Delete using pop
mydict.pop("age")

mydict.popitem()  # Removes the last inserted entry

# To check if the key in present in the dictionary
if "name" in mydict:
    print(mydict["name"])

# Loop through a dictionary
for key in mydict.keys():
    print(key)

# for key, value in mydict.items:
#     print(key, value)

# Copy a dictionary (Be careful with this way)
mydict_copy = mydict
print(mydict_copy)  # Both dictionaries point to the same dictionary in the memory.

mydict_copy = dict(mydict)

# Using copy() method for copying a dictionary, then the original dictionary will not be affected if you change the new one
mydict_copy = mydict.copy()

# Merge 2 dictionaries

# Key can be a number as well

# A Tuple can also be used as a key in the dictionary
mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)
# A list can not be used as a key. List is mutable and therefore it is also not hasable.
