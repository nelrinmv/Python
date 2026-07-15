# Q1.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1_greater_num2 = num1 > num2
print(f"Is the first number greater than the second number? {num1_greater_num2}")

# Q2.
num = int(input("Enter the first number: "))
num_even = num % 2 == 0
print(f"Is the number even? {num_even}")

# Q3.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

all_equal = num1 == num2 and num2 == num3
print(f"Are all three numbers equal? {all_equal}")

# Q4.
user_input = int(input("Enter a Number: "))
check_for_3_divisiblity = user_input % 3 == 0
check_for_5_divisiblity = user_input % 5 == 0
check_both_divisiblity = check_for_3_divisiblity and check_for_5_divisiblity
print("Is the number entered by the user divisible by both 3 and 5?",check_both_divisiblity)

# Q5. 
user_age = int(input("Enter your age: "))
teenager_check = 13 <= user_age <= 19 
print(f"Is the user teenager? {teenager_check}") 

# Q6.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print("The operator == is applied between them true/false?",num1 == num2)
print("The operator != is applied between them true/false?",num1 != num2)
print("The operator > is applied between them true/false?",num1 > num2)
print("The operator < is applied between them true/false?",num1 < num2)
print("The operator >= is applied between them true/false?",num1 >= num2)
print("The operator <= is applied between them true/false?",num1 <= num2)

# Q7.
year = int(input("Enter a year: "))
leap_year = year % 4 == 0
check_divisiblity_with_100 = year % 100 == 0 
check_divisiblity_with_400 = year % 400 == 0

condition = leap_year and (not check_divisiblity_with_100 or check_divisiblity_with_400)

print("The year is a leap year and is not divisible by 100 and 400. True or False?", condition)

# Q8.
number_input = int(input("Enter a number: "))
number_input += 15
print("The Final result is",number_input)

# Q9.
user_input = input("Please enter a string: ")
len_string = len(user_input) > 10
print(f"Is the length of string greater than 10? {len_string}")

# Q10.
user_marks = int(input("Enter your marks out of 100: "))
pass_conditon = user_marks >= 40
print("Have the user passed the exam?",pass_conditon)
distinction_conditon = user_marks >= 75
print("Have the user achived distinction in the exam?",distinction_conditon)

# Q11.
User_input = int(input("Enter a number: "))
condition = User_input % 7 == 0 and not User_input % 2 == 0
print("The number is divisibe by 7 and not 2?",condition)

# Q12.
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

is_compare = number1 is number2
print("Is case:",is_compare)
equal_compare = number1 == number2
print("Equal case:",equal_compare)
# == asks: "do these have the same value?"
# is asks: "are these literally the same object in memory?"
# It is because in case of small integers it memory can by same to save some space while for large integers it keep it seprate for efficency. 

# Q13.
username = input("Enter your user name: ")
password = input("Enter your password: ")

conditions = username == "admin" and password == "1234"
print("The boolean Check for username and password is", conditions)

# Q14.
side1 = int(input("Enter the length of side of triange: "))
side2 = int(input("Enter the length of side of triange: "))
side3 = int(input("Enter the length of side of triange: "))
condition = side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2
print("The boolean check for the triangle is", condition)

# Q15.
user_input = int(input("Enter a number: "))
condition = [(user_input % 2 == 0), (user_input % 3 == 0), (user_input % 5 == 0)]
print("The boolean check for the divisiblity of 2 is", condition[0])
print("The boolean check for the divisiblity of 3 is", condition[1])
print("The boolean check for the divisiblity of 5 is", condition[2])

# Q16.
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
condition = (number1 > 0 and number2 < 0) or (number1 < 0 and number2 > 0)
print("The boolean check for the condition is", condition)

# Q17.
fourdigit_number = int(input("Enter a four digit number: "))
lastdigit = fourdigit_number % 10
second_lastdigit = (fourdigit_number // 10) % 10
third_lastdigit = (fourdigit_number // 100) % 10
firstdigit = fourdigit_number // 1000
sum_of_digits =  lastdigit + second_lastdigit + third_lastdigit + firstdigit
condition = sum_of_digits % 3 == 0
print("The boolean check for the sum of the digits of the four digit number is divisible by 3 is", condition)

# Q18.
user_input_time = input("Enter a time in format(hh:mm:ss): ")
hh,mm,ss = user_input_time.split(":")
hh = int(hh)
mm = int(mm)
ss = int(ss)
hrs_in_sec = hh * 60 * 60
min_in_sec = mm * 60
total_time_in_sec = hrs_in_sec + min_in_sec + ss
condition = total_time_in_sec > 43200
print("The boolean check for the time entered by the user is greater than half day is", condition)

# Q19.
temp_celsius = float(input("Enter the temperature in Celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
condition = 60 <= temp_fahrenheit <= 80
print("The boolean check for the temperature in Fahrenheit is in the room temperature range is", condition)

# Q20.
subject1_marks = float(input("Enter the marks of subject 1: "))
subject2_marks = float(input("Enter the marks of subject 2: "))
subject3_marks = float(input("Enter the marks of subject 3: "))

avg_marks = (subject1_marks + subject2_marks + subject3_marks) / 3
avg_marks = round(avg_marks, 2)
condition = avg_marks >= 75 and subject1_marks >= 33 and subject2_marks >= 33 and subject3_marks >= 33
print("The boolean check for the student passed the exam and achieved distinction is", condition)