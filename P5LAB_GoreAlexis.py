#Alexis Gore
#11/30/25
#P5LAB
#Monetary Values Extended

import random
def disperse_change(change_owed):
    print(f"Change is: ${change_owed:.2f}")
    cents = int(round(change_owed *100))
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
def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${total_owed:.2f}")
    while True:
        amount_paid = float(input("How much cash will you put in the self-checkout? "))
        if amount_paid < total_owed:
            print ("Error. Please enter suffient amount.")
        else:
            break
    change_owed = amount_paid - total_owed
    disperse_change(change_owed)


if __name__== "__main__":
    main()
    

