"""List Modification Exercise."""

values = [0, 1, 2, 3, 4, 5]

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
