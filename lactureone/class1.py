# Mark sheet in python
# generate a mark sheet using if else and elif statement
student_percentage:int = int (input("Enter student percentage:"))
if student_percentage >= 90:
    print("you got A+ grade")
elif student_percentage>=80:
    print(input("you got A grade"))
elif student_percentage >=70:
    print(input("you got B grade"))
elif student_percentage >=60:
    print(input("You got  C grade"))
elif student_percentage >=50:
    print(input("You got D grade"))
    
else:
    print(input("You are fail in exam"))