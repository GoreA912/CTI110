#Alexis Gore
#11/9/25
#P4HW2
#Employee Salary Enhanced

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

while True:
    employee_name = input(f"Enter employee's name or 'Done' to terminate: ")
    if employee_name == 'Done':
        break
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hour_pay = 40 * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        hours_worked * pay_rate
    overtime_hours = hours_worked - 40
    regular_hour_pay = 40 * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_hour_pay + overtime_pay

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_hour_pay
    total_gross_pay += gross_pay
    num_employees += 1
    print("\n")
    print(f"Employee Name: {employee_name}")
    print("\n")
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("----------------------------------------------------------------------------------")
    print(f"{hours_worked:>3.1f}{pay_rate:>15.2f}{overtime_hours:>12.1f}{overtime_pay:>15.2f}{regular_hour_pay:>12.2f}{gross_pay:>15.2f}")
print(f"Total number of emplyoyess entered: {num_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")