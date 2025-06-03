import random
print("===================")
print("Rock Paper Scissors")
print("===================")
print()
print()
print("1) ✊")
print("2) ✋")
print("3) ✌️")
x = int(input("Pick a number:"))
y = random.randint(1,3)
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