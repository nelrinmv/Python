bankacc = {
    "Name" : "Nelrin",
    "accno" : 31425412523,
    "balance" : 255000,
    "phoneno" : 9053503045
}

print("[1] Check Balance")
print("[2] Deposit Money")
print("[3] Withdraw Money")
print("[4] Account Details")

user_input = input("\nPlease type the number of the option that you want to continue with: ")

if user_input == "1":
    print("Loading Bank Balance...")
    print("\nBank balance is:", bankacc["balance"])
elif user_input == "2":
    print("Loading program for Deposit of money...\n")
    newbalance = bankacc["balance"] + int(input("Please enter the amount that you have deposited: "))
    bankacc.update({"balance" : newbalance})
    print("The account current balance is: Rs.",bankacc["balance"])
elif user_input == "3" and bankacc["balance"] > 0:
    print("Loading program for Withdraw of money...\n")
    newbalance = bankacc["balance"] - int(input("Please enter the amount that you want to withdraw: "))
    bankacc.update({"balance" : newbalance})
    print("The account current balance is: Rs.",bankacc["balance"])
elif user_input == "4":
    print("Loading Account Details...\n")
    print(bankacc)
else:
    print("!!ERROR!! ..The option entered by you is irrelevent please try again later or the balance in the account is 0 or less.. !!ERROR!!")
