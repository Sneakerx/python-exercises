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
