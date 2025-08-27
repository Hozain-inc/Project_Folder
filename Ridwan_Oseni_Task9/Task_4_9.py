student = {}
items_list = ['Name', 'Age', 'Scores']
name = input('Enter name here ')
age = int(input('Enter your age here '))

student['scores'] = [65, 70 ,85]
if sum(student['scores']) / len(student['scores']) >= 50:
    print('Passed')
else:
    print('Failed')