marks = {
    # "English" : 85,
    "Maths" : int(input("Please enter you maths marks: ")),
    "Physics" : int(input("Please enter you physics marks: ")),
    "Chemistry" : int(input("Please enter you chemistry marks: ")),
    # "Physical Education" : 98
}

if ((marks["Chemistry"]+marks["Maths"]+marks["Physics"]) >= 120) and (marks["Chemistry"] >= 33) and (marks['Maths'] >= 33) and (marks['Physics'] >= 33):
    print("Passed overall!")
else:
    print("Failed the exam")