"""Calculates the average of a variable number of input values."""


def calculate_average(*values):
    """calculate the average of the given values."""
    length = len(values)
    total = sum(values)

    return total / length if length > 0 else "error: no values provided"


result = calculate_average(1, 2, 3, 4, 5, 6)
print("Average:", result)
