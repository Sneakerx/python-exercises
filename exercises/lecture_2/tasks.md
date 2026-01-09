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