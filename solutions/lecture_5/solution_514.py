"""Deleting an Object with Exception Handling."""


class Zahl:
    def __init__(self, wert):
        self.wert = wert


try:
    wert = int(input("Geben Sie einen Wert an: "))
    zahl = Zahl(wert)
    ergebnis = 42 / zahl.wert
except ZeroDivisionError:
    print("Es kann nicht durch 0 geteilt werden")
except ValueError:
    print("Bitte geben Sie eine gültige Zahl ein")
finally:
    try:
        del zahl
    except NameError:
        print("Das Objekt wurde nicht gelöscht, weil es nicht existiert!")
    else:
        print("Das Zahl-Objekt wurde gelöscht!")
