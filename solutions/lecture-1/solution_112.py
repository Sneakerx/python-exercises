"""Demonstrating variable assignments and references in Python."""

A = 42  # Initial assignment
B = A  # B points to the same object in memory as A
C = A  # C points to the same object in memory as A
A = 10  # A is reassigned to point to a new object in memory
B = C  # B points to the same object in memory as C

print(A, B, C)
# Expected output:
# 10 42 42
