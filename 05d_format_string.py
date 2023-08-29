# 3 ways:
# %, .format, f-String
# https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings

var = 3.14159265359
var2 = 6.898
my_string = "The value of variable is: %.2f" % var
my_string = "The value of variable is: {}".format(var)
my_string = "The value of variable is: {:.2f} and {}".format(var, var2)
print(my_string)

# Using f-string
# Controlling the number of digits after the decimal point using f-String.
var3 = 1.14589
my_string2 = f"The value of var3 is {var3:.2f}"
print(my_string2)
my_string = f"The value of variable is {var} and {var2} and {var3:.2f}"
print(my_string)
