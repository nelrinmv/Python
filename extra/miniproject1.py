# Q_Bonus. Password Strength Checker. Ask the user for a password and check: Length is at least 8 characters, Contains at least one number, Contains at least one uppercase letter. Then print whether the password is: Strong Moderate Weak

print("""Please generate a password. Please make sure that 
Length is at least 8 characters. \nContains at least one number. \nContains at least one uppercase letter""")

password = input("The password is : ")

length = len(password)

alpabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

integer = ('1','2','3','4','5','6','7','8','9','0')

if any(char in password for char in alpabet) and (any(char in password for char in integer) and length >= 8) :
    print("The password is strong")
elif (any(char in password for char in alpabet) and length >= 8) or (any(char in password for char in integer) and length >= 8) :
    print("The password is Moderate")
elif (any(char in password for char in alpabet)) or (length >= 8) or (any(char in password for char in integer)) :
    print("The password is weak")
else :
    print("Password is irrelevent")
