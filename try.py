import os

# Create a file
with open("demo.txt", "w") as f:
    f.write("Hello!")

print("File created!")

# Delete the file
os.remove("demo.txt")

print("File deleted!")