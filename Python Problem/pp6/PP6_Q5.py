name = ['Aarav Sharma','Vivaan Gupta','Arjun Mehta','Rohan Verma','Kabir Singh']

user_input_name = input("Enter The Name: ")

if any(naam in user_input_name for naam in name):
    print("Yes the name is present.")
else:
    print("Nooooooooooo!! The name is not present")