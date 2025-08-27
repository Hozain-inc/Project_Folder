store = {"Book": 10, "Pen": 20, "Bag": 5}
print(f"Before purchase: {store}")
item = input("Enter the item you want to buy: ").title()
quantity = int(input("Enter the quantity you want to purchase: "))
if item in store and store[item] >= quantity:
    store[item] -= quantity
else:
    print("Sorry, item not available or insufficient quantity.")
print(f"After purchase: {store}")