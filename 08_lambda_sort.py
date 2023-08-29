# lambda argument:expression
add10 = lambda x: x + 10
print(add10(15))

mult = lambda x, y: x * y
print(mult(4, 5))

# Sorting
myList = [(1, 2), (15, -1), (4, 6), (3, 4)]
myList_sorted = sorted(myList)
print(myList)
print(myList_sorted)  # result: [(1, 2), (3, 4), (4, 6), (15, -1)]

# Sort by y axis
myList_sorted = sorted(myList, key=lambda k: k[1])
print(myList)
print(myList_sorted)  # result: [(15, -1), (1, 2), (3, 4), (4, 6)]

# sort by the sum of x-axis and y-axis
myList_sorted = sorted(myList, key=lambda x: x[0] + x[1])
print(myList)
print(myList_sorted)  # result: [(1, 2), (3, 4), (4, 6), (15, -1)]
