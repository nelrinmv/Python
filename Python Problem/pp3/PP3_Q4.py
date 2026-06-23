text = input("Please write a sentence : \n") 

if "  " in text :
    print("Problem Detected! There is double space in the sentence.")
    print("Corrected sentence is : ")
    print(text.replace("  " , " "))
    
else :
    print("No problem detected.")