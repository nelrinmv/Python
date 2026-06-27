sandwich = {
    "Grilled Sandwich" : 79 ,
    "Veggi Sandwich" : 89 ,
    "Panner Tikka Sandwich" : 99 ,
    "Aloo Tikki Sandwich" : 69 ,
    "Fruit Sandwich" : 89 
}
fries = {
    "Plain Fries" : 79,
    "Veggi Loaded Fries" : 79,
    "Cheese Fries" : 89,
    "Peri Peri Fries" : 99
}
burger = {
    "Double Patty Burger" : 79,
    "Veggi Patty Burger" : 89,
    "Panner Patty Burger" : 99,
    "Panner - Aloo Double Patty Burger" : 109
}
shakes = {
    "Mango Shake" : 79,
    "Banana Shake" : 69,
    "Chocolate Shake" : 79,
    "Butterscotch Shake" : 89,
    "Hazelnut Shake" : 99,
    "Kit Kat Shake" : 89
}
pasta = {
    "White Sauce Pasta" : 99,
    "Red Sauce Pasta" : 99,
    "Mix Sauce Pasta" : 99,
}
drinks = {
    "Hot Coffee" : 79,
    "Cold Coffee" : 79,
    "Virgin Mojito" : 69,
    "Shikangi" : 89,
    "Irish Coffee" : 89,
}
maggi = {
    "Tandori Maggi" : 89,
    "Veggi Maggi" : 79
}

menu = [sandwich,fries,burger,shakes,pasta,drinks,maggi]

print("Hello welecome to the Hydra Bar!")
print("[1] Would you like to see our menu or")
print("[2] Would you like to end the Conversation.")


user_input = input("Choose the option that you want to continue with: ")

if user_input == "1":
    print("\nLoading menu...\n")
    print(menu)
    print()
    print("Would you like to continue with the order or end the conversation?")
    print("[1] Yes")
    print("[2] No\n")
    user_input = input("Choose the option that you want to continue with: \n")
    if user_input == "1":
        print("Loading interface for adding food...")
    else:
        print("Thank you for visiting our cafe do come again later.")
else:
    print("Thank you for visiting our cafe do come again later.")