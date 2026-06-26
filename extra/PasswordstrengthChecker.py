password = input("Please enter the Password: ")

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

integer = ['1','2','3','4','5','6','7','8','9','0']
# print(integer)
# print(type(integer))

if len(password) >= 8:
    print("Length +8.")
    if password.find("@") > 0:
        print("@ found")
        if any(char in password for char in alphabet):
            print("UpperCase Found")
            if any(numb in password for numb in integer):
                print("Integer Found. \nStrong Password")
            else:
                print("Weak Password")
        else:
            print("Weak Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")