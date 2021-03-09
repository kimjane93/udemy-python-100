# Radomization

# wrangle deterministic machiines

# Python uses a Mersenne Twister - a pseudorandom number generator

# khan academy vid on pseudnum gens


# Python uses random module methods
# diff methods for rand ints, rand whole, random flaoting poitn etc

# just import random

# random.randint(1,5)

# includes start and end

# random floating point
# random.random()
# returns a random floating point number bewteen 0 and 1 but not including 1

# to get a randompflating number between 0 and a larger number, mutople the float from random.random() by the cap number

# random_float * 5
# 0.00000 - 4

# random.choice wil randomly pick an items from a list for you etc, passing the list in the paratheses etc


# lists in python - data strucutre in python, like arrays
# indexing
#
# append is equvalent of push
# .insert(i, x)
# .remove(x) - removes first itmf form the list whose values matches x
# raises a valueError if no such item exists

# .extend - adds a whole nunch of items to end of list
# could do .extend(["ab", "cd"]) add those items to the previous list etc

# .pop(i) - remvoes teh items at teh given position in the list, and returns it. if no index is specified, removes and returns the last items in the list. 

# .count() - returns c ount of character in parantehses found in string or list etc. 

# .index, .sort




import random
# python module
# module is respondible for different bits of functionaltiy for your project,
# same principle as when we import a file into another, that's a module

your_move = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors"))

computer_move = random.randint(0, 2)

if your_move == computer_move:
    print("It's A Draw")
elif your_move == 0 and computer_move == 1:
    print("Computer Wins")
elif your_move == 1 and computer_move == 2:
    print("Computer Wins")
elif your_move == 2 and computer_move == 0:
    print("Computer Wins")
elif computer_move == 0 and your_move == 1:
    print("You Win")
elif computer_move == 1 and your_move == 2:
    print("You Win")
elif computer_move == 2 and your_move == 0:
    print("You Win")
else:
    print("Incorrect Input - Forfeit")