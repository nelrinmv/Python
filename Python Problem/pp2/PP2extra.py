# Q1. Personal Information Card: Ask the user for: Name, Age, City

name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
city = input("Please enter the city that you live in : ")
print("   ") #Using as a breaker

print("Student information :")
print("Student Name :", name)
print("Student Age :", age)
print("Student City of residence :", city)
print("   ") #Using as a breaker

# Q2. Age After 10 Years: Ask the user's age and print it

print("Your age after 10 years will be :", age + 10)
print("   ") #Using as a breaker

# Q3. Ask the user for: Length, Width. Calculate and print the area.

sidea = int(input("Please enter the lenght of rectangle : "))
sideb = int(input("Please enter the breath of rectangle : "))
print("   ") #Using as a breaker

print("The area of rectangle is :" , sidea*sideb)
print("   ") #Using as a breaker

#Q5. Ask for marks in: Physics, Chemistry, Maths. Calculate: Total Marks, Percentage.

markphy = int(input("Please enter the marks scored in Physics : "))
markchem = int(input("Please enter the marks scored in Chemistry : "))
markmaths = int(input("Please enter the marks scored in Maths : "))
print("   ") #Using as a breaker

print("Total Marks scored is :", markchem+markmaths+markphy)
print("Percentage is :", (markphy+markchem+markmaths)*100/300)
print("   ") #Using as a breaker

# Q10. Ask: Name, Hours of Python studied today, Hours of IELTS studied today. Print: Daily Study Report, Name, Python, IELTS. Total Study Time.

studypy = int(input("Please tell no of hours python studied today : "))
studyielts = int(input("Please tell no of hours IELTS studied today : "))
print("   ") #Using as a breaker

print("""Daily study Report: 
Name :""", name)
print("Python :", studypy)
print("Ielts :", studyielts)
print("Total study time :", studyielts+studypy)
print("   ") #Using as a breaker

# Ask for: Name Physics Marks Chemistry Marks Maths Marks. Then print: Student Report Name Total Marks Percentage and Result
TM = markchem + markmaths + markphy
percentage = TM*100/300
print("Student Report \n \n Name :", name)
print()
print("Total marks :", TM)
print("Percentage :", percentage)

if percentage >= 33 : 
    print("Result = Pass")
else : 
    print("Result = Fail")