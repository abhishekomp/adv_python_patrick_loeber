def outer_function():
    message = "Hi"

    def inner_function():
        print(
            message
        )  # Inner function has access to the variable in outer function. Free variable.

    return inner_function


myfunc = outer_function()  # inner function is returned waiting to be executed
myfunc()
myfunc()
myfunc()
