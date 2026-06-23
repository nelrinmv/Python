message = input("Enter a message: ")
l = len(message)
print("First character:", message[0])
print("Last character:", message[-1])
print("First 5 characters:", message[0:6])  
print("Every second character:", message[0:l+1:2])
print("Position of python:", message.find("python"))

modifedmeg = message.replace(" ","_")

print("Modified Message:", modifedmeg)