# # keyword arguments allow tou to add the parameter to name and set it equal to the value in the parathenses
# # (a=3, b=2)
# # or you default use positoional arguments, where you go based off of the placeholders indicated in function definition
# # (a, b)

from art import *

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(msg, num, direction):
    transformed_message = ''
    if cipher_direction == 'decode':
        num *= -1
    if num > len(alphabet):
        num = num % len(alphabet)
    for char in msg:
        if char in alphabet:
            idx_of_char_in_alphabet = alphabet.index(char)
            new_positon = idx_of_char_in_alphabet + num
            if new_positon > len(alphabet) - 1:
                new_positon = new_positon - len(alphabet)
            shifted_char = alphabet[new_positon]
            transformed_message += shifted_char
        else:
            transformed_message += char
    print(f"Here's the {direction}d result: {transformed_message}")

should_continue = True

while should_continue:
    print(logo)

    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    message = input("Type your message:\n").lower()

    shift_number = int(input("Type the shift number (whole):\n"))

    caesar(msg=message, num=shift_number, direction=cipher_direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")
