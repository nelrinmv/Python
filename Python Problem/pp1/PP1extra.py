# Q1. quote 

print("“The best way to get started is to quit talking and begin doing.” – Walt Disney")

# Q2. Ask for User name and print a greeting message    

name = input("Please enter your Name: ")
print("Hello" , name + "," , "Greating of the day." )

# Q3. Print the multiplication table of a number entered by the user.

multiple = int(input("Please enter the number for which you want to know the Table : "))
number = (1,2,3,4,5,6,7,8,9,10)
for n in number : 
    print(multiple, "x" , n , "=" , n*multiple)

# Q4. Print all files and folders in the current directory using the os module.

import os

print("The Name of the directory is : " , os.getcwd())
print("The list of Files and Folder in this Directory is : " , os.listdir())

# Q5. Create a simple learning log and combine Q2 also.

whatdidyoulearn = input("Please tell what did you learn today : ")
howmanyhrs = int(input("How many hours did you studied today : "))

print("Todays topic : ", whatdidyoulearn)
print("Hours Studied by you : ", howmanyhrs)
print("Great Job" , name + "!" , "You have done a great job today.")