#Automatic Dice Roller
#Lucia Crosby and Ned Derdeyn

from random import randint #let us make random integers

print("Automatic Dice Roller") #print "automatic dice roller"

value = input("Press ENTER to roll. Press X, then ENTER to quit.") #print instructions for how to run the game

while (value == ""): #while the user continues to input nothing
    print(randint(1,6)) #print a number between 1 and 6
    value = input() #another place to input nothing if the user wants to continue or literally anything else to quit
