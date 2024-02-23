student_scores = input("Scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = highest_score

print(highest_score)
