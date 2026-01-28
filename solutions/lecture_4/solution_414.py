"""Create method transfer_health from one Pokemon to another."""


class Pokemon:
    def __init__(self, name, number, height, weight, trainer, poke_type):
        self._name = name
        self._number = number
        self._height = height
        self._weight = weight
        self._trainer = trainer
        self._poke_type = poke_type
        self._health = 20

    def get_health(self):
        return self._health

    def increase_health(self, health):
        self._health += health

    def decrease_health(self, health):
        self._health -= health

    def transfer_health(self, other, health):
        healthLeft = self.get_health() - health
        if healthLeft >= 1:
            self.decrease_health(health)
            other.increase_health(health)
        else:
            print("Low health. Could not be transferred.")


schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")

schiggy.transfer_health(pikachu, 5)
print(f"Pikachu: {pikachu.get_health()}")
print(f"Schiggy: {schiggy.get_health()}")

pikachu.transfer_health(schiggy, 35)
print(f"Pikachu: {pikachu.get_health()}")
print(f"Schiggy: {schiggy.get_health()}")
