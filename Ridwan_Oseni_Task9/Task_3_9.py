name = input("Enter your name: ")
age = int(input("Enter your Age: "))
if age >= 18:
    print("you are eligible")
else:
    print("you are not eligible")
gender = input("gender: ")
courses = input("courses: ")
user1 = {
    "name": name,
    "age": age,
    "gender": gender,
    "courses": [courses]
}
print(f"{user1["name"]}\t{user1["age"]}\n{user1["gender"]}\t{user1["courses"]}")