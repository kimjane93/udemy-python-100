student_scores = input("Input a list of student scores separated by spaces").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


# max(student_scores) out puts max value in that list

# min(student_scores) out puts min value in that list\

# for loop, range function cant use max or min
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")