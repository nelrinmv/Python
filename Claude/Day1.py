# Q1. 
name = "Nelrin"
age = 18
branch = "Energy Engineering"

print("My name is", name, "and I am", age, "years old. I am pursuing my degree in", branch + ".")

# Q2.
num1 = input("Enter the first number: ")
num1_int = int(num1)
num2 = input("Enter the second number: ")
num2_int = int(num2)

print("The sum of", num1_int, "and", num2_int, "is", num1_int + num2_int)

# Q3.
a = 10
print("Before change a:",a)
b = 20
print("Before change b:",b)
temp = a
a = b
b = temp 
print("After change a:",a ,"\nAfter change b:", b)

# Q4.
celcius_str = input("Enter the temperatuer in celcius: ")
celcius_int = int(celcius_str)

print("Temp in Faranhite = " , (celcius_int*9/5)+32)

# Q5. 
x = int(input("Enter your favorite number: "))
print("The square of your favorite number is ", x ** 2)

# Q6.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(name,"will be",age+10,"years old after 10 years.")

# Q7.
principal = int(input("Enter the principal: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time: "))
simple_intrest = principal*rate*time/100
print("The simple interst will be",simple_intrest)

# Q8.
a = 10
b = 20
print(a,b)
a = a + b
b = a - b 
a = a - b
print(a,b)

# Q9.
import math
radius = int(input("Enter the radius: "))
area = math.pi * (radius**2)
print("Area of circle is:",round(area,2))

perimeter = math.pi * radius * 2
print("Circumference of circle is:", round(perimeter,2))

# Q10.
user_input = float(input("Enter a number with decimal: "))
print(round(user_input,1))

# Q11.
weight = float(input("Enter the Weight(in kg): "))
height = float(input("Enter the height(in m): "))
bmi = weight/(height**2)
print("The BMI of the person is:",round(bmi,1))

# Q12.
subject1_marks = float(input("Enter the marks of subject 1: "))
subject2_marks = float(input("Enter the marks of subject 2: "))
subject3_marks = float(input("Enter the marks of subject 3: "))

avg_marks = (subject1_marks + subject2_marks + subject3_marks) / 3
print("The average marks of the student is:", round(avg_marks, 2))

# Q13.
user_input = input("Enter a string: ")
string_length = len(user_input)
even = string_length % 2 == 0
print("The length of the string is:", string_length)
print("Is the length even?", even)

# Q14.
user_input_time = int(input("Enter time in seconds: "))
time_in_hours = user_input_time // 3600
remaining_seconds_after_hours = user_input_time % 3600
time_in_minutes = remaining_seconds_after_hours // 60
remaining_seconds = remaining_seconds_after_hours % 60
print("Time is:", time_in_hours, "hours,", time_in_minutes, "min,", remaining_seconds, "sec.")

# Q15.
fourdigit_number = int(input("Enter a four digit number: "))
lastdigit = fourdigit_number % 10
second_lastdigit = (fourdigit_number // 10) % 10
third_lastdigit = (fourdigit_number // 100) % 10
firstdigit = fourdigit_number // 1000
print("The sum of the digits is:", lastdigit + second_lastdigit + third_lastdigit + firstdigit)

# Q16.
userinput = input("Enter a Number: ")
rev_number = userinput[::-1]
print("The reversed number is:", rev_number)

# Q17.
dis_km = float(input("Enter the distance in kilometer: "))
time_hrs = float(input("Enter the time in hours: "))
speed = dis_km/time_hrs
print("The speed of the vehical is", round(speed,2),"km/hrs")

time_to_cover_double_in_hrs = (2 * dis_km)/ speed
time_to_cover_double_in_min = time_to_cover_double_in_hrs * 60
print("The time take to cover double the distance with the same speed in minute is",time_to_cover_double_in_min,"min.")

# Q18.
string_input = input("Enter a tuple in format(name,age,branch): ")
name,age,branch = string_input.split(",")
print(f"My name is {name}, I am {age} years old. My branch is {branch}.")