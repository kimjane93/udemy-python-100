import random

word_list = ['ardvark', 'baboon', 'camel']

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word = random.choice(word_list)
blanked_word = []

for letter in chosen_word:
    blanked_word.append('_')
print(blanked_word)

lives = 6
end_of_game = False

while not end_of_game:
    print(stages[lives])
    user_letter_guess = input("Guess a letter: ").lower()
    for idx, letter in enumerate(chosen_word):
        if user_letter_guess == letter:
            blanked_word[idx:idx+1] = user_letter_guess
    print(stages[lives])        
    print(f"{' '.join(blanked_word)}")       
    if user_letter_guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You've Lost!")
    if "_" not in blanked_word:
        end_of_game = True
        print("You've Won!")

