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
