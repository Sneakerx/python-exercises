"""Demonstrating formatted string literals (f-strings) in Python."""

FIRST_NAME = "Lisa"
LAST_NAME = "Mueller"
HEIGHT = 180
DAY = 23
MONTH = "January"
YEAR = "1999"

print(
    f"""Hi, my name is {FIRST_NAME} {LAST_NAME}.
I am {HEIGHT}cm tall and I was born on {DAY} {MONTH} {YEAR}."""
)
