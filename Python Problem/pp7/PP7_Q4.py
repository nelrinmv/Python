# The program to find whether a given number is a prime number.
from sympy import isprime, prime

userinput = int(input("Enter a number: "))
if isprime(userinput):
    print("Prime Number")
else:
    print("Not a prime number")