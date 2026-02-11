"""
Beispielmodul für Pylint-Fehler
"""


# pylint: disable=too-few-public-methods
# pylint is right, but this is just an example to demonstrate pylint errors.
class ExampleClass:
    """Eine Beispielklasse mit PEP 8 Konventionen"""

    def __init__(self, value):
        """Initialisiert die Klasse mit einem Wert"""
        self.value = value

    def get_value(self):
        """Gibt den gespeicherten Wert zurück"""
        return self.value


def add_numbers(x, y):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück"""
    return x + y


def say_hello():
    """Gibt eine Begrüßung aus"""
    print("Hallo, Welt!")
