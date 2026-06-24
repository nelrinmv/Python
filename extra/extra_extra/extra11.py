words = {
    "python": "Programming Language",
    "list": "Ordered collection",
    "tuple": "Immutable collection",
    "set": "Unordered collection"
}

wordinput = input("Enter a Word: ")

wordfinder = any(key in wordinput for key in words)
if wordfinder == True:
    print(words[wordinput])
else:
    print("No word found")