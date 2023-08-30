# Random module for Pseudo Random Numbers
# Secret module for Cryptographic strong random number
# NumPy module for arrays with random numbers

import random

# Numbers seem random but can be re-produced

# Random float in the range 0 to 1
a = random.random()
print(a)  # results s float for example 0.12371739303467688

a = random.uniform(1, 2)
print(a)  # random float in the range. for example: 1.9678604023252113

# Generate a random integer
a = random.randint(1, 10)  # upper bound is included
print(a)

# Generate a random integer
a = random.randrange(1, 10)  # upper bound is NOT included
print(a)

# Mu and Sigma
a = random.normalvariate(0, 1)
print(a)  # useful when working in statistics. Mean and deviation concept involved here.

# Random module has different functions to work with Sequences
# Working with sequences (example: list)

# Pick a random character from a list
mylist = list("ABCDEF")
print(mylist)  # ['A', 'B', 'C', 'D', 'E', 'F']
a = random.choice(mylist)
print(a)

# Pick more than 1 random unique elements from a list (No duplication)
myList = list("ABCDEF")
print(myList)  # ['A', 'B', 'C', 'D', 'E', 'F']
a = random.sample(myList, 3)
print(a)

# For duplication of random elemets
myList = list("ABCDEF")
print(myList)  # ['A', 'B', 'C', 'D', 'E', 'F']
a = random.choices(myList, k=3)
print(a)  # can return ['F', 'D', 'D']

# Random shuffle our list in place
myList = list("ABCDEF")
random.shuffle(myList)
print(myList)


# Reproducing the random result using seed function
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
