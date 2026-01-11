"""basic operations on tuples"""

tupel = (0, 1, 2, 3, 3, 0)
copy = tupel  # creating a reference

print(tupel[2])  # output: 2
print(copy[5])  # output: 0
print(tupel.index(0))  # output: 0
index = tupel.index(3)  # index = 3
print(copy[index])  # output: 3
index = copy.count(3)  # index = 2
print(tupel[index])  # output: 2
print(5 in copy)  # output: False
