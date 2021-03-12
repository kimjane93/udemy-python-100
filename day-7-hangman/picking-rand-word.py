import random

word_list = ['ardvark', 'baboon', 'camel']

# randomly choose a random word from that list
# ask that user to guess a letter
# check id letter guessed is one of the letters in chose
# n_word


chosen_word = random.choice(word_list)

user_letter_guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if user_letter_guess == letter:
        print("Correct!")
    else: 
        print("Incorrect!")