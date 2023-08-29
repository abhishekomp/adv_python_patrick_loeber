from timeit import default_timer as timer

# Creates a list with 100000 'a'
my_list = ["a"] * 1000000


# not so good way to create the string from the list
start = timer()
my_string = ""
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)
# print(my_string)

# better way to create the string from list
start = timer()
my_string = "".join(my_list)
stop = timer()
print(stop - start)
# print(my_string)  # prints aaaaaa
