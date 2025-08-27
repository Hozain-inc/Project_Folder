# # CONDITIONAL STATEMENT
# # if statement
# age = 20
# if age >= 18:
#     print("You are eligible to vote")

# # if-else statement
# wallet = 400
# price = 500
# if wallet >= price:
#     print("Purchase successful")
# else:
#     print("Insufficient balance")

# # if-elif-else
# score = 69
# if score >= 70:
#     print("Grade A")
# elif score >= 60:
#     print("Grade B")
# else:
#     print("Grade C")

#     # Nested if
#     age = 19
#     citizen = True

#     if age >= 18:
#         if citizen:
#             print("You can vote")
#         else:
#             print("You must be a citizen to vote")
#     else:
#         print("Too young to vote")


# # LOOPS
# # for loop (it is used for iteration)
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(f"I like {fruit}")

# # Iterates through each element in a TUPLE.
# coordinates = (0.34654,-0.48585, 0.57477)
# for point in coordinates:
#     print(f"point: {point}")

# # Iterates through each element in a DICTIONARY.
# student = {"name": "Tunde", "age": 16, "grade": "A"}
# for key, value in student.items():
#     print(f"{key}: {value}")

# # Iterates through each element in a STRING.
# word = "PYTHON"
# for char in word:
#     print(char)    

# # Using while loop


# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1

# # Incrementing with `while`
# num = 1
# while num <= 10:
#     print(num, end=" ")
#     num += 1


# # Decrementing with `while`
# timer = 10
# while timer >= 0:
#     print("Countdown:", timer)
#     timer -= 1

# # While with User Input

# password = " "
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access Granted")

# # While True
# # Keep asking the user for a name until they type "exit".
# while True:
#     name = input("Enter your name (type 'exit' to quit): ")
#     if name.lower() == "exit":
#         print("Goodbye!")
#         break
#     print(f"Hello, {name}")


# #LOOP CONTROL STATEMENTS (break, continue and pass)
# # break
# for num in range(1, 10):
#     if num == 5:
#         break
#     print(num)

# # continue
# for num in range(1, 6):
#     if num == 3:
#         continue
#     print(num)

# # pass
# for num in range(1, 6):
#     if num == 3:
#         pass
#     else:
#         print(num)


# # while True
# while True:
#     print("\nMenu:")
#     print("1. Say Hello")
#     print("2. Say Goodbye")
#     print("3. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         print("Hello")
#     elif choice == "2":
#         print("Goodbye")
#     elif choice == "3":
#         print("Exiting program ...")
#         break
#     else:
#         print("Invalid choice. Try again.")



# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         print(f"Your age is {age}")
#         break
#     else:
      #   print("Invalid input. Please enter a number.")

# secret = "python"

# while True:
#     guess = input("Guess the secret word: ")
#     if guess.lower() == secret:
#         print("Correct!, You guessed the word.")
#         break
#     else:
#         print("Wrong! Try again.")



balance = 1000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM, Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
