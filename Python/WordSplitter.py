#Strings and Loops
#Code by Ned Derdeyn

text = input("Type a sentence: ")

wordArr = text.split()

numWords = len(wordArr)

for i in range(0, numWords):
    word = wordArr[i]
    numLetters = len(word)
    for j in range(0, numLetters):
        letter = word[j]
        print(letter)
    print("-")
