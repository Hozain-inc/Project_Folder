# basic usage of print()
print("Hello, world!")
print("Welcome to python programming.")

# using print() with variables
name = "Ridwan"
age = "26"
print("Name:", name)
print("age:", age)
print("Name:", name,"\n" "age:", age)

# using f-strings with print()
name = "Bimbo"
score = 92
print(f"{name} scored {score} in her last examination")

# using string concatenation
first_name = "Ridwan"
last_name = "Oseni"
middle_name = "Obasanjo"
print("Full name: "+ first_name + " " + last_name)
print("Full name: " + first_name + " " + middle_name + " " + last_name)

# comma vs concatenation
print("Hello", "world!")
print("Hello" + " " + "world!")

# escape sequence in print - "\n", "\t"
print("Item1\nItem2") 
print("Item1\tItem2")
print("He said, \"Hello\"")
print("it\'s Python!")

# Newline (\n)
print("Welcome to Python\nLet's learn together!")

# Tab (\t)
print("Name\tAge\tLocation")
print("Ridwan\t26\tAbeokuta")

# Quote inside string
print("She said, \"Hello there!\"")
print("He asked, \"why did it take forever?\"")
print('it\'s a sunny day')

# backlash
print("File path: C:\\Users\\Aisha\\Documents")
print("File path: C:\\Usera\\Ridwan\\Downloads")

# Carriage return(\r)
print("123456\rABC")

# Backspace (\b)
print("Helloo\b") 

print("\a")
print("Hello\fworld")

# Using sep and end in print
print("Python", "is", "fun", sep=" - ")
print("This is the first line.", end=" ")
print("This is the second line.")

# GETTING STARTED WITH INPUT() STATEMENT
# basic usage of input()
name = input("Enter your name: ")
print("Hello,", name)
print("How are you,", name)

# convert input to integer
age = int(input("Enter your age:"))
print(f"You will be {age + 1} years old next year.")


# calculator using input
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
diff_in_num = num1 - num2
print(diff_in_num)
print(f"The difference between {num1} and {num2} is {diff_in_num}")
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}")