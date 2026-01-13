# Vorlesung 2
## Übungsaufgabe 1 - Listen
### Aufgabe 1
```python
data = ["abc123", 12, True, 0.25, -3, "J", "N"]
```

Welche Elemente werden in folgendem Programm indiziert?
```python
data[0]        
data[3]        
data[-2]       
data[-5]       
data[2]        
data[2+2]      
data[3*0-1]    
data[3//3]     
data[-1*3]     
data[7-2]  
```

### Aufgabe 2
```python
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
```

Welche Elemente werden in folgendem Programm indiziert?
```python
alphabet[2:5]
alphabet[-5:-1]
alphabet[:]
alphabet[5:]
alphabet[:3]
alphabet[:-5]
alphabet[2:2]
alphabet[::2]
alphabet[2::2]
alphabet[-50:50]
alphabet[: len(alphabet)]
```

### Aufgabe 3
Welche Liste erhalten Sie nach diesen Eingaben?
```python
[0, 1, 2] * 2
3 * [True, False]
[1, 1] + [2, 2] + [3, 3]
["Hallo"] + ["Python", "!"]
2 * ([True] + [True, False])
```

### Aufgabe 4
```python
values = [0, 1, 2, 3, 4, 5]
```

Geben Sie für jede Zeile an, wie sich die Liste verändert?

```python
values[2] = 5
values.remove(1)
values.append(7)
values.remove(4)
values += [1, 2, 3]
values.insert(3, 0)
values.sort(reverse=True)
values.insert(2, 3)
values.append(values.count(0))
values.remove(values.index(3))
values.clear()
```

### Aufgabe 5
Wie lauten die Ausgaben des Programms?

```python
print(",".join(["3", "14"]))
print(".".join(["Max", "Mustermann"]))
print("*".join(["1", "2", "3", "4", "5"]))
print("".join(["F", "l", "o"]))
print("--".join(["-", "-", "-"]))
```

### Aufgabe 6
```python
matrix = [[1, 0, 1],
          [0, 1, 0],
          [3, 2, 1],
          [1, 2, 3],
          [3, 0, 3]]
```

Wie lauten die Ausgaben des Programms?

```python
matrix[0][2]    
matrix[2][2]    
matrix[4][2]    
matrix[1][1]    
matrix[3][1]    
matrix[2][0]    
matrix[0]       
matrix[2]
```

## Übungsaufgabe 2 - Datenstrukturen
### Aufgabe 1
Was unterschiedet Tupel und Listen voneinander?
Welche Vorteile bieten Tupel gegenüber Listen?


### Aufgabe 2
Was wird durch folgendes Programm ausgegeben?

```python
tupel = (0, 1, 2, 3, 3, 0)
copy = tupel

print(tupel[2])
print(copy[5])
print(tupel.index(0))
index = tupel.index(3)
print(copy[index])
index = copy.count(3)
print(tupel[index])
print(5 in copy)
```

### Aufgabe 3

```python
a = (1,2,3)
b = (4,5,6)
```

Wandeln Sie die beiden Tupel in folgende Liste um: `[1, 2, 3, 4, 5, 6]`


### Aufgabe 4

Schreiben Sie eine Funktion mit dem Namen `is_in_set()`, die als Parameter eine Variable 
und ein Set erhält. Die Funktion soll `True` zurückgeben, sollte die Zahl in dem Set
vorhanden sein.


### Aufgabe 5

Geben Sie an, wie das dictionary nach jeder Zeile aussieht.

```python
values = {"eins" : 1, "zwei" : 2, "drei" : 3}

values.update({"eins": 2})
del values["drei"]
values.clear()
values.update({"null": 0})
values.update({"eins": 0})
values["eins"] = 1
del values["null"]
```

### Aufgabe 6
Erstellen Sie eine Liste mit allen Namen und eine zweite Liste mit jedem Alter.
```python
names = {"Florian": 25, "Bertel": 28, "Eva": 51, "Günter": 60}
```

### Aufgabe 7

Definieren Sie ein Dictionary mit allen Schulnoten als Schlüssel (1-6). 
Als Werte soll die jeweilige Note verbalisiert sein (z.B. 1: Sehr gut).

Schreiben Sie eine Funktion, die als Input eine Zahl nimmt und als Output die Note als Text ausgibt. Die Funktion muss das Dictionary verwenden.

## Übungsaufgabe 3 - Kontrollstrukturen
### Aufgabe 1

Geben Sie jede zweite Zahl aus der Liste aus.
```python
my_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```

### Aufgabe 2

Geben Sie folgende Liste mit Index aus.
```python
names = ["Anna", "Bella", "Charlotte", "Diana", "Erika", "Fiona"]
```

### Aufgabe 3

Schreiben Sie eine Funktion, welche eine zweidimensionale Liste aus Integern erhält. 
Diese soll mit der folgenden Formatierung ausgegeben werden. Die einzelnen Listen müssen alle gleich lang sein.
```
    0 1 2
    — — —
0 | 1 2 3 
1 | 4 5 6 
2 | 7 8 9
```

### Aufgabe 4

Wie viele Ausrufezeichen werden ausgegeben?

```python
x = 0
for i in range(5):
  x += 1
  for j in range(x):
    print("!")
```

### Aufgabe 5

Welche der Schleifen sind Endlosschleifen?

Schleife 1:
```python
while True and False:
  print("Text")
```

Schleife 2:
```python
running = False
while running:
  running = True
  if running:
    print("Das Programm wird ausgeführt.")
  else:
    print("Das Programm wird nicht ausgeführt.")
```

Schleife 3:
```python
running = True
while running:
  running = input("Weitermachen? ")
  if running != False:
    running = True
```

### Aufgabe 6

Ersetzen Sie diese while Schleife durch eine for Schleife
```python
value = [12.50, 13.99, 21.75, 3.14, 13, 37]
i = 0
while True:
    if i == len(value):
        break
    print(value[i])
    i += 1
```