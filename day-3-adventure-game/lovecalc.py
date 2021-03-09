your_name = input("What is your full name? \n").lower()
their_name = input("What is their full name? \n").lower()

t_count = your_name.count("t") + their_name.count("t")

r_count = your_name.count("r") + their_name.count("r")

u_count = your_name.count("u") + their_name.count("u")

e_count = your_name.count("e") + their_name.count("e")

true_num = str(t_count + r_count + u_count + e_count)

l_count = your_name.count("l") + their_name.count("l")

o_count = your_name.count("o") + their_name.count("o")

v_count = your_name.count("v") + their_name.count("v")

e_count_2 = your_name.count("e") + their_name.count("e")

love_num = str(l_count + o_count + v_count + e_count_2)

percentage = int(true_num + love_num)

print(percentage)