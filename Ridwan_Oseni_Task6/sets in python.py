# using curly braces
fruits = {"apples", "banana", "mango"}
print(fruits)

# using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)

# creating an empty set "set() not set{}"
empty_set = set()
print(empty_set)

# From a string (duplicates removed automatically)
letter = set("mississippi")
print(letter)

# adding elements
colours = {"red", "blue"}
colours.add("green")
print(colours)

# removing elements
colours.remove("blue")
print(colours)

# pop an element
removed = colours.pop()
print("Removed:", removed)
print("Remaining:", colours)
colours.add("Yellow")
print(colours)

# clear a set
colours.clear()
print(colours)

# MATHEMATICAL SET OPERATIONS
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# union set
print(set1 | set2)
print(set1.union(set2))

# intersection
print(set1 & set2)
print(set1.intersection(set2))

# difference
print(set1 - set2)
print(set2 - set1)

# symmetric difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))


# WORKING WITH SETS
# Collecting unique visitors to an event
visitors = set()
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu")
print("Visitors:", visitors)
name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")