# keyword arguments allow tou to add the parameter to name and set it equal to the value in the parathenses
# (a=3, b=2)
# or you default use positoional arguments, where you go based off of the placeholders indicated in function definition
# (a, b)


user_answer = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

message = input("Type your message:\n")

shift_number = int(input("Type the shift number (whole):\n"))



if user_answer == 'encode':
    print(f"Here's the encoded result: {}")
elif user_answer == 'decode':
    print(f"Here's the decoded result: {}")


repeat_cycle = input("Type 'yes' if you wan tto go again. Otherwise type 'no'.\n")
