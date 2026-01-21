---
marp: true
math: mathjax

title: "Programmieren in Python"
header: "Programmieren in Python - Vorlesung 3"
footer: "Duale Hochschule Baden-Württemberg"

theme: python_A4
paginate: true

---

# Vorlesung 3
## Übungsaufgabe 1 - Dateien lesen und schreiben
### Aufgabe 1.1

Was macht das folgende Programm?

```python
my_grades = []
with open("grades.txt", "r", encoding="utf-8") as grades:
    for grade in grades:
        my_grades.append(grade)

print(my_grades)
```

### Aufgabe 1.2

Das folgende Programm soll in die Datei `zutaten.txt` Zutaten eintragen. Finden und korrigieren Sie die Fehler.

```python
with open("zutaten.txt", "r+"):
    zutaten.write("Butter\n")
    zutaten.write("Zucker\n")
zutaten.close()
```

### Aufgabe 1.3

Schreiben Sie den Code so, dass der Kontextmanager verwendet wird

```python
my_movies = []
movies = open("movies.txt", "r", encoding="utf-8")
for movie in movies:
    my_movies.append(movie)
movies.close()
```

---

### Aufgabe 1.4

Entwickeln Sie ein einfaches Bank System, welches Einzahlen und Auszahlen über die Konsole ermöglicht. 
Der Wert des Kontos soll in einer Datei gespeichert werden. Es ist ausreichend, den Kontostand beim Start zu lesen und beim Beenden des Programms zu schreiben.

Implementieren Sie für jede Aktion eine Funktion:
- Einzahlen
- Abgeben
- Guthaben anzeigen
- Schließen und speichern

## Übungsaufgaben 2 - Bibliotheken: Module und Pakete
### Aufgabe 2.1

Was unterscheidet ein Paket von einem Modul?

### Aufgabe 2.2

Berechnen Sie mithilfe der Standardbibliothek den größten gemeinsamen Teiler der Zahlen 112 und 220. Verwenden Sie das Modul `math`.

### Aufgabe 2.3

Schreiben Sie ein Programm, welches den aktuellen Systemnutzer mit einer Nachricht begrüßt. Verwenden Sie das Paket `os`.

### Aufgabe 2.4

Schreiben Sie ein Programm, welches die aktuelle Version des Python Interpreters ausgibt. Verwenden Sie das Modul `sys`.

---

### Aufgabe 2.5

Schreiben Sie ein Programm, welches die aktuelle Zeit in folgendem Format ausgibt: Tag.Monat.Jahr Stunde:Minute:Sekunde. Nutzen Sie das Modul `datetime`.



### Aufgabe 2.6

Suchen Sie im Modul `random` nach einer Funktion, welche aus einer Liste mit Zahlen von 1 bis 100 fünf zufällig auswählen kann.

### Aufgabe 2.7

Entwickeln Sie eine eigene Bibliothek (ein eigenes Modul) für die Aufgaben 2.3 bis 2.6. Es sollen alle Funktionalitäten der Aufgaben im Modul enthalten sein. Binden Sie das Modul in eine weitere Datei ein und führen Sie alle Methoden aus.

## Übungsaufgabe 3 - Argumente und Kontrollstrukturen
### Aufgabe 3.1

Schreiben Sie eine Funktion, welche den Durchschnitt aller Input Werte berechnet. Als Parameter soll `*args` verwendet werden.

### Aufgabe 3.2

Schreiben sie eine Funktion, welche `positional`, `*args` und `**kwargs` Parameter empfangen kann. Die Parameter sollen alle über die `print()` Funktion ausgegeben werden. Bei jedem Parameter soll ausgegeben werden, um welche Positional-Kategorie es sich handelt.

---

### Aufgabe 3.3

Gegeben ist folgende Liste: 
`numbers = [4, -2, 102, -5, -12, 3]`

Es soll eine neue Liste erstellt werden, welche nur die Positiven Zahlen der gegebenen
Liste enthält. Die Negativen Zahlen sollen entfernt werden.

Schreiben Sie zwei Varianten des Programms. Eines mit einer "klassischen" for Schleife (mehrere Zeilen) und eines mit einer "vereinfachten" for Schleife (in einer Zeile).