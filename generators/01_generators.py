# A generator is a function that returns an object that can be iterated over.
# they generate the items in the object lazily hence they are efficient


def mygenerator():
    yield 3
    yield 2
    yield 1


g = mygenerator()
print(g)

# for i in g:
#     print(i)

# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)

# print(sum(g))

print(sorted(g))
