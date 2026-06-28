menu = {
    "Grilled Sandwich" : 79 ,
    "Veggi Sandwich" : 89 ,
    "Panner Tikka Sandwich" : 99 ,
    "Aloo Tikki Sandwich" : 69 ,
    "Fruit Sandwich" : 89 ,
    "Plain Fries" : 79,
    "Veggi Loaded Fries" : 79,
    "Cheese Fries" : 89,
    "Peri Peri Fries" : 99,
    "Double Patty Burger" : 79,
    "Veggi Patty Burger" : 89,
    "Panner Patty Burger" : 99,
    "Panner - Aloo Double Patty Burger" : 109,
    "Mango Shake" : 79,
    "Banana Shake" : 69,
    "Chocolate Shake" : 79,
    "Butterscotch Shake" : 89,
    "Hazelnut Shake" : 99,
    "Kit Kat Shake" : 89,
    "White Sauce Pasta" : 99,
    "Red Sauce Pasta" : 99,
    "Mix Sauce Pasta" : 99,
    "Hot Coffee" : 79,
    "Cold Coffee" : 79,
    "Virgin Mojito" : 69,
    "Shikangi" : 89,
    "Irish Coffee" : 89,
    "Tandori Maggi" : 89,
    "Veggi Maggi" : 79
}

print("Hello welecome to the Hydra Bar!")
print("[1] Would you like to see our menu or")
print("[2] Would you like to end the Conversation.")

user_bill = []
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
        print("Loading interface for adding food...\n")
        itemtobeadded0 = input("Please enter the name of the dish that you want to order: ")
        if any(food in itemtobeadded0 for food in menu):
            user_bill.insert(0,itemtobeadded0)
            print("Food is added to order.\nWould you like to continue with [1]adding food in the order or [2] Proceed for payment")
            user_input = input("Choose the option that you want to continue with: ")
            if user_input == "1":
                itemtobeadded1 = input("\nPlease enter the name of the dish that you want to order: ")
                if any(food in itemtobeadded1 for food in menu):
                    user_bill.insert(1,itemtobeadded1)
                    print("\nFood is added to order.\nWould you like to continue with [1] Adding food in the order or [2] Proceed for payment")
                    user_input = input("Choose the option that you want to continue with: ")
                    if user_input == "1":
                        itemtobeadded2 = input("\nPlease enter the name of the dish that you want to order: ")
                        user_bill.insert(2,itemtobeadded2)
                        print("\nFood is added to order.\nWould you like to continue with [1] Adding food in the order or [2] Proceed for payment")
                        user_input = input("Choose the option that you want to continue with: ")
                        if user_input == "1":
                            itemtobeadded3 = input("\nPlease enter the name of the dish that you want to order: ")
                            user_bill.insert(3,itemtobeadded3)
                            print("\nFood is added to order.\nWould you like to continue with [1] Adding food in the order or [2] Proceed for payment")
                            user_input = input("Choose the option that you want to continue with: ")
                            if user_input == "1":
                                itemtobeadded4 = input("\nPlease enter the name of the dish that you want to order: ")
                                user_bill.insert(4,itemtobeadded4)
                                print("\nFood is added to order.\nWould you like to continue with [1] Adding food in the order or [2] Proceed for payment")
                                user_input = input("Choose the option that you want to continue with: ")
                            else:
                                print("\nPreparing Bill for the following item...\n")
                                print("Name of Item:",user_bill, "| Price to be paid:", menu[itemtobeadded0]+menu[itemtobeadded1]+menu[itemtobeadded2]+menu[itemtobeadded3])
                                end = input()
                        else:
                            print("\nPreparing Bill for the following item...\n")
                            print("Name of Item:",user_bill, "| Price to be paid:", menu[itemtobeadded0]+menu[itemtobeadded1]+menu[itemtobeadded2])
                            end = input()
                    else:
                        print("Preparing Bill for the following item...")
                        print("Name of Item:",user_bill, "| Price to be paid:", menu[itemtobeadded0]+menu[itemtobeadded1])
                        end = input()
                else:
                    print("Sorry, It seems that you entered either the wrong details or unavailable item. Please begin the order again.")
                    end = input()
            else:
                print("Preparing Bill for the following item...")
                print("Name of Item:",itemtobeadded0, "| Price to be paid:", menu.get(itemtobeadded0))
                end = input()
        else:
            print("Sorry, It seems that you entered either the wrong details or unavailable item. Please begin the order again.")
            end = input()
    else:
        print("Thank you for visiting our cafe do come again later.")
        end = input()
else:
    print("Thank you for visiting our cafe do come again later.")
    end = input()