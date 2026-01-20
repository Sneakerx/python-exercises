"""Open text file in read and write mode and add ingredients to the file."""

with open("zutaten.txt", "r+"):
    zutaten.write("Butter\n")
    zutaten.write("Zucker\n")
zutaten.close()
