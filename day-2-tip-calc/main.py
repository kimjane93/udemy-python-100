print("Welcome To The Tip Calculator!")
total_bill = input("What was the total of your meal? \n$")
number_of_payers = input("How many of you will be splitting the cost? \n")
tip_percentage = input("What percentage would you like to tip? \n15, 18, or 20: \n")

total_bill_int = int(total_bill)
number_of_payers_int = int(number_of_payers)
tip_percentage_int = int(tip_percentage)

tip = total_bill_int * (tip_percentage_int/100)
final_amount = total_bill_int + tip
per_person = round(final_amount/number_of_payers_int, 2)


print(f"Subtotal: {total_bill_int}, \n Tip: {tip} \n Total: {final_amount} \n Cost Per Person: {per_person}")

# integers
# particular element from a string is a subscript
# with integers, numbers in python, rather than commas, we can put underscores, and it will be interrpeted by the computer as if the underscores weren't there

# float
# a floating point number, has a decimal in it, after it, a float data type


# Boolean
# True 
# False
# no quotations

# len(input())
# length of something 

# type() give you the type of data something is within the paratheses

# can use str() to conver an integer into a string so you cna concacetenate with a string etc

# can turn an integer or a string into a float with float()

# int()


# number = input("Number: \n")
# new_num = int(number[0]) + int(number[1])
# print(f"{new_num}")

# () ** to the power of

# order of priority - PEMDAS
# paranths, power of, multi/divid, +, -


# BMI Calculator

# height = input("enter your height in m: ")
# weight = input("enter your height in kg: ")

# result = float(weight)/(float(height)**2)
# result_as_int = int(result)
# print(f"{result_as_int}")

# rounding numbers
# round(8/3, 2) rounds into a whole number, OR can use second arg to specify number of decimal places to round too


# floor division 
# ( // )  a shortcut to get a whole number without have to convert to an integer




# Your Life in Weeks

# age = input("What is your current age?")

# age_as_int = int(age)

# time_in_years = 100 - age_as_int
# time_in_months = time_in_years * 12
# time_in_weeks = time_in_months * 4
# time_in_days = time_in_weeks * 7

# message = f"You have {time_in_years} years, {time_in_months} months, {time_in_weeks} weeks, {time_in_days} days left"

# print(message)
