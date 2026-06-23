name1 = input("Please enter the name of the first person : ")
name2 = input("Please enter the name of the second person : ")
name3 = input("Please enter the name of the third person : ")
namelist = (name1,name2,name3)

print()

date = input("Please enter the date in DD/MM/YYYY format : ")

print()

for m in namelist :
    print("Dear", m)
    print("You are selected!")
    print(date) 
    print()

