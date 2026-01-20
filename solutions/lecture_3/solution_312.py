"""Open text file in read and write mode and add ingredients to the file."""

with open("zutaten.txt", "r+", encoding="utf-8") as zutaten:
    zutaten.write("Butter\n")
    zutaten.write("Süßstoff\n")
