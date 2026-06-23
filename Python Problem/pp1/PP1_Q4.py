import os

print("Current working directory: ", os.getcwd())

files = os.listdir()

print("\nContents of the directory:")

for item in files:
    print(item)

