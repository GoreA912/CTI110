#Alexis Gore
#10/11/25
#P2HW1
#Budget Input
print("This program calculates and displays travel expenses")
print("\n")
budget=float(input("Enter Budget: "))
print("\n")
travel_dest=input("Enter your travel destination: ")
print("\n")
gas_exp=float(input("How much do you think you will spend on gas? "))
print("\n")
hotel_exp=float(input("Approximately, how much would you need for accomodation/hotel? "))
print("\n")
food_exp=float(input("Lastly, how much do you need for food? "))
width=15
print("\n")
print("------------Travel Expenses------------")
print(f"Location: {travel_dest:>27}")
print(f"Initial Budget: {"$":>15}{budget:.2f}")
print(f"Fuel: {"$":>25}{gas_exp:.2f}")
print(f"Accomodation: {"$":>17}{hotel_exp:.2f}")
print(f"Food: {"$":>25}{food_exp:.2f}")
remain_bal=float(budget-gas_exp-hotel_exp-food_exp)
print("-----------------------------------------")
print(f"Remaining Balance: {"$":>12}{remain_bal:.2f}")