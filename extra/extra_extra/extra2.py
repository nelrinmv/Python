username = input("Enter your username: ")

print("Capitalized username:", username.capitalize())
print("Length:",len(username))
print("Ends with 123:", username.endswith("123"))
print("No of a's in the Username:", username.count("a") or username.count("A")) 
print("Modified Username:", username.replace("a","@") or username.replace("A","@"))