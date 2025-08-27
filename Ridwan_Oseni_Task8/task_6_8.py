
# Task6
UTME_score = int(input("Enter your Jamb score: "))
choice = input("Is UNILAG your first choice? ").title()
Olevel = int(input("You passed with 5 credits in how many sitting? "))
Cut_off = int(input("Enter your overall score:"))
eligibility = (UTME_score >= 200) and (choice == 'Yes') and (Olevel == 1) and ((Cut_off >= 200) and (Cut_off <= 320))
print("Eligible:", eligibility)