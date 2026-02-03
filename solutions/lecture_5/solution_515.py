"""Cefine a custom exception IsNotPrimeError that is
raised when the user inputs a non-prime number."""


class IsNotPrimeError(Exception):
    def __init__(self, wert):
        self.wert = wert

    def __str__(self):
        return f"{self.wert} ist keine Primzahl!"


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


zahl = int(input("Gib eine Primzahl ein: "))

if not is_prime(zahl):
    raise IsNotPrimeError(zahl)
