"""Handling exceptions when calculating BMI."""

try:
    # ValueError: Hier kann etwas eingegeben werden, das keine Zahl ist.
    weight = int(input("Gewicht (in kg): "))
    # ValueError: Hier kann etwas eingegeben werden, das keine Zahl ist.
    height = float(input("Körpergröße (in m): "))
    # ZeroDivisionError: Bei "height==0" erfolgt Division durch 0.
    bmi = weight / height**2
    print(f"Dein BMI ist {bmi}")
except ValueError:
    print(f"Es wurde etwas eingegeben, das keine Zahl ist.")
except ZeroDivisionError:
    print("Die Körpergröße wurde mit 0 angegeben. Das ist undefiniert.")
