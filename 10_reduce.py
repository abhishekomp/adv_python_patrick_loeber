# Reduce function
from functools import reduce

a = [1, 2, 3, 4]
# compute the product of all elements
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
