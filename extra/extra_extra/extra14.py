student = {
    "name" : "Rahul",
    "Math" : 88,
    "Science" : 92,
    "English" : 76,
    "Computer" : 95
}

print("Highest marks:", max(student["English"],student["Computer"],student["Math"],student["Science"]))
print("Lowest marks:", min(student["English"],student["Computer"],student["Math"],student["Science"]))

print("Avg marks" , (student["English"]+student["Computer"]+student["Math"]+student["Science"])/(len(student)-1))

marks90 = any(marks >= "90" for marks in student)

if marks90 == True:
    print("Above 90 in any subject is True")
else:
    print("Above 90 marks in any subject is False")