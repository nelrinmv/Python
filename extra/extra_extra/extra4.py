# Getting basic details
name = input("Enter your Name: ")
age = input("Enter your Age: ")
fav_num = input("Enter you Favorite Number: ")
print()

# Conversion of string to integer
intage = int(age)
intfav_num = int(fav_num)

# Display of Informmation 
print("User's Name in Capitalised:", name.capitalize())
print("Square of Favorite Number:", intfav_num**2)

if intage >= 18 :
    print("Age is greater than 18.")
else :
    print("Age is less than 18.")

print("Profile String:")
print("Name:" + name.capitalize() , "| Age:" + age , "| Favorite Number:" + fav_num)