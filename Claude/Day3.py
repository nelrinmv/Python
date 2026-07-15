# Q1. 
number_input = int(input("Enter a number: "))
if number_input > 0 :
    print("The number is positive.")
elif number_input < 0 :
    print("The number is negative.")
else:
    print("The number is zero.")

# Q2.
user_age = int(input("Enter your age: "))
if user_age >=18 :
    print("User can vote.")
else:
    print("User can not vote.")

# Q3.
number_input = int(input("Enter a number: "))
if number_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Q4.
number1_input = int(input("Enter the 1st number: "))
number2_input = int(input("Enter the 2nd number: "))
number3_input = int(input("Enter the 3rd number: "))

if (number1_input > number2_input > number3_input) or (number1_input > number3_input > number2_input):
    print(f"The largest number is {number1_input}")
elif (number2_input > number1_input > number3_input) or (number2_input > number3_input > number1_input):
    print(f"The largest number is {number2_input}")
else :
    print(f"The largest number is {number3_input}")

# Q5.
character_input = input("Enter a character in lower case: ")
if character_input == "a" or character_input == "e" or character_input == "i" or character_input == "o" or character_input == "u" :
    print("The character is vowel.")
else :
    print("The character is a consonant.")

# Q6.
user_marks = int(input("Enter your marks: "))
if user_marks >= 90:
    print("Grade: A")
elif user_marks >= 75:
    print("Grade: B")
elif user_marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Q7.
year = int(input("Enter a year: "))
leap_year = year % 4 == 0
check_divisiblity_with_100 = year % 100 == 0 
check_divisiblity_with_400 = year % 400 == 0
condition = leap_year and (not check_divisiblity_with_100 or check_divisiblity_with_400)

if condition == True:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")

# Q8.
side_length1 = float(input("Enter the length of 1st side: "))
side_length2 = float(input("Enter the length of 2nd side: "))
side_length3 = float(input("Enter the length of 3rd side: "))

condition = side_length1 + side_length2 > side_length3 and side_length2 + side_length3 > side_length1 and side_length1 + side_length3 > side_length2
equ_condition = side_length2 == side_length1 == side_length3
iso_condition = (side_length1 == side_length2 != side_length3) or (side_length1 == side_length3 != side_length2) or (side_length3 == side_length2 != side_length1)

if condition and equ_condition:
    print("Yes the triangle exsists and it is a type of equilateral triangle.")
elif condition and iso_condition:
    print("Yes the triangle exsists and it is a type of isoscales triangle.")
elif condition :
    print("Yes the triangle exsists and it is a type of scales triangle.")
else:
    print("The triangle does not exsists.")

# Q9.
number_input = int(input("Enter a number: "))
if number_input % 15 == 0:
    print("FizzBuzz")
elif number_input % 3 == 0:
    print("Fizz")
elif number_input % 5 == 0:
    print("Buzz")
else:
    print("Just number",number_input)

# Q10.
username = input("Enter your user name: ")
password = input("Enter your password: ")

if  username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")