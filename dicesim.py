# Simulates rolling dice
import random

# Rolls however many dies with however many sides
def roll(numDies, numSides):
    roll_value = 0
    for i in range(1, numDies):
        roll_value += random.randint(1,numSides)
    print("You rolled a {}".format(roll_value) ) 

# Number input
def get_number(prompt):
    while True:
        try:
            value = int(raw_input(prompt))
        except ValueError:
            print("Please enter a number!")
            continue
        if value < 0:
            print("We need a positive number. Try again!")
            continue
        else:
            break
    return value

# Checking if user wants to quit or not
def get_info(prompt):
    while True:
        value = raw_input(prompt).strip().lower()
        if value == "yes" or value == "y" or value == "no" or value == "n":
            break
        else:
            print("This is a yes or no question. Try again!")
            continue
    if value == "yes" or value == "y":
        return False
    return True

# Gets info from user
def get_input():
    numDies = get_number("How many dies would you like? ")
    numSides = get_number("How many sides per die? ")
    roll(numDies,numSides)

while True:
    get_input()
    wantsOut = get_info("Would you like to roll again? ")
    if wantsOut:
        break