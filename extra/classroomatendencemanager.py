name1 = input("Enter the name of the student 1: ")
name2 = input("Enter the name of the student 2: ")
name3 = input("Enter the name of the student 3: ")
name4 = input("Enter the name of the student 4: ")
name5 = input("Enter the name of the student 5: ")

studentlist = [name1,name2,name3,name4,name5]
print("Complete Name list:" , studentlist)
print("Total Number of Student:", len(studentlist))

studentlist.sort()
print("First Student in Alphabetical Order:", studentlist[0])
print("Lasr Student in Alphabetical Order:", studentlist[-1])

studentlist[1] = "Rahul"
print("This is the updated list:",studentlist)

if "Rahul" in studentlist :
    print("TRUE") 
else:
    print("FALSE")