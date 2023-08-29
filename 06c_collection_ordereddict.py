# It is similar to a normal dictionary with the difference that it will have a default value if the key has not been set yet.

from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
d["c"] = 3

print(f"Default Dictionary: {d}")
print(d["a"])  # prints 1
print(
    d["d"]
)  # prints default value of int i.e. 0. A normal dictionary would return an error when the key does not exist
