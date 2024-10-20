grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()

# Решение без циклов
average_score = []
average_score.append((sum(grades[0]) / (len(grades[0]))))
average_score.append((sum(grades[1]) / (len(grades[1]))))
average_score.append((sum(grades[2]) / (len(grades[2]))))
average_score.append((sum(grades[3]) / (len(grades[3]))))
average_score.append((sum(grades[4]) / (len(grades[4]))))
students_grades = {}
students_grades.update({students[0]: average_score[0]})
students_grades.update({students[1]: average_score[1]})
students_grades.update({students[2]: average_score[2]})
students_grades.update({students[3]: average_score[3]})
students_grades.update({students[4]: average_score[4]})
print(students_grades)

# Решение с применением цикла
average_score = []
for x in grades:
    average_score.append(sum(x) / len(x))
students_grades = {}
for i in range(len(students)):
    students_grades.update({students[i]: average_score[i]})
print(students_grades)
