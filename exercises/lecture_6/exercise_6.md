---
marp: true
math: mathjax

title: "Programmieren in Python"
header: "Programmieren in Python - Vorlesung 5"
footer: "Duale Hochschule Baden-Württemberg"

theme: python_A4
paginate: true

---

# Vorlesung 6
## Übungsaufgabe 1 - Unittests
### Aufgabe 1.1

Gegeben ist folgendes Modul: `circle.py`

```python
from math import pi

def calculate_area(radius):
    return pi * (radius**2)

def calculate_circumference(radius):
    return 2 * pi * radius
```

Schreiben Sie Unittests für die beiden Funktionen.
Es sollen alle realistisch möglichen Edge-Cases getestet werden.

### Aufgabe 1.2

Wie Sie hoffentlich gemerkt haben, ist das Modul aus Aufgabe 1 nicht gut gegen Fehleingaben abgesichert. Dementsprechend sollten einige Unittests fehlschlagen.

Entwickeln Sie das Modul circle.py weiter, sodass falsche Typen mit einem TypeError und negative Werte mit einem ValueError versehen werden.

Testen Sie, ob Ihre Unittests jetzt erfolgreich sind und erstellen Sie gegbenefalls neue Unittests, die auf die die neuen Fehler abtesten.

### Aufgabe 1.3
Lassen Sie die `coverage` der Tests berechnen und erreichen Sie 100% Abdeckung.

---

## Übungsaufgabe 2 - Unittests Patchen
