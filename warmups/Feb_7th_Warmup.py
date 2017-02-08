# simulate two dice rolls and display the sum to the user

import random

def roll_dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    return roll1 + roll2

roll_dice()
