#Alexis Gore
#10/11/25
#P2HW2
#Module Grades
#Pseudocode

grade_list=[]

grade_list.append(float(input("Enter the grade for Module 1: ")))
grade_list.append(float(input("Enter the grade for Module 2: ")))
grade_list.append(float(input("Enter the grade for Module 3: ")))
grade_list.append(float(input("Enter the grade for Module 4: ")))
grade_list.append(float(input("Enter the grade for Module 5: ")))
grade_list.append(float(input("Enter the grade for Module 6: ")))


lowest_grade=min(grade_list)
highest_grade=max(grade_list)
sum_of_grades=sum(grade_list)
average_grade=sum_of_grades / len(grade_list)

print("\n")
print("------------Results------------")
print(f"Lowest Grade:  {lowest_grade:>10}")
print(f"Highest Grade: {highest_grade:>10}")
print(f"Sum of Grades: {sum_of_grades:>10}")
print(f"Average Grade: {average_grade:>10.2f}")
