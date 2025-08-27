# COMMON BUILT-IN FUNCTIONS
#range()
# for i in range(3):
#     print(i)

#zip()
# names =["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

#map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)

#filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)

#Student performance & Feedback system
# name1 = input("Enter first student name: ")
# name2 = input("Enter second student name: ")
# name3 = input("Enter Third student name: ")

# score1 = int(input("Enter score for " + name1 + ": "))
# score2 = int(input("Enter score for " + name2 + ": "))
# score3 = int(input("Enter score for " + name3 + ": "))

# names = [name1, name2, name3]
# scores = [score1, score2, score3]
# print("\nStudent Data")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# ranked = sorted(zip(names, scores), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# upper_names = list(map(lambda n: n.upper(), names))
# print("\nUppercase Names:", upper_names)

# print("\nHelp on len():")
# help(len)


#USERDEFINED FUNCTION
#dEFINING A FUNCTION
# def greet():
#     print("Hello, Welcome to AI Fellowship") 

# greet()
# greet()
# greet()
#Function Arguments and Parameters
#Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to python learning")

#calling with parameter- the actual name
# greet("Class rep")
# greet("Ridwan")

# When to use return, print() and yield keywords inside a function

# def greet(name):
#     print("Hello", name)

# result = greet("Esther")
# print("Result:", result)


#return
# def add(a, b):
#     return a + b
# result = add(4, 6)
# print("The sum is:", result)

#yield
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1
# for number in count_up_to(5) :
#     print(number)

#TYPES OF ARGUMENTS
#Positional Arguments
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")
# introduce("Ngozi", "AI Engineering")
# introduce("AI Engineering", "Ngozi")  #INCORRECT ORDER

#Keyword Arguments
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")
# introduce(name = "Ngozi", track = "AI Engineering")
# introduce(track = "AI Engineering", name = "Ngozi")

#Default Argument
# def introduce(name, track ="AI Engineering"):
#     print("My name is", name)
#     print("I am learning", track, ".")
#     introduce("paul")
    # introduce("Tunji Paul", track = "AI Development")

#Varying length Argument
# non-keyword (Tuple)
# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#         print("Sum:", total)
# add_numbers(2, 4, 6)
# add_numbers(10, 20, 30, 40, 50)

#kEYWORD ARGUMENR (DICTIONARY)
# def student_details(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# student_details(name="Peter", track = "AI Engineering", interest= "Block chain", gender= "Male")

# def participant_profile(name,  age, track="AI Development", *skills, **extra_info):
#     """
#      Generate a profile for a bootcamp participant using different types of arguments.
#     """
#     profile = f"\n--- Bootcamp Participant profile ---\n"
#     profile += f"Name: {name}\n"
#     profile += f"Age: {age}\n"
#     profile += f"Track: {track}\n"
#     if skills:
#         profile += "Skills: " + ", ".join(skills) + "\n"
#     else:
#         profile += "Skills: Not yet specified\n"
#     if extra_info:
#         profile += "Additional Info:\n"
#         for key, value in extra_info.items():
#             profile += f" - {key.capitalize()}: {value}\n"
#     return profile
# print(participant_profile("Peter", 24))
# print(participant_profile("Ridwan", 29, track="AI Engineering"))
# print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine learning"))
# print(participant_profile(
#             "Sophia", 30, "Cybersecurity",
#             "Networking", "Ethical Hacking", "Python",
#             interest="Blockchain", city="Shagamu", phone="080123456789"
#         ))

#NAMESPACE AND SCOPE
#TYPES OF NAMESPACE
#Global Namespace
# employee = "General Employee"

# def IT_department():
#     employee = "Chris (IT)"
#     print("Inside IT departmment:", employee)
# def Training_department():
#     employee = "Chris (Training)"
#     print("Inside Training department:", employee)
# print("In Global Namespace:", employee)
# IT_department()
# Training_department()

#Scope
x = "global x"
def outer():
    x = "enclosing x"

    def inner():
        x = "local x"
        print("Inside inner:", x)

    inner()
    print("Inside outer:", x)

outer()
print("In global:", x)


### Global keyword
# Used when you want to modify a global variable inside a function.

x = 5
def change_global():
    global x
    x = 10

change_global()
print(x)


# nonlocal keyword
#Used in nested functions when you want to modify the variable from the enclosing scope (not global).
def outer():
    x ="outer x"

    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inside inner:", x)

    inner()
    