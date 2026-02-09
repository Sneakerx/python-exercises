---
marp: true
math: mathjax

title: "Programmieren in Python"
header: "Programmieren in Python - Vorlesung 5"
footer: "Duale Hochschule Baden-Württemberg"

theme: python_A4
paginate: true

---

# Vorlesung 6
## Übungsaufgabe 1 - Unittests
### Aufgabe 1.1

Gegeben ist folgendes Modul: `circle.py`

```python
from math import pi

def calculate_area(radius):
    return pi * (radius**2)

def calculate_circumference(radius):
    return 2 * pi * radius
```

Schreiben Sie Unittests für die beiden Funktionen.
Es sollen alle realistisch möglichen Edge-Cases getestet werden.

### Aufgabe 1.2

Wie Sie hoffentlich gemerkt haben, ist das Modul aus Aufgabe 1 nicht gut gegen Fehleingaben abgesichert. Dementsprechend sollten einige Unittests fehlschlagen.

Entwickeln Sie das Modul circle.py weiter, sodass falsche Typen mit einem TypeError und negative Werte mit einem ValueError versehen werden.

Testen Sie, ob Ihre Unittests jetzt erfolgreich sind und erstellen Sie gegbenefalls neue Unittests, die auf die die neuen Fehler abtesten.

### Aufgabe 1.3
Lassen Sie die `coverage` der Tests berechnen und erreichen Sie 100% Abdeckung.

---

## Übungsaufgabe 2 - Unittests Patchen
### Aufgabe 2.1
### Aufgabe 3

Gegeben ist ein einfaches Pokemon Spiel. Es handel sich hierbei nur um eine `main()` Funktion, die den User Input behandelt. Alle anderen Funktionen sind nur "Dummy" Funktionen. Schreiben Sie einen Tests für die `main()` Funktion. Die anderen Funktionen müssen nicht getestet werden. Versuchen Sie, alle relevanten Optionen zu testen.

```python
# game.py

import time

def create_new_pokemon():
    # DUMMY FUNCTION -> Will never exit
    while True:
        pass

def attack_pokemon(poke_list):
    # DUMMY FUNCTION -> Will never exit
    while True:
        pass

def welcome():
    print("Welcome to the game")

def main():
    game = True
    pokemon_storage = []

    welcome()
    while game:
        choice = input(
            "Please select\n1: Create new pokemon\n2: Attack a pokemon\nQ: Quit Game\n"
        )

        if choice == "1":
            print("Create Pokemon")
            new_pokemon = create_new_pokemon()
            pokemon_storage.append(new_pokemon)
        elif choice == "2":
            print("Attack Pokemon")
            attack_pokemon(pokemon_storage)
        elif choice in ("q", "Q"):
            print("Bye")
            game = False   
        else:
            print("Invalid option")

        time.sleep(1)

if __name__ == "__main__":
    main()

```