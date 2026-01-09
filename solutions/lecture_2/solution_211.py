"""List Indexing Exercise."""

data = ["abc123", 12, True, 0.25, -3, "J", "N"]
# Accessing elements using indexing
# [0, 1, 2, 3, 4, 5, 6]
# [-7,-6,-5,-4,-3,-2,-1]

print(data[0])  # Output: abc123
print(data[3])  # Output: 0.25
print(data[-2])  # Output: "J"
print(data[-5])  # Output: True
print(data[2])  # Output: True
print(data[2 + 2])  # Output: -3
print(data[3 * 0 - 1])  # Output: "N"
print(data[3 // 3])  # Output: 12
print(data[-1 * 3])  # Output: -3
print(data[7 - 2])  # Output: "J"
