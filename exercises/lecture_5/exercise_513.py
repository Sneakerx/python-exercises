"""Handling exceptions when calculating BMI."""

try:
    weight = int(input("Gewicht (in kg): "))
    height = float(input("Körpergröße (in m): "))
    bmi = weight / height**2
    print(f"Dein BMI ist {bmi}")
# TODO: Handle exceptions here