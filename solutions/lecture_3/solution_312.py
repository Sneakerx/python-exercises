"""Open text file in read and write mode and add ingredients to the file."""

with open("./data/lecture3/zutaten.txt", "r+") as zutaten:
    zutaten.write("Butter\n")
    zutaten.write("Zucker\n")
