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
    contactsearch = input("Enter the contact that you want to search: ")

    if any(name in contactsearch for name in contacts):
        print("The contact number of " + contactsearch + " is: " + str(contacts[contactsearch]))
    else:
        print("Contact not found.")
elif user_click == "2":
    print("Process starting...")

    contactupdatekey = input("Enter the contact that you want to update: ")
    contactupdatevalue = int(input("Enter the contact no. "))
    contacts.update({contactupdatekey:contactupdatevalue})
    print(contacts)
elif user_click == "3":
    print("The Contacts stored are: ", sorted(contacts))
    
    # print("Enter the contact that you want to search:")
    contactsearch = input("Enter the contact name whose idendtity you want to know: ")
    
    if any(name in contactsearch for name in contacts):
        print("The contact number of " + contactsearch + " is: " + str(contacts[contactsearch]))
    else:
        print("Contact not found.")
else:
    print("Contact not found.")