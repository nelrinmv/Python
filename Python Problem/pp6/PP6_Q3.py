# Q. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams

userinput = input("Type out a text: ")
mustnothave = ['make a lot of money', 'buy now', 'subscribe this', 'click this']

if any(keyword in userinput for keyword in mustnothave):
    print("The message is a spam")
else:
    print("The message is legit")