# Create a set
# Set is unordered, no duplicates
mySet = {1, 2, 3}
print(mySet)
mySet = {1, 2, 3, 1, 2}
print(mySet)  # Set does not store duplicate elements

# Creating a set using the set method
mySet = set([1, 2, 3])

# We can also use a string to create a set
mySet = set("Hello")
print(mySet)

# Trick: How many different letters are there in a given word/string.
# Use set function to find it because a set in python does not store duplicate element

# Create an empty set
mySet = set()

# A set is mutable
mySet.add(1)
mySet.add(2)
print(mySet)

# Remove an element from a set
mySet.remove(2)
# mySet.remove(4)  # if the element is not present in the set, it will raise key error

# Another way of removing an element
mySet.discard(3)  # if the element is not present in the set, no error is returned

# Empty a set
mySet.clear()

# Using pop() method to remove an artitrary element from the set
mySet = {1, 3, 5}
print("Element removed:", mySet.pop())
print(mySet)

# Looping over a set
mySet = {1, 3, 5}
for i in mySet:
    print(i)

# Union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

# Difference of 2 Sets (This always returns a new set and does not modifies the original set)
# This returns a set with all elements from the 1st set that are not present in the 2nd set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {2, 4, 6, 8, 10}
diffSet = setA.difference(setB)
print(f"Difference of 2 sets: {diffSet}")
diffSet = setB.difference(setA)
print(f"Difference of 2 sets: {diffSet}")

# Symmetric difference method
# This method returns a set of all the elements that are present in both sets but not those elements that are in both the sets
symmetricDiffSet = setA.symmetric_difference(setB)
print(f"Symmetric difference of 2 sets: {symmetricDiffSet}")

# Update a set from another set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {2, 4, 6, 8, 10}
setA.update(setB)
print(setA)

# Intersection_update method
# This updates a set in such a way that only the intersection (common) elements remain after the method execution
setA = {1, 3, 5, 7, 9}
setB = {2, 3, 5, 7, 11}
setA.intersection_update(setB)
print(setA)  # will print {3, 5, 7} as these are the common elements in both sets

# Difference_update
setA = {1, 3, 5, 7, 9}
setB = {2, 3, 5, 7, 11}
setA.difference_update(setB)
print(setA)

# Symmetric difference update
# This is same as symmetric difference method. In addition it updates the 1st set as well.
setA = {1, 3, 5, 7, 9}
setB = {2, 3, 5, 7, 11}
setA.symmetric_difference_update(setB)
print(f"Symmetric difference update: {setA}")

# Sub set
setA = {1, 2, 3, 5, 7, 9}
setB = {1, 2, 3}
setC = {10, 11}
print(setA.issubset(setB))
print(setB.issubset(setA))

print(setA.issuperset(setB))
# No same element in both sets then True
print(f"isDisjoint: {setA.isdisjoint(setB)}")
print(f"isDisjoint: {setA.isdisjoint(setC)}")

# Copy set
setA = {1, 2, 3}
setB = setA
setB.add(5)  # This will change the original set as well
print(setA)
print(setB)

# Copy method 2
setA = {1, 2, 3}
setB = set(setA)

# Copy method 3
setB = setA.copy()

# Frozen Set (is also a collection data type but it is immutable set)
setA = frozenset([1, 2, 3, 4])
setA.add(5)  # Will give an error
setA.remove(1)  # Will give an error
