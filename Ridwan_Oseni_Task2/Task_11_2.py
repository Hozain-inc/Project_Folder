Naira = float(input("How much do you want to convert?\u20A6"))
USD = float(input("Enter the exchange rate to USD:\u20A6 "))
GBP = float(input("Enter the exchange rate to GBP:\u20A6 "))
Naira_to_USD = Naira/USD
Naira_to_GBP = Naira/GBP
print(f"Nigerian Currency Converter:\nAmount in Naira: \u20A6{Naira:,}\nNaira to USD: ${Naira_to_USD:,}\nNaira to GBP: #{Naira_to_GBP:,}")
