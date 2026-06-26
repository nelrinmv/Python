contacts = {
    "Papa ji":9711154530,
    "Mummy ji":8882220934,
    "Dadi ji":9499131210,
    "Nelrin":9053503045,
    "Dada ji":9253089274,
    "Nani ji":9991450374,
    "Rinku mama ji":8930109237,
    "Junk1":9711177372,
    "Junk2":9814154530,
    "Junk3":9411154540,
    "Junk4":9111154630,
    "Junk5":9711155530,
    "Junk6":9212164530,
    "Junk7":9711254530,    
}

print("[1] Search Contacts")
print("[2] Update Contacts")
print("[3] Display All Contacts")

user_click = input("Type a number and press Enter: ")

if user_click == "1":
    print("Process started.")
elif user_click == "2":
    print("Process started.")
elif user_click == "3":
    print("The Contacts stored are: ", sorted(contacts))
    usersearchcontact = input("Type the Name of the person whose contact you want to know: ")
    if usersearchcontact == contacts.items(usersearchcontact) :
        print(contacts.get(usersearchcontact))
    else:
        print("Contact does not exist or typing Error.")
        