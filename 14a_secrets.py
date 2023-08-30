# Disadvantage of secrets module: Takes time for the algorithm but they will generate a true random number
# Has only 3 functions
import secrets

a = secrets.randbelow(10)  # It implies from 0 till 10. Upper bound is not included
print(a)

a = secrets.randbits(4)
print(a)

myList = list("ABCDEF")
a = secrets.choice(myList)  # results in random choice not reproducible
print(a)
