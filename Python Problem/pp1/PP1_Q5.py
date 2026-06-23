import os
 
# This line of code will print the current working directory to the console
print("Current working directory: ", os.getcwd())

# This line of code will list all files in the current directory in separate lines
files = os.listdir()

print("\nContents of the directory:")

for item in files:
    print(item)

