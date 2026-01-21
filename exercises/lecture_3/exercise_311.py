"""Was macht das folgende Programm?"""

my_grades = []
with open("grades.txt", "r", encoding="utf-8") as grades:
    for grade in grades:
        my_grades.append(grade)

print(my_grades)
