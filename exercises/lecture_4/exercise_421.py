"""Which comparisons return True and which return False?"""


class Pokemon:
    def __init__(self, name, number, height, weight, trainer, poke_type):
        self._name = name
        self._number = number
        self._height = height
        self._weight = weight
        self._trainer = trainer
        self._poke_type = poke_type

    def __eq__(self, other):
        return self._name == other._name


schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu1 = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")
pikachu2 = pikachu1
pikachu3 = Pokemon("Pikachu", 25, 0.35, 5, "Max", "Elektro")
glumanda = Pokemon("Schiggy", 4, 0.61, 8.5, "Ash", "Feuer")

print(schiggy == pikachu1)
print(schiggy == schiggy)
print(schiggy is schiggy)
print(pikachu1 == pikachu2)
print(pikachu2 is pikachu1)
print(glumanda is glumanda)
print(glumanda == schiggy)
print(glumanda is schiggy)
print(pikachu1 == pikachu3)
print(pikachu1 is pikachu3)
