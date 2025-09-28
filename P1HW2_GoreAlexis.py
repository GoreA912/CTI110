#Alexis Gore
#9/28/25
#P1HW2
#Budget Input
#Psuedocode (logic)
print("This program calculates and displays travel expenses")
print("\n")
budget=int(input("Enter Budget: "))
print("\n")
travel_dest=input("Enter your travel destination: ")
print("\n")
gas_exp=int(input("How much do you think you will spend on gas? "))
print("\n")
hotel_exp=int(input("Approximately, how much would you need for accomodation/hotel? "))
print("\n")
food_exp=int(input("Lastly, how much do you need for food? "))
print("\n")
print("------------Travel Expenses------------")
print("Location:", travel_dest)
print("Initial Budget:", budget)
print("\n")
print("Fuel:", gas_exp)
print("Accomodation:", hotel_exp)
print("Food:", food_exp)
print("\n")
remain_bal=budget-gas_exp-hotel_exp-food_exp
print("Remaining Balance:", remain_bal)