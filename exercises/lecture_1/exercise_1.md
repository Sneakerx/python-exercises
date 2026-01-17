---
marp: true
math: mathjax

title: "Programmieren in Python"
header: "Programmieren in Python - Vorlesung 1"
footer: "Duale Hochschule Baden-Württemberg"

theme: python_A4
paginate: true

---

# Vorlesung 1
## Übungsaufgabe 1 - Variablen
### Aufgabe 1.1
Gegeben sind folgende Variablen:
```python
FIRST_NAME = "Mustermann"
LAST_NAME = "Max"
```

Schreiben Sie ein Programm, welches die Werte der beiden Variablen vertauscht, sodass Vor- und Nachname richtig zugeordnet sind.



### Aufgabe 1.2
Gegeben ist das folgende Python Programm:

```python
A = 42
B = A
C = A
A = 10
B = C
```

Welche Werte werden durch die folgende Zeile ausgegeben:

`print(A, B, C)`

---

### Aufgabe 1.3
Welche der folgenden Umwandlungen sind möglich und was ist das Ergebnis?

```python
int(5.5)
float(-1)
str(0.3)
bool(0.0001)
str("False")
int(False)
bool('0')
int("False")
float("True")
```

### Aufgabe 1.4
Wie lautet die Ausgabe des folgenden Programms?

```python
FIRST_NAME = "Lisa"
LAST_NAME = "Mueller"
HEIGHT = 180
DAY = 23
MONTH = "January"
YEAR = "1999"

print(
    f"""Hi, my name is {FIRST_NAME} {LAST_NAME}.
I am {HEIGHT}cm tall and I was born on {DAY} {MONTH} {YEAR}."""
)
```
---

## Übungsaufgabe 2 - Kontrollstrukturen und Input
### Aufgabe 2.1
Entwickeln Sie ein Programm, welches den BMI aus Benutzer-Inputs berechnet.

Formel: $\mathrm{BMI} = \mathrm{Koerpergewicht (kg)} / \mathrm{Groesse (m)} ^ 2$

### Aufgabe 2.2
Entwickeln Sie ein Programm welches den Satz des Pythagoras berechnet. 
Es soll die Länge der Ankathete und Gegenkathete eingegeben werden. 
Als Ergebnis soll die Hypotenuse ausgegeben werden.


### Aufgabe 2.3
Programmieren Sie einen Taschenrechner, welcher Plus, Minus, Mal und Geteilt rechnen kann. 
Der Rechner soll mit zwei Zahlen arbeiten können.


## Übungsaufgabe 3 - Funktionen
### Aufgabe 3.1
Bearbeiten Sie den Taschenrechner aus Übung 2. 
Das Programm soll mit verschiedenen Funktionen programmiert werden. 
Für jede Rechenart soll eine Funktion vorhanden sein.

