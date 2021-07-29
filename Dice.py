import random

def dice():
    diceNumber = random.randint(1,6)
    print(f"you rolled a {diceNumber} Type Y to roll again")
    if input() == 'y':
        dice()
    else:
        print("have a great day, run me again if you need a dice.")

dice()