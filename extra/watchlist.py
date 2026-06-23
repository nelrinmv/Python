m1 = input("Enter the name of the 1 movie: ")
m2 = input("Enter the name of the 2 movie: ")
m3 = input("Enter the name of the 3 movie: ")
m4 = input("Enter the name of the 4 movie: ")
m5 = input("Enter the name of the 5 movie: ")

movielist = [m1,m2,m3,m4,m5]
print("Original List:", movielist)

print("The number of movies in the list is:", len(movielist))

movielist.sort()

print("The first movie in alphabetical order :", movielist[0])
print("The last movie in alphabetical order :", movielist[-1])

movielist.insert(2,"Inception")
movielist.remove(movielist[3])

print("The updated movie list is:", movielist)
print("The movie on the second number is:", movielist[1])