student_heights = input("Input a list of student heights:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
total_no = 0

for student_height in student_heights:
    sum += student_height
    total_no += 1

average = round(sum / total_no)

print(average)
