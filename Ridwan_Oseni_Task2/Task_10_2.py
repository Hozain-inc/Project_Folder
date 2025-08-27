name = input("Kindly enter school name: ")
tuition = float(input("Kindly enter the tuition fee: \u20A6"))
hostel = float(input("Kindly enter your hostel fee: \u20A6"))
feeding = float(input("Kindly enter your allowance: \u20A6"))
Total = tuition + hostel + feeding
print(f"Name: {name}\n Tuition fee: \u20A6{tuition:,}\n Hostel fee: \u20A6{hostel:,}\n Food allowance: \u20A6{feeding:,}\n Total bill: \u20A6{Total:,}")
