# Getting Basic details 
name = input("Enter you full name: ")
capname = name.capitalize()

# print(capname)
# Extra caustion case for multi space in between words
if name.find("  "):
    name.replace("  ", " ")

    # Conversion and finding much requirement
    char = len(name)
    space = name.count(" ")
    kumarend = name.endswith("kumar") or name.endswith("Kumar")
    firstspace = name.find(" ")
    newname = name.replace(" ","-")
    lastchar = name[-1:-5]

    # printing the detals that have been fined out
    print("Total Character:", char)
    print("No of space:", space)
    print("Ends with Kumar:", kumarend)
    print("First Space:", firstspace)
    print("Modified Name:", newname)
    print("Last 4 characters:", lastchar)
elif name.find("   "):
    name.replace("   "," ")

    # Conversion and finding much requirement
    char = len(name)
    space = name.count(" ")
    kumarend = name.endswith("kumar") or name.endswith("Kumar")
    firstspace = name.find(" ")
    newname = name.replace(" ","-")
    lastchar = name[-1:-5]

    # printing the detals that have been fined out
    print("Total Character:", char)
    print("No of space:", space)
    print("Ends with Kumar:", kumarend)
    print("First Space:", firstspace)
    print("Modified Name:", newname)
    print("Last 4 characters:", lastchar)
else:
    name.replace(" "," ")

    # Conversion and finding much requirement
    char = len(name)
    space = name.count(" ")
    kumarend = name.endswith("kumar") or name.endswith("Kumar")
    firstspace = name.find(" ")
    newname = name.replace(" ","-")
    lastchar = name[-1:-5]

    # printing the detals that have been fined out
    print("Total Character:", char)
    print("No of space:", space)
    print("Ends with Kumar:", kumarend)
    print("First Space:", firstspace)
    print("Modified Name:", newname)
    print("Last 4 characters:", lastchar)
