# avwerage height calculator 

student_heights = input("Input a list of student heights separated by spaces").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


# print(sum(student_heights))
# cant use sum or len function

sum_of_heights = 0
number_of_students = 0

for student_height in student_heights:
    sum_of_heights += student_height
    number_of_students += 1
avg_height = int(sum_of_heights/number_of_students)
print(f"The average height of these students is {avg_height}")