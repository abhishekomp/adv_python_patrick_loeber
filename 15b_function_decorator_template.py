# Adds new functionality to the function "dosomething"
# A decorator is a function that takes another function and add new functionality
import functools


# This is the decorator function
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result

    return wrapper


@my_decorator
def add5(x):
    return x + 5


# print_name = start_end_decorator(print_name)
result = add5(10)
print(result)
# print(help(add5))
# print(add5.__name__)
