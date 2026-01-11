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