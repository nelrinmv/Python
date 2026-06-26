password = input("Please enter the Password: ")

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# integer = str([1,2,3,4,5,6,7,8,9,0])
# print(integer)
# print(type(integer))

if len(password) >= 8:
    print("Length +8.")
    if password.find("@") > 0:
        print("@ found")
        if password.find("1") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")
        elif password.find("2") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")        
        elif password.find("3") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")
        elif password.find("4") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")
        elif password.find("5") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")
        elif password.find("6") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")
        elif password.find("7") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")
        elif password.find("8") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")   
        elif password.find("9") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")
        elif password.find("0") > 0:
            print("Integer Found")
            if any(char in password for char in alphabet):
                print("UpperCase Found, Strong Password ")
            else:
                print("Weak Password")          
else:
    print("Weak Password")








































































