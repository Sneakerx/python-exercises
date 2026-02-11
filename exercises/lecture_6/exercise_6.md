---
marp: true
math: mathjax

title: "Programmieren in Python"
header: "Programmieren in Python - Vorlesung 6"
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

---

## Übungsaufgabe 3 - Static Type Checking
### Aufgabe 3.1

Gegeben ist folgende Pokemon Klasse `pokemon.py`.

Führen Sie `mypy --disallow-untyped-defs --disallow-untyped-calls pokemon.py` aus und analysieren Sie die Fehler.
Ändern Sie nun die `pokemon.py` Datei, damit keine MyPy Fehler mehr vorhanden sind.

```python
"""
Module to control pokemon and different poke types.
"""

import random


class Pokemon:
    """
    Class with all relevant data for a Pokemon.
    Functions to attack another Pokemon.
    """

    def __init__(self, name, number, poke_type):
        self._name = name
        self._number = number
        self._poke_type = poke_type
        self._health = 100
        self._max_health = 100
        self._level = 1
        self._level_progress = 0
        self._is_alive = True
        self._strength = random.randint(1, 30)

    def __eq__(self, other):
        if not isinstance(other, Pokemon):
            return NotImplemented
        return self._name == other.get_name()

    def __str__(self):
        return (
            f"Name: {self._name}\n"
            f"Type: {self._poke_type}\n"
            f"Level: {self._level}\n"
            f"Health: {self._health}\n"
            f"Strength: {self._strength}"
        )

    def _level_up(self):
        self._level += 1
        print(f"Pokemon {self._name} is now level {self._level}!")
        self._max_health += 10
        self._health += 10

```

---

```python

    def attack(self, opponent):
        """
        Attacks another pokemon by calculating the attack factor.
        After the fight, the attacking pokemon receives XP.
        """
        if not self._is_alive:
            print("Pokemon is dead already!")
        elif not opponent.get_is_alive():
            print("Opponent is dead already!")
        else:
            print(f"{self._name} attacks {opponent.get_name()}!")
            attack_factor = get_attack_factor(self._poke_type, opponent.get_poke_type())
            attack_damage = self._strength * attack_factor

            if attack_factor == 2:
                print("Effective")
            elif attack_factor == 1:
                print("Not very effective")
            elif attack_factor == 4:
                print("Very effective")

            opponent.receive_damage(attack_damage)
            self.earn_xp(attack_damage)

    def receive_damage(self, damage):
        """
        Reduces the health of a pokemon by amount of damage
        and checks if the pokemon is dead.
        """
        print(f"{self._name} looses {damage} health!")
        self._health -= damage
        if self._health <= 0:
            self._is_alive = False
            print(f"Pokemon {self._name} is dead!")

    def earn_xp(self, xp):
        """
        Training of a pokemon.
        Earns XP and increases the level of a pokemon.
        """
        self._level_progress += xp
        while self._level_progress >= 100:
            self._level_progress -= 100
            self._level_up()
```

---

```python
    def use_health_potion(self):
        self._health = self._max_health
        print(f"Pokemon {self._name} was healed.")

    def get_name(self):
        return self._name

    def get_poke_type(self):
        return self._poke_type

    def get_health(self):
        return self._health

    def get_level(self):
        return self._level

    def get_is_alive(self):
        return self._is_alive

    def get_strength(self):
        return self._strength


def get_attack_factor(attack_type, defend_type):
    """
    Return the attack factor for a combination of types.
    Returns 2 if no special combination is available.
    """
    attack_types = {
        ("Water", "Fire"): 4,
        ("Fire", "Water"): 1,
        ("Plant", "Water"): 4,
        ("Water", "Plant"): 1,
        ("Fire", "Plant"): 4,
        ("Plant", "Fire"): 1,
    }
    return attack_types.get((attack_type, defend_type), 2)
```