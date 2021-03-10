# while x != True
# or while not contidon:

# Reeborg's World instructions for hurdle three



def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def hurdle():    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()