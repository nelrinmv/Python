# Q13: Ask the user for a sentence and count how many words it contains.

sentence = input("Please enter a Sentence : ")

l = len(sentence)
last_letter = sentence[-1:l+1:l]
# print(last_letter)

if last_letter == " " :
    no_of_word = sentence.count(" ")
    print("The number of words in the sentence is" , no_of_word)
else :
    no_of_word = sentence.count(" ") + 1
    print("The number of words in the sentence is" , no_of_word)


# 49program hand written