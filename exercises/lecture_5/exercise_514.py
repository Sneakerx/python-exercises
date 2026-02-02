"""Deleting an Object with Exception Handling."""


class Zahl:
    def __init__(self, wert):
        self.wert = wert


try:
    wert = int(input("Geben Sie einen Wert an: "))
    zahl = Zahl(wert)
    ergebnis = 42 / zahl.wert
# TODO: Handle the possible exceptions that may occur here.
