# Rock Paper Scissors Game
# Author: Masaki0211
# This is a simple command-line game where the user plays against the computer.

import random

print("===================")
print("Rock Paper Scissors")
print("===================")
print()
print()


#Displays options
print("1) ✊")
print("2) ✋")
print("3) ✌️")

#Get user input
x = int(input("Pick a number:"))

#Computer picks random number among 1 and 3
y = random.randint(1,3)

#prints outcome
if x == 1 and y == 1:
    print("You chose: ✊")
    print("CPU chose: ✊")
    print("It's a tie!")
elif x == 1 and y == 2:
    print("You chose: ✊")
    print("CPU chose: ✋")
    print("The CPU won!")
elif x == 1 and y == 3:
    print("You chose: ✊")
    print("CPU chose: ✌️")
    print("The player won!")
elif x == 2 and y == 1:
    print("You chose: ✋")
    print("CPU chose: ✊")
    print("The player won!")
elif x == 2 and y == 2:
    print("You chose: ✋")
    print("CPU chose: ✋")
    print("It's a tie!")
elif x == 2 and y == 3:
    print("You chose: ✋")
    print("CPU chose: ✌️")
    print("The CPU won!")
elif x == 3 and y == 1:
    print("You chose: ✌️")
    print("CPU chose: ✊")
    print("The CPU won!")
elif x == 3 and y == 2:
    print("You chose: ✌️")
    print("CPU chose: ✋")
    print("The player won!")
elif x == 3 and y == 3:
    print("You chose: ✌️")
    print("CPU chose: ✌️")
    print("It's a tie!")
