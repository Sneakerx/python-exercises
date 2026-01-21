"""
The file "grades.txt" contains a list of grades, one per line.
The following program opens the file with character encoding 'utf-8' to
ensure that special characters like umlauts are correctly read,
reads the grades from the file and stores them in a list called `my_grades`.
Finally, it prints the list of grades.
"""

my_grades = []
with open("grades.txt", "r", encoding="utf-8") as grades:
    for grade in grades:
        my_grades.append(grade)

print(my_grades)
