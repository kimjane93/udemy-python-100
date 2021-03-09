

year = int(input("Which year do you want to check? \n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year!")
        else: print("Nope")
    else:
        print("Leap Year!")
else:
    print("Nope")


# if/elif only one carried out, multiple ifs will all be excuted if all are true however



# logical operators

# single &, or, and not
# not reverses the condition liek a js bang operator
