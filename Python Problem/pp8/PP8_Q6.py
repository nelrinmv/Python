def inchtocm(n):
    if n >= 0:
        return n * 2.54 
    else:
        return "The length can't be negative."
    
userinput = int(input("Enter a number: "))
if userinput >= 0: 
    print(inchtocm(userinput) , "cm")
else:
    print(inchtocm(userinput))