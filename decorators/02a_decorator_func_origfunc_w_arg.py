# Corey
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"\nwrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("Display function ran")


@decorator_function
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


display()
display_info("John", 25)
