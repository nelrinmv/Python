lang1 = input("Enter your vote: ")
lang2 = input("Enter your vote: ")
lang3 = input("Enter your vote: ")
lang4 = input("Enter your vote: ")
lang5 = input("Enter your vote: ")
lang6 = input("Enter your vote: ")

lang1 = lang1.capitalize()
lang2 = lang2.capitalize()
lang3 = lang3.capitalize()
lang4 = lang4.capitalize()
lang5 = lang5.capitalize()
lang6 = lang6.capitalize()

votelistv1 = [lang1,lang2,lang3,lang4,lang5,lang6]

uniquelangset = set(votelistv1)
print("Unique Language Voted:\n",uniquelangset)

print("Total Votes:",len(votelistv1))   
print("Total Unique Votes",len(uniquelangset))   

if len(uniquelangset) == 1 :
    print("Every One voted for the same language.")
else:
    print("No One voted for the same language.")

if "Python" in votelistv1:
    print("Python in the votes")
    print("No of Python in code: ", votelistv1.count("Python"))
    if votelistv1.count("Python") > votelistv1.count(uniquelangset[0:len(uniquelangset)]):
        print("Python won the votes")
else:
    print("Python Did not won ")