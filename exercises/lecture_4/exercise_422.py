"""Print special greeting when a Pokemon is created."""


class Pokemon:
    def __init__(self, name, number, height, weight, trainer, poke_type):
        self._name = name
        self._number = number
        self._height = height
        self._weight = weight
        self._trainer = trainer
        self._poke_type = poke_type


schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pokeX = Pokemon("X", 7, 0.5, 9, "Ash", "Wasser")
pikachu = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")
