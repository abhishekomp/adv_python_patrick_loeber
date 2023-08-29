from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)  # [1, 2, 3, 4]
print(list(acc))  # [1, 3, 6, 10]

acc = accumulate(a, func=operator.mul)
print(a)  # [1, 2, 3, 4]
print(list(acc))  # [1, 2, 6, 24]

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)  # [1, 2, 5, 3, 4]
print(list(acc))  # [1, 2, 5, 5, 5]
