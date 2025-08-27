# upper()
# convert all characters in the string to uppercase
name = "Ada Balogun"
print(name.upper())

# lower()
# convert all characters in the string to lowercase
sentence = "PYTHON IS AMAZING"
print(sentence.lower())
print(sentence.title())

# strip()
# remove whitespace( or specified characters) from both ends of the string
text = "   Abuja  "
print(text.strip())

# replace
# replace occurences of a substring with another substring
message = "I love Java"
print(message.replace("Java", "Python"))

# swapcase()
# switch lowercase to uppercase and vice versa
text = "hello ABEOKUTA"
print(text.swapcase())

# lstrip()
# remove whitespace (or specified characters) from the left side only
text = "   Nigeria"
print(text.lstrip())

# rstrip()
# remove whitespace (or specified characters) from the right side only
text = "Nigeria    "
print(text.rstrip())

# # split()
# # split a string into a list using separator (default is space)
fruits ="mango  orange banana"
print(fruits.split())

# rsplit()
# split a string into a list from the right side
text = "one,two,three,four"
print(text.rsplit())
print(text.rsplit(",",2))

# splitlines()
# split a string into a list at each newline(\n)
lines = "line 1\nline 2\nline 3"
print(lines.splitlines())

# join()
# join a list of strings into one string with a specified separator
words = ["I", "love", "Python"]
print(" ".join(words))

# center()
# center the string with a specified width, padding with spaces or characters
text = "Python"
print(text.center(20,"-"))

#ljust()
# left-aligns the string within a specified width, padding with spaces or characters
text = "Python"
print(text.ljust(10, "*"))

# rjust()
# right-aligns the string within a specified width, padding with spaces or characters
text = "Python"
print(text.rjust(10, "*"))

# zfill()
# pad a numeric string on the left with zeros until it reaches a given length
num = "42"
print(num.zfill(5))

# isalpha()
# check if the strings contain only letters
print("Lagos".isalpha())
print("Lagos123".isalpha())

# isdigit
# check if the strings contain only letters
print("12345".isdigit())
print("123a".isdigit())

# isalnum()
# check if the string contains only letters and digits
print("Python3".isalnum())
print("Python 3".isalnum())



# Reverse a string
text = "ABEOKUTA"
print(text[::-1])

