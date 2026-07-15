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

