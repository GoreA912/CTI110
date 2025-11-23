#Alexis Gore
#11/9/25
#P4HW1
#Module Grades Enhanced



def grades():
    grade_list = []
    num_grades = int(input("How many scores do you want to enter? "))
    for i in range(num_grades):
        while True:
            grade = float(input(f"Enter score {i + 1}: "))
            if 0 <= grade <= 100:
                grade_list.append(grade)
                break
            else:
                print("Invalid score entered. Please enter score between 0 and 100")
    lowest_grade = min(grade_list)
    grade_list.remove(lowest_grade)
    avg = sum(grade_list) / len(grade_list)
    print("------------Results-------------")
    print(f"Lowest Score: {lowest_grade}")
    print(f"Modified List: {grade_list}")
    print(f"Scores Average: {avg:.2f}")
    if avg >= 90:
        print('Grade: A')
    elif avg >= 80:
        print('Grade: B')
    elif avg >= 70:
        print('Grade: C')
    elif avg >= 60:
        print('Grade: D')
    else:
        print('Grade: F')
grades()
    