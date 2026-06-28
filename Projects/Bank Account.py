bankacc = {
    "Name" : "Nelrin",
    "accno" : 31425412523,
    "balance" : 176390,
    "phoneno" : 9053503045
}


print("[1] Check Balance")
print("[2] Deposit Money")
print("[3] Withdraw Money")
print("[4] Account Details")

user_input = input("\nPlease type the number of the option that you want to continue with: ")

if user_input == "1":
    print("Loading Bank Balance...")
elif user_input == "2":
    print("Loading program for Deposit of money...")
elif user_input == "3":
    print("Loading program for Withdraw of money...")
elif user_input == "4":
    print("Loading Account Details...")
else:
    print("!!ERROR!! ..The option entered by you iss irrelevent please try again later.. !!ERROR!!")