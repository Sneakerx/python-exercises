"""List Modification Exercise."""

values = [0, 1, 2, 3, 4, 5]

values[2] = 5
print(values)  # Output: [0, 1, 5, 3, 4, 5]
values.remove(1)
print(values)  # Output: [0, 5, 3, 4, 5]
values.append(7)
print(values)  # Output: [0, 5, 3, 4, 5, 7]
values.remove(4)
print(values)  # Output: [0, 5, 3, 5, 7]
values += [1, 2, 3]
print(values)  # Output: [0, 5, 3, 5, 7, 1, 2, 3]
values.insert(3, 0)
print(values)  # Output: [0, 5, 3, 0, 5, 7, 1, 2, 3]
values.sort(reverse=True)
print(values)  # Output: [7, 5, 5, 3, 3, 2, 1, 0, 0]
values.insert(2, 3)
print(values)  # Output: [7, 5, 3, 5, 3, 3, 2, 1, 0, 0]
values.append(values.count(0))
print(values)  # Output: [7, 5, 3, 5, 3, 3, 2, 1, 0, 0, 2]
values.remove(values.index(3))  # Removes first occurrence of the index of 3
print(values)  # Output: [7, 5, 3, 5, 3, 3, 1, 0, 0, 2]
values.clear()
print(values)  # Output: []
