student_marks = int(input("Enter your marks: "))

if student_marks in range(90 , 101):
    print("Ex")
elif student_marks in range(80,90):
    print("A")
elif student_marks in range(70,80):
    print("B")
elif student_marks in range(60,70):
    print("C")
elif student_marks in range(50,60):
    print("D")
else:
    print("F")

