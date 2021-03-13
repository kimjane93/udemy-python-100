# how many cans of paint we need to buy for a surface area of wall

# use inputs to modfuy our funciton 


# can round with round, int
# BUT if you need to ROUNG UP 
# import math
# math.ceil(input)

import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
# i can of paint covers 5 sq meters of wall

def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height * width) / cover)
    print(f"You will need {num_of_cans} paint cans to cover a wall with a height of {height}m and a width of {width}m")



paint_calc(height=test_h, width=test_w, cover=coverage)