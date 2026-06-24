hindidictionary = {
    "Naam" : "Name",
    "Pata" : "Address",
    "Neend" : "Sleep",
    "Khana" : "Food",
    "Kitab" : "Book",
    "Katori" : "Bowl",
    "Bartan" : "Utensils",
}

userquestion = input("Please enter the hindi word in latian script: ")
propque = userquestion.capitalize()

check = any(key in propque for key in hindidictionary)

if check == True :
    print(hindidictionary[f"{propque}"])
else:
    print("The word is not present in the Dictonary.")
