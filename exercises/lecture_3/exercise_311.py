"""Was macht das folgende Programm?"""

myGrades = []
with open("grades.txt", "r") as grades:
    for grade in grades:
        myGrades.append(grade)

print(myGrades)
