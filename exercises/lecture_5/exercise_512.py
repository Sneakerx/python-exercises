"""Handling a KeyError exception when accessing a dictionary."""

names = {"Jürgen": "Müller", "Martin": "Freund", "Lisa": "Sonntag"}

try:
    first_name = input("Enter first name: ")
    # KeyError, falls der Schlüssel nicht im Dictionary vorhanden ist
    last_name = names[first_name]
    print(f"{first_name} {last_name}")
# TODO: Handle exceptions here
