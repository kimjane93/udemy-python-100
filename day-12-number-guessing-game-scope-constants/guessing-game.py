import random
from art import *

def guess_check(number_guessed, attempts, secret_num):
    while not number_guessed:
        if attempts == 0:
            print(f"You are out of guesses, the secret number was {secret_num}")
            number_guessed = True
        else:
            guess = int(input("Make a guess: "))
            if guess == secret_num:
                print("You win!")
                number_guessed = True
            elif guess < secret_num:
                attempts -= 1
                print(f"Too low")
                if attempts > 0:
                    print(f"You have {attempts} left")
            elif guess > secret_num:
                attempts -= 1
                print(f"Too high")
                if attempts > 0:
                    print(f"You have {attempts} left")
            else:
                print("Invalid input, end of game triggered")
                number_guessed = True


def guessing_game():
    numbers = []
    for num in range(1, 101):
        numbers.append(num)
    
    secret_num = random.choice(numbers)

    number_guessed = False

    print(logo)

    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    difficulty = input("Type 'easy' or 'hard':\n")

    if difficulty == 'hard':
        attempts = 5
        guess_check(number_guessed, attempts, secret_num)
    elif difficulty == 'easy':
        attempts = 10
        guess_check(number_guessed, attempts, secret_num)
    else:
        print("Invalid input, game exited")
        
        
        



guessing_game()