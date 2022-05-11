student_scores = input("Input a list of student scores:\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_no = -9999999999

for score in student_scores:
    if score > max_no:
        max_no = score

print(f"The highest score in the class is: {max_no}")