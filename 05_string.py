# Strings: ordered, immutable, text representation
my_string = "Hello World"
print(my_string)
my_string = "I'm a good boy"
print(my_string)

my_string = """Hello \
World!"""
print(my_string)

# Substring
my_string = "Hello World"
char = my_string[0]
print(char)  # prints H

char = my_string[-1]  # is the last character
print(char)

# Slicing
my_string = "Hello World"
subStr = my_string[1:5]  # from index 1 till 4
print(subStr)  # prints ello

subStr1 = my_string[:5]  # No start index means start from index 0
print(subStr1)  # prints Hello
subStr2 = my_string[:]  # No end index means go till end
print(subStr2)  # prints Hello World

subStr3 = my_string[::2]  # Every 2nd character

# Reverse a String
my_string = "Hello World"
reversedStr = my_string[::-1]  # Reverse a string
print(reversedStr)

# Concatenate string
greeting = "Hello"
name = "Joe"
sentence = greeting + " " + name
print(sentence)

# Iterate over a String
greeting = "Hello"
for char in greeting:
    print(char)

# Check if a character or a sub-string is present in a given string
greeting = "Hello"
if "e" in greeting:
    print("yes")
else:
    print("no")

# Stripping white space
my_string = "  Hello World  "
my_string_stripped = my_string.strip()
print(my_string_stripped)

# Convert to upper case
greeting = "Hello"
greeting_upper = greeting.upper()
print(greeting_upper)
print(greeting)

# Check if a given string starts with a character or sub-string
my_string = "Hello World"
print(my_string.startswith("H"))  # True
print(my_string.endswith("d"))  # True
print(my_string.endswith("World"))  # True

# Find the index of a character or sub-string in a given string (Returns the 1st index where found)
my_string = "Hello World"
print(my_string.find("o"))  # returns 4
print(my_string.find("lo"))  # returns 3
print(my_string.find("lop"))  # returns -1

# Count the number of times a character/sub-string in a given string
my_string = "Hello World"
print(my_string.count("o"))  # returns 2

# Replace
my_string = "Hello World"
my_string_modified = my_string.replace("World", "Universe")
print(my_string.replace("World", "Universe"))

print(
    my_string.replace("Worrld", "Universe")
)  # Does nothing as it cannot find the string "Worrld"

# Convert a string to a list
my_string = "How are you doing"
my_list = my_string.split()  # By default the delimiter is a space
print(my_list)

my_string = "How,are,you,doing"
my_list = my_string.split(",")
print(my_list)

# Convert a list to a string
my_list = ["How", "are", "you", "doing"]
new_string = "".join(my_list)
print(new_string)  # Howareyoudoing

new_string = " ".join(my_list)
print(new_string)  # prints "How are you doing"
