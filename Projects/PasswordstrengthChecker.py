password = input("Please enter the Password: ")

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

integer = ['1','2','3','4','5','6','7','8','9','0']

if (len(password) >= 8) and (password.find("@") > 0) and any(char in password for char in alphabet) and any(numb in password for numb in integer):
    print("Strong Password")
else:
    print("Weak Password")