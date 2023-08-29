# map
a = [1, 2, 3, 4]
b = map(lambda x: x * x, a)
print(list(b))  # result [1, 4, 9, 16]

# Achieve the same thing using list comprehension
b = [x * x for x in a]
print(b)  # result [1, 4, 9, 16]

# Filter
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))  # result [2, 4, 6]

# Achieve the same filter thing using list comprehension
a = [1, 2, 3, 4, 5, 6]
b = [x for x in a if x % 2 == 0]
print(b)  # result [2, 4, 6]
