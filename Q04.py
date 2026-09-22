# Here we'll take marks as input and displays the grade using if, elif, and else.

print("--- Grade Calculator ---")
marks = float(input("Enter your marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
else:
    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    else:
        grade = 'Fail'

    print(f"Your grade is: {grade}")