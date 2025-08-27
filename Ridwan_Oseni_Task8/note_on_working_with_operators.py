a = 10
b = 20
# print(a == b)
print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(b <= 25)
# print(a >= 10)

# score = 75
# print(score >= 50)
# print(score < 50)
# print(score == 100)

# Assignment Operators
x = 10
print("initial value:", x)
x += 5
print("After x += 5:", x)
x -= 2
print("After x -= 2:", x)
x *= 3
print("After x *= 3:", x)
x /= 4
print("After x /= 4:", x)
x %= 3
print("After x %= 3:", x)
x //= 3
print("After x //= 3:", x)
x = 4
x **= 2
print("After x **= 2:", x)

# Use case Example:
# Define variables
balance = 1000
deposit = 200
withdraw = 150

balance += deposit
balance -= withdraw
print("Updated balance:", balance)

# LOGICAL OPERATORS
x = 10
y = 20

# and operator
print(x > 5 and y > 15)
# or operator
print(x < 5 or y > 15)
# not operator
print(not(x == 10))

# Use case example1 - Scholarship Eligibility
#Define variables
age = 17
score = 85
# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)
print("Scholarship Eligible:", eligible)

# Federal Government scholarship
 

#Use case example2 - Event Access
# age = 22
# has_ticket = False
# can_enter = (age >= 18) and (has_ticket or age < 25)
# print("Access Granted:", can_enter)


name = "Oseni"
score = 40
passed = (score >= 50)
print("Passed:", passed)

name = "Oba"
age = 15
teenager = (age >= 13) and (age <= 19)
print("Teenager:", teenager)