import csv 
from pathlib import Path

workspace = Path("Workspace_files")
csv_files = workspace / "contacts.csv"

# def Details():

 
# name = input("Enter your name: ").strip()
# while not name:
#     print("Name cannot be empty, Enter participant name: ")
#     continue
# age = int(input("Enter your age:"))
# while not age.isdigit() and len(age) <= 3:
#     print("Invalid age!, Enter a valid age (max 3 digits): ")
# phone = input("Enter your number:").strip()
# while len(phone) != 11 and not phone.isdigit():
#     print("Invalid! Enter 11 digits number")
# track = input("Enter your specialisation: ").strip()
# while not track:
#     print("Track cannot be empty, Enter track:")

# Participant_Details = Details()
# print(Participant_Details)




def Details():
    
    name = input("Enter your name: ").strip()
    while not name:
        name = input("Name cannot be empty, Enter participant name: ").strip()

    
    age = input("Enter your age: ").strip()
    while not (age.isdigit() and len(age) <= 2):
        age = input("Invalid age! Enter a valid age (max 2 digits): ").strip()
    age = int(age)

    
    phone = input("Enter your number: ").strip()
    while not (phone.isdigit() and len(phone) == 11):
         phone = input("Invalid! Enter 11 digits number: ").strip()
    
    track = input("Enter your specialisation: ").strip()
    while not track:
        track = input("Track cannot be empty, Enter track: ").strip()

    return {"name": name, "age": age, "phone": phone, "track": track}


Participant_Details = Details()
print(Participant_Details)

try:
    file_ops.save_participant(participant)
    print("Participant details saved successfully!")
except IOError as E:
    print(f"Error saving participant details: {E}")