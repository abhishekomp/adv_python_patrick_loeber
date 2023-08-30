# Adds new functionality to the function "dosomething"
# A decorator is a function that takes another function and add new functionality


# This is the decorator function
def start_end_decorator(func):
    def wrapper():
        print("start")
        func()
        print("end")

    return wrapper


@start_end_decorator
def print_name():
    print("Alex")


# print_name = start_end_decorator(print_name)
print_name()
