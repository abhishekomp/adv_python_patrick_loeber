# Similar to list comprehension
import sys

mygenerator = (i for i in range(100000) if i % 2 == 0)
# print(list(mygenerator))
print(sys.getsizeof(mygenerator))
# for i in mygenerator:
#     print(i)

mylist = [i for i in range(100000) if i % 2 == 0]
# print(mylist)
print(sys.getsizeof(mylist))
