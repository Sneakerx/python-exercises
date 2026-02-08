from math import pi


def calculate_area(radius):
    try:
        r = float(radius)
    except (TypeError, ValueError):
        raise TypeError("The radius must be a number.")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * (r**2)


def calculate_circumference(radius):
    try:
        r = float(radius)
    except (TypeError, ValueError):
        raise TypeError("The radius must be a number.")
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return 2 * pi * r
