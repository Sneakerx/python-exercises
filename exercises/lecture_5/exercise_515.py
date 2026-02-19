"""Define a custom exception IsNotPrimeError that is
raised when the user inputs a non-prime number."""


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


zahl = int(input("Gib eine Primzahl ein: "))

if not is_prime(zahl):
    raise IsNotPrimeError(zahl)
