"""Dictionary Manipulations"""

values = {"eins": 1, "zwei": 2, "drei": 3}

values.update({"eins": 2})
print(values)  # Output after updating {'eins': 2, 'zwei': 2, 'drei': 3}
del values["drei"]
print(values)  # Output after deleting {'eins': 2, 'zwei': 2}
values.clear()
print(values)  # Output after clearing {}
values.update({"null": 0})
print(values)  # Output after adding {'null': 0}
values.update({"eins": 0})
print(values)  # Output after adding {'null': 0, 'eins': 0}
values["eins"] = 1
print(values)  # Output after setting {'null': 0, 'eins': 1}
del values["null"]
print(values)  # Output after deleting {'eins': 1}
