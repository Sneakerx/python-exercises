"""List Slicing Exercise."""

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

print(alphabet[2:5])  # Output: ['C', 'D', 'E']
print(alphabet[-5:-1])  # Output: ['H', 'I', 'J', 'K']
print(alphabet[:])  # Output: all elements
print(alphabet[5:])  # Output: ['F', 'G', 'H', 'I', 'J', 'K', 'L']
print(alphabet[:3])  # Output: ['A', 'B', 'C']
print(alphabet[:-5])  # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(alphabet[2:2])  # Output: []
print(alphabet[::2])  # Output: ['A', 'C', 'E', 'G', 'I', 'K']
print(alphabet[2::2])  # Output: ['C', 'E', 'G', 'I', 'K']
print(alphabet[-50:50])  # Output: all elements
print(alphabet[: len(alphabet)])  # Output: all elements
