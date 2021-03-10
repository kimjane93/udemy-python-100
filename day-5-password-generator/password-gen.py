# import string
# print(string.printable)
import random


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['1', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']



print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would yo like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))



# Eazy
# password = ""
# for char in range(1, num_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# for num in range(1, num_numbers + 1):
#     random_num = random.choice(numbers)
#     password += random_num

# for symbol in range(1, num_symbols + 1):
#     random_symbol = random.choice(symbols)
#     password += random_symbol
# print(password)

# Hard

password_list = []
for char in range(1, num_letters + 1):
    random_char = random.choice(letters)
    # password_list += random_char
    # or
    password_list.append(random_char)

for num in range(1, num_numbers + 1):
    random_num = random.choice(numbers)
    password_list.append(random_num)

for symbol in range(1, num_symbols + 1):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)


random.shuffle(password_list)
# use a for loop with a empty string set up to put chars in new stirng or 

password = ""

print(password.join(password_list))

# in order to randomize a list
# use a for loop to shuffle
# and create randomly chosen character to put into new list based off of og


# or literall use random.shuffle(print_list)
