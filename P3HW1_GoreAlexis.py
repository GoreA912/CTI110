#Alexis Gore
#10/26/25
#P3HW1
#Debug Code


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 1: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
sum_grade = sum(grades)
avg = sum_grade / len(grades)
print("\n")
print("------------Results------------")
print(f"Lowest Grade:  {low:>10}")
print(f"Highest Grade: {high:>10}")
print(f"Sum of Grades: {sum_grade:>10}")
print(f"Average Grade: {avg:>10.2f}")
print("------------------------------------------")
if avg >= 90:
   print('Your grade is: A')
elif avg >= 80:
   print('Your grade is: B')
elif avg >= 70:
   print('Your grade is: C')
else:
   print('Your grade is: F') 





