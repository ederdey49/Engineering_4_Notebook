#Automatic Dice Roller
#Lucia Crosby and Ned Derdeyn

from random import randint

print("Automatic Dice Roller")

value = input("Press ENTER to roll. Press X, then ENTER to quit.")

while (value == ""):
    print(randint(1,6))
    value = input()

exit()
