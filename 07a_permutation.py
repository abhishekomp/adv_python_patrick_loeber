from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# Specify the length of the permutation
perm = permutations(a, 2)
print(list(perm))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
