import random

word_list = ['ardvark', 'baboon', 'camel']

# randomly choose a random word from that list
# ask that user to guess a letter
# check id letter guessed is one of the letters in chose
# n_word


chosen_word = random.choice(word_list)
blanked_word = []

for letter in chosen_word:
    blanked_word.append('_')
print(blanked_word)

user_letter_guess = input("Guess a letter: ").lower()

for idx, letter in enumerate(chosen_word):
    if user_letter_guess == letter:
        print("Correct!")
        blanked_word[idx:idx+1] = user_letter_guess
        print(blanked_word)
    else: 
        print("Incorrect!")


# OR

# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if letter == guess:
#         blanked_word[position] = letter