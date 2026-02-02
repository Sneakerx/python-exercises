---
marp: true
math: mathjax

title: "Programmieren in Python"
header: "Programmieren in Python - Vorlesung 5"
footer: "Duale Hochschule Baden-Württemberg"

theme: python_A4
paginate: true

---

# Vorlesung 5
## Übungsaufgabe 1 - Exceptions
### Aufgabe 1.1

Gegeben sind die folgenden Variablen und Datenstrukturen

```python
name = "Nico"
i = 42
my_list = [i, name, True]
j = 42
book = {"angreifen": "attack", "schreiben": "write"}
```

Geben Sie für jede Zeile an, welche Art von Exception geworfen wird:

```python
int(i)                                                         
float(name)
my_list[3]
i / (i - j)
my_list[i - 40]
print(f'Hallo {name}!")
book["Maske"]
  bool(name)      
i / (j % 6)
file = open("test.txt",'r')  # "test.txt" existiert nicht.
```

### Aufgabe 1.2

Welche Exception könnte in folgendem Programm geworfen werden?
Ergänzen Sie eine except Anweisung um den Fehler abzufangen und geben Sie darin aus, warum der Fehler aufgetreten ist.

```python
names = {"Jürgen": "Müller", "Martin": "Freund", "Lisa": "Sonntag"}

try:
    first_name = input("Enter first name: ")
    # KeyError, falls der Schlüssel nicht im Dictionary vorhanden ist
    last_name = names[first_name]
    print(f"{first_name} {last_name}")
```

---

### Aufgabe 1.3

Welche Exceptions können in folgendem Programm geworfen werden?
Ergänzen Sie mehrere except Anweisungen, um die Fehler abzufangen und geben Sie darin aus, warum der Fehler aufgetreten ist.

```python
try:
    weight = int(input("Gewicht (in kg): "))
    height = float(input("Körpergröße (in m): "))
    bmi = weight / height**2
    print(f"Dein BMI ist {bmi}")
```

### Aufgabe 1.4

Gegeben ist das folgende Programm:

```python
class Zahl:
    def __init__(self, wert):
        self.wert = wert
    
try:
    wert = int(input("Geben Sie einen Wert an: "))
    zahl = Zahl(wert)
    ergebnis = 42 / zahl.wert
```

Sorgen Sie mit einem finally Block dafür, dass das Objekt zahl immer gelöscht wird. Gib dem Nutzer eine Nachricht aus, dass das Objekt gelöscht wurde. Sollte das Objekt nicht gelöscht werden können, z.B. wenn das Objekt nicht erzeugt werden konnte, entsteht ein NameError. Dieser muss auch im finally Block abgefangen werden.