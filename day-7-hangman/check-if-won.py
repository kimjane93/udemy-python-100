import random
import string

word_list = ['ardvark', 'baboon', 'camel']


chosen_word = random.choice(word_list)
blanked_word = []

for letter in chosen_word:
    blanked_word.append('_')
print(blanked_word)

# blank_string = ''
# blank_string = blank_string.join(blanked_word)
# print(blank_string)

end_of_game = False

while not end_of_game:
    user_letter_guess = input("Guess a letter: ").lower()
    for idx, letter in enumerate(chosen_word):
        if user_letter_guess == letter:
            blanked_word[idx:idx+1] = user_letter_guess
            print(blanked_word)
    if "_" not in blanked_word:
        end_of_game = True
        print("You've Won!")




# while blanked_word != list(chosen_word):
#     user_letter_guess = input("Guess a letter: ").lower()
#     for idx, letter in enumerate(chosen_word):
#         if user_letter_guess == letter:
#             blanked_word[idx:idx+1] = user_letter_guess
#             print(blanked_word)
#         else: 
#             print("Incorrect!")
# if blanked_word == list(chosen_word):
#     print("You've Won!")