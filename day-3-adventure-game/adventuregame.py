print("Welcome to Treasure Island.\nYou're mission is to find the treasure.\nYou're at a cross road.")
first_choice = input("Where do you want to go? Type 'left' or 'right'\n")
if first_choice == "right":
    print("Game Over")
else:
    print("You come to a lake.\nThere is an island in the middel of the lake.")
    second_choice = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if second_choice == "swim":
        print("Game Over")
    else:
        print("You arrive at the island unharmed. \nThere is a house with 3 doors.\nOne red, one yellow and one blue.")
        third_choice = input("Which color do you choose?\n")
        if third_choice == "red":
            print("Game Over")
        elif third_choice == "blue":
            print("Game Over")
        elif third_choice == "yellow":
            print("You Win!")
        else:
            print("User Error - Game Lost By Default")
