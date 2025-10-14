#Alexis Gore
#10/5/25
#P2LAB2
#Dictionary

automobile_mpg={"Camaro": 18.21, "Prius": 52.36, "Model s": 110, "Silverado": 26}
automobile_mpg.keys()
print(automobile_mpg.keys())
automobile=input("Enter a vehicle to see its mpg: ")
mpg=automobile_mpg[automobile]
print("The", automobile, "gets", mpg, "mpg")
miles= float(input("How many miles will you drive?" , ))
gallons_needed= miles/mpg         
print(f"{gallons_needed:.2f}, gallon(s) of gas are needed to drive the", automobile, miles, "miles")