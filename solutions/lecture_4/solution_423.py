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

    def __sub__(self, other):
        zaehler = self.zaehler * other.nenner - self.nenner * other.zaehler
        nenner = self.nenner * other.nenner
        return Bruch(zaehler, nenner)

    def __mul__(self, other):
        zaehler = self.zaehler * other.zaehler
        nenner = self.nenner * other.nenner
        return Bruch(zaehler, nenner)

    def __truediv__(self, other):
        zaehler = self.zaehler * other.nenner
        nenner = self.nenner * other.zaehler
        return Bruch(zaehler, nenner)

    def __eq__(self, other):
        return self.zaehler / self.nenner == other.zaehler / other.nenner

    def __lt__(self, other):
        return self.zaehler / self.nenner < other.zaehler / other.nenner

    def __gt__(self, other):
        return self.zaehler / self.nenner > other.zaehler / other.nenner


x = Bruch(1, 2)
y = Bruch(3, 4)
z = Bruch(2, 4)

print(x)  # 1/2
print(y)  # 3/4
print(x + z)  # 8/8
print(x - y)  # -2/8
print(x * y)  # 3/8
print(x / y)  # 4/6
print(x == z)  # True
print(x < y)  # True
print(x > y)  # False
