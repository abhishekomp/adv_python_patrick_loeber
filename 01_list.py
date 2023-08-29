mylist = ["banana", "cherry", "apple"]
print(mylist)

#Creating a blank list
mylist2 = list()
mylist2.append("Volvo")
print(mylist2)

#IndexError

print(mylist[-1])
# -1 is the last element

# Number of elements in a list
len(mylist)

# Insert element at specific index
mylist.insert(1, "blueberry")
print(mylist)

# Remove the last item from the list
item = mylist.pop()

# Remove specific element
mylist.remove("cherry")
mylist.remove("cherryy") #throws error that the item is not present in the list

# clear the list
#mylist.clear()

# reverse a list
mylist.reverse()

#sort a list
mylist.sort() # Sorts method sort the list in place

new_list = sorted(mylist) #if you do not want to sort the original list

# Create a list with 5 zeros
mylist = [0] * 5

# Concat 2 lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2


