---
marp: true
math: mathjax

title: "Programmieren in Python"
header: "Programmieren in Python - Vorlesung 7"
footer: "Duale Hochschule Baden-Württemberg"

theme: python_A4
paginate: true

---

# Vorlesung 7
## Übungsaufgabe 1 - Statische Code-Analyse
### Aufgabe 1.1
Gezeigt ist ein kurzes Python-Skript, das gegen PEP 8 verstößt und mit pylint korrigiert werden soll.


```python
def addNumbers(x,y): return x+y

def Say_Hello(): print("Hallo, Welt!") 

class exampleclass:
  def __init__(self,value): self.Value=value
  def getvalue(self): return self.Value
```

## Übungsaufgabe 2 - Logging
### Aufgabe 2.1

Erstellen Sie eine einfache Mathematik Bibliothek `math_lib.py`, welche die Funkionen `add()` und `sub()` beinhaltet und einige Info und Fehlermeldungen ausgibt. Dabei soll der Logger aus dem Hautprogramm genutzt werden.

Erstellen Sie das dazugehörige Hauptprogramm `main.py`, welches einen Logger konfiguriert und die `math_lib` importiert. Von hier sollen die beiden Funktionen aufgerufen werden können.

## Übungsaufgabe 3 - Debugging
### Aufgabe 3.1
Setzen Sie im Hauptprogramm an den Anfang der `main()` einen `breakpoint()`. Steppen Sie sich durch die Funktion. Ändern Sie im Debugger die Variable `c` auf einen gültigen Zahl-Wert.