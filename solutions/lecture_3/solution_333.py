"""Remove negative numbers from list."""

numbers = [4, -2, 102, -5, -12, 3]

# Version 1: Using a for loop
numbers1 = []
for x in numbers:
    if x > 0:
        numbers1.append(x)

# Version 2: Using list comprehension
numbers2 = [x for x in numbers if x > 0]

print(f"Variante 1: {numbers1}")
print(f"Variante 2: {numbers2}")
