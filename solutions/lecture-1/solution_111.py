"""Swapping the values of two variables."""

FIRST_NAME = "Mustermann"
LAST_NAME = "Max"

# Pythonic: Create tuple and unpack it to swap values
FIRST_NAME, LAST_NAME = LAST_NAME, FIRST_NAME
print(FIRST_NAME, LAST_NAME)
