# Q1. Ask the user for their name and print the total number of characters in it.

name = input("Please enter your name : ")

print("Your name contains", len(name) ,"Characters" )

# Q2. Ask the user for their name and print: First character, Last character

l = len(name)

print(name[0:l:l-1])

# Q3. Ask the user for a sentence and a character. Print how many times that character appears in the sentence.

sentence = input("Please enter a sentence : ")
character = input("Please enter the character that you want to count in the sentence : ")

smallcapsen = sentence.lower()

count = smallcapsen.count(character)

print(count)

# Q6. Ask the user for a sentence and replace every occurrence of the word "bad" with "good".

badword = smallcapsen.count("bad")
print("No of bad in the sentence :" , badword)

goodsentence = smallcapsen.replace("bad" , "good")

print(goodsentence)

# Q11. Ask the user for their name and print it in reverse order.

reversedname = name[::-1]

print("So the name is",name)
print("Therefor the reversed name will be" , reversedname)

# Q12. Ask the user for a word and determine whether it is a palindrome.

word = input("Please enter the word that you want to check if it is a Palindrome : ")
revword = word[::-1]

if word == revword :
    print("The word is a palindrome.")
else : 
    print("The word is not a palindrome.")

# Q_Bonus. Password Strength Checker. Ask the user for a password and check: Length is at least 8 characters, Contains at least one number, Contains at least one uppercase letter. Then print whether the password is: Strong Moderate Weak

print("""Please generate a password. Please make sure that 
Length is at least 8 characters. \nContains at least one number. \nContains at least one uppercase letter""")

password = input("The password is : ")

length = len(password)

alpabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

integer = ('1','2','3','4','5','6','7','8','9','0')

if any(char in password for char in alpabet) and (any(char in password for char in integer) and length >= 8) :
    print("The password is strong")
elif (any(char in password for char in alpabet) and length >= 8) or (any(char in password for char in integer) and length >= 8) :
    print("The password is Moderate")
elif (any(char in password for char in alpabet)) or (length >= 8) or (any(char in password for char in integer)) :
    print("The password is weak")
else :
    print("Password is irrelevent")
