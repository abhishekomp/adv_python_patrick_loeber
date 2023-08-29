# Collections: Counter, namedtuple, OrderedDict, defaultDict, deque
# Counter: It is a container which stores the elements as dictionary keys and their count as dictionary value
from collections import Counter

a = "aaaabbbbbcc"
my_counter = Counter(a)
print(my_counter)

for key, value in my_counter.items():
    print(f"{key}->{value}")

all_keys = my_counter.keys()
print(list(all_keys))

# Most common element
print(my_counter.most_common(1))  # Note: This returns a list of tuples
print(
    my_counter.most_common(1)[0]
)  # This will now give the 1st tuple from the list which is ('b', 5) in this case
print(
    my_counter.most_common(1)[0][0]
)  # This now gives the most common element in our string.

# Question:
# Given a string find the most common character in the string. For example, in the string "Hello", 'l' is the most common.
given_string = "Hello"
character = Counter(given_string).most_common(1)[0][0]
print(f"Most common character is: {character}")
