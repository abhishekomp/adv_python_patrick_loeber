# Working with arrays
import numpy as np

# Generate an array with random floats
a = np.random.rand(3)
print(a)  # [0.26356291 0.45868199 0.99337123]

# Generate an array with random Integers
a = np.random.randint(
    0, 10, 3
)  # upperbound is excluded. 0, 10 is the range and 3 is the size
print(a)  # [6 7 8]

# Shuffle
