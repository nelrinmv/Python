def sumofnnumbers(n):
    if n > 0:
        return n + sumofnnumbers(n - 1)
    elif n == 0:
        return 0
    else:
        return "Invalid input: n must be a non-negative integer."
    

userinput = int(input("Enter a Number: "))    
print(sumofnnumbers(userinput))