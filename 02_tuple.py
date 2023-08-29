mytuple = ("Max", 28, "boston")
mytuple2 = "Max", 28, "boston"
mytuple = ("Max",) # just 1 element in tuple
# mytuple = {"Max"} # Not recognized as a tuple

#Creating a tuple from an iterable for example a list
mytuple3 = tuple(["Max", 28, "boston"]) 
print(mytuple3)

# Access element from a tuple. Index based

#Iterate over a tuple
for i in mytuple:
    print(i)

# Checking if an element is in a tuple
if "boston" in mytuple:
    print("present")
else:
    print("not present")

# Get number of elements inside a tuple
print(len(mytuple))

# Count some element inside an element
print(mytuple.count("boston"))

# Index of an element
mytuple = ("Max", 28, "boston")
print(mytuple.index("boston")) #gives the index of the element boston

# Create a list from a tuple and vice versa
mylist = list(mytuple) #get list from a tuple

# Slicing with tuple

# Reverse a tuple
reversed_tuple = mytuple[::-1]

# Unpacking a tuple
my_tuple = "Max", 28, "boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

# Compare a tuple with a list
# tuple can be efficient when working with a large number of data
