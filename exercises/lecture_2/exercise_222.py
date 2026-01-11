"""Tupel exercise"""

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
