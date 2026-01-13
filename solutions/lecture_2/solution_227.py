"""Convert Grades to Descriptions"""

grades = {
    1: "Sehr gut",
    2: "Gut",
    3: "Befriedigend",
    4: "Ausreichend",
    5: "Mangelhaft",
    6: "Ungenügend",
}


def print_grade(grade):
    print(f"Du hast die Note {grades[grade]} erhalten!")


print_grade(2)
print_grade(6)
