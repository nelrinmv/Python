# 4. Use comparison operator to find out whether ‘a’ given variable is greater than ‘b’ or not.

a = int(input("Please enter the First number : "))
b = int(input("Please enter the Second number : "))

if a == b :
    print("Both the number are equal")
elif a > b :
    print("The First number is greater than the Second number.")
else :
    print("The Second number is greater than the First nummber")