text = input("Player 1, enter a word or phrase: ")
wordArr = text.split()
print(wordArr)
letterArray = []
spaces = []
numWords = len(wordArr)
numHangman = 0

def search(char, array):
    for i in range(0, len(array)):
        if(array[i] == char):
            return i
    return -1

def printSpaces():
    print("\n")
    for l in range(0, len(spaces)):
        print(spaces[l] + ' ', end = '')

def drawMSP(num):
    print("---|")
    if(num > 0):
        print("   O")
    if(num > 1):
        print("  /", end = '')
    if(num > 2):
        print("|", end = '')
    if(num > 3):
        print("\ ")
    if(num > 4):
        print("   |")
    if(num > 5):
        print("  /", end = '')
    if(num > 6):
        print(" \ ")

for i in range(0, numWords):
    word = wordArr[i]
    numLetters = len(word)
    for j in range(0, numLetters):
        letterArray.append(word[j])
    letterArray.append(' ')
    
print("\n" * 50)

for k in range(0, len(letterArray) - 1):
    if(letterArray[k] != ' '):
        spaces.append("_")
    else:
        spaces.append(' ')
printSpaces()
        
while((numHangman < 7) and (search('_', spaces) != -1)):
    guess = input("\nPlayer 2, guess a letter: ")
    index = search(guess, letterArray)
    if(index == -1):
        numHangman = numHangman + 1
    else:
        spaces[index] = guess
        letterArray[index] = ' '
        index = search(guess, letterArray)
        while(index != -1):
            spaces[index] = guess
            letterArray[index] = ' '
            index = search(guess, letterArray)
    drawMSP(numHangman)
    printSpaces()
    if(search('_', spaces) == -1):
        print("\nYou Win!")
    if(numHangman == 7):
        print("\nYou Lose.")

