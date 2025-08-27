# creating dictionaries
# using curly braces
student = {"name": "Ada",
           "age": 20,
           "course": "Computer Science"}
print(student)

# using the dict() constructor
student_info = dict(name="John", age=25, course="Maths")
print(student_info)

# empty dictionary
empty_dict = {}
print(empty_dict)

### DICTIONARY COMPREHENSION
# create a dictionary of numbers and their squares
squares = {x: x**2 for x in range (1, 6)}
print(squares)

# Dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(evens_cube)

# from existing dictionary
students = {"Ada": 85, "John": 40, "Musa": 65}
passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)