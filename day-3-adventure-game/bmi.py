 
 # Updgraded Version of BMI calculator, an interpreation of their results


height = input("enter your height in m: ")
weight = input("enter your height in kg: ")

result = float(weight)/(float(height)**2)
rounded_result = round(result, 1)

if rounded_result < 18.5:
    print("You could put on some padding!")
elif rounded_result < 25:
    print("You're in a good spot")
elif rounded_result < 30:
    print("You've got something extra, but not in a bad way!")
elif rounded_result < 35:
    print("There's a little more of you to love, just make sure you're checking in with a doctor about how to keep your nutriton on track!")
else:
    print("You do you, but see if there's anything you could be doing to help keep you active if that is something you are able to do, you're joints are probably a little weary")