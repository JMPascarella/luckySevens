"""
Program Name: luckySevens.py
Author: JMP
Date: 09-13-19

Program allows the play to roll a pair of die and wins $4 on a roll of a seven, otherwise they lose $1. The program will first prompt the user to input the amount of money they want to put into the 'pot' and then the game is played untiil the pot is empty
"""

import random

win = 0
loss = 0

print("Welcome to Lucky Sevens! The game is simple: you put money into the pot and roll two dice: \nFor every roll of a seven (7) you win $40\nBut on any other roll you only lose $1! \nTo win, you only need to roll a (6, 1), (5,2), (4, 3), (3, 4), (2, 5), or a (1, 6)!")

playerMoney = int(input("Please enter how much you'd like to start with >>> "))
print("You've put $" + str(playerMoney) + " in the pot! \nLets begin!" )

while playerMoney > 0:
    die1 = random.randint(1, 6)
    die2 = random.randint(1,6)

    if (die1 + die2 == 7):
        playerMoney += 4
    else:
        playerMoney -= 1

    print("The first die was a " + str(die1) + " and the second die was " + str(die2) + " which totaled to a roll of " + str((die1 + die2)))
    if (die1 + die2 == 7):
        print("You won the roll!")
        win += 1
    else:
        print("You lost the roll!")
        loss += 1

    print("The pot now has $" + str(playerMoney) + " in it.")

print("The pot is empty! You lose!")
print("You won the roll " + str(win) + " times. \nYou loss the roll " + str(loss) + " times.")
