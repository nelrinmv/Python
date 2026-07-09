no_of_student = int(input("Enter the number of students: "))

def newdictionary(name,markspython,marksmaths,marksenglish):
    return {
        "name": f"{name}",
        "marks_python": markspython,
        "marks_maths": marksmaths,
        "marks_english": marksenglish
    }

# for every student, take input and store it in a dictionary
students = []
for i in range(no_of_student):
    name = input(f"Enter the name of student {i+1}: ")
    markspython = int(input(f"Enter the marks in Python for {name}: "))
    marksmaths = int(input(f"Enter the marks in Maths for {name}: "))
    marksenglish = int(input(f"Enter the marks in English for {name}: "))
    print()
    student_dict = newdictionary(name, markspython, marksmaths, marksenglish)
    students.append(student_dict)

def calculate_average(student):
    total_marks = student["marks_python"] + student["marks_maths"] + student["marks_english"]
    average_marks = total_marks / 3
    return average_marks

for student in students:
    print(f"Student Name: {student['name']}")
    print(f"Total Marks: {student['marks_python'] + student['marks_maths'] + student['marks_english']}")
    print(f"Average Marks: {calculate_average(student):.2f}")
    print("Grade: ", end="")
    if calculate_average(student) >= 90:
        print("A+")
    elif calculate_average(student) >= 80:
        print("B")
    elif calculate_average(student) >= 70:
        print("C")
    elif calculate_average(student) >= 60:
        print("D")
    elif calculate_average(student) >= 50:
        print("E")
    else:
        print("F")
    print("Status: ", end="")
    if student["marks_python"] >= 33 and student["marks_maths"] >= 33 and student["marks_english"] >= 33:
        print("Pass")
    else:
        print("Fail")
    print()

# Use the max() function on the list of students, comparing them by their average marks
top_student = max(students, key=calculate_average)
highest_avg = calculate_average(top_student)

print(f"Highest Average Marks: {highest_avg:.2f} by {top_student['name']}")

end =  input("Press any key to exit...")