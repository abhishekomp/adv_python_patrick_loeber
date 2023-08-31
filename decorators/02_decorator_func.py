# Corey
def decorator_function(original_function):
    def wrapper_function():
        print(f"\nwrapper executed this before '{original_function.__name__}'")
        return original_function()

    return wrapper_function


@decorator_function
def display():
    print("Display function ran")


# decoreated_display = decorator_function(display)
# decoreated_display()

display()
