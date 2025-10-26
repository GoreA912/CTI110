#detail algorithm

#Alexis Gore
#10/26/25
#P3HW2
#Employee Salary

employee_name=input("Enter employee's name: ")
hours_worked=float(input("Enter number of hours worked: "))
pay_rate=float(input("Enter employee's pay rate: "))
print("-------------------------------------")
overtime_hours= 0.0
overtime_pay= 0.0
regular_hours= 0.0

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40 * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    regular_hours * pay_rate

gross_pay = regular_hours + overtime_pay

print(f"Employee Name: {employee_name}")
print("\n")
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("----------------------------------------------------------------------------------")
print(f"{hours_worked:>3.2f}{pay_rate:>15.2f}{overtime_hours:>12.2f}{overtime_pay:>15.2f}{regular_hours:>12.2f}{gross_pay:>15.2f}")