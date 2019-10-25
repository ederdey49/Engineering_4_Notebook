#Strings and Loops
#Code by Ned Derdeyn

text = input("Type a sentence: ") #prompts the user to type in an input sentence

wordArr = text.split() #make an array in which each element is one of the words from the input sentence

for i in range(0, len(wordArr)): #do this until the counter i equals the number of words in wordArr
    word = wordArr[i] #set the i-th element of wordArr to a new string
    for j in range(0, len(word)): #do this until the counter j equals the number of letters in word
        print(word[j]) #print the j-th letter of word
    print("-") #print a dash between words to separate them
