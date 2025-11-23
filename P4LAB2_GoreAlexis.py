def multiplication_table():
    while True:
        num_str = input("Enter an integer: ")
        num = int(num_str)
        if num < 0:
            print("This program does not handle negative numbers")
        else:
            for i in range(1,13):
                print(f"{num} x {i} = {num * i}")
        run_again = input("Would you like to run the program again?")
        if run_again != "yes":
            print("Exiting program...")
            break

multiplication_table()