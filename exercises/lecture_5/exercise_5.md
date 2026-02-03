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

---

### Aufgabe 1.5
Gegeben ist folgendes Programm:

```python
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


zahl = int(input("Gib eine Primzahl ein: "))

if not is_prime(zahl):
    raise IsNotPrimeError(zahl)
```

Die Funktion `is_prime()` gibt für eine Zahl zurück, ob es sich um eine Primzahl handelt.
Das Hauptprogramm fragt einen Nutzer nach einer Zahl. Handelt es sich nicht um eine Primzahl, wird die Exception `IsNotPrimeError` geworfen. Für die Eingabe 12 soll folgende Fehlermeldung erscheinen:
__main__.IsNotPrimeError: 12 ist keine Primzahl!

Implementieren Sie die `IsNotPrimeError` Exception

---

## Übungsaufgabe 2 - Web Requests
Dieses Kapitel enthällt mehrere Aufgaben zu einer Crypto API.
Dokumentation der API: [Kucoin API](https://www.kucoin.com/docs/beginners/introduction)

### Aufgabe 2.1

Schreiben Sie ein Programm, welches Daten von einer Crypto API abrufen kann. Nutzen Sie hierfür die Kucoin API. Der Nutzer soll über die Konsole einen Coin und eine Währung eingeben können. Das Programm soll den aktuellen Preis in der passenden Währung ausgeben. Es soll zusätzlich das Datum und die Uhrzeit ausgegeben werden, von der der aktuelle Preis stammt.

Info: Die Funktionalität der Kucoin API ist sehr umfangreich. Sie benötigen keinen API key, um diese zu verwenden. Die Aufgaben beziehen sich nur auf das Kapitel "Market Data" der Dokumentation. Nutzen Sie die Funktion "Get Ticker" um die Aufgabe zu lösen: [Get Ticker](https://www.kucoin.com/docs-new/rest/spot-trading/market-data/get-ticker)

**Beispiel:** Request für BTC in EURO: https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-EUR

---

### Aufgabe 2.2

Überlegen Sie welche Fehlermöglichkeiten es gibt (z.B. Nutzereingaben) und fangen Sie diese mit Exceptions ab.

### Aufgabe 2.3

Erweitern Sie ihr Programm sodass die Eingabe weiterhin gleich funktioniert, aber die Ausgabe den "vollständigen Namen" der Währung und der Cryptowährung enthält.

Beispiel: 
- Eingabe: ETC USD
- Ausgabe: <timetag>: Der Wert von Ethereum beträgt: 30.000 US Dollar

Verwenden Sie hierfür die "Get Currency Detail" Funktion: [Dokumentation](https://www.kucoin.com/docs/rest/spot-trading/market-data/get-currency-detail)
