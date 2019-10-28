text = input("Player 1, enter a word or phrase: ") #prompt player 1 to create the word/phrase to be guessed
wordArr = text.split() #split it into an array of the different words
print(wordArr)
letterArray = [] #all the letters in the phrase
spaces = [] #all the guessed and unguessed letters
numWords = len(wordArr)
numHangman = 0 #a counter used as an argument for drawMSP

def search(char, array): #this function searches a specified array for an instance of the specified character
    for i in range(0, len(array)):
        if(array[i] == char):
            return i #if the character is found, return its position in the array (index).
    return -1 #if it is not found, return -1.

def printSpaces(): #this function displays all the blanks and guesses so far
    print("\n") #start on a new line
    for l in range(0, len(spaces)): #that's a lowercase L, not the number 1
        print(spaces[l] + ' ', end = '') #print every element of spaces (all the guesses and blanks) separated by spaces

def drawMSP(num): #this function prints a certain amount of the hangman depending on the input
    print("---|") #always do this
    if(num > 0): #prints all the parts for which the input is greater than the given number
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

for i in range(0, numWords): #for the number of words
    word = wordArr[i] #make a new list out of the given element of wordArr
    numLetters = len(word)
    for j in range(0, numLetters): #for the number of letters in the given word,
        letterArray.append(word[j]) #add all the letters to letterArray
    letterArray.append(' ') #in between words, add a space
    
print("\n" * 50) #make 50 new lines to clear the display window

for k in range(0, len(letterArray) - 1): #for every character in the input phrase
    if(letterArray[k] != ' '): #if the character is not a space
        spaces.append("_") #put in an underscore
    else: #but if it is a space
        spaces.append(' ') #add one so we can see the spaces between words
printSpaces()
        
while((numHangman < 7) and (search('_', spaces) != -1)): #prior to 7 incorrect guesses and while there are still blanks left,
    guess = input("\nPlayer 2, guess a letter: ") #prompt the player for a guess
    index = search(guess, letterArray) #find where the guess appears in letterArray, if at all
    if(index == -1): #if guess isn't there
        numHangman = numHangman + 1 #increment this counter, indicating an incorrect guess
    else: #but if it is there,
        spaces[index] = guess #set that location of the spaces list to the guess
        letterArray[index] = ' ' #remove that letter from letterArray
        index = search(guess, letterArray) #search for the same guess again
        while(index != -1): #do the same thing again and again while the guess appears in the phrase
            spaces[index] = guess
            letterArray[index] = ' '
            index = search(guess, letterArray)
    drawMSP(numHangman) #draw the hangman thus far, with how much of it is drawn determined by the amount of incorrect guesses
    printSpaces() #show all the correct guesses and empty spaces again
    if(search('_', spaces) == -1): #if there are no underscores left in spaces
        print("\nYou Win!") #you win
    if(numHangman == 7): #if you get seven incorrect guesses (and the hangman is complete)
        print("\nYou Lose.") #you lose

