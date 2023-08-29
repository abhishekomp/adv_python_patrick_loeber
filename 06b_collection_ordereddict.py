from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["e"] = 5
ordered_dict["a"] = 1

print(f"Ordered Dictionary: {ordered_dict}")

# From Python 3.6 onwards even a normal Dictionary remembers the order of its entries
normal_dict = {}

normal_dict["b"] = 2
normal_dict["c"] = 3
normal_dict["d"] = 4
normal_dict["e"] = 5
normal_dict["a"] = 1

print(f"Normal Dictionary: {normal_dict}")
