from art import *


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    first_num = float(input("What's the first number?\n"))

    should_continue = True

    while should_continue:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        second_num = float(input("What's the next number?\n"))
        answer = operations[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation\n") == 'y':
            first_num = answer
        else:
            should_continue = False
            calculator()

calculator()