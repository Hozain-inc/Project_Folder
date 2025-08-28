
import data
import utils

#To add some students
data.add_student("Paul", "AI Engineering")
data.add_student("Blessing", "AI Development")

# Print formatted student records
for s in data.get_students():
    print(utils.format_student(s))