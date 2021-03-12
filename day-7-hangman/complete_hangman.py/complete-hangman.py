# hangman logic

# upon load have a random word genereated,
# and a string of underscores/blanks that match that words length
# while the blank string does not equal the radmom word prompt the user for a letter
# while lives > 0?
# if it is correct find the index/indices that that letter occurs at in the random word
# replace/splice that letter into the corrseponding index of the blank strinf
# check if all blanks filled, if not go back to beginnng
# if incorrect, add a piecde to teh hang man, and remove that letter from possible options, lose a life, if out of lives game over, if not go back to beginning
# while balnk string does not equal random word. 

import random
from hangman_art import *
from hangman_words import *
from replit import clear

chosen_word = random.choice(word_list)

print(logo)

blanked_word = []
for letter in chosen_word:
    blanked_word.append('_')

lives = 6

end_of_game = False

while not end_of_game:
    print(stages[lives])

    user_letter_guess = input("Guess a letter: ").lower()
    
    clear()

    if user_letter_guess in blanked_word:
        print(f"You've already guessed '{user_letter_guess}'")

    for idx, letter in enumerate(chosen_word):
        if user_letter_guess == letter:
            blanked_word[idx:idx+1] = user_letter_guess
    print(stages[lives])        
    print(f"{' '.join(blanked_word)}")       
    if user_letter_guess not in chosen_word:
        print(f"You've guessed '{user_letter_guess}'. You use a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You've Lost!")
    if "_" not in blanked_word:
        end_of_game = True
        print("You've Won!")

