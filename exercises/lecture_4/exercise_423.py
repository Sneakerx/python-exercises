"""Implement string representation and basic operations for a Fraction class."""


class Bruch:
    def __init__(self, zaehler, nenner):
        self.zaehler = zaehler
        self.nenner = nenner

    def __str__(self):
        if self.zaehler == 0:
            return "0"
        elif self.nenner == 0:
            return "Bruch ist nicht definiert"
        elif self.nenner == 1:
            return str(self.zaehler)
        elif (self.zaehler < 0) ^ (self.nenner < 0):
            return f"-{abs(self.zaehler)}/{abs(self.nenner)}"
        else:
            return f"{abs(self.zaehler)}/{abs(self.nenner)}"

    def __add__(self, other):
        zaehler = self.zaehler * other.nenner + self.nenner * other.zaehler
        nenner = self.nenner * other.nenner
        return Bruch(zaehler, nenner)


x = Bruch(1, 2)
y = Bruch(3, 4)
z = Bruch(2, 4)

print(x)
print(y)
print(x + z)
print(x - y)
print(x * y)
print(x / y)
print(x == z)
print(x < y)
print(x > y)
