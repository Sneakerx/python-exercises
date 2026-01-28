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

print(schiggy == pikachu1)  # False, weil die Namen der Objekte unterschiedlich sind.
print(schiggy == schiggy)  # True, weil die Namen der Objekte gleich sind.
print(schiggy is schiggy)  # True, weil die Objekte identisch sind.
print(pikachu1 == pikachu2)  # True, weil die Namen der Objekte gleich sind.
print(pikachu2 is pikachu1)  # True, weil pikachu1 und 2 auf dasselbe Objekt zeigen.
print(glumanda is glumanda)  # True, weil die Objekte identisch sind.
print(glumanda == schiggy)  # True, weil die Namen der Objekte gleich sind.
print(glumanda is schiggy)  # False, weil die Objekte nicht identisch sind.
print(pikachu1 == pikachu3)  # True, weil die Namen der Objekte gleich sind.
print(pikachu1 is pikachu3)  # False, weil die Objekte nicht identisch sind.
