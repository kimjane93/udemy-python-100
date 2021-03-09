import random

names_string = input("Give me everybody's name separated by a comma.\n")
names = names_string.split(", ")

num_people = len(names) - 1

random_selection = random.randint(0, num_people)

print(f"Looks like {names[random_selection]} is paying this time!")


# random.choice wil randomly pick an items from a list for you etc, passing the list in the paratheses etc

# common IndexError: index out of range - when you are trying to access an index that doesnt exist, beyodn the end of the range of indeixes in your list etc.
# length of list is 50, but index is 0-49