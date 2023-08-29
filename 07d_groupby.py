from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))

a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))

persons = [
    {"name": "Tim", "age": 25},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Claire", "age": 28},
]

group_obj = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))
