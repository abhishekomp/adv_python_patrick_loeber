from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

# d.pop()
d.popleft()
# d.clear()
print(d)

d.extend([4, 5, 6])
print(d)

# rotate deque
d = deque()
d.append(1)
d.append(2)
d.extend([3, 4])
print(d)  # prints deque([1, 2, 3, 4])

# d.rotate() # prints deque([4, 1, 2, 3])
# d.rotate(2) # results in deque([3, 4, 1, 2])
d.rotate(-1)  # results in deque([2, 3, 4, 1])
print(d)
