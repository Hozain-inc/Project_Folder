# An Empty list using square brackets and list()
# empty_list = []
# print(empty_list)

# empty_list = list()
# print(empty_list)

# List of integers
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# List of strings
# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# Mixed data types
# mixed_list = ["Alice", 25, 5.8, True]
# print(mixed_list)

# From a string (each character becomes an element)
# chars = list("hello")
# print(chars)

# From a tuple
# my_tuple = (10, 20, 30)
# list_from_tuple = list(my_tuple)
# print(list_from_tuple)

# From a range
# numbers_range = list(range(5))
# print(numbers_range)

# Squares of numbers 0-4
# squares = [x**2 for x in range(5)]
# print(squares)

# squares = [x**2 for x in range(5,9)]
# print(squares)

# Even numbers between 0-10
# evens = [x for x in range(11) if x % 2 == 0]
# print(evens)

# odds = [x for x in range(11) if x % 3 == 1]
# print(odds)

# Matrix-like list
# matrix = [[1, 2], [3, 4], [5, 6]]
# print(matrix)

# print(matrix[0])
# print(matrix[0][1])
# print(matrix[2])

# CHARACTERISTICS OF A LIST
# Ordered Collection
# fruits = ["mango", "orange", "banana", "pawpaw"]
# print(fruits)
# print(fruits[1])
# print(fruits[2])
# print(fruits[1:4:2])
# print(fruits[0:5:3])
# print(fruits[2:5])
# print(fruits[1:3])
# print(fruits[1:4])

# Allows duplicate
# items = ["rice", "beans", "yam", "rice"]
# print(items)

# Mutable
# numbers = [1, 2, 3]
# numbers[1] = 20
# print(numbers)
# numbers[2] = 15
# print(numbers)

# Contains different data types
# mixed = [10, "Nigeria", 3.14, True]
# print(mixed)

# Can be nested
# nested_list = [[1, 2], ["a", "b"]]
# print(nested_list)
# print(nested_list[0][1])
# print(nested_list[1])

# Dynamic size
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)