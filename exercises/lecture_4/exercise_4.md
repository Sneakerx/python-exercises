---
marp: true
math: mathjax

title: "Programmieren in Python"
header: "Programmieren in Python - Vorlesung 4"
footer: "Duale Hochschule Baden-Württemberg"

theme: python_A4
paginate: true

---

# Vorlesung 1
## Übungsaufgabe 1 - Variablen
### Aufgabe 1.1
- Was sind die Vorteile von objektorientierter Programmierung? 
- Wann sollte man sie nutzen?

### Aufgabe 1.2

Geben Sie für jede Zeile an, ob eine Methode oder eine Funktion aufgerufen wird.

```python
len([1,2,3,4,5])                      
"Hallo Python!".index('y')           
["Amina","Aurelia","Anna"].count('A')
random.shuffle([4,8,15,16,23,42])     
print("Hallo Python!")                
math.sqrt(9)                          
{}.clear()                           
set().add(0) 
```

### Aufgabe 1.3

Gegeben ist folgende Account Klasse:

```python
class Account:
    def __init__(self, owner, account_number, initial_balance):
        self._owner = owner
        self._account_number = account_number
        self._initial_balance = initial_balance
```

Schreiben Sie eine Methode `get_info`, mit der der Kontoinhaber und die Kontonummer ausgelesen werden kann. Auf den Geldbetrag darf nicht zugegriffen werden. Die Schnittstelle soll einen Parameter key bekommen. Ist dieser key `owner` soll der Eigentümer, ist dieser key `account_number`, soll die Nummer zurückgegeben werden.

---

### Aufgabe 1.4

Gegeben sei die folgende Pokemon Klasse:

```python
class Pokemon:
    def __init__(self, name, number, height, weight, trainer, poke_type):
        self._name = name
        self._number = number
        self._height = height
        self._weight = weight
        self._trainer = trainer
        self._poke_type = poke_type
        self._health = 20 

    def get_health(self):
        return self._health
```

Schreiben Sie eine Methode `transfer_health`, die als Parameter ein Pokemon und die Anzahl an  Lebenspunkten erhält. Diese wird z. B. so aufgerufen:

```python
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")

schiggy.transfer_health(pikachu, 5)
```

Nach dem Aufruf soll Pikachu nun 25 und Schiggy 15 Leben haben.

Ein Pokemon kann die gewünschte Anzahl an Leben aber nur übertragen, wenn noch mindestens ein  Lebenspunkt übrig ist. Ansonsten soll die Funktion einen Fehler melden.

---

## Übungsaufgabe 2 - Operatoren Überladen
### Aufgabe 2.1

Gegeben ist die folgende Klasse

```python
class Pokemon:
    def __init__(self, name, number, height, weight, trainer, poke_type):
        self._name = name
        self._number = number
        self._height = height
        self._weight = weight
        self._trainer = trainer
        self._poke_type = poke_type

    def __eq__(self, other):
        return self._name == other._name
```

Welche Ausgabe erzeugt das folgende Programm?

```python
schiggy = Pokemon("Schiggy", 7, 0.5, 9, "Ash", "Wasser")
pikachu1 = Pokemon("Pikachu", 25, 0.41, 6, "Ash", "Elektro")
pikachu2 = pikachu1
pikachu3 = Pokemon("Pikachu", 25, 0.35, 5, "Max", "Elektro")
glumanda = Pokemon("Schiggy", 4, 0.61, 8.5, "Ash", "Feuer")

print(schiggy == pikachu1)     
print(schiggy == schiggy)       
print(schiggy is schiggy)  
print(pikachu1 == pikachu2)     
print(pikachu2 is pikachu1)     
print(glumanda is glumanda)
print(glumanda == schiggy)      
print(glumanda is schiggy)      
print(pikachu1 == pikachu3)     
print(pikachu1 is pikachu3) 
```

---

### Aufgabe 2.2

Erweitern Sie die `Pokemon` Klasse aus Aufgabe 1 so, dass beim instanziieren eines Pokemon mit dem Namen "Schiggy" folgende Meldung erscheint: "Schiggy, Schiggy!"
Beim instanziieren der Pokemon mit dem Namen "X", soll folgende Meldung erscheinen: "X, X!"
Das Pokemon Pikachu stellt eine Ausnahme dar. Hier soll "Pika, Pika!" ausgegeben werden.

### Aufgabe 2.3

Entwickeln Sie die `Bruch` Klasse aus der Vorlesung weiter.
Es soll zusätzlich zur Addition auch Subtraktion, Multiplikation und Division verwendet werden können. 

Außerdem sollen Vergleiche zwischen zwei Brüchen möglich sein. Es soll "ist gleich", "kleiner als" und "größer als" möglich sein. Als Antwort soll jeweils True oder False zurückgegeben werden.

Hierfür müssen die Methoden `__eq__`, `__lt__` und `__gt__` überschrieben werden. 

---

## Übungsaufgabe 3 - Vererbung
### Aufgabe 3.1
Gegeben ist die folgende Tier Klasse:
```python
class Tier:
    def __init__(self, name):
        self.name = name
        self.tierart = "Tier"

    def __str__(self):
        return f"{self.name} ist ein {self.tierart}."

    def reden(self):
        print("...")

class Hund(Tier):
    def __init__(self, name):
        self.name = name
        self.tierart = "Hund"

    def reden(self):
        print("Wuff, wuff!")

class Ente(Tier):
    pass

class Robbe(Tier):
    def __init__(self, name):
        super().__init__(name)
        self.tierart = "Robbe"

    def reden(self):
        print("Ow, ow!")

```

Wie lautet die Ausgabe des Programms?

```python
benni = Tier("Benni")
maya = Hund("Maya")
robin = Robbe("Robin")
darkwing = Ente("Darkwing")

print(benni)       
print(maya)       
print(robin)     
print(darkwing)  
benni.reden()       
robin.reden()     
darkwing.reden()    
maya.reden()  
```

---

### Aufgabe 3.2

Erstellen Sie eine Klasse `Person` mit den Eigenschaften "name" und "alter". Implementieren Sie eine Methode namens `geburtstag_feiern`, die das Alter der Person um eins erhöht. 
Erstellen Sie dann eine Unterklasse `Student`, die von der Klasse `Person` erbt. Der Student soll zusätzlich die private Eigenschaft `matrikelnummer` haben. Die Klasse Student muss außerdem die Klassenvariable `altersgrenze` besitzen.
Implementieren Sie eine Methode namens `studieren`, die eine Ausgabe erzeugt wie "Der Student 'Name' mit Matrikelnummer 'Matrikelnummer' studiert fleißig."
Wenn das Alter des Studenten über der Altersgrenze ist, soll stattdessen die Ausgabe "Der Student 'Name' ist zu alt zum Studieren." erfolgen.