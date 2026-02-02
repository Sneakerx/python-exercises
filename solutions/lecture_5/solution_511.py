"""This module contains code that raises various exceptions."""

name = "Nico"
i = 42
my_list = [i, name, True]
j = 42
book = {"angreifen": "attack", "schreiben": "write"}

int(i)  # valid
float(name)  # ValueError, cannot convert string to float
my_list[3]  # IndexError, list index out of range
i / (i - j)  # ZeroDivisionError, division by zero
my_list[i - 40]  # valid, my_list[2] is True
# print(f'Hallo {name}!") # SyntaxError, unmatched quote
book["Maske"]  # KeyError, key does not exist
#   bool(name) # IndentationError, unexpected indent
i / (j % 6)  # ZeroDivisionError, division by zero
file = open("test.txt", "r")  # FileNotFoundError, file does not exist
