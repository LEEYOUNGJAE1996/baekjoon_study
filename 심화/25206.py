# 230320

# 평점계산기
subjects = []
grades = []
ratings = []
for count in range(20):
    subject, grade, rating = input().split()
    subjects.append(subject)
    grades.append(float(grade))
    ratings.append(rating)

sum_grades = sum(grades)
sum_ratings = 0
for count in range(len(subjects)):
    if ratings[count] == 'P':
        sum_grades -= grades[count]
    else:
        if ratings[count] == 'A+':
            sum_ratings += 4.5 * grades[count]
        elif ratings[count] == 'A0':
            sum_ratings += 4.0 * grades[count]
        elif ratings[count] == 'B+':
            sum_ratings += 3.5 * grades[count]
        elif ratings[count] == 'B0':
            sum_ratings += 3.0 * grades[count]
        elif ratings[count] == 'C+':
            sum_ratings += 2.5 * grades[count]
        elif ratings[count] == 'C0':
            sum_ratings += 2.0 * grades[count]
        elif ratings[count] == 'D+':
            sum_ratings += 1.5 * grades[count]
        elif ratings[count] == 'D0':
            sum_ratings += 1.0 * grades[count]
        elif ratings[count] == 'F':
            sum_ratings += 0.0 * grades[count]
        else:
            continue

print(round(sum_ratings/sum_grades, 6))
