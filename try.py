dict = {
    "Item1" : 75924125412,
    "Item2" : 97464125412,
    "Item3" : 97433125412,
    "Item4" : 86733125412,
    "Item5" : 97433125352
}

print("[1] Menu list")
print("[2] Search list")
print("[3] Update list")

inputlist= input("enter the new number: ")

print(dict[inputlist])

userchoose = input("Please choose ur number selection for further information: ")
if userchoose == "1":
    print(sorted(dict))
    contactsearch = input("Enter the contact name whose idendtity you want to know: ")
elif userchoose ==  "2":
    print("Enter the contact that you want to search:")
    contactsearch = input("Enter the contact name whose idendtity you want to know: ")
elif userchoose == "3":
    print("Enter the contact that you want to edit:")
    input()
else:
    print("!!ERROR!! Option Not available in the selection Menu. !!ERROR!!")