fruits = [
    "Apple",
    "Pears",
    "Banana",
]

fruits_copy = fruits # Be careful. If you make a change to the copy, the original list is also impacted
fruits_copy.append("lemon")
print(fruits_copy)
print(fruits)

# Method 2
fruits_copy = list(fruits)

#Method 3
fruits_copy = fruits.copy()

# Method 4
fruits_copy = fruits[:]

# Creating a list from another list
numList = [1, 2, 3, 4]
b = [i*i for i in numList]
print(b)  # prints [1, 4, 9, 16]