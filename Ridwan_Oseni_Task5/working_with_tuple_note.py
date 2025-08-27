# Using parentheses ()
fruits = ("apple", "banana", "cherry")
print(fruits)

# without parentheses
numbers = 1, 2, 3
print(numbers)
gadgets = "iphone", "tecno", "itel", "samsung"
print(gadgets)

# simgle-item tuple
single_item = ("apple",)
print(single_item)
print(type(single_item))

# using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# Ordered
colours = ("red", "green", "blue")
print(colours[0])
print(colours[0:2])
print(colours[1:3])
print(colours[0:3:2])

# Immutable 
#colors[1] = "yellow"
# print(colour[1])

# allow duplicates
numbers = (1, 2, 2, 3)
print(numbers)

# mixed data types
mixed = ("apple", 3, True,  5.6)
print(mixed)

# nested tuples
nested = (("a", "b"), (1, 2))
print(nested)

# Tuple Operations
# indexing
fruits = ("apples", "banana", "cherry")
print(fruits[0])
# slicing
print(fruits[0:2])
print(fruits[::-1])

# concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)

# repetition
nums = (1, 2)
print(nums*3)

# membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

# iteration
for fruit in fruits:
    print(fruit)

# UNPACKING TUPLES
person = ("John", 25, "Nigeria")
name, age, country = person
print(name)     
print(age)     
print(country)  
person2 = ("Ridwan", 26, "Nigeria")
name, age, country = person2
print(name)
print(age)
print(country)

# Tuple Methods
# dot count() and dot index()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2))
print(numbers.index(3))

# Tuple to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)
l = tuple(lst)
print(l)

# built-in functions with tuples
nums = (4, 1, 7, 3)
print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))