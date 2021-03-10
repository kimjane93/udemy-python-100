# using range function 

# use for loops with the rnage funciton

# good for genrating a range of numbers to loop through

# for number in range(a, b):
#     print(number)


# DOES NOT INCLUDE END OF THE RANGE

# for number in range(1, 10):
#     print(number)
    # out puts 1-9
# if wanted all, would have to make it 1-11
# will default incrment by, otherwise add a third argument determining step number

# for number in range(1, 11, 3):
# out puts 1, 4, 7, 10

# total = 0
# for number in range(1, 101):
#     total += number

sum_evens = 0
for num in range(2, 101, 2):
    sum_evens += num
print(sum_evens)

# or

# total2 = 0
# for num in range(1, 101):
#     if number % 2 == 0;
#     total2 += number