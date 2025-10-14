#Alexis Gore
#10/14/25
#P3LAB
#Monetary Values

amount = float(input("Enter the amount of money as a float: "))
cents = int(round(amount*100))
dollars = cents // 100
cents = cents - (dollars*100)
quarters = cents // 25
cents = cents - (quarters*25)
dimes = cents // 10
cents = cents - (dimes*10)
nickels = cents // 5
cents = cents - (nickels*5)
pennies = cents
print(f"{dollars} Dollars")
print(f"{quarters} Quaters")
print(f"{dimes} Dimes")
print(f"{nickels} Nickels")
print(f"{pennies} Pennies")