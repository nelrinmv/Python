import random

option = ["Snake","Water","Gun"]
print("Hey today we will be playing the game of Snake, Water, Gun. These are the option that you can chose from\n",option)

userinput = input("Enter the option that you choose: ")
computerinput = random.choice(option)
print(f"The option chosen by the computer is {computerinput}")

if userinput == computerinput:
    print("!!Tie!!")
elif userinput == "Snake" and computerinput == "Water":
    print("Player won the round.")
elif userinput == "Snake" and computerinput == "Gun":
    print("Player lost the round.")
elif userinput == "Water" and computerinput == "Gun":
    print("Player won the round.")
elif userinput == "Water" and computerinput == "Snake":
    print("Player lost the round.")
elif userinput == "Gun" and computerinput == "Snake":
    print("Player won the round.")
elif userinput == "Gun" and computerinput == "Water":
    print("Player lost the round.")
else:
    print("The input by the user does not match the option available")

end = input()